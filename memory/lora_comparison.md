# LoRA比較テスト記録

## 2026-02-16 LoRA比較テスト（hassakuXLベース）

### 背景
- manga_gene + NTR_selfie の2つLoRAを使っていたが、構図への副作用が懸念
- LoRAなしで試したら品質低下（テカテカ肌、体型太め、衣装出ない、輪郭線薄い）
- manga_geneの代替となる画風安定LoRAを探すことに

### 重要な発見
- **LoRA複数使いは干渉する**: 1つだけの方が素直に効果が出る
- **manga_geneは構図生成LoRA**: 画風安定は副次効果だった
- **LoRAなしだと品質低下**: 肌テカテカ、体型太め、衣装出ない、輪郭線薄い

### 新規ダウンロードLoRA（2026-02-16）
1. **anime_screencap-IL-NOOB_v3.safetensors** (69MB)
   - Fine Anime Screencap XL（Illustrious v3.0版）
   - トリガー: `anime screencap, anime coloring`
   - 推奨weight: 0.7〜1.2
   - 色・影・ライティング・背景品質向上

2. **ThickOutline.safetensors** (228MB)
   - Thick Lines | Pony & Illustrious
   - トリガー: `thick outline`
   - 推奨weight: 1.0
   - 太い輪郭線に特化、構図に影響しにくい

3. **Hand_Draw_Manga_Style.safetensors** (228MB)
   - Hand Draw Manga Style
   - トリガー: `hand_draw, manga_style`
   - 推奨weight: 0.8
   - 手描き漫画スタイルに特化、Illustrious対応

### 新規ダウンロード エンベディング（2026-02-16）
- **negativeXL_D.safetensors** (131KB)
  - 配置先: `/Applications/Data/Packages/ComfyUI/models/embeddings/`
  - ネガティブプロンプトに `negativeXL_D` と書くだけで品質向上
  - 手の崩れ・顔の崩れ抑制、全体品質UP

### 参考にしている画風（ninoさん @chichi-pui）
- プロフィール: https://www.chichi-pui.com/users/user_nTx4yGJWyN/?age_limit=R18
- URL1: https://www.chichi-pui.com/posts/7d3fd528-a97c-43cb-a2b5-62672f75e3a4/ （★表情再現ターゲット）
- URL2: https://www.chichi-pui.com/posts/64be90e8-5b49-4523-9d0b-13ac28ba0b03/

#### ninoさんプロンプト詳細分析（5作品調査済み）

**共通設定:**
- モデル: Stable Diffusion XL（具体的なチェックポイント不明）
- Steps: 30, CFG: 7, Sampler: Euler a
- ネガティブ共通: `(worst quality:1.5, low quality:1.4), lowres, blurry, painting, watermark, text, error, ((bad anatomy, bad hands:1.4)), missing fingers, extra digit, fewer digits, long body, fused limbs, negativeXL_D`

**品質タグ（2パターン確認）:**
- 旧: `(masterpiece, best quality), ultra detailed, official art, delicate, vulgarity, hetero, BREAK`
- 新（マグロ系彼女）: `(masterpiece, best quality, amazing quality, very aesthetic, absurdres), detailed eyes, detailed face, ultra detailed, official art, delicate, pale color, anime screenshot, vulgarity, hetero, BREAK`
- → `amazing quality, very aesthetic, absurdres, detailed eyes, detailed face, pale color, anime screenshot` が追加

**表情タグ（作品別）:**
| 作品 | 表情タグ | LoRA |
|---|---|---|
| 童貞クン（笑顔系） | `heavy breathing, embarrassed, orgasm, ecstasy, smirk` | なし |
| ほら彼氏に（★clenched teeth系） | `embarrassed, close eyes, clenched teeth` | なし |
| ちょっと優しくして（感じてる系） | `heavy breathing, embarrassed, orgasm, ecstasy` | なし |
| まだまだ夜は長い（empty eyes系） | `embarrassed, empty eyes, open mouth` | `lotion play_illustrious_V1.0:1` |
| マグロ系彼女（無表情系） | `expressionless, sleepy` | なし |

**重要な発見:**
- ninoさんは表情LoRAを使っていない（プロンプトのタグだけ）
- `embarrassed` がほぼ全作品に共通
- `clenched teeth` は直接プロンプトに書いている
- `BREAK` で品質タグとキャラ描写を分離
- `vulgarity, hetero` が共通
- LoRAは基本使わない（1作品だけ lotion play LoRA使用）
- `(bokeh:1.5)` は一部作品のみ、全作品ではない
- `(faceless male:1.4)` で男性の顔を映さない手法

**画風の特徴:**
- 肌のツヤ感が絶妙（テカすぎずマットすぎず）
- 輪郭線がくっきり太め ← うちのはまだ弱い
- 目の描き込みが繊細
- 肌色が白くて透明感ある
- ボケ感（bokeh）で画面に立体感

### nino画風に近づけるための変更点
- `ultra detailed, official art, delicate` をポジティブに追加 ✅
- Sampler を `euler_ancestral` に変更 ✅
- `negativeXL_D` をネガティブに追加 ✅
- Steps: 30 に変更 ✅
- 今後の検討: `(bokeh:1.5), depth of field` の追加

### ワイルドカード修正（ntr_face.txt）
- アヘ顔系を削除:
  - 旧11行目: `ahegao, tongue out, eyes rolling back, drool, reluctant pleasure`
  - 旧15行目: `empty eyes, broken, mind break, drooling`
- 「歯を食いしばって耐える」系に置換:
  - 新11行目: `clenched teeth, enduring, tears, reluctant pleasure, gritting teeth`
  - 新15行目: `gritting teeth, enduring pain, tears, clenched jaw, frustrated`
- ネガティブにもアヘ顔防止追加: `ahegao, tongue out, rolling eyes, drooling, mind break`

### 比較テスト計画（5パターン）

**共通ネガティブ（最新版）:**
```
smile, happy, relaxed, calm expression, consensual, bad face, deformed face, asymmetric eyes, lowres, bad anatomy, bad hands, text, error, worst quality, low quality, blurry, (fat:1.3), (chubby female:1.3), (thick thighs:1.2), (plump:1.2), (wide body:1.2), (wide hips:1.2), split screen, multiple views, comic panels, border, frame, multiple angles, restrained, tied up, rope, bondage, handcuffs, chains, bound, ahegao, tongue out, rolling eyes, drooling, mind break, negativeXL_D
```

**共通ベースプロンプト（丸山体型強化 + nino風）:**
```
(masterpiece, best quality:1.2), ultra detailed, official art, delicate,
heroine_ponytail,
1girl, 1man, (adult woman:1.2), mature female,
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(large breasts:1.3), (slim waist:1.3), (narrow waist:1.2), (slim legs:1.2), slender limbs, (thin arms:1.2),
(fair skin:1.1), wedding ring, (married woman:1.2),
__ntr_clothes__, __ntr_scene__, __ntr_face__, __ntr_location__, __ntr_camera__,
1boy, (ugly bastard:1.2), (chubby:1.1), (belly:1.2),
(round face:1.3), (slit eyes:1.4), very short black hair, crew cut,
double chin, thick neck, wide nose, fat fingers, thick arms, hairy arms,
detailed skin, (shiny skin:1.3), glossy skin, sweat, detailed lighting, cinematic lighting,
(detailed face:1.3), (detailed eyes:1.2),
manga style, (thick outlines:1.4), bold lines
```

**共通設定:**
- Sampler: euler_ancestral
- Steps: 30
- CFG: 7
- LoRAローダー: heroine_ponytail_lora strength 0.90（全パターン共通）

**パターン0: heroine_ponytail 単体**
- 画風LoRAなし、heroine_ponytailのみ

**パターン1: heroine_ponytail + Anime Screencap**
- ベースプロンプトに `anime screencap, anime coloring` 追加
- `<lora:anime_screencap-IL-NOOB_v3:0.8>`

**パターン2: heroine_ponytail + Thick Lines**
- ベースプロンプトに `thick outline` 追加
- `<lora:ThickOutline:1.0>`

**パターン3: heroine_ponytail + Hand Draw Manga**
- ベースプロンプトに `hand_draw, manga_style` 追加
- `<lora:Hand_Draw_Manga_Style:0.8>`

**パターン4: heroine_ponytail + Hand Draw + Thick Lines**
- ベースプロンプトに `hand_draw, manga_style, thick outline` 追加
- `<lora:Hand_Draw_Manga_Style:0.8>, <lora:ThickOutline:0.8>`

### テスト結果

**パターン0: heroine_ponytail単体**
- 咲の顔: ◎（LoRA干渉なしで安定、ポニテ・前髪・茶髪OK）
- 画風: △（輪郭線薄い、肌テカテカ気味でリアル寄り）
- 丸山: ✗（マッチョ・イケメンになった。体型タグが弱すぎた→強化版で以降反映）
- **結論:** 顔◎、画風△。画風LoRA追加が必要

**パターン1: heroine_ponytail + Anime Screencap（+ nino風変更全部入り）**
- 1枚目(00122): ◎ 丸山太ってる、crew cut出た、咲の顔良い、画風漫画っぽい（weight 0.8）
- 2枚目(00123): ◎ バニーのやつ良い（weight 0.5）
- 3枚目: ink lines, lineart, high contrast 追加版 → ✗ 効きすぎ、肌にアーティファクト（赤い染み）
- 4枚目: anime_screencap 0.6 + (bokeh:1.5) + depth of field → ◎ 画風良い！bokeh効いて背景のボケ綺麗。nino風に近い。ただし表情が無表情気味

**パターン2: ThickOutline** → ✗ ホラー丸山。画像削除済み
**パターン3: Hand Draw Manga** → △ 2枚試したが微妙。画像削除済み
**パターン4: Hand Draw + ThickOutline** → ✗ 顔が幼い。画像削除済み

### 現在の最有力プロンプト

#### A: 丸山入り2ショット版（テスト5で使用、表情◎だが丸山の表情問題あり）
```
(masterpiece, best quality, amazing quality, very aesthetic, absurdres),
detailed eyes, detailed face, ultra detailed, official art, delicate,
pale color, anime screenshot,
vulgarity, hetero,
BREAK
heroine_ponytail,
1girl, 1man, (adult woman:1.2), mature female,
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(large breasts:1.3), (slim waist:1.3), (narrow waist:1.2), (slim legs:1.2), slender limbs, (thin arms:1.2),
(fair skin:1.1), wedding ring, (married woman:1.2),
(embarrassed:1.2), (clenched teeth:1.3), close eyes,
__ntr_clothes__, __ntr_scene__, __ntr_location__, __ntr_camera__,
1boy, (ugly bastard:1.2), (chubby:1.1), (belly:1.2),
(round face:1.3), (slit eyes:1.4), very short black hair, crew cut,
double chin, thick neck, wide nose, fat fingers, thick arms, hairy arms,
detailed skin, (shiny skin:1.3), glossy skin, sweat, detailed lighting, cinematic lighting,
(bokeh:1.5), depth of field,
anime screencap, anime coloring, manga style, (thick outlines:1.4), bold lines,
<lora:anime_screencap-IL-NOOB_v3:0.6>
```
- 次回改善: 丸山側に `(smirk:1.2), (grinning:1.2)` で表情分離

#### B: faceless male版 nino構図再現 超シンプル版（テスト12確定・セーブポイント）
```
(masterpiece, best quality, amazing quality, very aesthetic, absurdres),
detailed eyes, detailed face, ultra detailed, official art, delicate,
pale color, anime screenshot,
vulgarity, hetero,
BREAK
boob focus, ntr, upper body, close-up face,
heroine_ponytail,
1girl, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(adult woman:1.2), mature female, (fair skin:1.1), wedding ring,
(slim waist:1.3), slender limbs,
completely nude, spread legs,
sex, intense sex, vaginal,
sex from behind, standing sex, reaching,
embarrassed, close eyes, clenched teeth,
(faceless male:1.4),
(motion lines, motion blur),
simple background, white background,
pov, from directly below, from below:1.8, worm's eye view, looking at viewer,
soft lighting, warm colors,
<lora:anime_screencap-IL-NOOB_v3:0.8>
```
- コンセプト: **ninoさんはタグ盛りなしであの画風を出してる → シンプルにしてLoRAに任せる**
- 大幅削除: detailed skin/shiny skin/sweat/glossy skin全削除、lighting系全削除、bokeh削除、anime style/cel shading/flat color/thick outlines/bold lines/manga style/anime coloring全削除
- 表情のweight全部外し（ninoさんと同じ）
- simple background, white background追加
- soft lighting, warm colors追加（テスト12）
- **★セーブポイント: ダメだったらこのプロンプトに戻る**

### ninoさん構図再現テスト（URL1: ほら彼氏に）

**ターゲット構図:** 後背位・煽り・faceless male・clenched teeth
**再現ポイント:** `boob focus, ntr, upper body, close-up face` がBREAK直後、`from directly below, from below:1.8, worm's eye view`

**テスト5: 丸山入りバージョン（nino品質タグ+表情直接指定）**
- 結果: ◎ 咲の表情が良い！clenched teethで歯を食いしばって嫌がってる
- 咲の顔・髪型完璧、丸山の体型も太ってる
- 問題: 丸山の顔もclenched teethになってしまう（表情タグが両方に効く）
- → 丸山側に `(smirk:1.2), (grinning:1.2)` 等の対抗タグが必要

**テスト6: faceless male版（nino構図忠実再現）**
- プロンプト: nino品質タグ最新版 + BREAK + 構図直接指定 + `(faceless male:1.4)`
- 結果: ◎ 表情良い（clenched teeth出た）、構図も煽りで再現できた
- 問題: **画風がリアル寄り、線が漫画的でない**、肌のCG感が強い
- → `shiny skin` が効きすぎ、`thick outlines` が弱い

**テスト7: faceless male版 漫画感強化**
- 変更: `shiny skin` 1.3→0.8、`glossy skin` 削除、`thick outlines` 1.4→1.6、`bold lines` 1.3追加、`cel shading` 追加、LoRA 0.6→0.7
- 結果: △ まだテカテカ、チーク(blush)足してみた

**テスト8: blush追加 + shiny skin 0.5 + flat color 1.2**
- 結果: △ 表情良くなったがまだリアルCG寄り、線が細い

**テスト9: ネガティブにリアル排除追加 + anime style + flat color強化 + LoRA 0.8**
- ネガティブに `(realistic:1.5), (photorealistic:1.5), (3d:1.5), painting, smooth shading, gradient shading` 追加
- 結果: △ 少し改善したがまだテカリ、腕が太い

**テスト10: 構図強化（full body, spread legs, spread arms, closed eyes強化, ceiling追加）**
- 結果: △ 構図は近づいた。目を瞑りすぎ、腕T字、天井映りすぎ、表情苦しすぎ
- → weightの盛りすぎが原因

**テスト11: ninoさんシンプル方式（タグ大幅削除）**
- コンセプト: ninoさんはタグ盛りなしであの画風 → 装飾タグ全削除してLoRAに任せる
- 削除: shiny skin/glossy skin/sweat/lighting系/bokeh/anime style/cel shading/flat color/thick outlines/bold lines
- 表情weightも全外し、simple background追加
- 結果: ◎ 構図・表情かなり良い！ただし肌がまだCG塗り感（テカリ・硬い質感）

**テスト12: soft lighting + warm colors追加**
- テスト11に `soft lighting, warm colors` だけ追加
- 結果: 構図OK、肌の柔らかさは微改善したがまだCG塗り感。**hassakuXLの限界かも**
- → **チェックポイント変更を試す方向に転換**

### チェックポイント変更テスト（セーブポイントBベース）

**テスト13: waiIllustriousSDXL_v160（品質タグ元のまま）**
- チェックポイント: waiIllustriousSDXL_v160
- プロンプト: セーブポイントBそのまま（masterpiece, best quality系）
- 結果: △ hassakuXLよりややマシだがCG感はまだ強い。LoRA互換性OK
- ユーザー評価: 「早速いい感じかも」「まんがっぽくはないよね。いい感じなんだけど」「でもさっきよりいいかも！」

**テスト14: animagineXLV31（品質タグ元のまま）**
- チェックポイント: animagineXLV31_v31
- プロンプト: セーブポイントBそのまま（masterpiece, best quality系）
- 結果: △ CG感強め。LoRA互換性OK（heroine_ponytail動作）

**テスト15: animagineXLV31（品質タグscore系に変更）**
- チェックポイント: animagineXLV31_v31
- 品質タグ変更: `score_9, score_8_up, score_7_up, source_anime` に差し替え
- 結果: ◎ かなり改善！表情・構図・clenched teeth出てる。まだ肌ツヤにCG感残り
- ユーザー評価: 「いい感じになってきたかも」
- **次の改善案:**
  1. ネガティブに `shiny skin, glossy skin` 追加（肌ツヤCG感対策）
  2. `flat color, cel shading` 追加（アニメ塗り強化）
  3. anime_screencap LoRA 0.8→0.9（アニメ感強化）
  4. ポニテが出てない→heroine_ponytail weight確認

#### テスト15 セーブポイントC（animagine + score系品質タグ）
```
score_9, score_8_up, score_7_up, source_anime,
detailed eyes, detailed face, ultra detailed, official art, delicate,
pale color, anime screenshot,
vulgarity, hetero,
BREAK
boob focus, ntr, upper body, close-up face,
heroine_ponytail,
1girl, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(adult woman:1.2), mature female, (fair skin:1.1), wedding ring,
(slim waist:1.3), slender limbs,
completely nude, spread legs,
sex, intense sex, vaginal,
sex from behind, standing sex, reaching,
embarrassed, close eyes, clenched teeth,
(faceless male:1.4),
(motion lines, motion blur),
simple background, white background,
pov, from directly below, from below:1.8, worm's eye view, looking at viewer,
soft lighting, warm colors,
<lora:anime_screencap-IL-NOOB_v3:0.8>
```
ネガティブ: セーブポイントBと同じ

**テスト16: animagine + ネガティブにshiny skin追加**
- セーブポイントCのネガティブに `shiny skin, glossy skin` 追加
- 結果: ✗ 色味薄くなりすぎ、顔が幼くなった。逆効果
- → セーブポイントCに戻し

**テスト17: animagine + anime_screencap LoRA 0.9** ← ★暫定ベスト
- セーブポイントCからLoRAのみ 0.8→0.9 に変更
- 結果: ◎◎ **今までで一番良い！** アニメ塗り感UP、表情・構図・ポニテ全部OK
- ユーザー評価: 「めちゃいいかんじ！」
- motion linesも自然に出る

#### テスト17 セーブポイントD（animagine + score系 + LoRA 0.9）★暫定ベスト
```
score_9, score_8_up, score_7_up, source_anime,
detailed eyes, detailed face, ultra detailed, official art, delicate,
pale color, anime screenshot,
vulgarity, hetero,
BREAK
boob focus, ntr, upper body, close-up face,
heroine_ponytail,
1girl, (large breasts:1.3),
(dark brown hair:1.3), long hair, (ponytail:1.4), (bangs:1.2), (brown eyes:1.2),
(adult woman:1.2), mature female, (fair skin:1.1), wedding ring,
(slim waist:1.3), slender limbs,
completely nude, spread legs,
sex, intense sex, vaginal,
sex from behind, standing sex, reaching,
embarrassed, close eyes, clenched teeth,
(faceless male:1.4),
(motion lines, motion blur),
simple background, white background,
pov, from directly below, from below:1.8, worm's eye view, looking at viewer,
soft lighting, warm colors,
<lora:anime_screencap-IL-NOOB_v3:0.9>
```
ネガティブ: セーブポイントBと同じ（shiny skin追加なし）
設定: animagineXLV31_v31 / euler_ancestral / Steps30 / CFG7 / heroine_ponytail 0.90

**テスト18: animagine + anime_screencap LoRA 1.0**
- セーブポイントDからLoRAのみ 0.9→1.0 に変更
- 結果: △ CG感戻った、色味暗くなった。0.9の方がバランス良い
- → **LoRA 0.9がベスト確定。セーブポイントDが最良**

**テスト19: prefectIllustriousXL_v60（セーブポイントDプロンプト）**
- 結果: △ 輪郭線くっきりだが肌テカリ・CG感がanimagineより強い。ギラギラしすぎ

**テスト20: prefectPonyXL_v6（セーブポイントDプロンプト）**
- 結果: ◎ 肌の塗り柔らかい、CG感少なめ。animagineに次ぐ2番手
- ユーザー評価: 「けっこういいかも？」

**テスト21: autismmixSDXL_autismmixPony（セーブポイントDプロンプト）**
- 結果: ✗ 微妙
- ユーザー評価: 「微妙だった」

### チェックポイント比較 最終結果
| チェックポイント | 煽り構図 | 騎乗位構図 | コメント |
|---|---|---|---|
| hassakuXLIllustrious_v34 | △ | 未テスト | CG感強い、限界 |
| waiIllustriousSDXL_v160 | △+ | 未テスト | hassakuよりマシ程度 |
| **animagineXLV31_v31** | **◎◎** | **✗** | **煽り構図ベスト。騎乗位は構図が全くダメ** |
| prefectIllustriousXL_v60 | △ | **◎** | 煽りはテカリ問題。**騎乗位の構図が一番良い** |
| prefectPonyXL_v6 | ◎ | ◎ | 両構図とも安定。肌柔らかい |
| autismmixSDXL_autismmixPony | ✗ | △ | 微妙 |

**→ 構図によってチェックポイント使い分けが必要！**
- 煽り構図: animagineXLV31（セーブポイントD）
- 騎乗位構図: prefectIllustriousXL_v60（質感調整中）or prefectPonyXL

### 騎乗位構図テスト（chichi-pui ukkripp「ビクビクしてるw」参考）

**テスト22: animagineXLV31 騎乗位構図（タグ多め）**
- 構図変更: 煽りアングル系 → `girl on top, squatting, bowlegged pose, cowgirl position, bent over, lying on person, facing down`
- 結果: △ 構図は出たが不安定。表情がclenched teethではなく笑顔寄り、目が開いてる

**テスト23: animagineXLV31 騎乗位構図（タグ絞り + 1boy + faceless 1.6）**
- 構図シンプル化: `girl on top, cowgirl position, squatting` のみ
- `1boy` 追加、`faceless male` 1.4→1.6
- 結果: △ 男が2人出た（faceless効いてない）。構図はスクワット出てる

**テスト24: prefectPonyXL_v6 騎乗位構図（テスト23と同じプロンプト）**
- 結果: ◎ いい感じ。肌柔らかい
- ユーザー評価: 「いい感じかな」

**テスト25: autismmixSDXL 騎乗位構図**
- 結果: △ 微妙

### 騎乗位構図テスト2（chichi-pui ukkripp「スパイダーママン」参考）
- 参考URL: https://www.chichi-pui.com/posts/a5e09b3c-6bdb-4965-8957-4de71945f626/
- 参考プロンプト構図タグ: `cowgirl position, squatting, spread legs, bent over, (licking pov nipple:1.3), tongue out, piston, motion lines, foreshortening, perspective`
- 設定: Steps30, Scale7, Sampler DPM++ 2M

**テスト26: 「スパイダーママン」構図再現**
- `bent over` 復活、`(licking nipple:1.3)` 追加
- `foreshortening, perspective` 追加（迫力・煽り感）
- `heavy breathing, sweat, blush` 追加
- `close eyes` 外し、`looking at viewer` 削除
- **animagineXLV31での結果: ✗ 構図が全くダメ。騎乗位構図はanimagineと相性悪い**
- **prefectIllustriousXL_v60での結果: ◎ 構図が一番良い！** ただしテカリ・色味が課題
  - → CFG 6.0 + `(soft lighting:1.3)` + `muted colors` で質感修正テスト中

#### テスト26 プロンプト（騎乗位 スパイダー構図版）
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
completely nude, spread legs,
cowgirl position, squatting, bent over,
(licking nipple:1.3),
sex, intense sex, vaginal,
piston, motion lines,
heavy breathing, sweat, blush,
embarrassed, clenched teeth,
(faceless male:1.6),
foreshortening, perspective,
simple background, white background,
soft lighting, warm colors,
<lora:anime_screencap-IL-NOOB_v3:0.9>
```
ネガティブ: セーブポイントBと同じ

### 学んだこと（漫画感テストシリーズ）
- **タグ盛りは逆効果**: thick outlines, cel shading, flat color等を足しても hassakuXLではリアル描写が勝つ
- **shiny skin/glossy skinがテカリの元凶**: 削除するのが正解
- **ninoさんのプロンプトはシンプル**: 肌描写・ライティング・画風タグがほぼない
- **ネガティブにrealistic/photorealistic追加は多少効果あり**
- **表情のweight盛りは逆効果**: ninoさんはweight無しで出してる
- **LoRAのweightで画風を調整する方が効果的**: 0.6→0.7→0.8→0.9と上げていく（1.0は逆効果）
- **anime_screencap LoRAのベストweight = 0.9**（animagineXLV31環境）
- **spread arms → T字ポーズになりがち**: reaching だけの方が自然
- **ceiling追加 → 天井が構図を支配**: 煽りアングルには不要
- **animagineXLV31は騎乗位構図が全くダメ**: 煽り構図は◎だが騎乗位は構図崩壊する
- **prefectIllustriousXLは騎乗位構図が最も良い**: ただしテカリ・CG感の質感問題あり
- **構図によってチェックポイント使い分けが有効**: 1つで全部まかなえない

### 残課題
- **prefectIllustriousXLの質感修正テスト結果確認** ← ★今ここ
  - CFG 6.0 + (soft lighting:1.3) + muted colors で改善するか
- **丸山入りバージョンで丸山の表情制御**: clenched teethが両方に効く問題
- 表情は `embarrassed, close eyes, clenched teeth`（weight無し）で安定 ✅（煽り構図では）
- 煽り構図は `from directly below, from below:1.8, worm's eye view` で再現可能 ✅

### 方針
- **構図によってチェックポイント使い分け**
  - 煽り構図: animagineXLV31（セーブポイントD確定）
  - 騎乗位構図: prefectIllustriousXL_v60（質感調整中）or prefectPonyXL
- **animagineは騎乗位構図が全くダメ** → 騎乗位は別チェックポイント必須
- 表情は `clenched teeth` 直接指定で解決（ワイルドカードやめる方向）
- 丸山入りバージョンの表情分離が次の課題
- 確定後 → 同人誌プロンプト集に反映 → P38（騎乗位）制作

## 既存LoRA一覧（ComfyUI/models/loras/）
| ファイル名 | 用途 | 状態 |
|---|---|---|
| heroine_ponytail_lora.safetensors | 咲の顔LoRA（自作） | 確定済み |
| manga_gene.safetensors | 漫画構図生成 | 代替検討中 |
| manga_gene_hard.safetensors | 漫画構図生成（ハード） | 未使用 |
| NTR_selfie.safetensors | NTR構図 | 外す方針 |
| NTR_rankou.safetensors | NTR乱交構図 | 未使用 |
| NTR_watching.safetensors | NTR寝取られ視点 | 未使用 |
| Netorare_video_letter_situation-000008.safetensors | NTRビデオレター | 未使用 |
| RCDNTRSP.safetensors | NTR系 | 未使用 |
| kijoui.safetensors | 騎乗位特化 | 未使用 |
| anime_screencap-IL-NOOB_v3.safetensors | アニメ画風（新規） | ★ほぼ確定（weight 0.6） |
| ThickOutline.safetensors | 太い輪郭線 | ✗ ホラー化。単体不可 |
| Hand_Draw_Manga_Style.safetensors | 手描き漫画風 | △ 微妙 |

## エンベディング一覧（ComfyUI/models/embeddings/）
| ファイル名 | 用途 | 状態 |
|---|---|---|
| negativeXL_D.safetensors | ネガティブ品質向上 | ✅ 導入済み・使用中 |
