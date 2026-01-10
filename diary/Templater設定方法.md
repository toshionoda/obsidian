# Templaterで日記のタスク自動引き継ぎを設定する方法

## 現在の状況
- ✅ Templaterプラグインはインストール済み
- ❌ 日記テンプレートが標準機能を使用しているため、自動化が機能していない

## 設定手順

### 1. Templaterプラグインの設定を開く
1. Obsidianの設定を開く（`Cmd/Ctrl + ,`）
2. 「Community plugins」→「Templater」を選択
3. または、コマンドパレット（`Cmd/Ctrl + P`）→「Templater: Open settings」

### 2. テンプレートフォルダの設定
- 「Template folder location」を `.obsidian/templates` に設定
- または、`diary` フォルダを指定

### 3. Daily Notesのテンプレートを変更
**方法A: TemplaterのDaily Notes機能を使用**
1. Templater設定で「Trigger Templater on new file creation」を有効化
2. Daily Notesの設定で、Templaterテンプレートを使用するように変更

**方法B: 標準Daily Notes + Templaterテンプレート（推奨）**
1. Daily Notesの設定（`.obsidian/daily-notes.json`）はそのまま
2. 新しい日記を作成する際に、手動でTemplaterテンプレートを適用
   - コマンドパレット → 「Templater: Create new note from template」
   - テンプレート: `diary/diary-templete-templater.md` を選択

### 4. 自動化の完全実装（上級者向け）
Templaterの「Folder Templates」機能を使用：
1. Templater設定で「Folder Templates」を有効化
2. `diary` フォルダに新しいファイルが作成されたときに自動的にテンプレートを適用

## 簡単な解決策（今すぐ使える）

現在、1月4日の日記には手動でタスクを引き継ぎました。

今後は以下のいずれかの方法で対応できます：

### オプション1: 手動コピー（現在の方法）
- 前日の日記を開く
- 未完了タスクをコピー
- 新しい日記に貼り付け

### オプション2: Templaterコマンドを使用
1. 新しい日記を作成
2. コマンドパレット → 「Templater: Replace templates in active file」
3. または、日記作成時にTemplaterテンプレートから作成

### オプション3: 完全自動化
上記の「設定手順」を完了させる

## テンプレートファイル
- `diary/diary-templete-templater.md` - Templater用の自動化テンプレート（作成済み）
- `diary/diary-templete.md` - 標準テンプレート（現在使用中）



