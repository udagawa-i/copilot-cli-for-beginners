![Chapter 01: First Steps](images/chapter-header.png)

> **AI が瞬時にバグを見つけ、複雑なコードを説明し、動作するスクリプトを生成する様子を見てください。次に、GitHub Copilot CLI を使う 3 つの異なる方法を学びます。**

このチャプターは魔法が始まる場所です！AI がセキュリティバグを数秒で見つけ、複雑なコードをわかりやすい日本語で説明し、すぐに動作するスクリプトを生成する様子を実際に体験できます。その後、3 つのインタラクションモード（Interactive、Plan、Programmatic）を習得して、どのタスクにどのモードを使うべきか正確に判断できるようになります。

> ⚠️ **前提条件**: まず **[Chapter 00: Quick Start](../00-quick-start/README.md)** を完了してください。下記のデモを実行する前に、GitHub Copilot CLI がインストール・認証されている必要があります。

## 🎯 学習目標

このチャプターの終わりまでに、以下ができるようになります：

- ハンズオンデモを通じて GitHub Copilot CLI の生産性向上を体験する
- タスクに応じて適切なモード（Interactive、Plan、または Programmatic）を選択できる
- スラッシュコマンドを使ってセッションを制御できる

> ⏱️ **所要時間**: 約 45 分（読む時間 15 分 + ハンズオン 30 分）

---

# 初めての Copilot CLI 体験

<img src="images/first-copilot-experience.png" alt="Developer sitting at a desk with code on the monitor and glowing particles representing AI assistance" width="800"/>

さあ、Copilot CLI でできることを実際に試してみましょう。

---

## 快適に始める：最初のプロンプト

すごいデモに飛び込む前に、今すぐ試せるシンプルなプロンプトから始めましょう。**コードリポジトリは必要ありません！** ターミナルを開いて Copilot CLI を起動するだけです：

```bash
copilot
```

これらのビギナー向けプロンプトを試してみてください：

```
> Explain what a dataclass is in Python in simple terms

> Write a function that sorts a list of dictionaries by a specific key

> What's the difference between a list and a tuple in Python?

> Give me 5 best practices for writing clean Python code
```

Python を使ってない？ 問題ありません！ 好きな言語について質問するだけです。

自然に感じられることに気づくでしょう。同僚に話しかけるようにするだけです。探索が終わったら `/exit` で セッションを終了します。

**重要なポイント**：GitHub Copilot CLI は会話形式です。始めるのに特別な構文は必要ありません。普通に英語で質問するだけです。

## 実際の動作を見る

では、なぜ開発者が Copilot CLI を「シニアエンジニアを即座に雇える」と呼ぶのかを見てみましょう。

> 📖 **例の読み方**：`>` で始まる行は、Copilot CLI の interactive セッション内で入力するプロンプトです。`>` がない行はターミナルで実行するシェルコマンドです。

> 💡 **出力例について**：このコース全体に示されるサンプル出力は参考用です。Copilot CLI の応答は毎回異なるため、表現方法、フォーマット、詳細度が異なります。正確なテキストではなく、返される**情報のタイプ**に注目してください。

### デモ 1：秒単位でコードレビュー

このコースには意図的なコード品質の問題が含まれているサンプルファイルが含まれています。ローカルマシンで作業していて、まだリポジトリをクローンしていない場合は、下の `git clone` コマンドを実行して、`copilot-cli-for-beginners` フォルダに移動し、その後 `copilot` コマンドを実行してください。

```bash
# ローカルで作業していてまだクローンしていない場合、コースリポジトリをクローン
git clone https://github.com/github/copilot-cli-for-beginners
cd copilot-cli-for-beginners

# Copilot を起動
copilot
```

Copilot CLI の interactive セッション内で、以下を実行します：

```
> Review @samples/book-app-project/book_app.py for code quality issues and suggest improvements
```

> 💡 **`@` 記号は何ですか？** `@` 記号は Copilot CLI にファイルを読み込むよう指示します。これについては Chapter 02 で詳しく学びます。今のところ、コマンドをそのまままたは コピーしてください。

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Code Review Demo](images/code-review-demo.gif)

*デモの出力は異なります。あなたのモデル、ツール、応答は、ここに示されているものと異なります。*

</details>

---

**ポイント**：数秒でプロフェッショナルなコードレビュー。手動レビューはもっと時間がかかるでしょう...つまり、これより長いということです！

---

### デモ 2：複雑なコードを説明する

コードを見て何をしているのか不思議に思ったことはありますか？ Copilot CLI セッションでこれを試してください：

```
> Explain what @samples/book-app-project/books.py does in simple terms
```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Explain Code Demo](images/explain-code-demo.gif)

*デモの出力は異なります。あなたのモデル、ツール、応答は、ここに示されているものと異なります。*

</details>

---

**何が起こるか**：（出力は異なります）Copilot CLI はファイルを読み込んでコードを理解し、わかりやすい日本語で説明します。

```
This is a book collection management module using Python dataclasses.

Think of it like a digital bookshelf:
- Book is a dataclass - a simple way to store book information (title, author, year, read status)
- BookCollection manages the entire collection and handles saving/loading

Key components:

1. @dataclass decorator (line 8)
   - Automatically creates __init__, __repr__, etc.
   - Clean way to define data structures in Python

2. BookCollection class (line 16)
   - Maintains a list of Book objects
   - Handles persistence with JSON file I/O
   - load_books() reads from data.json
   - save_books() writes to data.json using asdict()

3. Book operations:
   - add_book() - creates and saves new books
   - find_book_by_title() - searches collection
   - mark_as_read() - updates read status
   - find_by_author() - filters by author name

Common pattern: Read from JSON → Work with Python objects → Write back to JSON
```

**ポイント**：複雑なコードが、忍耐強いメンターが説明するようにわかりやすく説明されます。

---

### デモ 3：動作するコードを生成する

Google で 15 分かけて探すはずだった関数が必要ですか？ 同じセッションで：

```
> Write a Python function that takes a list of books and returns statistics: 
  total count, number read, number unread, oldest and newest book
```

---

<details>
<summary>🎬 実際の動作を見る！</summary>

![Generate Code Demo](images/generate-code-demo.gif)

*デモの出力は異なります。あなたのモデル、ツール、応答は、ここに示されているものと異なります。*

</details>

---

**何が起こるか**：秒単位で、コピーして貼り付けて実行できる完全で動作する関数が生成されます。

探索が終わったら、セッションを終了します：

```
> /exit
```

**ポイント**：即座の満足感。そして、始まりから終わりまで同じセッション内にいました。

---

# モードとコマンド

<img src="images/modes-and-commands.png" alt="Futuristic control panel with glowing screens, dials, and equalizers representing Copilot CLI modes and commands" width="800"/>

これで Copilot CLI がどんなことができるかが見えました。次は、これらの機能を**効果的に使う方法**を理解しましょう。重要なのは、異なるシーンで 3 つのインタラクションモードのどれを使うべきかを知ることです。

> 💡 **注**：Copilot CLI には **Autopilot** モードもあります。このモードは入力を待たずにタスクを進めます。強力ですが、完全な権限の付与が必要で、プレミアムリクエストを自律的に使用します。このコースでは下記の 3 つのモードに焦点を当てています。基礎に慣れたら Autopilot についても説明します。

---

## 🧩 現実の類比：外食に行くこと

GitHub Copilot CLI の使い方を外食に行くことに例えてみましょう。旅の計画からオーダーまで、異なるシーンではアプローチが異なります：

| モード | 食事の類比 | 使う時 |
|--------|-----------|-------|
| **Plan** | レストランへの GPS ルート | 複雑なタスク - ルートを計画し、立ち寄り地を確認し、計画に同意してから実行 |
| **Interactive** | ウェイターと話す | 探索と反復 - 質問して、カスタマイズして、リアルタイムでフィードバックを得る |
| **Programmatic** | ドライブスルー注文 | 素早く具体的なタスク - 環境から出ず、結果を得る |

外食と同じように、自然と各アプローチが適切な場面がわかってきます。

<img src="images/ordering-food-analogy.png" alt="Three Ways to Use GitHub Copilot CLI - Plan Mode (GPS route to restaurant), Interactive Mode (talking to waiter), Programmatic Mode (drive-through)" width="800"/>

*タスクに基づいてモードを選択してください：計画的には Plan、対話的には Interactive、素早い場合は Programmatic*

### どのモードから始めるべき？

**Interactive モードから始めてください。**
- 実験してフォローアップの質問ができます
- 会話を通じて自然にコンテキストが蓄積されます
- `/clear` で簡単に修正できます

快適になったら、以下を試してください：
- **Programmatic モード**（`copilot -p "<your prompt>"`）素早い 1 回限りの質問用
- **Plan モード**（`/plan`）コード化する前に詳しく計画する必要がある場合

---

## 3 つのモード

### モード 1：Interactive モード（ここから始める）

<img src="images/interactive-mode.png" alt="Interactive Mode - Like talking to a waiter who can answer questions and adjust the order" width="250"/>

**最適な用途**：探索、反復、マルチターンの会話。ウェイターと話すような感じで、質問でき、フィードバックに対応し、その場で注文を調整できます。

interactive セッションを開始：

```bash
copilot
```

これまで見たように、自然に入力できるプロンプトが表示されます。利用可能なコマンドについてヘルプを得るには、以下を入力してください：

```
> /help
```

**重要なポイント**：Interactive モードはコンテキストを保持します。各メッセージは前のメッセージに基づいています。実際の会話と同じです。

#### Interactive モードの例

```bash
copilot

> Review @samples/book-app-project/utils.py and suggest improvements

> Add type hints to all functions

> Make the error handling more robust

> /exit
```

各プロンプトが前の回答に基づいていることに注目してください。毎回リセットされるのではなく、会話しているのです。

---

### モード 2：Plan モード

<img src="images/plan-mode.png" alt="Plan Mode - Like planning a route before a trip using GPS" width="250"/>

**最適な用途**：実行前にアプローチをレビューしたい複雑なタスク。旅の前に GPS を使ってルートを計画するようなものです。

Plan モードは、コード化する前に段階的な計画を作成するのに役立ちます。`/plan` コマンドを使うか、**Shift+Tab** を押して Plan モードに切り替えます：

```bash
copilot

> /plan Add a "mark as read" command to the book app
```

> 💡 **ヒント**：**Shift+Tab** はモード間を切り替えます：Interactive → Plan → Autopilot。interactive セッション中いつでも押して、コマンドを入力せずにモードを切り替えることができます。

`--plan` フラグを使って Copilot CLI を直接 Plan モードで起動することもできます：

```bash
copilot --plan
```

**Plan モードの出力：**（出力は異なる場合があります）

```
📋 Implementation Plan

Step 1: Update the command handler in book_app.py
  - Add new elif branch for "mark" command
  - Create handle_mark_as_read() function

Step 2: Implement the handler function
  - Prompt user for book title
  - Call collection.mark_as_read(title)
  - Display success/failure message

Step 3: Update help text
  - Add "mark" to available commands list
  - Document the command usage

Step 4: Test the flow
  - Add a book
  - Mark it as read
  - Verify status changes in list output

Proceed with implementation? [Y/n]
```

**重要なポイント**：Plan モードでは、コードが書かれる前にアプローチをレビューして修正できます。計画が完了したら、後で参照するために Copilot CLI にファイルに保存するよう指示することもできます。たとえば、「Save this plan to `mark_as_read_plan.md`」と言うと、計画の詳細が含まれるマークダウンファイルが作成されます。

> 💡 **もっと複雑なことをしたいですか？** 試してください：`/plan Add search and filter capabilities to the book app`。Plan モードは単純な機能から完全なアプリケーションまでスケールします。

> 📚 **Autopilot モード**：Shift+Tab が **Autopilot** と呼ばれる第 3 のモードを循環することに気づいたかもしれません。Autopilot モードでは、各ステップの後に入力を待つことなく、Copilot が計画全体を進めます。同僚にタスクを渡して「終わったら知らせてね」と言うようなものです。典型的なワークフローは計画 → 受け入れ → Autopilot です。つまり、最初に良い計画を作成することが重要です。`copilot --autopilot` で直接 Autopilot に起動することもできます。Interactive と Plan モードに慣れたら、準備ができたら [公式ドキュメント](https://docs.github.com/copilot/concepts/agents/copilot-cli/autopilot) を参照してください。

---

### モード 3：Programmatic モード

<img src="images/programmatic-mode.png" alt="Programmatic Mode - Like using a drive-through for a quick order" width="250"/>

**最適な用途**：自動化、スクリプト、CI/CD、単発のコマンド。ウェイターと話さずにドライブスルーで素早く注文するようなものです。

単発のコマンドに `-p` フラグを使い、相互作用は不要です：

```bash
# コードを生成
copilot -p "Write a function that checks if a number is even or odd"

# 素早くヘルプを得る
copilot -p "How do I read a JSON file in Python?"
```

**重要なポイント**：Programmatic モードは素速い回答を得て終了します。会話ではなく、入力 → 出力のみです。

<details>
<summary>📚 <strong>もっと詳しく：スクリプト内で Programmatic モードを使う</strong>（クリックして展開）</summary>

慣れたら、`-p` をシェルスクリプトで使用できます：

```bash
#!/bin/bash

# コミットメッセージを自動生成
COMMIT_MSG=$(copilot -p "Generate a commit message for: $(git diff --staged)")
git commit -m "$COMMIT_MSG"

# ファイルをレビュー
copilot --allow-all -p "Review @myfile.py for issues"
```
> ⚠️ **`--allow-all` について**：このフラグはすべての権限プロンプトをスキップし、Copilot CLI がファイルを読み込み、コマンドを実行し、URL にアクセスすることを最初に尋ねずに許可します。プログラマティックモード（`-p`）では相互作用なしのセッションがないため、これが必要です。自分で書いたプロンプトと信頼できるディレクトリでのみ使用してください。信頼できないインプットや機密ディレクトリでは使用しないでください。

</details>

---

## 不可欠なスラッシュコマンド

これらのコマンドは interactive モードで動作します。**最初はこれら 6 つだけで始めてください** - 日常的な使用の 90% をカバーしています：

| コマンド | 何をするか | いつ使う |
|---------|----------|--------|
| `/clear` | 会話をクリアして新しく開始 | トピックを切り替える時 |
| `/help` | すべての利用可能なコマンドを表示 | コマンドを忘れた時 |
| `/model` | AI モデルを表示または切り替え | AI モデルを変更したい時 |
| `/plan` | コード化する前に仕事を計画 | より複雑な機能の場合 |
| `/research` | GitHub と web ソースを使って深い調査 | コード化の前にトピックを調査したい場合 |
| `/exit` | セッションを終了 | 終わった時 |

これが始まりです！快適になったら、追加のコマンドを探索できます。

> 📚 **公式ドキュメント**：[CLI コマンドリファレンス](https://docs.github.com/copilot/reference/cli-command-reference) でコマンドとフラグの完全なリストを参照してください。

<details>
<summary>📚 <strong>追加コマンド</strong>（クリックして展開）</summary>

> 💡 上記の基本的なコマンドは、日常的な使用の大部分をカバーしています。このリファレンスはさらに探索する準備ができた時のためにあります。

### Agent 環境

| コマンド | 何をするか |
|---------|----------|
| `/agent` | 利用可能な agent を閲覧して選択 |
| `/init` | リポジトリに Copilot 指示を初期化 |
| `/mcp` | MCP サーバー設定を管理 |
| `/skills` | 機能強化スキルを管理 |

> 💡 Agent は [Chapter 04](../04-agents-custom-instructions/README.md) で、スキルは [Chapter 05](../05-skills/README.md) で、MCP サーバーは [Chapter 06](../06-mcp-servers/README.md) で取り上げています。

### モデルと Subagent

| コマンド | 何をするか |
|---------|----------|
| `/delegate` | GitHub Copilot クラウド agent にタスクを委譲 |
| `/fleet` | 複雑なタスクを並列サブタスクに分割して完了を高速化 |
| `/model` | AI モデルを表示または切り替え |
| `/tasks` | バックグラウンド subagent と detached シェルセッションを表示 |

### コード

| コマンド | 何をするか |
|---------|----------|
| `/diff` | 現在のディレクトリで行われた変更をレビュー |
| `/pr` | 現在のブランチのプルリクエストを操作 |
| `/research` | GitHub と web ソースを使ってディープリサーチ調査を実行 |
| `/review` | コードレビュー agent を実行して変更を分析 |
| `/terminal-setup` | マルチライン入力サポートを有効化（shift+enter と ctrl+enter） |

### 権限

| コマンド | 何をするか |
|---------|----------|
| `/add-dir <directory>` | ディレクトリを許可リストに追加 |
| `/allow-all [on\|off\|show]` | すべての権限プロンプトを自動承認；`on` を有効化、`off` を無効化、`show` で現在の状態を確認 |
| `/yolo` | `/allow-all on` の素速い別名 — すべての権限プロンプトを自動承認。 |
| `/cwd`, `/cd [directory]` | 作業ディレクトリを表示または変更 |
| `/list-dirs` | 許可されたすべてのディレクトリを表示 |

> ⚠️ **注意して使用してください**：`/allow-all` と `/yolo` は確認プロンプトをスキップします。信頼できるプロジェクトでは素晴らしいですが、信頼できないコードには注意してください。

### セッション

| コマンド | 何をするか |
|---------|----------|
| `/clear` | 現在のセッションを放棄（履歴は保存されない）して新しい会話を開始 |
| `/compact` | コンテキスト使用を削減するために会話を要約 |
| `/context` | コンテキストウィンドウトークン使用状況と可視化を表示 |
| `/new` | 現在のセッションを終了（履歴に保存）して新しい会話を開始 |
| `/resume` | 別のセッションに切り替え（オプションでセッション ID を指定） |
| `/rename` | 現在のセッションの名前を変更（名前を省略すると自動生成） |
| `/rewind` | タイムラインピッカーを開いて、会話内の任意の前のポイントにロールバック |
| `/usage` | セッション使用メトリクスと統計を表示 |
| `/session` | セッション情報とワークスペース概要を表示 |
| `/share` | セッションをマークダウンファイル、GitHub gist、または自己完結型 HTML ファイルとしてエクスポート |

### ヘルプとフィードバック

| コマンド | 何をするか |
|---------|----------|
| `/changelog` | CLI バージョンのチェンジログを表示 |
| `/feedback` | GitHub にフィードバックを送信 |
| `/help` | すべての利用可能なコマンドを表示 |
| `/theme` | ターミナルテーマを表示または設定 |

### 素速いシェルコマンド

`!` を前置詞として使用して、AI をスキップしてシェルコマンドを直接実行：

```bash
copilot

> !git status
# AI をスキップして git status を実行

> !python -m pytest tests/
# pytest を直接実行
```

### モデルを切り替える

Copilot CLI は OpenAI、Anthropic、Google などの複数の AI モデルをサポートしています。利用可能なモデルはサブスクリプションレベルと地域によって異なります。`/model` を使って選択肢を表示してモデルを切り替えてください：

```bash
copilot
> /model

# 利用可能なモデルを表示して選択できます。Sonnet 4.5 を選択します。
```

> 💡 **ヒント**：いくつかのモデルは他のモデルよりも多くの「プレミアムリクエスト」を消費します。**1x** でマークされたモデル（Claude Sonnet 4.5 など）は素晴らしいデフォルトです。能力があり、効率的です。高倍数のモデルはプレミアムリクエストクォータをより速く消費するため、それらが本当に必要な場合は保存してください。

</details>

---

# 実践

<img src="../images/practice.png" alt="Warm desk setup with monitor showing code, lamp, coffee cup, and headphones ready for hands-on practice" width="800"/>

これまで学んだことを実行に移す時です。

---

## ▶️ 自分でやってみる

### Interactive 探索

Copilot を起動し、フォローアッププロンプトを使ってブックアプリを反復的に改善：

```bash
copilot

> Review @samples/book-app-project/book_app.py - what could be improved?

> Refactor the if/elif chain into a more maintainable structure

> Add type hints to all the handler functions

> /exit
```

### Plan a Feature

Use `/plan` to have Copilot CLI map out an implementation before writing any code:

```bash
copilot

> /plan Add a search feature to the book app that can find books by title or author

# Review the plan
# Approve or modify
# Watch it implement step by step
```

### Automate with Programmatic Mode

The `-p` flag lets you run Copilot CLI directly from your terminal without entering interactive mode. Copy and paste the following script into your terminal (not inside Copilot) from the repository root to review all Python files in the book app.

```bash
# Review all Python files in the book app
for file in samples/book-app-project/*.py; do
  echo "Reviewing $file..."
  copilot --allow-all -p "Quick code quality review of @$file - critical issues only"
done
```

**PowerShell (Windows):**

```powershell
# Review all Python files in the book app
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
  $relativePath = "samples/book-app-project/$($_.Name)";
  Write-Host "Reviewing $relativePath...";
  copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only" 
}
```

---

After completing the demos, try these variations:

1. **Interactive Challenge**: Start `copilot` and explore the book app. Ask about `@samples/book-app-project/books.py` and request improvements 3 times in a row.

2. **Plan Mode Challenge**: Run `/plan Add rating and review features to the book app`. Read the plan carefully. Does it make sense?

3. **Programmatic Challenge**: Run `copilot --allow-all -p "List all functions in @samples/book-app-project/book_app.py and describe what each does"`. Did it work on the first try?

---

## 💡 Tip: Control Your CLI Session from Web or Mobile

GitHub Copilot CLI supports **remote sessions**, letting you monitor and interact with a running CLI session from a web browser (on desktop or mobile) or the GitHub Mobile app without being physically at your terminal.

Start a remote session with the `--remote` flag:

```bash
copilot --remote
```

Copilot CLI will display a link and provide access to a QR code. Open the link on your phone or in a desktop browser tab to watch the session in real time, send follow-up prompts, review plans, and steer the agent remotely. Sessions are user-specific so you can only access your own Copilot CLI sessions.

You can also enable remote access from inside an active session at any time:

```
> /remote
```

Additional details about remote sessions can be found in the [Copilot CLI docs](https://docs.github.com/copilot/how-tos/copilot-cli/steer-remotely).

---

## 📝 Assignment

### Main Challenge: Improve the Book App Utilities

The hands-on examples focused on reviewing and refactoring `book_app.py`. Now practice the same skills on a different file, `utils.py`:

1. Start an interactive session: `copilot`
2. Ask Copilot CLI to summarize the file: `@samples/book-app-project/utils.py What does each function in this file do?`
3. Ask it to add input validation: "Add validation to `get_user_choice()` so it handles empty input and non-numeric entries"
4. Ask it to improve error handling: "What happens if `get_book_details()` receives an empty string for the title? Add guards for that."
5. Ask for a docstring: "Add a comprehensive docstring to `get_book_details()` with parameter descriptions and return values"
6. Observe how context carries between prompts. Each improvement builds on the last
7. Exit with `/exit`

**Success criteria**: You should have an improved `utils.py` with input validation, error handling, and a docstring, all built through a multi-turn conversation.

<details>
<summary>💡 Hints (click to expand)</summary>

**Sample prompts to try:**
```bash
> @samples/book-app-project/utils.py What does each function in this file do?
> Add validation to get_user_choice() so it handles empty input and non-numeric entries
> What happens if get_book_details() receives an empty string for the title? Add guards for that.
> Add a comprehensive docstring to get_book_details() with parameter descriptions and return values
```

**Common issues:**
- If Copilot CLI asks clarifying questions, just answer them naturally
- The context carries forward, so each prompt builds on the previous
- Use `/clear` if you want to start over

</details>

### Bonus Challenge: Compare the Modes

The examples used `/plan` for a search feature and `-p` for batch reviews. Now try all three modes on a single new task: adding a `list_by_year()` method to the `BookCollection` class:

1. **Interactive**: `copilot` → ask it to design and build the method step by step
2. **Plan**: `/plan Add a list_by_year(start, end) method to BookCollection that filters books by publication year range`
3. **Programmatic**: `copilot --allow-all -p "@samples/book-app-project/books.py Add a list_by_year(start, end) method that returns books published between start and end year inclusive"`

**Reflection**: Which mode felt most natural? When would you use each?

---

<details>
<summary>🔧 <strong>Common Mistakes & Troubleshooting</strong> (click to expand)</summary>

### Common Mistakes

| Mistake | What Happens | Fix |
|---------|--------------|-----|
| Typing `exit` instead of `/exit` | Copilot CLI treats "exit" as a prompt, not a command | Slash commands always start with `/` |
| Using `-p` for multi-turn conversations | Each `-p` call is isolated with no memory of previous calls | Use interactive mode (`copilot`) for conversations that build on context |
| Forgetting quotes around prompts with `$` or `!` | Shell interprets special characters before Copilot CLI sees them | Wrap prompts in quotes: `copilot -p "What does $HOME mean?"` |

### Troubleshooting

**"Model not available"** - Your subscription may not include all models. Use `/model` to see what's available.

**"Context too long"** - Your conversation has used the full context window. Use `/clear` to reset, or start a new session.

**"Rate limit exceeded"** - Wait a few minutes and try again. Consider using programmatic mode for batch operations with delays.

</details>

---

# 要約

## 🔑 重要なポイント

1. **Interactive モード** は探索と反復用です。コンテキストが前に進みます。これまで言ったことを覚えている誰かと会話しているようなものです。
2. **Plan モード** は通常より複雑なタスク用です。実装前にレビューします。
3. **Programmatic モード** は自動化用です。相互作用は必要ありません。
4. **基本的なコマンド**（`/help`、`/clear`、`/plan`、`/research`、`/model`、`/exit`）は日常的な使用の大部分をカバーしています。

> 📋 **クイックリファレンス**：[GitHub Copilot CLI コマンドリファレンス](https://docs.github.com/en/copilot/reference/cli-command-reference) でコマンドとショートカットの完全なリストを参照してください。

---

## ➡️ 次は何？

3 つのモードを理解したので、コードについてのコンテキストを Copilot CLI に与える方法を学びましょう。

**[Chapter 02: Context and Conversations](../02-context-conversations/README.md)** では、以下について学びます：

- ファイルとディレクトリを参照するための `@` 構文
- `--resume` と `--continue` でのセッション管理
- コンテキスト管理が Copilot CLI を本当に強力にする方法

---

**[← コースホームに戻る](../README.md)** | **[Chapter 02 に進む →](../02-context-conversations/README.md)**
