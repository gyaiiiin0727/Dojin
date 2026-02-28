# sta プロジェクト メモリ

## ユーザーの好み・作業スタイル
- **品質に対する要求が非常に高い**:
  - 中途半端な品質で提示しない。十分に調査・検証してから見せる
  - 「二度とこの品質で出さないでほしい」「もうこれ以上ないってくらい調べた？」← 実際の発言
  - 時間の無駄になるアプローチは早めに切り上げる
- **プロンプトを提示するときのフォーマット**:
  - 基本いじらない部分（①品質 → ②キャラ → ⑦男 → ⑪ライティング）を上から順に並べる
  - 変える部分（④構図・ポーズ、⑤体位、⑥表情、⑧カメラ、⑨背景、⑩フレーミング）は★印で区別
  - 各タグが何の指示をしているか日本語で説明を添える
  - そのままComfyUIに貼れる形で渡す（日本語コメントは入れない）
- **プロンプト分析時**: 構造化して番号付きセクションで説明
- **参考にしている人**: ninoさん（chichi-pui）、ukkrippさん、tazikuさん（note.com）

## プロジェクト情報
- 画像生成AI全般のプロジェクト
- ComfyUI を使用（パス: /Applications/Data/Packages/ComfyUI/）
- ベースモデル: hassakuXL（Illustrious系）→ チェックポイント比較で複数使い分けに移行

## 詳細ファイルへのリンク
- [LoRA比較テスト記録](lora_comparison.md) — LoRA比較テスト・nino画風再現・全プロンプト
- [タグリファレンス](tag_reference.md) — 体位・構図・ポーズタグの日英対応＋注意点
- [Dayce PWA](dayce_pwa.md) — ライフログPWAアプリ開発メモ（Stripe本番・難読化・リリース状況）
- [SD1.5実験記録](sd15_experiment.md) — SD1.5テスト全記録・結論:失敗（2026-02-28）
- [スタイル一貫性問題](style_consistency_problem.md) — キャラ間画風統一の課題・解決策候補（2026-02-28）

## 制作物一覧
1. `同人誌_ストーリー構成_完全版_v4.md` — ストーリー＋セリフ（全49P）
2. `同人誌_コマ割り指示書_全49P.md` — コマ割り＋構図＋演出
3. `同人誌_プロンプト集_全49P.md` — 画像生成プロンプト
4. `checkpoint_comparison_test.md` — チェックポイント比較用10シーン
5. `comfyui_batch_test.py` — ComfyUI APIバッチ実行スクリプト（autismmix vs pony比較用）
6. `comfyui_pony_20scenes.py` — prefectPonyXL 20シーンx3枚バッチ
7. `comfyui_pony_batch2.py` — 残り17+追加20シーンバッチ
8. `comfyui_pony_vs_illustrious.py` — Pony vs Illustrious 10シーン比較スクリプト
9. `comfyui_p1_panels.py` — P1コマ2（バッグ手）＋コマ3（翔太顔）生成スクリプト
10. `comfyui_sd15_manga_test.py` — SD1.5 v1テスト（失敗・参考用）
11. `comfyui_sd15_manga_test2.py` — SD1.5 v2テスト（失敗・参考用）
12. `comfyui_sd15_manga_test3.py` — SD1.5 v3テスト（失敗・参考用）
13. `comfyui_sd15_color_test.py` — SD1.5カラーvs モノクロ比較（失敗・参考用）
14. `comfyui_shota_sdxl.py` — SDXL beretMixManga翔太テスト
15. `comfyui_style_consistency_test.py` — スタイル一貫性テスト（翔太6パターン+咲1パターン）✅実行済
16. `comfyui_shota_refined2.py` — ThickOutline weight調整テスト（0.3〜0.6×3シード）途中中断

## 登場人物
- 咲（人妻・主人公）、丸山（上司・悪役）、翔太（旦那）

### 翔太（旦那）キャラ設定 ※2026-02-28変更
- **性格**: 気が弱い、優しいけど頼りない、咲に頭が上がらない、おどおど
- **容姿**: **faceless male方式**（顔を描かない）、暗い茶髪、ほんのちょっとボサボサ、やや細め
- **服装（普段）**: Tシャツ、スウェット（部屋着）
- **印象**: いい人だけど頼りない。咲を大事にしてるが言葉にできないタイプ
- **旧設定から変更**: 「前髪で目隠し」→「faceless male（顔なし）」（2026-02-28）
- **プロンプト（ポジティブ）**:
```
score_9, score_8_up, score_7_up, source_anime,
HDR, 8K, (best quality),
glossy body, shiny skin, volumetric lighting,
BREAK
(faceless male:1.6), 1boy, solo,
(young adult male:1.2), (adult man:1.2),
(slightly messy hair:1.1), (dark brown hair:1.2), (short hair:1.1),
(slim build:1.2), (narrow shoulders:1.1), (thin neck:1.1),
plain white t-shirt, sweatpants,
BREAK
★ ここにカメラ・フレーミング
★ ここに背景
```
- **プロンプト（ネガティブ）**:
```
(worst quality), (low quality), (normal quality), watermark,
bad anatomy, bad hands,
(detailed face:1.3), (detailed eyes:1.3), (face:1.2),
(girl:1.3), (female:1.3), (1girl:1.4),
(muscular:1.3), (broad shoulders:1.2),
(child:1.4), (boy:1.3), (shota:1.4), (baby face:1.3), (teenage:1.3),
(ugly:1.2), (dirty:1.2),
speech bubble, text,
negativeXL_D
```

## 現在のステータス（2026-02-28更新）

### 確定済み
- ✅ 咲の肌質感・体型（メリハリ体型: slim waist + wide hips + slim legs）
- ✅ 丸山のキャラデザ（髪型: crew cut、体型: chubby:1.1 + belly:1.2）
- ✅ IPAdapterセットアップ（PLUS FACE portraits, ワークフロー「最終」に保存）
- ✅ LoRA学習 heroine_ponytail 完了
- ✅ negativeXL_D エンベディング導入済み
- ✅ ntr_face.txt ワイルドカード修正（アヘ顔削除→歯を食いしばる系に）
- ✅ **画風確定: beretMixManga_v30**（漫画調セピア風）
- ✅ **表情**: `embarrassed, clenched teeth`（weight無し）で安定
- ✅ **全チェックポイント比較完了**（6モデル比較済み）
- ✅ **ComfyUI API自動化**: Pythonスクリプトでバッチ生成できるようになった
- ✅ **Imminent Penetration LoRA 導入済み**
- ✅ **ワイルドカード整理完了**（2026-02-23）
- ✅ **インペイントワークフロー構築済み**（「修正」タブ）
- ✅ **各種プロンプト分析・咲バージョン変換**（複数パターン作成）
- ✅ **翔太キャラ方針: faceless male方式に確定**（2026-02-28）
- ✅ **咲の後ろ向きプロンプト作成**（完全背中向き・ヒール履き）
- ✅ **SD1.5実験 → 失敗確定**（速度メリットなし・品質低い・faceless効かない）→ [詳細](sd15_experiment.md)
- ⚠️ **rembg導入**: venvインストール済みだがComfyUIノード未表示（要調査）
- ❌ **キャラ間スタイル一貫性問題**: 咲と翔太が同じ漫画に見えない → [詳細](style_consistency_problem.md)

### ★★★ 最重要課題: キャラ間スタイル一貫性 ★★★
- 咲（heroine_ponytail LoRA）= 美しいグレースケールイラスト
- 翔太（LoRAなし + faceless）= 粗い線画 + オレンジアーティファクト
- **同じ漫画のキャラに見えない** ← これが根本問題
- 解決策候補: IPAdapter / 共通スタイルLoRA / 翔太LoRA学習 → [詳細](style_consistency_problem.md)

### 進行中 — IPAdapterスタイル転写テスト ← ★次のセッションここから

**2026-02-28セッション④（テスト実行〜IPAdapter調査）でやったこと:**
1. **スタイル一貫性テスト（7枚）実行 → 全枚完了**
   - T1（LoRAなし）: ❌ 黄色い線（既知のオレンジ問題）
   - T2（Mnga 0.8）: ❌ セピア茶色 + solo崩壊（2人出る）
   - T3（Mnga 1.0）: ❌ T2と同傾向
   - T4（waiIllustrious）: ❌ 緑がかった色味
   - T5（wai+Mnga 0.8）: ❌ 黒潰れシルエット
   - **T6（ThickOutline 0.7）: ⭐最有力** クリーンB&W、faceless動作OK
   - S1（咲 基準）: ✅ 繊細なグレースケール線画
   - **結論: T6が一番近いがグレートーン不足（ベタ黒すぎ）**
2. **ThickOutline weight調整テスト（R1〜R4, 各3シード）**
   - R1（0.3）3枚: solo崩壊多発、緑アーティファクト、ベタ黒変わらず
   - R2（0.4）3枚: 同傾向
   - R3（0.5）1枚生成で中断
   - **結論: ThickOutline単体では画風ガイド力が不足。weightを下げてもグレートーンは出ない**
3. **IPAdapter PLUSスタイル転写の徹底調査**
   - **DL必要ファイル**: `ip-adapter-plus_sdxl_vit-h.safetensors`（848MB）
     - URL: `https://huggingface.co/h94/IP-Adapter/resolve/main/sdxl_models/ip-adapter-plus_sdxl_vit-h.safetensors`
     - 配置先: `/Applications/Data/Packages/ComfyUI/models/ipadapter/`
   - 現在のFACEモデル（ip-adapter-plus-face）はスタイル転写に使えない
   - **CLIPエンコーダーは既存のものが流用可能**（追加DL不要）
   - **weight_type = "style transfer"**: SDXLのUNetレイヤー6のみに作用。画風（線の質、シェーディング、色調）を転写しキャラは変えない
   - **推奨設定**: weight 0.8、steps 30+、cfg 7-8
   - **ワークフロー**: CheckpointLoader → IPAdapter Unified Loader(PLUS preset) → IPAdapter Advanced(style transfer) → KSampler
   - 咲の高品質画像を参照画像として入力 → 翔太プロンプトで生成 → 咲の画風で翔太が出る
   - `style transfer precise` = 構図漏れを防ぐ精密版もある
4. **GitHub認証**: Claude Code内からの`gh auth login`はインタラクティブ入力がタイムアウトする → 別ターミナルから実行する必要あり（未完了）

**★次のセッションでやること（優先順）:**
1. `ip-adapter-plus_sdxl_vit-h.safetensors`（848MB）をDL
2. IPAdapter Advanced + style transfer weight_type で翔太を生成
   - 参照画像: S1（咲の基準画像 `style_S1_saki_baseline_00001_.png`）
   - weight 0.8 から開始、0.6〜1.2で調整
3. 結果が良ければ P1コマ3 用の翔太本番画像を生成
4. GitHub認証 → MEMORY.md push

**2026-02-28セッション③（スタイル一貫性調査〜テスト準備）でやったこと:**
1. **3並列エージェントで徹底調査**
   - IPAdapterスタイル転写の正しい使い方（style transfer weight_type）
   - Mnga-illustriousXL / ThickOutline LoRAの活用法
   - waiIllustriousでの全キャラ統一アプローチ
2. **重要な発見**
   - 現在のIPAdapterはFACE用（顔転写）→ スタイル転写にはPLUSモデルが必要
   - Mnga-illustriousXL（手持ち）がモノクロ線画特化 → 翔太に適用で画風統一の可能性
   - IPAdapterのstyle transfer weight_type = SDXLレイヤー6のみに作用
3. **テストスクリプト作成・実行済み**（セッション④で実行）

**2026-02-28セッション②（SD1.5実験〜スタイル問題特定）でやったこと:**
1. **AI漫画制作サイト徹底調査**（50+日本語サイト、英語リソース多数）
   - キャラ書き分け手法: LoRA個別学習、Regional Prompting、Attention Couple
   - 背景描写: ControlNet Canny/Depth、waiIllustrious推奨
2. **SD1.5実験（Option B: ラフ出しツール）→ 完全失敗**
   - AnythingV5 + Manga Master/MANGA General LoRA + Detail Tweaker ダウンロード
   - SD1.5 ControlNet 4種ダウンロード
   - テスト4回（v1基本/v2キャラ投入/v3設定改訂/カラー比較）→ すべて品質不足
   - v1: LoRA干渉でシルエット化、monochrome高weightで黒潰れ
   - v2: モノクロ漏れ（カラーが出る）、faceless male効かない
   - v3: Detail Tweaker追加・CFG下げ → 改善するも不十分
   - カラー比較: カラーでもSDXLに遠く及ばない品質
   - **Mac MPSではSD1.5は速くない**（~75-110s vs SDXL 65-90s）
   - tazikuさん（note.com/taziku/n/n21ad2b0ebfb6）が同チェックポイントで高品質出してるが設定だけでは到達不可
   - → [SD1.5実験の全記録](sd15_experiment.md)
3. **SDXL翔太再生成テスト → タイムアウト**
   - `comfyui_shota_sdxl.py` でberetMixManga翔太をSDXLで再生成試行
   - SD1.5→SDXLのチェックポイント切替で+60秒以上かかり全タイムアウト
   - 結果確認できず
4. **根本問題を特定: キャラ間スタイル一貫性**
   - ユーザーがberetMixMangaで生成した翔太（P1コマ3候補）と咲を比較
   - 翔太: オレンジ線アーティファクト、粗い線画（SD1.5テスト結果と同程度の品質）
   - 咲: 美しいグレースケールイラスト（heroine_ponytail LoRAあり）
   - 「同じ漫画で出てくる人？」→ 明らかにNO
   - SD1.5 vs SDXLの問題ではなく、**LoRA有無による画質差が本質**
   - → [スタイル一貫性問題の詳細](style_consistency_problem.md)
5. **ユーザーからの重要フィードバック**
   - 品質が低い画像を提示すると時間の無駄でやる気を失う
   - 十分に調査してから提示すること
   - SD1.5に逃げるのは根本解決にならない

**2026-02-28セッション①でやったこと:**
1. **プロンプト構成分析**（えっちシーンの4セクションBREAK構成を解説）
2. **咲の後ろ向きプロンプト作成**（完全背中向き・ヒール履き途中）
3. **翔太のキャラ方針変更: faceless male方式に決定**
4. **rembg導入**（venvインストール済み、ノード未表示問題残存）
5. **リモートコントロール**: ターミナルから `claude remote-control` で動作確認済み（Claude Code内からは不可）

**2026-02-26セッション②（続き）でやったこと:**
1. **クリスタ合成方法を修正: 乗算→通常モードに変更**
   - 乗算モードだと白ブラウス等も透けてしまう問題を発見
   - **正しい方法**: 咲レイヤーをラスタライズ → 彩度-100（完全モノクロ化）→ 自動選択ツール(`W`)で外側の白背景を選択 → Delete → 合成モードを「通常」に
   - これで白ブラウスは不透明のまま、背景だけ透明になる
2. **背景ドアノブ貫通問題の対処**
   - 背景レイヤーをラスタライズ → 白ブラシ(`B`)でドアノブ部分を塗りつぶし
   - 消しゴムだと透明になるので白ブラシが正解
3. **クリスタ操作ノウハウ蓄積**（後述のセクション参照）
4. **P1コマ構成を変更**（顔見せ演出のため）
   - コマ1: 大ゴマ（咲の後ろ姿）— 既存
   - コマ2: バッグを持つ手のアップ — NEW
   - コマ3: 翔太の顔 — 変更（旧: 咲）
5. **P2を追加: 咲の顔アップ「いってきます！」**（メインヒロイン紹介ページ）
6. **コマ2・3の画像生成開始**（`comfyui_p1_panels.py`）
   - バッグを持つ手: 3パターン（bag_a/b/c）→ **bag_aが最有力**（結婚指輪+取っ手）
   - 翔太の顔: 3パターン（shota_a/b/c）→ 前髪で目が隠れて頼りない感じ◎

**2026-02-26セッション①でやったこと:**
1. **漫画背景プロンプト徹底調査** → 完全ガイド作成
2. **ControlNet環境構築完了**
   - `comfyui_controlnet_aux` プラグイン インストール
   - `controlnet-union-sdxl-promax.safetensors` (2.3GB) ダウンロード
   - Canny/Lineart/Depth等オールインワン対応
3. **Mnga-illustriousXL LoRA導入** (`Mnga-illustriousXL_v01_V1-CAME.safetensors` 338MB)
   - トリガー: `monochrome` / weight: 1.0 / 漫画モノクロ特化
4. **背景生成方式確定: waiIllustrious + ControlNet Canny 0.8**
   - 参考写真→Canny前処理→ControlNet→モノクロ線画背景
   - beretMixMangaはセピア色がオレンジ線になるので背景には不向き
   - waiIllustriousが最もクリーンな白背景モノクロ線画を出す
5. **P1コマ1 玄関背景 本番サイズ生成完了** (`p1bg_final_2_00001_.png`)
6. **P1コマ1 咲の後ろ姿 本番サイズ生成完了** (`p1c1_heels_final_00001_.png`)
   - パンツスタイル + ヒール履く動作（片足上げ）
   - beretMixManga + heroine_ponytail 0.9 + 白背景
7. **クリスタで合成テスト成功**（→ セッション②で方法修正）
8. **P1セリフ確定**
9. **咲の初期衣装: パンツスタイル**（丸山に染まってからミニスカに変わる演出）

**2026-02-25セッションでやったこと:**
1. 漫画制作開始 — 1コマ1枚で直接生成する方式に決定
2. **画風方針確定**: 日常パート=モノクロ線画調 / えっちパート=beretMixMangaセピア調
3. CLIP STUDIO PAINT EX でコミック新規作成（B5/600dpi/7ページ）
4. コマ割り・セリフ入力を開始
5. **ストーリー変更**: 新P1（出社の朝シーン）を追加、旧P1-P6が1ページずつ後ろにずれて計7P
6. **翔太のキャラ変更**: だらしない→弱々しい・頼りない（前髪が目にかかる容姿）
7. 全7ページ分のセリフを翔太の新キャラに合わせて更新
8. P1コマ1（咲の後ろ姿・玄関ドア）のモノクロ線画生成テスト成功
9. クリスタの操作方法を調査・まとめ

### P1 セリフ確定版（コマ構成変更後）
```
コマ1（大ゴマ：咲の後ろ姿＋玄関背景）
  咲「久しぶりの出勤だし、こういうのは初日が大事だから」

コマ2（バッグを持つ手のアップ）
  （セリフなし or ナレーション）

コマ3（翔太の顔）
  翔太「…もう行くの？」
```

### P2 構成（NEW — メインヒロイン紹介ページ）
```
コマ1（大ゴマ：咲の顔アップ）
  咲「いってきます！」

コマ2（翔太・小さく）
  翔太「…いってらっしゃい」
```
※P1で顔を見せず、P2で初めて顔見せ → 漫画の王道テクニック
※「育休明け」はP1-P2では明示しない → 丸山との飲みシーンで「育休明けで大変だろ」と自然に出す

### 咲の衣装変化（演出方針）
- **序盤（日常パート）**: パンツスタイル（dress pants + blouse + high heels）
- **丸山に染まってから**: ミニスカ・タイトスカートに変化
- 衣装の変化で堕ちていく過程を視覚的に表現

### 漫画背景生成 確定設定
**チェックポイント:** waiIllustriousSDXL_v160.safetensors（背景専用）
**ControlNet:** controlnet-union-sdxl-promax.safetensors / Canny / strength 0.8
**参考画像:** ComfyUI input/ に保存 → Canny前処理 → 生成
**プロンプトテンプレート（背景用）:**
```
score_9, score_8_up, score_7_up,
(masterpiece, best quality:1.2),
no humans, scenery, indoors,
(monochrome:1.4), (greyscale:1.3), (lineart:1.2),
BREAK
[場所のタグ],
detailed background,
```
**ネガティブ（背景用）:**
```
(worst quality), (low quality), (normal quality),
(color:1.3), (colorful:1.3),
1girl, 1boy, person, human, character,
speech bubble, text, watermark,
blurry, noise,
negativeXL_D
```

### 咲モノクロ線画プロンプト（日常パート用）
**チェックポイント:** beretMixManga_v30.safetensors
**LoRA:** heroine_ponytail_lora 0.9
```
score_9, score_8_up, score_7_up, source_anime,
(best quality),
(monochrome:1.4), (greyscale:1.3), (lineart:1.2),
manga, ink drawing,
simple background, white background,
BREAK
heroine_ponytail,
1girl, solo, [ポーズ・構図],
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2),
(adult woman:1.2), mature female,
(slim waist:1.3), slender limbs,
office lady, white blouse, (dress pants:1.3),
[フレーミング],
```
**ネガティブ:**
```
(worst quality), (low quality), (normal quality),
(color:1.3), (colorful:1.3),
bad anatomy, bad hands, (bad feet:1.4),
(deformed legs:1.3), (extra limbs:1.4),
speech bubble, text, watermark,
blurry, noise,
(face:1.2), (looking at viewer:1.3),
background, scenery, room,
(skirt:1.4), (miniskirt:1.4),
negativeXL_D
```

### モノクロ線画調プロンプトのコツ（調査結果）
- `(monochrome:1.4), (greyscale:1.3), (lineart:1.2), manga, ink drawing`
- ネガティブに `(color:1.3), (colorful:1.3)`
- beretMixMangaでモノクロ線画が出せるが、**オレンジ線になりがち**
- **背景はwaiIllustriousが最もクリーン**（白い壁+きれいな線画）
- ControlNet Cannyで参考写真の構図を忠実に再現できる
- strength 0.8で参考画像にかなり忠実、0.5-0.6だと自由度高い
- **スクリーントーンはAIより クリスタのトーン機能が高品質**
- **ハイブリッドワークフロー推奨**: AI 80% + クリスタ手修正 20%
- **色の単語を避ける**: プロンプトに red, blue 等入れるとモノクロが崩れる
- CFG 7がモノクロ線画に安定

### 導入済みLoRA一覧（最新）
**SDXL用:**
- heroine_ponytail_lora.safetensors — 咲のキャラLoRA
- Mnga-illustriousXL_v01_V1-CAME.safetensors — 漫画モノクロ特化
- Hand_Draw_Manga_Style.safetensors — 手描き漫画風
- manga_gene.safetensors / manga_gene_hard.safetensors — 漫画構図
- anime_screencap-IL-NOOB_v3.safetensors — アニメスクリーンキャプ風
- ThickOutline.safetensors — 太い輪郭線
- Imminent_Penetration_Pose_ILLUSTRIOUS.safetensors — 挿入直前ポーズ
- NTR_rankou / NTR_selfie / NTR_watching / RCDNTRSP / Netorare_video_letter — NTR系

**SD1.5用（実験で導入、削除可）:**
- manga_general_marvin.safetensors (144MB) — MANGA General
- manga_master_v2.safetensors (9.1MB) — Manga Master v2
- detail_tweaker.safetensors (36MB) — Detail Tweaker

### 生成済み画像（P1用）
- **コマ1 玄関背景（採用）**: `/Applications/Data/Packages/ComfyUI/output/p1bg_final_2_00001_.png`
  - waiIllustrious + ControlNet Canny 0.8 + 896x1152
- **コマ1 咲の後ろ姿（採用）**: `/Applications/Data/Packages/ComfyUI/output/p1c1_heels_final_00001_.png`
  - beretMixManga + heroine_ponytail 0.9 + 896x1152 + seed: 2089188965138902
  - パンツ+ヒール、片足上げて履く動作、白背景
- **コマ2 バッグを持つ手（候補）**:
  - `p1c2_bag_a_00001_.png` ★最有力 — 結婚指輪+バッグ取っ手、線しっかり
  - `p1c2_bag_b_00001_.png` — トートバッグ、線薄め
  - `p1c2_bag_c_00001_.png` — ショルダーバッグ、線薄すぎ
- **コマ3 翔太の顔（候補）**:
  - `p1c3_shota_a_00001_.png` — 前髪で目が隠れてる＋暗い雰囲気 ◎
  - `p1c3_shota_a_00002_.png` — 同上バリエーション
  - `p1c3_shota_test_00001_.png` — やや短髪寄り
  - `p1c3_shota_b/c` — 生成済み（要確認）
- 参考画像: `/Applications/Data/Packages/ComfyUI/input/ref_genkan.png`

### ControlNet環境
- プラグイン: `/Applications/Data/Packages/ComfyUI/custom_nodes/comfyui_controlnet_aux/`
- モデル: `/Applications/Data/Packages/ComfyUI/models/controlnet/controlnet-union-sdxl-promax.safetensors`
- 対応: Canny / Lineart / Depth / OpenPose 等オールインワン
- ComfyUIノード: `CannyEdgePreprocessor` → `ControlNetLoader` → `ControlNetApplyAdvanced`
- **LineArtPreprocessorは `coarse: 'disable'` パラメータ必須**（省略するとエラー）

### rembg（背景除去）導入状況 ※2026-02-28
- **ノード**: `rembg-comfyui-node`（`/Applications/Data/Packages/ComfyUI/custom_nodes/rembg-comfyui-node/`）
- **依存**: rembg + onnxruntime → ComfyUI venvにインストール済み
- **import確認**: `/Applications/Data/Packages/ComfyUI/venv/bin/python3 -c "from rembg import remove"` → OK
- ⚠️ **ComfyUIのノード検索に表示されない問題が残っている**
  - `__pycache__` は cpython-312 で作られている（venvは認識している）
  - ComfyUI起動時のログでエラーが出ていないか確認する必要あり
  - 別のrembgノード（comfyui-rembg等）を試す手もある
- **使い方**: VAE Decode → Image Remove Background (rembg) → Save Image
- **特徴**: AIベースなので白背景でなくても切り抜き可能

### 次のステップ（優先順）
1. **★最優先: キャラ間スタイル一貫性を解決** → [詳細](style_consistency_problem.md)
   - まずIPAdapterでスタイル転写を試す（環境構築済み）
   - 次にMnga-illustriousXL等の共通スタイルLoRAで統一テスト
   - 最終手段: 翔太専用LoRA学習
2. **rembgノードがComfyUIに表示されない問題を解決**
3. **P1コマ2・3の画像を選定・配置**
4. **P2: 咲の顔アップ「いってきます！」生成**
5. **P2: 翔太「…いってらっしゃい」生成**
6. **P3以降の生成に進む**

**ページ構成（変更後）:**
- P1: 出社の朝（新規追加）
- P2: 復帰祝い（旧P1）
- P3: 旦那への注意＋上司の裏（旧P2）
- P4: 旦那の伏線（旧P3）
- P5: 職場復帰（旧P4）
- P6: 旦那の噂（旧P5）
- P7: 仕事のミス＋深夜残業（旧P6）

**クリスタでの作業手順:**
1. コマ枠フォルダー作成（レイヤー→新規レイヤー→コマ枠フォルダー）
2. 枠線分割ツールでコマ分割（Shift押しで水平/垂直固定）
3. ComfyUIで各コマの画像を生成
4. ファイル→読み込み→画像 でコマ枠フォルダー内に配置
5. フキダシツールで吹き出し追加 → テキストツールでセリフ入力

### クリスタ操作ノウハウ（2026-02-26蓄積）

**キャラ画像の合成方法（確定版）:**
1. キャラレイヤーを右クリック → **ラスタライズ**
2. 編集 → **色調補正 → 色相・彩度・明度** → 彩度 **-100**（完全モノクロ化）
3. `W`キー → **自動選択ツール** → キャラ外側の白背景をクリック
4. `Delete`で白背景削除（透明に）
5. 合成モードは **「通常」** のまま（乗算は使わない！）
※ 乗算だと白ブラウス等も透けてしまう

**背景との重なり問題（ドアノブ等の貫通）:**
- 背景レイヤーを**ラスタライズ** → **白ブラシ(`B`)** で重なり部分を塗りつぶし
- 消しゴム(`E`)だと透明になるので**白ブラシが正解**

**ショートカットキー:**
- `V` → 移動ツール（レイヤー内の画像を動かす）
- `E` → 消しゴムツール
- `B` → ブラシツール
- `W` → 自動選択ツール
- `H` → 手のひらツール（キャンバス移動）
- `Space`長押し → 一時的に手のひらツール
- `Ctrl+T` → 自由変形（拡大縮小・回転）
- `Ctrl+Z` → 取り消し（何回も押せる）

**コマ枠操作:**
- コマ枠フォルダー削除: オブジェクトツール → 枠線クリック → Delete
- コマ枠分割: コマ枠ツール → 枠線分割サブツール → ドラッグ（Shift=水平/垂直固定）
- 分割すると別々のコマ枠フォルダーがレイヤーに作られる

**画像挿入:**
- 対象のコマ枠フォルダーを先に選択 → ファイル → 読み込み → 画像
- 読み込み画像は**画像素材レイヤー**になる → ブラシ/消しゴム使うには**ラスタライズ必須**
- 別のコマに移す: レイヤーをドラッグ&ドロップで目的のコマ枠フォルダーに

**その他:**
- 編集 → 取り消し履歴: 一覧から特定の時点に一気に戻れる
- CLIP STUDIO PAINT EXトライアル: 30日間は全機能使用可能（透かしは出ないはず）

**前回セッション（2026-02-23）でやったこと:**
1. ワイルドカード整理（不要な項目を削除、必要なものだけに絞った）
2. インペイントワークフローの接続確認（API経由で全接続OK確認済み）
3. 複数の外部プロンプトを分析・咲バージョンに変換
4. 壁に手をつくポーズ、煽りアングル、母乳シーン等のプロンプトを作成
5. 白背景はberetMixMangaと相性悪い（オレンジ一色になる）ことを発見

### ワイルドカード最新状態（2026-02-23更新）

**ntr_clothes.txt — 5種**
1. 裸エプロン（naked apron）
2. マイクロビキニ（micro bikini）
3. バニーガール（bunny girl）
4. チアリーダー（cheerleader）
5. 学校の制服（school uniform）
※ すべて `breasts out, nipples exposed` 付き

**ntr_scene.txt — 5種**
1. 窓際・片足上げ（standing, leg lifted, against window）
2. フェラチオ（fellatio, oral sex, on knees, looking up）
3. ディープキス（deep kiss, tongue kiss, french kiss, saliva trail）
4. 壁に手・立ちバック前傾（standing back, bent forward, hands on wall）
5. 複数プレイ・乱交（gangbang, group sex, multiple boys, double penetration, surrounded by men）
※ 乱交はネガティブの `(2boys:1.8)` と衝突するので外す必要あり

**ntr_location.txt — 4種**
1. 夜の公園（park at night, bench, dark, trees, streetlight）
2. オフィス（office, after hours, desk, dim lighting）
3. 公衆トイレ（public restroom, tile walls, cramped space, fluorescent light）
4. 露天風呂（outdoor onsen, open air bath, hot spring, steam, night sky, rocks）

**ntr_camera.txt — 16種（変更なし）**

**ntr_outfit.txt — 3種（旧版、未使用）**

### Imminent Penetration LoRA
- ファイル: `Imminent_Penetration_Pose_ILLUSTRIOUS.safetensors`（Illustrious系対応）
- 場所: `/Applications/Data/Packages/ComfyUI/models/loras/`
- トリガーワード: `IMPT_VN, impt_concept`
- 関連タグ: `penis on pussy, imminent penetration, just the tip`
- 推奨weight: **0.4**（0.8だと顔崩れる）
- Civitai: https://civitai.com/models/2041580/imminent-penetration-pose-illustrious

### 生成済み画像の場所
- `/Applications/Data/Packages/ComfyUI/output/xbp_*` — breast press 3枚（色味良い✅）
- `/Applications/Data/Packages/ComfyUI/output/xgs_*` — glass_sex テスト
- `/Applications/Data/Packages/ComfyUI/output/test_*` — autismmix vs pony比較
- `~/Documents/sta/comparison_results/` — 比較結果コピー

### 今のComfyUI設定（xerena系 = beretMixManga）

**チェックポイント:** beretMixManga_v30.safetensors
**Sampler:** euler_ancestral / **Steps:** 32 / **CFG:** 6 / **Clip Skip:** -2
**解像度:** 896x1152
**LoRAローダー:** heroine_ponytail_lora strength 0.9

**ポジティブ（xerena系ベーステンプレート）:**
```
score_9, score_8_up, score_7_up, source_anime,
HDR, 8K, (best quality), detailed eyes, detailed face,
(eye highlights:1.4), (reflected light in eyes:1.3), bright eyes,
volumetric lighting,

heroine_ponytail,
1girl, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(adult woman:1.2), mature female, (fair skin:1.3), wedding ring,
(slim waist:1.3), slender limbs,

ntr,
completely nude, (sweat:1.2),

★ ここに体位・ポーズ（④⑤）
★ ここに表情（⑥）
★ ここにカメラ・フレーミング（⑧⑩）

BREAK
(faceless male:1.8), 1boy,
(fat man:1.3), (large body:1.2), (belly:1.3), (chubby:1.2),
(thick arms:1.1), (large hands:1.2),

★ ここに背景（⑨）
(soft lighting:1.3), dim lighting, night,
```

**ネガティブ:**
```
(worst quality), (low quality), (normal quality), watermark,
bad anatomy, bad hands, bad face, deformed face, asymmetric eyes,
(fat female:1.3), (chubby female:1.3), (thick thighs:1.2), (plump female:1.2),
speech bubble, dialogue, sound effect, onomatopoeia, text,
empty eyes, dull eyes, no highlights in eyes,
(2boys:1.8), (multiple boys:1.8), (multiple males:1.5), (3boys:1.8),
negativeXL_D
```

### 「最終」ワークフローのプロンプト（ワイルドカード版）
```
score_9, score_8_up, score_7_up, source_anime,
detailed eyes, detailed face, ultra detailed, official art, delicate,
pale color, anime screenshot,
vulgarity, hetero,
BREAK
boob focus, ntr,
heroine_ponytail,
1girl, 1boy, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(adult woman:1.2), mature female, (fair skin:1.1), wedding ring,
(slim waist:1.3), slender limbs,
__ntr_clothes__,
__ntr_scene__,
__ntr_location__,
__ntr_camera__,
embarrassed, clenched teeth,
(faceless male:1.6),
(soft lighting:1.3),
<lora:anime_screencap-IL-NOOB_v3:0.9>
```

### インペイント（部分修正）
- ComfyUIでインペイント環境構築済み（「修正」タブ）
- ノード構成: `LoadImage → VAEEncode → SetLatentNoiseMask → KSampler → VAEDecode → SaveImage`
- **API経由で全ノード接続確認済み（link34: VAE→VAEEncode, link36: VAE→VAEDecode 等）**
- KSampler設定: **denoise 0.5**（元画像を残しつつ修正）/ steps 32 / cfg 6 / euler_ancestral / normal
- LoadImageの画像を右クリック → Open in MaskEditor でマスクを塗る → **「Save to node」を必ず押す**
- model / positive / negative は元のワークフローから接続する
- face_yolov8m.pt, hand_yolov8s.pt 顔検出・手検出モデル導入済み
- **特定部分だけ修正（肌を白くする等）**: プロンプトを修正内容だけに変更 + denoise 0.3程度に下げる
- **VAE Encode vs VAE Encode (for Inpainting)**: beretMixMangaは通常モデルなのでVAE Encode + SetLatentNoiseMask方式が正しい

### 体が暗くなる問題の対処法
- `(fair skin:1.1)` → `(fair skin:1.3), (pale skin:1.2)` に強化
- `darkness` は外す（強すぎ）。`dim lighting, night` 程度に抑える
- ネガティブに `(dark skin:1.5)` 追加
- BREAKで肌色タグと暗さタグを分離
- `(from below:1.5)` 等の煽りアングルは影で暗くなりやすい

### 白背景の問題
- `simple background, white background` は beretMixManga と相性悪い
- セピア調の色味が肌色に集中してオレンジ一色になる
- 対策: 白背景を避けて `dim lighting, night` + `soft lighting` を使う

### 今セッションで作成した咲バージョンプロンプト
1. **正常位（missionary）** — from below, legs up, man on top
2. **バック四つん這い + POV腰掴み** — all fours, looking back, pov grabbing waist, from above
3. **立ちバック + 真下から煽り** — standing sex, sex from behind, from below, worm's eye view
4. **壁に手つき + 乳首舐め** — arms extended, hands on wall, spread fingers, man lick nipple, breast milk
5. **高級オフィスロビー正常位** — missionary, ultra-luxury corporate lobby

### 次のステップ
1. **インペイントを実際に試す**（マスク保存忘れに注意）
2. **壁に手つき + 乳首舐めプロンプト** で生成テスト
3. **揺れ・動き系タグ**のテスト（bouncing breasts, motion lines）
4. **背景切り抜き（rembg）**の導入検討
5. 良い設定が決まったらワイルドカードにも反映
6. 各種プロンプト構成を試す（正常位・種付けプレス・しゃがみ騎乗位等）

## 確定プロンプト

### えっちシーン用共通テンプレート（最新版 = xerena系）
→ 上記「今のComfyUI設定」セクション参照

### 咲（完全後ろ向き・ヒール履き途中）※2026-02-28作成
**ポジティブ:**
```
score_9, score_8_up, score_7_up, source_anime,
HDR, 8K, (best quality),
glossy body, shiny skin, volumetric lighting,
BREAK
heroine_ponytail,
1girl, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2),
(adult woman:1.2), mature female, (fair skin:1.1), wedding ring,
(slim waist:1.3), slender limbs,
BREAK
(from behind:1.5), (facing away:1.4), (back turned:1.3),
(looking away:1.2),
(putting on shoes:1.3), (wearing high heels:1.2),
(one foot raised:1.2), (bending forward:1.2),
(high heels:1.3), (black heels:1.2),
white blouse, (dress pants:1.3),
(full body:1.2),
(soft lighting:1.3),
```
**ネガティブ:**
```
(worst quality), (low quality), (normal quality), watermark,
bad anatomy, bad hands, (bad feet:1.4),
(deformed legs:1.3), (extra limbs:1.4),
(facing viewer:1.3), (looking at viewer:1.3), (front view:1.2), (face:1.2),
(1boy:1.3), (male:1.2),
speech bubble, text,
blurry, noise,
negativeXL_D
```

### 咲ベース（肌テスト確定版）
```
(masterpiece, best quality:1.2),
heroine_ponytail,
1girl, solo, adult woman, mature female,
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
wedding ring, (married woman:1.2), (large breasts:1.3),
(slim waist:1.3), (narrow waist:1.2), (wide hips:1.2), (slim legs:1.2), slender limbs,
(pale skin:1.4), (fair skin:1.2), white skin,
detailed skin, (shiny skin:1.3), glossy skin, sweat, detailed lighting, cinematic lighting,
(detailed face:1.3), (detailed eyes:1.2),
manga style, thin outlines
```

### 丸山ベース（体型確定版）
```
(masterpiece, best quality:1.2),
1boy, solo, mature male, middle-aged man,
(ugly bastard:1.2), (chubby:1.1), (belly:1.2),
(round face:1.3), (slit eyes:1.4), (closed eyes:1.2), >_<,
very short black hair, crew cut, neat hair,
double chin, thick neck, wide nose, small mouth,
(gentle smile:1.2), harmless, friendly, nonthreatening,
white dress shirt, necktie loosened, pants,
detailed skin, (shiny skin:1.1), detailed lighting, cinematic lighting,
(detailed face:1.3),
manga style, thin outlines
```

## IPAdapter状況
- セットアップ完了、ワークフロー「最終」に保存済み
- テスト結果: weight 0.5 + heroine_ponytail 0.90 → 顔が幼くなった（干渉）
- 次回: LoRA外してIPAdapter単体テスト or weight 0.3に下げる

## 既知の問題・注意点
- Claude in Chromeのスクリーンショットは画像サイズ制限（2000px）あり
- Chrome拡張はlocalhost（127.0.0.1:8188）に移動すると切断される
- Colab操作中はChrome拡張と接続切れやすい
- バッチサイズ3はMacで遅い → 1枚ずつシード変え推奨
- **ComfyUI APIバッチ: バックグラウンド実行がセッション切断で死ぬ → `nohup`で回避**
- MPS環境(Mac)で1枚約65-90秒（チェックポイント切替時は+60秒程度）
- **白背景はberetMixMangaと相性悪い**（オレンジ一色になる）
- **LoRAなしキャラ（翔太等）はberetMixManga+白背景でオレンジアーティファクトが顕著**
- **チェックポイント切替は+60秒以上**: SD1.5→SDXL切替後の最初の生成でタイムアウトしやすい
- **SD1.5はMac MPSで遅い**: ~75-110s/枚、SDXLと同等かそれ以上

## 学んだこと・パターン
- **LoRAトリガーワード必須**: `heroine_ponytail` 等をプロンプトに入れないと発動しない
- **LoRA複数使いは干渉する**: 1つだけの方が素直に効果が出る
- **LoRAローダーとImpactWC内`<lora:>`の二重適用注意**: 片方0.00にする
- **PonyXLのscore_9系タグはアニメ塗り感を強める**: ツヤ肌したいなら外す
- **score_9系 + anime style/cel shading/flat color外す**: ツヤ肌に近づく
- **体型プロンプト**: `curvy`は全体ぽっちゃり。パーツ指定が有効
- **肌色**: `(pale skin:1.3-1.4), (fair skin:1.2), white skin`
- **manga_geneは構図生成LoRA**: 画風安定は副次効果だった
- **LoRAなしだと品質低下**: 肌テカテカ、体型太め、衣装出ない、輪郭線薄い
- **negativeXL_Dはエンベディング**: ネガティブに書くだけで品質UP（手・顔の崩れ抑制）
- **ComfyUIの euler_a = euler_ancestral**: A1111と名前が違う
- **AnythingV5はSD1.5系でNG**: Anything XL（SDXL）なら互換性あり
- **SD1.5はMac MPSで速くない**: ~75-110s/枚。NVIDIA CUDAでのみ20-35倍速い
- **SD1.5のモノクロ制御は不安定**: weight 1.3→黒潰れ、1.0→色漏れ。スイートスポットなし
- **faceless maleはSDXL専用**: SD1.5では無視される
- **SD1.5 LoRAスタッキングNG**: Manga Master + MANGA Generalは同時使用不可（上書き）
- **キャラ間スタイル差の主因はLoRA有無**: チェックポイントやSD世代の問題ではない
- **画風タグ盛りは逆効果**: cel shading, flat color, thick outlines等をhassakuXLに入れてもリアル描写が勝つ
- **shiny skin/glossy skinがテカリの元凶**: 削除が正解
- **shiny skinをネガティブに入れると逆効果**: 色味薄く顔幼くなる（animagine環境）
- **ninoさん方式はシンプル**: 肌描写・ライティング・画風タグほぼなしであの画風
- **表情weightは盛らない方がいい**: ninoさんはweight無しで安定
- **anime_screencap LoRAのベストweight = 0.9**: 0.8だと弱い、1.0だとCG感戻る
- **animagineXLV31はscore系品質タグ必須**: masterpiece系だとCG感強い
- **チェックポイント変更は画風改善に最も効果的**: タグ盛りより根本解決
- **無表情系タグは使わない**: vacant/emotionless/empty eyes → CG的な表情になりがち
- **表情は嫌がり系で統一**: embarrassed, clenched teeth, furrowed brow, reluctant がベスト
- **ComfyUI APIでバッチ自動化可能**: ImpactWildcardEncodeの"Select to add Wildcard"の値に注意
- **`full body`は男が全身映って崩れる**: `upper body` 必須
- **`sex from behind` は weight 1.2 が安定**: 1.4以上だと挿入描写が支配的
- **`standing sex` は入れない**: full body寄りの構図になりがち
- **Imminent Penetration LoRA は weight 0.4 から**: 0.8だと顔・目が崩れる
- **LoRAはプロンプト内 `<lora:名前:weight>` で呼ぶ**: テキストだけでは発動しない
- **暗いシーンに `dim lighting, night, darkness` 必要**: ないと白飛びする
- **目の崩れ対策**: LoRA weight下げ > 品質タグ強化 > ネガティブ追加 の順で効く
- **腕タグは3個以内に絞る**: 盛りすぎると構図が不安定に（arms extended + hands on wall + spread fingers で十分）
- **白背景 + beretMixManga = オレンジ一色**: セピア調と干渉。dim lighting, nightに戻す
- **乳首を出すには `completely nude, nipples` 必須**: 入れ忘れると服着たまま生成される
- **他のプロンプトで使えるテクニック**:
  - `just the tip` — 先端だけ触れてる状態
  - `gasping` — 喘ぎ・息切れ
  - `oiled skin` — shiny skinより強いテカリ
  - `full-face blush` — blushより赤面が強い
  - `male pov` — povより男視点が明確
  - `(light particles:1.2)` — 光の粒で映画的雰囲気
  - `(blurred background)` — 背景ぼかし
  - `nervous` — 緊張感
  - `undressing clothes` — 脱がされてる途中（全裸より効果的な場合あり）
  - `solo focus` — 男を描かず女の子にフォーカス
  - `before sex` — セックス前。`imminent penetration` の別表現
  - `incoming sex` — セックスが始まる直前。同上
  - `half-closed eyes` — トロ目・恍惚。堕ちかけ表現に
  - `bedroom eyes` — 色っぽい目つき
  - `moody lighting` — ムーディーな照明。`soft lighting` の代替
  - `heavy breathing` — 荒い息。臨場感UP
  - `exhausted` — 疲弊。事後感や長時間感
  - `drooling` — よだれ。堕ち表現
  - `messy hair` — 髪の乱れ。行為中の生々しさ
  - `crotch aside` — 下着をずらしてる。着衣プレイに
  - `1faceless male` — 1 + faceless male を1語で
  - `holding penis` — ペニスを握ってる。手コキ・挿入直前に
  - `clothed female` — 着衣プレイ指定
  - `bouncing breasts` — 胸揺れ（動き感に効果的、構図崩れにくい）
  - `motion lines` — モーション線（漫画的動き演出）
  - `spread fingers` — 指を開く（壁に手をつくポーズに必須）
  - `outstretched arms` — 腕を伸ばす
  - `breast milk` — 母乳
  - `man lick nipple` — 乳首舐め（男タグも必要）
  - `worm's eye view` — 虫の視点（from belowの強化版）
  - `bust shot` — 胸から上のアップ
  - `arched back` — 腰を反らす（エロさUP）
- **BREAK活用**: SDXL系（beretMixManga含む）で使える。75トークンで強制チャンク分割
  - キャラと体位の間 → 髪色・体型の干渉防止
  - 男と女の間 → **chubby等が咲に影響するのを防ぐ**（特に重要）
- **体毛除去**: ネガティブに `(pubic hair:1.5), (body hair:1.3), (hairy:1.3)` + ポジティブ `hairy arms` 削除
- **NAI形式 → ComfyUI変換**: `{{tag}}` → `(tag:1.1)` / `1.2::tag::` → `(tag:1.2)`
- **体位を先頭に置く構成**（ukkripp式）: 品質タグより構図を優先させると構図が安定する場合あり
- **`before sex` + `penis on pussy` の二重指定**: 挿入直前を確実に出す

## フレーミング距離感（遠→近）
```
full body > cowboy shot > upper body > bust shot > portrait > close-up face
（全身）   （膝上）     （腰上）    （胸上）    （肩上）   （顔だけ）
```

## よく使うパス
- LoRA: /Applications/Data/Packages/ComfyUI/models/loras/
- チェックポイント: /Applications/Data/Packages/ComfyUI/models/checkpoints/
- エンベディング: /Applications/Data/Packages/ComfyUI/models/embeddings/
- ワイルドカード: /Applications/Data/Packages/ComfyUI/custom_nodes/comfyui-impact-pack/wildcards/
- ワークフロー: /Applications/Data/Packages/ComfyUI/user/default/workflows/
- 出力: /Applications/Data/Packages/ComfyUI/output/
- バッチスクリプト: /Users/shuhei.sugai/Documents/sta/

## ComfyUI APIバッチ実行方法
```bash
# セッション切断でも止まらないように nohup で実行
nohup python3 /Users/shuhei.sugai/Documents/sta/comfyui_pony_vs_illustrious.py > /Users/shuhei.sugai/Documents/sta/comparison_log.txt 2>&1 &

# 進捗確認
tail -20 /Users/shuhei.sugai/Documents/sta/comparison_log.txt

# 生成済み画像確認
ls /Applications/Data/Packages/ComfyUI/output/cmp_* | wc -l

# ComfyUI キュー停止
python3 -c "import urllib.request; urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8188/interrupt', method='POST'))"
```
