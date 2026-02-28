# SD1.5 実験記録（2026-02-28）— 結論: 失敗・非推奨

## 経緯
- 「白黒漫画ならSD1.5で十分では？」という仮説を検証
- Option B（SD1.5をラフ出しツールとして併用）を選択して実装

## ダウンロードしたSD1.5モデル
すべて `/Applications/Data/Packages/ComfyUI/models/` 配下:
- `checkpoints/AnythingV5-Prt-RE.safetensors` (2.0GB)
- `loras/manga_general_marvin.safetensors` (144MB) — MANGA General LoRA
- `loras/manga_master_v2.safetensors` (9.1MB) — Manga Master v2 LoRA
- `loras/detail_tweaker.safetensors` (36MB) — Detail Tweaker LoRA
- `controlnet/control_v11p_sd15_canny_fp16.safetensors` (689MB)
- `controlnet/control_v11p_sd15_lineart_fp16.safetensors` (689MB)
- `controlnet/control_v11p_sd15s2_lineart_anime_fp16.safetensors` (689MB)
- `controlnet/control_v11p_sd15_openpose_fp16.safetensors` (689MB)
※ 削除してもOK（使う予定なし）

## テストスクリプト（すべて `/Users/shuhei.sugai/Documents/sta/`）
1. `comfyui_sd15_manga_test.py` — v1: 基本テスト、品質ひどい
2. `comfyui_sd15_manga_test2.py` — v2: キャラ設定投入、まだ低品質
3. `comfyui_sd15_manga_test3.py` — v3: 設定全面改訂、改善するも不十分
4. `comfyui_sd15_color_test.py` — カラーvs モノクロ比較
5. `comfyui_shota_sdxl.py` — SDXL beretMixMangaで翔太テスト（タイムアウト）

## 失敗の理由

### 1. 速度メリットなし（Mac MPS）
- SD1.5: ~75-110秒/枚
- SDXL: ~65-90秒/枚
- **Mac MPSではSD1.5が速くない**（NVIDIA CUDAでのみ20-35倍速い）

### 2. モノクロ制御が不安定
- `(monochrome:1.3-1.4)` → シルエット化・黒潰れ
- `monochrome`（weight 1.0）→ 色漏れ
- 安定するスイートスポットがない

### 3. faceless maleタグが効かない
- SD1.5では `(faceless male:1.5)` が無視される
- SDXL（beretMixManga）では `(faceless male:1.6)` で動作確認済み

### 4. LoRAスタッキング問題
- Manga Master + MANGA General の同時使用はNG（Manga Master側が他LoRAを上書き）
- 正しくは Manga Master 0.6 単体 + Detail Tweaker 0.5

### 5. AnythingV5の特性
- カラーならそこそこの品質が出る（ただしSDXLには遠く及ばない）
- モノクロ線画に特化していない
- taziku（https://note.com/taziku/n/n21ad2b0ebfb6）等のクリエイターが同じチェックポイントで高品質を出しているが、設定だけでは到達できない

## テスト詳細

### v1: 基本テスト（comfyui_sd15_manga_test.py）
- 3シーン（女の子立ち絵/カップル会話/玄関背景）
- euler_ancestral / Steps 20 / CFG 7
- Manga Master 1.0 + MANGA General 0.5 同時使用 → LoRA干渉でシルエット化
- monochrome:1.3-1.4 → 黒潰れ
- **結果: 品質ひどい**

### v2: キャラ設定投入（comfyui_sd15_manga_test2.py）
- 6シーン（咲後ろ姿/咲顔アップ/翔太faceless/丸山/玄関背景/LoRAなし比較）
- dpmpp_2m karras / Steps 25-28 に変更
- monochrome weightなし(1.0)に下げた
- **結果: モノクロ漏れ（カラーが出る）、faceless male効かない、2人シーン崩壊**

### v3: 設定全面改訂（comfyui_sd15_manga_test3.py）
- Manga Master 0.6 単体 + Detail Tweaker 0.5 に変更
- CFG 5.5に下げた
- 品質タグ追加（extremely detailed, highres）
- **結果: v2より改善したが不十分。モノクロ制御相変わらず不安定**

### カラー比較（comfyui_sd15_color_test.py）
- モノクロが問題なのか確認 → カラーで同じキャラを生成
- **結果: カラーでもひどい。SDXLのberetMixMangaと比較にならない**

### SDXL翔太テスト（comfyui_shota_sdxl.py）
- SD1.5→SDXLのチェックポイント切り替えで全タイムアウト
- beretMixMangaで翔太を再生成する試みだったが完了せず

## ユーザーからの重要フィードバック
- 「サンプルの絵が酷すぎる。もっと工夫して」
- 「二度とこの品質で出さないでほしい」
- 「カラーでもひどい」
- 「もうこれ以上ないってくらい調べた？」
- 「だからSD1.5とかじゃないと思うよ、昨日beretMixMangaでこの画像なんだから。根本に問題がある」
- **→ 品質に対する要求は非常に高い。中途半端な品質で提示しないこと**

## 学んだこと
- SD1.5の「20-35倍速い」はNVIDIA CUDA限定。Mac MPSでは恩恵なし
- SD1.5のモノクロ制御は不安定（weightの調整幅が極めて狭い）
- faceless maleはSDXL系でしか安定動作しない
- LoRAは基本1つ（+ Detail Tweaker程度）に絞るのが正解
- **根本問題はSD1.5 vs SDXLではなく、キャラ間のスタイル一貫性**
