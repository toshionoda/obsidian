---
title: "ANN：Agentic Neural Network - マルチエージェント構築自動化手法"
source: "https://zenn.dev/boku_yaji/articles/8aa3ef7f772460"
author:
  - "[[Zenn]]"
published: 2025-06-17
created: 2025-06-18
description:
tags:
  - "clippings"
---
[tech](https://zenn.dev/tech-or-idea)

## Agentic Neural Network (ANN) 論文解説

2025/6/10の論文のAgentic Neural Networks: Self-Evolving Multi-Agent Systems via Textual Backpropagation についての解説記事です。

- [0\. TL;DR](https://zenn.dev/boku_yaji/articles/#0-tldr%E3%81%BE%E3%81%9A-3-%E8%A1%8C%E3%81%A7%E6%A6%82%E8%A6%81%E3%82%92%E3%81%A4%E3%81%8B%E3%82%80)
- [1\. 背景と課題 ― 「強いけど組むのが面倒」問題](https://zenn.dev/boku_yaji/articles/#1-%E8%83%8C%E6%99%AF%E3%81%A8%E8%AA%B2%E9%A1%8C-%E2%80%95-%E5%BC%B7%E3%81%84%E3%81%91%E3%81%A9%E7%B5%84%E3%82%80%E3%81%AE%E3%81%8C%E9%9D%A2%E5%80%92%E5%95%8F%E9%A1%8C)
	- [1.1 マルチエージェントは強い](https://zenn.dev/boku_yaji/articles/#11-%E3%83%9E%E3%83%AB%E3%83%81%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%81%AF%E5%BC%B7%E3%81%84)
	- [1.2 しかし設計は人力](https://zenn.dev/boku_yaji/articles/#12-%E3%81%97%E3%81%8B%E3%81%97%E8%A8%AD%E8%A8%88%E3%81%AF%E4%BA%BA%E5%8A%9B)
	- [1.3 ANN の狙い](https://zenn.dev/boku_yaji/articles/#13-ann-%E3%81%AE%E7%8B%99%E3%81%84)
- [2\. ANN の核心アイデア](https://zenn.dev/boku_yaji/articles/#2-ann-%E3%81%AE%E6%A0%B8%E5%BF%83%E3%82%A2%E3%82%A4%E3%83%87%E3%82%A2)
	- [2.1 ニューラルネットの再定義](https://zenn.dev/boku_yaji/articles/#21-%E3%83%8B%E3%83%A5%E3%83%BC%E3%83%A9%E3%83%AB%E3%83%8D%E3%83%83%E3%83%88%E3%81%AE%E5%86%8D%E5%AE%9A%E7%BE%A9)
	- [2.2 2 フェーズ構成](https://zenn.dev/boku_yaji/articles/#22-2-%E3%83%95%E3%82%A7%E3%83%BC%E3%82%BA%E6%A7%8B%E6%88%90)
- [3\. アーキテクチャ詳細（技術者向けに丁寧解説）](https://zenn.dev/boku_yaji/articles/#3-%E3%82%A2%E3%83%BC%E3%82%AD%E3%83%86%E3%82%AF%E3%83%81%E3%83%A3%E8%A9%B3%E7%B4%B0%E6%8A%80%E8%A1%93%E8%80%85%E5%90%91%E3%81%91%E3%81%AB%E4%B8%81%E5%AF%A7%E8%A7%A3%E8%AA%AC)
	- [3.1 Forward ― 動的チーム編成](https://zenn.dev/boku_yaji/articles/#31-forward-%E2%80%95-%E5%8B%95%E7%9A%84%E3%83%81%E3%83%BC%E3%83%A0%E7%B7%A8%E6%88%90)
	- [3.2 Backward ― 自然言語勾配](https://zenn.dev/boku_yaji/articles/#32-backward-%E2%80%95-%E8%87%AA%E7%84%B6%E8%A8%80%E8%AA%9E%E5%8B%BE%E9%85%8D)
	- [3.3 モーメンタムと安全機構](https://zenn.dev/boku_yaji/articles/#33-%E3%83%A2%E3%83%BC%E3%83%A1%E3%83%B3%E3%82%BF%E3%83%A0%E3%81%A8%E5%AE%89%E5%85%A8%E6%A9%9F%E6%A7%8B)
- [4\. 実験設定と結果](https://zenn.dev/boku_yaji/articles/#4-%E5%AE%9F%E9%A8%93%E8%A8%AD%E5%AE%9A%E3%81%A8%E7%B5%90%E6%9E%9C)
	- [4.1 データセット](https://zenn.dev/boku_yaji/articles/#41-%E3%83%87%E3%83%BC%E3%82%BF%E3%82%BB%E3%83%83%E3%83%88)
	- [4.2 学習コスト](https://zenn.dev/boku_yaji/articles/#42-%E5%AD%A6%E7%BF%92%E3%82%B3%E3%82%B9%E3%83%88)
	- [4.3 精度比較（抜粋）](https://zenn.dev/boku_yaji/articles/#43-%E7%B2%BE%E5%BA%A6%E6%AF%94%E8%BC%83%E6%8A%9C%E7%B2%8B)
- [5\. 既存手法との比較（要点だけ）](https://zenn.dev/boku_yaji/articles/#5-%E6%97%A2%E5%AD%98%E6%89%8B%E6%B3%95%E3%81%A8%E3%81%AE%E6%AF%94%E8%BC%83%E8%A6%81%E7%82%B9%E3%81%A0%E3%81%91)
- [6\. 限界と今後の課題](https://zenn.dev/boku_yaji/articles/#6-%E9%99%90%E7%95%8C%E3%81%A8%E4%BB%8A%E5%BE%8C%E3%81%AE%E8%AA%B2%E9%A1%8C)
- [7\. まとめ](https://zenn.dev/boku_yaji/articles/#7-%E3%81%BE%E3%81%A8%E3%82%81)
- [ぼくおも](https://zenn.dev/boku_yaji/articles/#%E3%81%BC%E3%81%8F%E3%81%8A%E3%82%82)

## 0\. TL;DR（まず 3 行で概要をつかむ）

- **Agentic Neural Network（ANN）** は、複数 LLM エージェントを「層」として束ね、 **Forward（構築）／Backward（自己改善）** の 2 段フェーズでワークフロー自体を学習・進化させる新フレームワーク。
- **学習で更新されるのは役割・接続・プロンプトのみ** 。LLM のパラメータは一切触らないため軽量。
- **コード生成・数学推論・データ分析・創作** の 4 ベンチマークすべてで、従来最強マルチエージェントを上回った。

---

## 1\. 背景と課題 ― 「強いけど組むのが面倒」問題

### 1.1 マルチエージェントは強い

単一 LLM に比べ、役割分担やツール連携のできる **Multi‑Agent System（MAS）** は精度も柔軟性も高い。

### 1.2 しかし設計は人力

- **役割** ：誰を呼ぶか
- **トポロジ** ：どう繋ぐか
- **プロンプト** ：どう指示するか

これらをタスクごとに手で試行錯誤するのは重い。

### 1.3 ANN の狙い

「ニューラルネットの **層 & 勾配** をそのまま MAS に移植し、設計と改善を自動化しよう」というのが ANN。

---

## 2\. ANN の核心アイデア

![image.png](https://res.cloudinary.com/zenn/image/fetch/s--gnVQSGV_--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/4115757/a6197c24-25c8-43f9-9546-450d58a96768.png)

### 2.1 ニューラルネットの再定義

| 従来の NN | ANN |
| --- | --- |
| 層 (Layer) | 同じサブタスクを受け持つ **エージェントチーム** |
| 重み θ | 役割・接続・プロンプトの集合 **θ** |
| 勾配 ∇θ | Critic/Repair エージェントが生成する **自然言語パッチ** |
| 順伝播 | チームを動かしてタスクを実行（結果・ログを得る） |
| 逆伝播 | テキストパッチを適用し、検証スコアが上がれば採用 |

### 2.2 2 フェーズ構成

- **Forward**
	1. タスクを自動でサブタスク分解
	2. 各サブタスクごとにチーム（層）を動的編成
	3. 出力と実行ログを保存
- **Backward**
	1. Global Critic が「どの層が失敗要因か」を文章で特定
	2. Local Repair が JSON 形式の “差分パッチ” を生成
	3. パッチ適用 → 検証指標が改善すれば **commit** 、悪化なら **rollback**
	4. “履歴” をモーメンタムに見立てて振動を抑制

---

## 3\. アーキテクチャ詳細

![image.png](https://res.cloudinary.com/zenn/image/fetch/s--WFZUr2uP--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_1200/https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/4115757/eebd88b4-96fb-4e01-b3f0-e95cf305f3a1.png)

### 3.1 Forward ― 動的チーム編成

`DynamicRoutingSelect` が「並列多数決」「逐次 Chain‑of‑Thought」「ツール呼び出しパイプライン」などから最適な集約関数を選択。実行ログ `(layer, agent_id, input, output)` は後段解析の鍵。

### 3.2 Backward ― 自然言語勾配

- **Critic** ：ボトルネック層を文章で指摘。
- **Repair** ：具体的に
	- 集約関数の置換
	- ノード追加／削除
	- プロンプトの句読点まで微修正  
		を JSON で提案。

学習率 **η** は「採用／棄却」そのもの（採用＝η=1、棄却＝η=0）。

### 3.3 モーメンタムと安全機構

| 機構 | 目的 |
| --- | --- |
| 履歴モーメンタム | 似た改善案をブーストし、行き過ぎを抑える |
| フォーマット検証 | JSON 破損・I/O ずれを自動拒否 |
| 性能検証 | val スコアが上がらなければ revert |

---

## 4\. 実験設定と結果

### 4.1 データセット

| タスク | 自動採点 | 用途 |
| --- | --- | --- |
| **HumanEval** (164 問) | ユニットテスト | コード生成 |
| **MATH** (7,500 問) | 文字列一致 | 数学推論 |
| **DABench** (CSV 700 問) | 生成数値一致 | データ分析 |
| **Creative Writing** (24 お題) | LLM 採点 | 物語生成 |
| **MMLU‑ML** (194 問) | 4 択一致 | 専門知識 |

### 4.2 学習コスト

- 各ベンチ **20 epoch** 、総入力 ~2.4 億 token

### 4.3 精度比較（抜粋）

| ベンチ | 既存最強 (%/点) | ANN (GPT‑4) | ANN (4o‑mini) |
| --- | --- | --- | --- |
| HumanEval (Pass@1) | 85.8 | **87.8** | **93.9** |
| MATH (Acc) | 77.6 | **80.0** | **82.5** |
| DABench (Acc) | 88.3 | **92.0** | **95.0** |

> 小型モデルでも従来大型モデル＋手動設計を上回る → **構成学習の効果が大** 。

---

## 5\. 既存手法との比較（要点だけ）

| 系統 | 設計 | 改善 | 汎用性 |
| --- | --- | --- | --- |
| Captain Agent | 動的チーム (会話) | リフレクション | タスク依存 |
| Symbolic | 固定構造 | プロンプト修正 | ローカル最適 |
| GPTSwarm | GA/MCTS 探索 | 離散置換 | 高コスト |
| **ANN** | Forward で自動設計 | テキスト勾配で連続最適化 | **タスク非依存** |

---

## 6\. 限界と今後の課題

- **Critic/Repair の LLM 依存**  
	小型 LLM だけだと勾配がノイズ化しやすい。
- **構造探索コスト**  
	1 ベンチ数億 token。頻繁に回すと課金が重い。
- **初期テンプレートは手動**  
	Meta‑Prompt Learning で自動生成を研究中。
- **マルチモーダル未対応**  
	画像・音声エージェントは今後の拡張。

---

## 7\. まとめ

- **ANN = “エージェント設計そのもの” を学習できる初の汎用フレームワーク** 。
- **Forward** ：タスクに合わせてチームを自動編成。
- **Backward** ：自然言語パッチで構造とプロンプトを少しずつ改善。
- 生成されたワークフローは可読 → **自動化＋人の最終チェック** のハイブリッドが簡単。
- 今後は **Meta‑Prompt 学習・動的ロール再割当・マルチモーダル対応** でさらに拡張予定。

## ぼくおも

(bokuが思ったこと)

ANNといっているが、Agentを層ごとにまとめて、どの層が悪いのかをまず見極め、そこから細かな修正していくというだけ。  
ただ、今までこういうちゃんとした改善サイクルを定義せずに一遍に改善を回す手法ばかりだったので、かなりいい線な気がするし、近い将来、業務でも使われる気がする。（コスト・スピード踏まえた改善サイクルが回るようになる必要はあるだろう）  
ちゃんとjson/yaml形式でワークフロー記述と全エージェントのプロンプトが書き出されて、人手でも修正できるのも良さそう。  
今後、Azureなどでのプラットフォームでも簡単にMulti Agentの構築ができるような対応をしてくるだろう。

こうなってくると、企業のDXをする上で大事になってくるのは下記３つくらいか

1. 正解データセットを定義できるレベルまで業務をタスクに落とし込めること
- 業務の範囲をザクっとしすぎると、正解データが定義できない。
1. 人は長年かけて、ある程度最適な業務の暗黙知をもっているので、それをAgentに落とし込むこと
- データセットを作るところにプロフェッショナルな知見を盛り込むことが大事。（画像処理と一緒な気がする。プロがラベル付して、あとはDeep Learningにぶちこむ）
- なるべく、アプリケーションを使いながらデータセットが収集する仕組み。これができれば、継続的に改善できる仕組みができる
1. Agentに利用可能なツール群を育てること
- データの整備などがメインになると思うが、人が業務を実行するときにアクセスできるデータにAgentがたどり着けないと同じ質のoutputは難しい。ここらへんはセキュリティ・権限管理などで結構難しいが、地道にやらないといけない。