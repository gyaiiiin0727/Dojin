#!/usr/bin/env python3
"""
IPAdapter スタイル転写テスト — 翔太をcheroine_ponytail咲の画風で生成
=================================================================

★前提:
  1. ip-adapter-plus_sdxl_vit-h.safetensors を DL済み
     → /Applications/Data/Packages/ComfyUI/models/ipadapter/ に配置
  2. CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors は既存のものを流用
     → /Applications/Data/Packages/ComfyUI/models/clip_vision/ にあればOK
  3. 参照画像: style_S1_saki_baseline_00001_.png を ComfyUI/input/ に配置済み
  4. ComfyUI が http://127.0.0.1:8188 で起動中

★実行:
  nohup python3 comfyui_ipadapter_style_transfer.py > ipadapter_log.txt 2>&1 &
  tail -f ipadapter_log.txt
"""

import json
import urllib.request
import urllib.error
import time
import random

COMFYUI_URL = "http://127.0.0.1:8188"

# ── 設定 ──────────────────────────────────────────────
CHECKPOINT = "beretMixManga_v30.safetensors"
REFERENCE_IMAGE = "style_S1_saki_baseline_00001_.png"   # 咲の基準画像（ComfyUI/input/ 内）
WIDTH = 896
HEIGHT = 1152
STEPS = 32
CFG = 6
SAMPLER = "euler_ancestral"
SCHEDULER = "normal"

# 翔太 ポジティブ（faceless male方式）
SHOTA_POSITIVE = """score_9, score_8_up, score_7_up, source_anime,
HDR, 8K, (best quality),
(monochrome:1.4), (greyscale:1.3), (lineart:1.2),
manga, ink drawing,
simple background, white background,
BREAK
(faceless male:1.6), 1boy, solo,
(young adult male:1.2), (adult man:1.2),
(slightly messy hair:1.1), (dark brown hair:1.2), (short hair:1.1),
(slim build:1.2), (narrow shoulders:1.1), (thin neck:1.1),
plain white t-shirt, sweatpants,
BREAK
(upper body:1.2), (from front:1.1),
(soft lighting:1.2),"""

# 翔太 ネガティブ
SHOTA_NEGATIVE = """(worst quality), (low quality), (normal quality), watermark,
bad anatomy, bad hands,
(detailed face:1.3), (detailed eyes:1.3), (face:1.2),
(girl:1.3), (female:1.3), (1girl:1.4),
(muscular:1.3), (broad shoulders:1.2),
(child:1.4), (boy:1.3), (shota:1.4), (baby face:1.3), (teenage:1.3),
(ugly:1.2), (dirty:1.2),
(color:1.3), (colorful:1.3),
speech bubble, text,
negativeXL_D"""


# ── テストパターン定義 ──────────────────────────────────
# IPAdapter weight × weight_type × embeds_scaling の組み合わせ
TEST_PATTERNS = [
    # Phase 1: weight_type = "style transfer" で weight を振る
    {"id": "ST_w06",  "weight": 0.6, "weight_type": "style transfer",        "embeds_scaling": "V only",  "desc": "style transfer w=0.6"},
    {"id": "ST_w08",  "weight": 0.8, "weight_type": "style transfer",        "embeds_scaling": "V only",  "desc": "style transfer w=0.8 ★推奨"},
    {"id": "ST_w10",  "weight": 1.0, "weight_type": "style transfer",        "embeds_scaling": "V only",  "desc": "style transfer w=1.0"},
    {"id": "ST_w12",  "weight": 1.2, "weight_type": "style transfer",        "embeds_scaling": "V only",  "desc": "style transfer w=1.2"},

    # Phase 2: strong style transfer
    {"id": "SST_w08", "weight": 0.8, "weight_type": "strong style transfer", "embeds_scaling": "V only",  "desc": "strong style transfer w=0.8"},
    {"id": "SST_w10", "weight": 1.0, "weight_type": "strong style transfer", "embeds_scaling": "V only",  "desc": "strong style transfer w=1.0"},

    # Phase 3: style transfer precise（構図漏れ防止版）
    {"id": "STP_w08", "weight": 0.8, "weight_type": "style transfer precise","embeds_scaling": "V only",  "desc": "style transfer precise w=0.8"},

    # Phase 4: K+V embeds_scaling（より強い転写）
    {"id": "KV_w08",  "weight": 0.8, "weight_type": "style transfer",        "embeds_scaling": "K+V",     "desc": "style transfer w=0.8 K+V"},
]


def build_workflow(pattern: dict, seed: int) -> dict:
    """IPAdapter style transfer ワークフローを構築"""
    return {
        # CheckpointLoader
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {
                "ckpt_name": CHECKPOINT
            }
        },
        # IPAdapter Unified Loader（PLUS preset で自動読み込み）
        "2": {
            "class_type": "IPAdapterUnifiedLoader",
            "inputs": {
                "model": ["1", 0],
                "preset": "PLUS (high strength)"
            }
        },
        # 参照画像（咲の基準画像）
        "3": {
            "class_type": "LoadImage",
            "inputs": {
                "image": REFERENCE_IMAGE
            }
        },
        # IPAdapter Advanced（スタイル転写）
        "4": {
            "class_type": "IPAdapterAdvanced",
            "inputs": {
                "model": ["2", 0],
                "ipadapter": ["2", 1],
                "image": ["3", 0],
                "weight": pattern["weight"],
                "weight_type": pattern["weight_type"],
                "start_at": 0.0,
                "end_at": 1.0,
                "combine_embeds": "concat",
                "embeds_scaling": pattern["embeds_scaling"]
            }
        },
        # ポジティブプロンプト
        "5": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": SHOTA_POSITIVE,
                "clip": ["1", 1]
            }
        },
        # ネガティブプロンプト
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": SHOTA_NEGATIVE,
                "clip": ["1", 1]
            }
        },
        # Empty Latent
        "7": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": WIDTH,
                "height": HEIGHT,
                "batch_size": 1
            }
        },
        # KSampler
        "8": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["4", 0],
                "positive": ["5", 0],
                "negative": ["6", 0],
                "latent_image": ["7", 0],
                "seed": seed,
                "steps": STEPS,
                "cfg": CFG,
                "sampler_name": SAMPLER,
                "scheduler": SCHEDULER,
                "denoise": 1.0
            }
        },
        # VAE Decode
        "9": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["8", 0],
                "vae": ["1", 2]
            }
        },
        # Save Image
        "10": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["9", 0],
                "filename_prefix": f"ipa_{pattern['id']}"
            }
        }
    }


def queue_prompt(workflow: dict) -> str:
    """ComfyUI にプロンプトを送信"""
    payload = json.dumps({"prompt": workflow}).encode("utf-8")
    req = urllib.request.Request(
        f"{COMFYUI_URL}/prompt",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    resp = urllib.request.urlopen(req, timeout=30)
    result = json.loads(resp.read())
    return result.get("prompt_id", "unknown")


def wait_for_completion(prompt_id: str, timeout: int = 300) -> bool:
    """生成完了を待つ（最大timeout秒）"""
    start = time.time()
    while time.time() - start < timeout:
        try:
            resp = urllib.request.urlopen(f"{COMFYUI_URL}/history/{prompt_id}", timeout=10)
            history = json.loads(resp.read())
            if prompt_id in history:
                return True
        except Exception:
            pass
        time.sleep(5)
    return False


def main():
    print("=" * 60)
    print("IPAdapter スタイル転写テスト")
    print(f"チェックポイント: {CHECKPOINT}")
    print(f"参照画像: {REFERENCE_IMAGE}")
    print(f"テストパターン: {len(TEST_PATTERNS)}種")
    print("=" * 60)

    base_seed = random.randint(100000000, 999999999)
    print(f"ベースシード: {base_seed}")

    results = []
    for i, pattern in enumerate(TEST_PATTERNS):
        seed = base_seed + i
        print(f"\n--- [{i+1}/{len(TEST_PATTERNS)}] {pattern['id']}: {pattern['desc']} (seed={seed}) ---")

        workflow = build_workflow(pattern, seed)

        try:
            prompt_id = queue_prompt(workflow)
            print(f"  キュー投入: prompt_id={prompt_id}")
        except urllib.error.URLError as e:
            print(f"  ❌ キュー投入失敗: {e}")
            results.append({"id": pattern["id"], "status": "QUEUE_FAIL", "error": str(e)})
            continue

        print(f"  生成待機中...", end="", flush=True)
        success = wait_for_completion(prompt_id, timeout=300)
        if success:
            print(f" ✅ 完了")
            results.append({"id": pattern["id"], "status": "OK", "seed": seed})
        else:
            print(f" ❌ タイムアウト (300s)")
            results.append({"id": pattern["id"], "status": "TIMEOUT", "seed": seed})

    # 結果サマリー
    print("\n" + "=" * 60)
    print("結果サマリー")
    print("=" * 60)
    for r in results:
        status_icon = "✅" if r["status"] == "OK" else "❌"
        print(f"  {status_icon} {r['id']}: {r['status']}")

    print(f"\n出力先: /Applications/Data/Packages/ComfyUI/output/ipa_*")
    print(f"確認: ls /Applications/Data/Packages/ComfyUI/output/ipa_* | sort")
    print("\n★評価ポイント:")
    print("  1. 咲(S1)と同じグレースケール画風になっているか")
    print("  2. オレンジアーティファクトが消えているか")
    print("  3. faceless maleが正しく動作しているか")
    print("  4. 線の繊細さ・シェーディングのグレートーンが出ているか")


if __name__ == "__main__":
    main()
