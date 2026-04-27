# MangaTL（Gemini版）— インストール手順

## 完全無料！クレジットカード不要

---

## ステップ1: Gemini APIキーを取得（無料）

1. https://aistudio.google.com/app/apikey をスマホまたはPCで開く
2. Googleアカウントでログイン（普段使いのGoogleアカウントでOK）
3. 「APIキーを作成」をタップ
4. 「AIza...」で始まる文字列が表示される → コピーして保存

---

## ステップ2: GitHubにアップロード

1. https://github.com にアクセス・ログイン
2. 右上「+」→「New repository」
3. Repository name: `mangatl`（任意）
4. Public を選択 → 「Create repository」
5. 「uploading an existing file」をクリック
6. 以下のファイルをすべてドラッグ＆ドロップ:
   - index.html
   - manifest.json
   - sw.js
   - icons フォルダごと（icon-192.png, icon-512.png）
7. 「Commit changes」をクリック

---

## ステップ3: GitHub Pagesを有効化

1. リポジトリの「Settings」タブ
2. 左メニュー「Pages」
3. Source → Branch: main → /(root) → 「Save」
4. 数分後、以下のURLでアクセス可能:

```
https://momo060331.github.io/mangatl/
```

---

## ステップ4: スマホにインストール

### iPhoneの場合（Safari必須）
1. 上記URLをSafariで開く
2. 画面下の「共有」ボタン（□↑）をタップ
3. 「ホーム画面に追加」をタップ
4. 「追加」→ ホーム画面にMangaTLアイコンが追加される

### Androidの場合（Chrome）
1. 上記URLをChromeで開く
2. メニュー（⋮）→「ホーム画面に追加」
3. 「追加」→ ホーム画面にアイコンが追加される

### PCの場合（Chrome）
- アドレスバー右端のインストールアイコンをクリック

---

## ステップ5: APIキーを設定してスタート！

1. アプリを起動
2. 右上「⚙」をタップ
3. Gemini APIキー欄に「AIza...」のキーを貼り付け
4. 「保存」→ 完了！

---

## 使い方

- 漫画画像のURLを入力 → 「翻訳」
- または「画像をアップロード」から画像を選択
- 吹き出しに日本語が重なって表示される
- 翻訳済みページは「前へ」「次へ」で履歴をたどれる

## 無料枠について

- Gemini Flash モデルを使用
- 1日あたり最大250リクエストまで無料
- 漫画なら1日250ページ分 → 個人利用なら十分！
- クレジットカード登録不要
