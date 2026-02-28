# Dayce PWA メモリ

## プロジェクト概要
- **アプリ名**: Dayce (Day + Voice) - ライフログPWA
- **場所**: `/Users/shuhei.sugai/Downloads/lifelog_pwa_ai_button_click_fix (1)/`
- **GitHub Pages**: gyaiiiin0727.github.io/lifelog
- **デプロイ方法**: GitHub Web で「Add file → Upload files」で手動アップロード
- **Worker**: `https://lifelog-ai.little-limit-621c.workers.dev`
- **Worker ソース**: `/Users/shuhei.sugai/Downloads/pwa_with_ai_and_worker_package/worker/src/worker.js`

## アーキテクチャ
- `index_original.html` → `obfuscate.py` → `index.html`（難読化済み）
- 外部JS: `*_original.js` → 難読化 → `*.js`
- **編集は必ず `_original` ファイルに対して行う**
- `_original` ファイルはGitHub Pagesにアップロードしない

## 難読化パイプライン
```bash
cd "/Users/shuhei.sugai/Downloads/lifelog_pwa_ai_button_click_fix (1)"
python3 obfuscate.py
```
- `javascript-obfuscator` 使用
- `renameGlobals=false`（HTML内onclick等との連携維持）
- 対象: index.html（51ブロック）+ cloud-sync.js, goals-v2.js, goal-ai-breakdown.js, voice-input-extra.js

## Stripe本番情報
- 価格ID: `price_1T2q1bCfVwTOOprV3gZAmbPC`（¥500/月）
- Webhook URL: `https://lifelog-ai.little-limit-621c.workers.dev/api/stripe/webhook`
- Customer Portal 設定済み（本番・テスト両方）
- Worker Secrets: `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`, `RESEND_API_KEY`, `RESEND_FROM`, `OPENAI_API_KEY`, `JWT_SECRET`

## リリースタスク完了状況（Session 12時点）
- ✅ 解約フロー（Customer Portal）
- ✅ 利用規約・プライバシーポリシー・特定商取引法
- ✅ Stripe本番モード
- ✅ コード難読化
- ✅ Resend連携
- ⬜ GitHub Pagesアップロード（設定パネル+バグ修正の最新版）

## 技術的注意
- `index_original.html` は約22,000行。Grep/行番号指定で読むこと
- ES5版とES6版のジャーナルAI処理が2箇所ある → 変更時は両方更新
- `journalEntriesV3` が現在のジャーナルストレージ（`.raw` フィールド）
- `window.DaycePlan` でプラン管理。AI呼び出し前に `checkLimit()` ゲート必須
- Worker デプロイ: `cd /Users/shuhei.sugai/Downloads/pwa_with_ai_and_worker_package/worker && npx wrangler deploy`

## 既知の技術的負債
- レガシー `addJournal()` 関数（旧 `journals` キーに保存、使われていないが残存）
- 30以上のsilent error catch
- 90以上のグローバル汚染（`window.xxx`）
