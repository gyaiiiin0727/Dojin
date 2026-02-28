# キャラ間スタイル一貫性問題（2026-02-28特定）

## 問題の本質
咲と翔太をberetMixMangaで生成すると、**同じ漫画のキャラに見えない**。

### 咲（heroine_ponytail LoRA あり）
- 美しいグレースケールイラスト
- 繊細なシェーディング、プロ品質
- LoRAが画風を強力にガイドしている

### 翔太（LoRA なし + faceless male）
- 粗い線画
- beretMixMangaのセピア色がオレンジ線のアーティファクトに
- faceless maleで情報量が減り、スタイルの手がかりも減る
- 白背景との相性問題がより顕著

## 原因分析
1. **LoRA有無の画質差**: heroine_ponytail LoRAが咲の品質を大幅に底上げしている
2. **beretMixManga + 白背景 = オレンジアーティファクト**: 既知の問題だが、LoRAなしキャラではより深刻
3. **faceless maleの情報量不足**: 顔がないとモデルがスタイルを安定させる手がかりが減る
4. **キャラ固有LoRAがないキャラの品質下限が低い**

## 検討すべき解決策（未実装）

### A: 翔太専用LoRA学習
- 咲と同じ画風で翔太の画像を複数生成 → LoRA学習
- メリット: 根本解決になりうる
- デメリット: 学習データの品質が低い（今の翔太画像が低品質なので）

### B: waiIllustriousで全キャラ統一
- 背景に使っているwaiIllustriousはクリーンなモノクロ線画が得意
- 全キャラをwaiIllustriousで統一すれば画風は揃う
- デメリット: 咲のberetMixManga品質を捨てることになる

### C: IPAdapterでスタイル転写
- 咲の生成画像をIPAdapterの参考画像として翔太に適用
- スタイルだけ転写、キャラ特徴は別プロンプトで制御
- メリット: 既にIPAdapter環境構築済み
- デメリット: weight調整が難しい（咲のテストでは顔が幼くなった実績あり）

### D: Regional Prompting / Attention Couple
- comfyui-prompt-control（MASK構文）をインストール
- 1枚の中で領域ごとに異なるプロンプト・LoRAを適用
- 2人以上のキャラが1コマに入るシーンで必須
- ※ 今回は別々に生成→クリスタで合成なので優先度は低い

### E: 共通スタイルLoRA（Mnga-illustriousXL等）で統一
- キャラLoRA（heroine_ponytail）の代わりに画風LoRA（Mnga-illustriousXL等）で全キャラ統一
- メリット: 画風が揃いやすい
- デメリット: 咲の顔の再現度が下がる

## 参考: 同じチェックポイントで高品質を出している事例
- taziku（https://note.com/taziku/n/n21ad2b0ebfb6）
- 同じAnythingV5等でもプロ品質の漫画を出している
- プロンプトだけの問題ではなく、LoRA・ワークフロー・後処理の総合力

## ユーザーの見解
- 「だからSD1.5とかじゃないと思うよ、昨日beretMixMangaでこの画像なんだから。根本に問題がある」
- 「同じ漫画で出てくる人？」（翔太と咲の比較を見て）→ 明らかにNO
- 問題の焦点はモデル選択ではなく、**キャラ間の画風統一**
- SD1.5実験で時間を無駄にしたことへの強い不満
- **品質が低いまま提示すると信頼を失う → 十分に調査・検証してから提示すること**

## 試したが失敗したアプローチ
- ❌ SD1.5（AnythingV5）でラフ出し → Mac MPSで速度メリットなし、品質不足 → [詳細](sd15_experiment.md)
- ❌ Mnga-illustriousXL（0.8/1.0）→ セピア色残る、solo崩壊、黒潰れ
- ❌ waiIllustrious（LoRAなし/Mnga併用）→ 緑色味、シルエット化
- △ ThickOutline 0.7 → B&Wは出るがグレートーンなし（ベタ黒すぎ）
- ❌ ThickOutline 0.3〜0.5 → weight下げてもグレートーン出ず、solo崩壊多発

## セッション④テスト結果（2026-02-28）

### Phase 1: LoRA単体テスト（7枚）✅完了
| ID | 設定 | 結果 |
|----|------|------|
| T1 | beretMixManga + LoRAなし | ❌ 黄色い線 |
| T2 | beretMixManga + Mnga 0.8 | ❌ セピア + solo崩壊 |
| T3 | beretMixManga + Mnga 1.0 | ❌ 同上 |
| T4 | waiIllustrious + LoRAなし | ❌ 緑色味 |
| T5 | waiIllustrious + Mnga 0.8 | ❌ 黒潰れシルエット |
| T6 | beretMixManga + ThickOutline 0.7 | ⭐ B&W OK だがベタ黒 |
| S1 | beretMixManga + heroine_ponytail 0.9 | ✅ 目標品質 |

### Phase 2: ThickOutline weight調整（12枚中7枚生成で中断）
- 0.3/0.4: solo崩壊多発、ベタ黒変わらず
- **結論: ThickOutline単体では画風ガイド力が不足**

### 根本原因の確定
- heroine_ponytail LoRAは「キャラ」だけでなく**画風全体をガイド**している
- ThickOutlineは線の太さだけ。画風（グレートーン、シェーディング）のガイド力がない
- **LoRAなしキャラにはIPAdapterスタイル転写が必要**

## 次のアクション ← ★ここから再開
1. **`ip-adapter-plus_sdxl_vit-h.safetensors`（848MB）をDL**
   - URL: `https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors`
   - 配置先: `/Applications/Data/Packages/ComfyUI/models/ipadapter/`
   - CLIPエンコーダーは既存の `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` を流用（追加DL不要）
2. **IPAdapter Advanced + style transfer で翔太を生成**
   - 参照画像: `style_S1_saki_baseline_00001_.png`（咲の基準画像）
   - weight_type: `style transfer`（UNetレイヤー6のみ）
   - weight: 0.8 → 0.6〜1.2で調整
   - ワークフロー: Checkpoint → IPAdapter Unified Loader(PLUS) → IPAdapter Advanced → KSampler
   - `style transfer precise` も試す（構図漏れ防止版）
3. **良ければ P1コマ3 本番画像を生成**
4. **最終手段: 翔太LoRA学習**

## 重要な制約
- **中途半端な品質で見せない**: 十分に調査・テストしてから提示
- **SD1.5は選択肢から除外**: Mac MPS環境では使い物にならない
- **SDXLのberetMixManga環境で解決する**: 他モデルに逃げない
