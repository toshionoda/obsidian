---
title: "完全自律型AIエージェントOSS【LangManus】完全に理解した！"
source: "https://zenn.dev/asap/articles/b27e832c2a49b7"
author:
  - "[[Zenn]]"
published:
created: 2025-03-29
description:
tags:
  - "clippings"
---
36 15

[tech](https://zenn.dev/tech-or-idea)

## LangManusとは

[https://github.com/langmanus/langmanus](https://github.com/langmanus/langmanus)

LangManusはLangGraphを利用したManusの再現実装です。  
そもそもManusは中国のAIスタートアップが発表した完全自律型のAIエージェントです。

通常の対話型のチャットボットAIではなく、ユーザの指示に基づいて、自発的に問題解決の方法を検討し、自律的にタスクを実行できます。  
みじかな例では、Open AIのDeep Researchに近いです。

LangManusは、その自律型のAIエージェントをLangGraphを利用して再現しようというオープンソースの試みです。  
試した感じでは、流石にまだまだ性能はDeep Researchなどには及んでいませんが、面白い試みだと思います。

## よりシンプルなAIエージェント実装する

今回はLangManusのように、LangGraphを用いて自律型のAIエージェントを構築する方法を学ぶために、LangManusを参考にして、シンプル版を実装します。

シンプル版であっても、実際に実装してみると、かなり中身を理解できたので今回記事を書きました。  
**LangManus完全に理解した！**

なお、今回の記事は、LangChainとLangGraphを理解していることを前提に記載しています。  
参考にできそうな書籍や記事は、本記事の最後に置いておきます。

## LangManusの構造

LangManusは下記のようなエージェントの構造になっています。

![](https://storage.googleapis.com/zenn-user-upload/525fe642f188-20250326.png)

各ノードの説明は下記です。

- Coordinator: 初期のインタラクションを処理し、タスクをルーティングするエントリーポイント
	- 雑談などが入ってきたらplannerノードに入力せずに返答して終わる
- Planner: タスクを分析し、実行戦略を作成
- Supervisor: 他のエージェントの実行を監督・管理する
	- 各ノード実行後に必ず呼ばれ、次はどのノードを呼ぶかを管理している
- Researcher: 情報を収集・分析する
	- Web検索などを行い、情報を取得する
- Coder: コードの生成・修正を行う
- Browser: ウェブ閲覧や情報収集を実施する
	- [browser-use](https://github.com/browser-use/browser-use) を利用して情報収集を行う
- Reporter: ワークフロー結果のレポートや要約を生成する
	- 最後に一度だけ呼ばれ、最終的な結果をコンソールに出力する

さらに、LangManusでは、Plannerノードには、Reasoningモデルを利用し、そのほかのノードで画像入力が必要（browser-useなど）な場合は、Visonモデルを、そうでない場合は普通のLLMを利用しており、 `conf.yaml` にて設定する形になっています。

## 今回作成するシンプルなAIエージェントの構造

![](https://storage.googleapis.com/zenn-user-upload/02bf10a38961-20250326.png)

なるべくシンプルにするために、多くの要素を削減してWeb検索のみにしています。  
その上で出力結果をファイル出力できるように、ノードを一つ追加しています。

各ノードの説明は下記です。

- Planner: タスクを分析し、実行戦略を作成
- Supervisor: 他のエージェントの実行を監督・管理する
	- 各ノード実行後に必ず呼ばれ、次はどのノードを呼ぶかを管理している
- Researcher: 情報を収集・分析する
	- Web検索などを行い、情報を取得する
- FileManager: 必要に応じて出力結果をファイルに保存する
- Reporter: ワークフロー結果のレポートや要約を生成する
	- 最後に一度だけ呼ばれ、最終的な結果をコンソールに出力する

このように、構造を学ぶためにだいぶシンプルな形にしました。  
また、Visionモデルを利用する必要がなくなったことと、よりシンプルにするために、全てのノードにおいて`.env` で指定した同じLLMを利用することとします。

## 成果物

下記のリポジトリをご覧ください。  
[https://github.com/personabb/simple\_langmanus](https://github.com/personabb/simple_langmanus)

## コード

実行方法と結果を確認したい場合は、次の章までスキップしてください。

## リポジトリ構成

今回のライブラリの構造は下記のようにシンプルな形にしました。  
（コードの中身はほとんどLangManusの流用です）

```md
simple_LangManus/
├── .env
├── graph.py
├── main.py
├── utils.py
└── prompt/
    ├── file_manager.md
    ├── planner.md
    ├── reporter.md
    ├── researcher.md
    └── supervisor.md
```

- `prompt/` フォルダ
	- LangManusの [こちら](https://github.com/langmanus/langmanus/tree/main/src/prompts) に各エージェントのシステムプロンプトが格納されているので、基本それを利用しています。
	- 一部適当に修正している箇所ありますが、大きな変更はないです。
- `main.py`
	- AIエージェントのメイン実行スクリプト
	- Graphを構築し、ユーザクエリを入力、結果の表示、ログの出力
- `graph.py`
	- エージェントのワークフローやノードを定義するスクリプト全般
- `utils.py`
	- LLMの初期化やプロンプト処理などの関数全般
- `.env`
	- 利用するLLMのモデル名やAPIキーを設定する環境設定ファイル

3つのpythonスクリプトのみで、最低限の実装しています。  
コード自体は、LangManusのコードをだいぶ流用しているので、本コードを理解すれば大体LangManusを理解できると思います。

## main.py

重要なのは下記の部分です。  
Graphを構築し、ユーザの入力をコンソールから受付け、それをLangGraphに入力しています。

```python
graph = build_graph()

user_query = input("Enter your query: ")

result = graph.invoke(
    {
        # Constants
        "TEAM_MEMBERS": TEAM_MEMBERS,
        # Runtime Variables
        "messages": [{"role": "user", "content": user_query}],
    }
)
```

`TEAM_MEMBERS` は `utils.py` で定義されている変数で、利用できるエージェントの種類（名前）のリストです。

## utils.py

ここでは、AIエージェント実装に利用する関数をまとめたスクリプトファイルです。

#### 環境変数の取得

```python
# .envファイルを読み込み
load_dotenv()

NAME = os.getenv('NAME')
MODEL_NAME = os.getenv('MODEL_NAME')
TEMPERATURE = os.getenv('TEMPERATURE', None)
if TEMPERATURE:
    TEMPERATURE = float(TEMPERATURE)
API_BASE = os.getenv('API_BASE', None)
API_KEY = os.getenv('API_KEY', None)
API_VERSION = os.getenv('API_VERSION', None)
os.environ["TAVILY_API_KEY"] = os.getenv('TAVILY_API_KEY')
```

`.env` ファイルの中で指定したモデル名やAPIキーなどをここで取得します。

#### 利用するノードの設定

```python
# Team configuration
TEAM_MEMBER_CONFIGRATIONS = {
    "researcher": {
        "name": "researcher",
        "desc": (
            "Responsible for searching and collecting relevant information, understanding user needs and conducting research analysis"
        ),
        "is_optional": False,
    },
    "reporter": {
        "name": "reporter",
        "desc": (
            "Responsible for summarizing analysis results, generating reports and presenting final outcomes to users, File output is not available."
        ),
        "is_optional": False,
    },
    "file_manager": {
        "name": "file_manager",
        "desc": (
            "Responsible for saving results to markdown files. Formats content nicely with proper markdown syntax before saving."
        ),
        "is_optional": True,
    },
}

TEAM_MEMBERS = list(TEAM_MEMBER_CONFIGRATIONS.keys())
```

`main.py` でも利用されていた `TEAM_MEMBERS` を定義しています。  
これは今回の実装の中で利用できるノードとその説明を定義しています。  
ここで定義したもの（ `researcher` 、 `reporter` 、 `file_manager` ）が `Planner` ノードのプロンプトに利用されます。  
（ただし `Supervisor` ノードは除く）

詳細はそちらの `prompt/planner.md` をご覧ください。  
（LangManusの実装ほぼ同じです）

#### プロンプトの設定

```python
# Initialize Jinja2 environment
env = Environment(
    loader=FileSystemLoader(os.path.dirname(__file__)),
    autoescape=select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True,
)

def apply_prompt_template(prompt_name: str, state: AgentState) -> list:
    """
    Apply template variables to a prompt template and return formatted messages.

    Args:
        prompt_name: Name of the prompt template to use
        state: Current agent state containing variables to substitute

    Returns:
        List of messages with the system prompt as the first message
    """
    # Convert state to dict for template rendering
    state_vars = {
        "CURRENT_TIME": datetime.now().strftime("%a %b %d %Y %H:%M:%S %z"),
        **state,
    }

    try:
        template = env.get_template(f"prompt/{prompt_name}.md")
        system_prompt = template.render(**state_vars)
        return [{"role": "system", "content": system_prompt}] + state["messages"]
    except Exception as e:
        raise ValueError(f"Error applying template {prompt_name}: {e}")
```

`apply_prompt_template` 関数にて、現在時刻を取得したのち、今回利用するノードごとに別々のmdファイルからプロンプトのテンプレートを取得し、 `State` 内の必要情報（例えば `TEAM_MEMBERS` など）と現在時刻からSystemプロンプトを構築します。

そして最後に、システムプロンプトとこれまでユーザ入力やLLMの返答履歴が格納されている `state["messages"]` をくっつけたリストを返します。

（LangManusの実装ほぼ同じです）

#### LangChainでのLLMモデルの定義

```python
def initialize_llm(name: str, model_name: str, temperature: float):
    """
    指定されたパラメータを用いて LLM を初期化する関数。
    """
    llm = None

    # 例: Azure, Google, VertexAI, HuggingFace, OpenAI_Base, xAI, Ollama 等
    if name == "Azure":
        from langchain_openai import AzureChatOpenAI
        llm = AzureChatOpenAI(
            azure_deployment=model_name,
            temperature=temperature,
            azure_endpoint=API_BASE,
            api_version=API_VERSION,
            api_key=API_KEY,
        )

    elif name == "Google":
        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=API_KEY,
            temperature=temperature
        )

    elif name == "OpenAI_Base":
        # DeepSeekやOpenAIのエンドポイント指定例。用途に応じて調整してください。
        api_key = API_KEY
        api_endpoint = "https://api.openai.com/v1"
        if "deepseek" in model_name:
            api_endpoint = "https://api.deepseek.com"

        if api_key == "":
            raise ValueError("OpenAI API Key が設定されていません。")

        from langchain_openai import ChatOpenAI  
        llm = ChatOpenAI(
            model=model_name,
            openai_api_key=api_key,
            openai_api_base=api_endpoint,
            temperature=temperature
        )

    elif name == "xAI":
        from some_xai_module import ChatXAI  # xAI用の仮の例
        llm = ChatXAI(
            model=model_name,
            api_key=API_KEY,
            temperature=temperature,
        )
    else:
        raise ValueError("サポートされていない LLM 名が指定されました。")

    return llm
```

ここだけ自分が使いやすいように、LangManusの実装から変更しています。  
2025年3月21日時点の実装では、 `o3-mini` などの `temperature` 指定を受け付けないモデルが利用できない実装になっていたため、自分で実装しています。  
ここでは下記のプロバイダーが利用可能です。

- Azure
- Google
- OpenAI
- DeepSeek
- xAI

それぞれ、`.env` ファイルで指定することで利用できます。

## graph.py

さて、最も重要な実装の部分です。  
ここでは、AIエージェントを構築する上で重要なLangGraphの実装が全て格納されています。  
解説のため、コード内の順番とは異なる順番で記載していきます。

#### グラフの構築

```python
class State(MessagesState):
    """State for the agent system, extends MessagesState with next field."""

    # Constants
    TEAM_MEMBERS: list[str]

    # Runtime Variables
    next: str
    full_plan: str

def build_graph():
    """Build and return the agent workflow graph."""
    builder = StateGraph(State)
    builder.add_edge(START, "planner")
    builder.add_node("planner", planner_node)
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("researcher", research_node)
    builder.add_node("file_manager", file_manager_node)
    builder.add_node("reporter", reporter_node)
    return builder.compile()
```

ここでグラフ全体の定義をしています。スタート以外でエッジの定義をしていないのは、各ノードの `return` にて `Command` コマンドにて動的に行き先を決定しているためです。  
ここをみてもわかるように、下記のノードを利用します。

- `planner`
- `supervisor`
- `researcher`
- `file_manager`
- `reporter`

また、Graph実行中は、各ノード間で `State` のやり取りを行うことになります。  
`State` には、今回利用できるノード名が格納されている `TEAM_MEMBERS` や、明示されてはいないですが過去の会話履歴が `message` として格納されています。

では、それぞれのノードについて解説していきます。

#### plannerノード

ちょっと長いので、ログ出力の部分などは省略しています。  
ログ出力部分含めた全文は、 [github](https://github.com/personabb/simple_langmanus/blob/main/graph.py) からご覧ください。

```python
llm = initialize_llm(name=NAME, model_name=MODEL_NAME, temperature=TEMPERATURE)

def planner_node(state: State) -> Command[Literal["supervisor", "__end__"]]:
    """
    プランナーノード: 今後の計画（フルプラン）を生成する。
    """
    messages = apply_prompt_template("planner", state)

    response = llm.invoke(messages)
    full_response = response.content

    # JSON構造の修正を試みる
    if full_response.startswith("\njson"):
        full_response = full_response.removeprefix("\njson")
    if full_response.endswith("\n"):
        full_response = full_response.removesuffix("\n")

    goto = "supervisor"
    try:
        repaired_response = json_repair.loads(full_response)
        full_response = json.dumps(repaired_response, ensure_ascii=False)
    except json.JSONDecodeError:
        goto = "__end__"

    return Command(
        update={
            "messages": [AIMessage(content=full_response, name="planner")],
            "full_plan": full_response,
        },
        goto=goto,
    )
```

ここでは、まず `apply_prompt_template` 関数を利用して、 `planner.md` を利用して、システムプロンプトとユーザクエリを `state["messages"]` に格納します。  
その後、設定したLLMに入力し、ユーザクエリを解決するために必要な小さなタスクを、手持ちのチーム `TEAM_MEMBERS` の範囲内で設計します。

得られた計画書を `state["messages"]` に格納して、 `Command` コマンドから、 `supervisor` ノードに移動します。

#### supervisorノード

```python
llm = initialize_llm(name=NAME, model_name=MODEL_NAME, temperature=TEMPERATURE)

OPTIONS = TEAM_MEMBERS + ["FINISH"]

class Router(TypedDict):
    """Worker to route to next. If no workers needed, route to FINISH."""

    next: Literal[*OPTIONS]

RESPONSE_FORMAT = "Response from {}:\n\n<response>\n{}\n</response>\n\n*Please execute the next step.*"

def supervisor_node(state: State) -> Command[Literal[*TEAM_MEMBERS, "__end__"]]:
    """
    スーパーバイザーノード: 次に動くノード(誰にタスクを渡すか)を判断する。
    """
    messages = apply_prompt_template("supervisor", state)
    for message in messages:
        if isinstance(message, BaseMessage) and message.name in TEAM_MEMBERS:
            message.content = RESPONSE_FORMAT.format(message.name, message.content)
    
    # LLMにSupervisorのプロンプトを渡し、次にどのノードへ行くかを取得
    response = (
        llm.with_structured_output(schema=Router, method="json_mode")
        .invoke(messages)
    )
    goto = response["next"]

    if goto == "FINISH":
        goto = "__end__"

    return Command(goto=goto, update={"next": goto})
```

この `supervisor` ノードは、各ノードが呼ばれた後に必ず呼ばれるノードになります。  
このノードが、これまでの実行内容をもとに、次にどのタスクを実行するかを決定します。

コードとしてはまず、 `apply_prompt_template` 関数により `supervisor.md` のプロンプトを呼び出し、これまでの実行内容をまとめてプロンプトにします。  
その後、 `RESPONSE_FORMAT` を各タスクの出力に適用し、LLMに入力します。

LLMの出力は `Router` クラスに従って出力されます。従って、ここで適切な（ `TEAM_MEMBERS` に入っている）ノードが選択され、そのノードに `Command` コマンドで移動します。

#### Researcherノード

```python
llm = initialize_llm(name=NAME, model_name=MODEL_NAME, temperature=TEMPERATURE)

tavily_search_tool = TavilySearch(
    max_results=5,
    topic="general",
)
tavily_extract_tool = TavilyExtract()

research_agent = create_react_agent(
    llm,
    tools=[tavily_search_tool, tavily_extract_tool],
    prompt=lambda state: apply_prompt_template("researcher", state),
    debug=False,
)

def research_node(state: State) -> Command[Literal["supervisor"]]:
    """
    リサーチノード: research_agent を起動して、外部検索や補助的な情報取得を行う。
    """

    result = research_agent.invoke(state)

    response_content = result["messages"][-1].content
    response_content = repair_json_output(response_content)

    return Command(
        update={
            "messages": [
                AIMessage(
                    content=response_content,
                    name="researcher",
                )
            ]
        },
        goto="supervisor",
    )
```

`Researcher` ノードでは、 `TavilySearch` と `TavilyExtract` ツールを利用して、Web検索、内容抽出を行う、 `research_agent` を利用します。  
そしてノードの最初に、 `research_agent` が実行され、検索結果とその内容が抽出されまとめられます。  
（agentを定義する際に、 `apply_prompt_template` 関数をpromptに指定しているため、実行( `invoke` )時に渡された `state` からプロンプトが構築されます）

抽出した結果を `state["messages"]` に追加し、 `Command` コマンドで `supervisor` ノードに移行します。

#### FileManagerノード

```python
llm = initialize_llm(name=NAME, model_name=MODEL_NAME, temperature=TEMPERATURE)

write_file_tool = WriteFileTool()

file_manager_agent = create_react_agent(
    llm,
    tools=[write_file_tool],
    prompt=lambda state: apply_prompt_template("file_manager", state),
    debug=False,
)

def file_manager_node(state: State) -> Command[Literal["supervisor"]]:
    """
    file_managerノード: 必要に応じて結果をファイルに保存する。
    """

    result = file_manager_agent.invoke(state)
    response_content = result["messages"][-1].content
    response_content = repair_json_output(response_content)

    return Command(
        update={
            "messages": [
                AIMessage(
                    content=response_content,
                    name="file_manager",
                )
            ]
        },
        goto="supervisor",
    )
```

`FileManager` ノードでは、 `WriteFileTool` ツールを利用して、内容をファイルとして保存する、 `file_manager_agent` を利用します。  
そしてノードの最初に、 `file_manager_agent` が実行され、これまでの結果をユーザが指定したフォルダ、もしくはエージェントが決めたフォルダにファイルとして保存されます。（ファイル名は勝手に決定してくれます）  
（agentを定義する際に、 `apply_prompt_template` 関数をpromptに指定しているため、実行( `invoke` )時に渡された `state` からプロンプトが構築されます）

こちらのノードも同様に `Command` コマンドで `supervisor` ノードに移行します。

#### Reporterノード

```python
def reporter_node(state: State) -> Command[Literal["supervisor"]]:
    """
    レポーターノード: 最終的なレポートやサマリーを作成する。
    """

    messages = apply_prompt_template("reporter", state)

    response = llm.invoke(messages)
    response_content = response.content
    response_content = repair_json_output(response_content)

    return Command(
        update={
            "messages": [
                AIMessage(
                    content=response_content,
                    name="reporter",
                )
            ]
        },
        goto="supervisor",
    )
```

`Reporter` ノードは、タスクの一番最後に一度だけ呼ばれるノードで、これまでのツール等の実行結果を踏まえて最終的な出力を用意するノードになります。  
ここでも `apply_prompt_template` 関数によりプロンプトが構築され、モデルに入力されます。そして結果を結果を `state["messages"]` に追加し、 `Command` コマンドで `supervisor` ノードに移行します。  
`reporter` ノードが実行されたら、基本的には `supervisor` ノードに移行した後、処理が終了します。

## 実行

ここからは、実際に `simple_langmanus` を実行します。

## 事前準備

### リポジトリのクローン

下記コマンドでリポジトリをクローンしてください。

```
git clone https://github.com/personabb/simple_langmanus.git
```

### 環境設定（.env）

続いて、利用するモデルやAPIキーなどの環境変数を設定します。  
まずは、サンプルをコピーします。下記コマンドを実行してください。

```
cd simple_langmanus
cp .env_example .env
```

続いて、`.env` の中身を設定してください。  
今回は、OpenAIのAPIを利用し、 `o3-mini` モデルを利用しようと思います。安いので  
その場合、下記のように設定してください。  
(OpenAIの)API\_KEYとTAVILY\_API\_KEYは自分で取得して投入してください。

`Azure` のAPIを利用したい場合は、「API\_BASE」にエンドポイントを「API\_VERSION」にAPIバージョンを入力し、コメントアウトをはずしてください。  
また、 `o3-mini` では `TEMPERATURE` は指定できないので、コメントアウトしていますが、そのほかのモデルを利用する場合は、この値を設定し、小さい値を設定すると出力が安定するのでおすすめです。  
（o3-miniでもTEMPERATUREの設定できるようにして）

```python
NAME="OpenAI_Base" #OpenAI_Base, Google, xAI
MODEL_NAME="o3-mini"
TAVILY_API_KEY=tvly-dxxxxx

#OPTIONAL
#TEMPERATURE=0.001
#API_BASE=https://xxxxx.openai.azure.com
API_KEY=xxxxx
#API_VERSION=2024-12-01-preview
```

## エージェントの実行

下記コマンドで実行できます。

```
python main.py
```

実行後、 `Enter your query: ` と表示されるため、お願いしたいタスクを入力してEnterを押せば、処理完了まで実行してくれます。

また、処理のログは `logs/output.log` に格納されるようになっています。

## 実行結果

#### 実行クエリ

今回は例として下記のタスクをお願いしました。

```
「https://litpla.com/space/lalaport_tokyo-bay/」左の公式サイトがある「リトルプラネット」について調査をして、実際に5さいの娘と遊んだレビュー記事を書いてください。この時、適当なことを書かれては困るので、他のリトルプラネットレビュー記事の内容を複数調査して、その情報を参考にしてレビュー記事を記載してください。加えて、そのほかの近隣の競合施設の調査を行い、ほかの施設と比較したリトルプラネットの良さに関しても、記事内に加えてください。記事の長さは長文で10000文字程度を想定します。レビュー記事は親目線で親しみやすい文章で記載してください。出力は「output」フォルダに保存してください。
```

#### 実行計画

結果として `Planner` は下記のような実行計画を立てました。

```python
{
  "thought": "ユーザーは、『https://litpla.com/space/lalaport_tokyo-bay/』の公式サイトを基に、『リトルプラネット』という施設について、実際に5歳の娘と遊んだという体験を元にしたレビュー記事を、他のレビュー記事や近隣競合施設の情報も参照して執筆するよう求めています。記事は親目線で親しみやすい文章で、約10000文字程度の長文にする必要があり、結果は『output』フォルダに保存する必要があります。",
  "title": "『リトルプラネット』レビュー記事執筆と競合施設比較に関する調査・作成プラン",
  "steps": [
    {
      "agent_name": "researcher",
      "title": "リトルプラネット公式サイトとレビュー記事の情報収集",
      "description": "『リトルプラネット』の公式サイト（https://litpla.com/space/lalaport_tokyo-bay/）に関する情報を詳細に確認し、施設の特徴、遊びのポイント、親目線での魅力（特に5歳児との体験に関連する情報）をピックアップする。また、既存のリトルプラネットのレビュー記事（複数の情報ソースから）を調査し、内容の傾向や重要なキーワード、評価ポイントをまとめる。"
    },
    {
      "agent_name": "researcher",
      "title": "近隣競合施設の調査",
      "description": "近隣の他施設（競合施設）に関する情報を複数収集し、各施設の特徴、遊び場としての魅力、設備や利用料金、利用者の口コミなどを調査する。これにより、リトルプラネットの特徴との比較ができるようにする。"
    },
    {
      "agent_name": "researcher",
      "title": "調査結果のまとめと記事構成の策定",
      "description": "収集したリトルプラネットと競合施設の情報を整理し、レビュー記事の構成（イントロダクション、体験談、比較検討、総評など）を策定する。記事内には、実際に5歳の娘と過ごした体験を元にした具体的なエピソードを含め、親しみやすい文章で読者に伝わるようにする。"
    },
    {
      "agent_name": "file_manager",
      "title": "記事のMarkdownファイルの生成・保存",
      "description": "調査と構成内容を踏まえた詳細なレビュー記事（10000文字程度の長文）をMarkdownファイルとして『output』フォルダに保存する。Markdown形式で適切にフォーマットし、見出し、段落、リストなどを利用して読みやすく整形する。"
    },
    {
      "agent_name": "reporter",
      "title": "最終報告と記事概要の提供",
      "description": "ファイルに保存されたレビュー記事を基に、記事の概要と重要なポイントをまとめた最終報告を作成する。報告書は親しみやすいトーンで記載し、記事の内容と調査過程についての全体像を簡潔に伝える。"
    }
  ]
}
```

#### 最終的なアウトプット

最終的な出力結果は下記をご覧ください  
[https://github.com/personabb/simple\_langmanus/blob/main/output/リトルプラネットレビュー-o3.md](https://github.com/personabb/simple_langmanus/blob/main/output/%E3%83%AA%E3%83%88%E3%83%AB%E3%83%97%E3%83%A9%E3%83%8D%E3%83%83%E3%83%88%E3%83%AC%E3%83%93%E3%83%A5%E3%83%BC-o3.md)

こちらを見ると、「リトルプラネット」の施設の説明はそこそこあっているように感じます。一方で近隣の競合施設の調査がボロボロです。そもそも近隣ですらないし、アトラクション施設ですらない・・・

#### なぜ、近隣の競合施設の調査がボロボロ？

これが発生してしまっている理由は、logを見るとわかります。logは下記に格納しております。  
[https://github.com/personabb/simple\_langmanus/blob/main/logs/output-o3-0326.log](https://github.com/personabb/simple_langmanus/blob/main/logs/output-o3-0326.log)

こちらを詳細に読んでいくとわかるのですが、下記のような流れになってしまっています。

- `Planner` が計画を立てる
	- 下記がたてた計画
		- `researcher` が「リトルプラネット」について調べる
		- `researcher` が近隣の競合施設を調査する
		- `researcher` が調査結果をまとめて記事構成を策定する
		- `file_manager` が記事を構成して結果をファイルに出力する
- `Supervisor` が `researcher` に転送する
- 最初の `researcher` が「リトルプラネット」ついて調べて、 **「なぜかレビュー記事を書き始める」**
- `Supervisor` がなぜか、 **「file\_managerに転送する」**
- レビュー記事がファイルに出力されて終了

本来であれば、複数回 `researcher` が呼ばれて、さまざまな要素を調査しないといけないのですが、最初の `researcher` が最初の検索を行った後に、それをもとにレビュー記事を書いてしまったせいで、後段の `Supervisor` がもう十分と判断してしまったことが原因です。

#### 現在の実装の悪い点

ここでは3つの悪いところがあります。

- `researcher` が自分の担当ではないのにレビュー記事を書いてしまったこと
- レビュー記事を書くときに調べていない近隣の競合施設を思い込みだけで書いてしまったこと（ハルシネーション）
- `Supervisor` が不十分な調査であるにもかかわらず、調査完了と判断してしまったこと

#### 対処法

これに対処するためには下記のような対処法が考えられます。

- `researcher` が担当領域以外のタスクを実行しないようにする
	- system promptに禁止事項として記載する
		- 実はこれはすでにsystemプロンプトに記載されてるんですが、無視されてます・・・
	- そもそもユーザプロンプトを見せない。 `Planner` が出力した担当タスクだけを見せる
		- その場合、 `Planner` はさらに細かくタスク内容を記載する必要がある。意図など
- `researcher` が調査して得た情報以外をもとに、最終出力をさせないようにする
	- わからないところは、まだわからないと記載させるようにプロンプトを作る
- `Supervisor` に思考をさせる
	- 現時点では、 `Supervisor` は行き先のノード名だけを出力するので、もっと思考させて行き先が妥当であるか判断させてから出力するのが良さそう

**もしかしたら、他にも良い実装があるかもしれないです。詳しい方ご存知でしたら教えてください。**

## まとめ

LangGraphでManusを再現しようという試みである、LangManusについて理解するために、シンプルなAIエージェントを実装しました。  
（今回記事の結果ではなくLangManusの）結果を見ると、正直Manusレベルには全く及んでいないように思ってしまいますし、実際、今回記事で実装した結果もほぼ同様な感じでした。  
ですが、まだまだ出てきたばかりなので、精度や使えるツールなど今度どんどん改善されていくことを期待します！

## おすすめ記事・書籍

（書籍のリンクはamazonアフィリエイトリンクになります）

### 記事

#### LangChain

[https://www.langchain.com/](https://www.langchain.com/)

[https://zenn.dev/asap/articles/aa587ad8d76105](https://zenn.dev/asap/articles/aa587ad8d76105)

#### LangGraph

[https://zenn.dev/asap/articles/5da9cf01703a47](https://zenn.dev/asap/articles/5da9cf01703a47)

[https://zenn.dev/pharmax/articles/d91085d904657d](https://zenn.dev/pharmax/articles/d91085d904657d)

[https://python.langchain.com/docs/how\_to/migrate\_agent/](https://python.langchain.com/docs/how_to/migrate_agent/)

[https://note.com/npaka/n/nf9bb361de223](https://note.com/npaka/n/nf9bb361de223)

### 書籍

とりあえず、体系的にLangChainとLangGraphを学ぶなら、下記1冊から始めるのがおすすめ  
[LangChainとLangGraphによるRAG・AIエージェント［実践］入門](https://amzn.to/4hMgiJ1)

最近出た本ですが、LangChainとLangGraphについてかなりのページ数を割いて説明している本です。  
LangChainとLangGraphの部分だけ読んだのですが、内容しっかりしており、また細かい発展的な部分まで解説されているので、2冊目に良いのではないかなと思います。  
[仕組みからわかる大規模言語モデル 生成AI時代のソフトウェア開発入門](https://amzn.to/4239wY3)

36 15