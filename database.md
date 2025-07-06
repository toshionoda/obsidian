## 🗓️ 第1ヶ月：基礎を固める（月1〜4週）

### Week 1：LLMの仕組みと文脈処理の理解

- Transformer（Attention）基礎理解
    
- GPT, BERTの違い
    
- Embeddingとは何か？（ベクトルの意味）
    

**教材**:

- 《動画》Attention is All You Need 解説
    
- Hugging Face のCourse
    
- OpenAI Embedding Playground（使ってみる）
    

---

### Week 2：SQL & データベース基礎

- テーブル設計、正規化、JOIN
    
- PostgreSQL or SQLiteで実践
    
- 実データをDBに格納してクエリを書く練習
    

**教材**:

- SQLBolt（実習型）
    
- PostgreSQL + pgAdminでハンズオン
    

---

### Week 3：ベクトルDBとチャンク処理

- FAISSで簡単なベクトルDB構築
    
- テキスト分割（チャンク化）とEmbedding保存
    
- k近傍検索（k-NN）の仕組み理解
    

**教材**:

- LangChainチュートリアル（RAG部分）
    
- FAISSの公式Notebook
    

---

### Week 4：土木設計情報をサンプルで構造化

- PDF, 仕様書などの設計情報をテーブル形式に
    
- SQLiteでデータベース化してクエリ作成
    

**教材**:

- PDFPlumber or PyMuPDF でPDF抽出
    
- Python + Pandasで表構造化
    

---

## 🗓️ 第2ヶ月：RAG構築とLLM連携（月5〜8週）

### Week 5：LangChainとRAGの基本理解

- Vector DB × LLMの構成理解
    
- チャットボットとしてRAG構築
    
- ChatGPT API or Hugging Face Modelsを使う
    

---

### Week 6：ドキュメント → ベクトルDB → 応答

- IFC、PDF、CSV などを前処理
    
- Embeddingを生成し、質問応答を構築
    

---

### Week 7：LLMに設計条件を問い合わせるプロトタイプ

- 「設計条件に基づく設計方針提示」などのユースケース実装
    
- 日本語LLMも試す（ELYZA, LLama3-JP）
    

---

### Week 8：社内/建設業データベースとの接続実験

- SQLとの統合（LangChain + SQL）
    
- BIM属性データとのクロス参照設計
    

---

## 🗓️ 第3ヶ月：BIM・土木設計の融合と実装（月9〜12週）

### Week 9：BIMデータ（IFC等）の構造理解と抽出

- ifcopenshellでIFCを読み取り
    
- 属性データをDataFrameへ変換
    
- IFC属性からナレッジ構築へ
    

---

### Week 10：AutoCAD, Civil 3D API理解

- Python + AutoCAD連携（pyautocadなど）
    
- Civil 3D の構造物データの抽出（形状・属性）
    

---

### Week 11：全データをRAGベースに統合

- IFC + 仕様書 + 社内DB の3種統合
    
- データ型ごとのチャンク戦略と前処理ルール設計
    

---

### Week 12：成果物プロトタイプ発表

- 社内向けチャットシステムのプロトタイプ完成
    
- PDF図面 + BIMモデルから「図面チェックアシスタント」を構築
    

---

## 📦 補足：習得に役立つライブラリ・サービスまとめ

|分野|ライブラリ / ツール|
|---|---|
|LLM API|OpenAI, HuggingFace Transformers|
|Embedding|OpenAI Embedding, Sentence-BERT|
|Vector DB|FAISS, Qdrant, Weaviate|
|PDF処理|PyMuPDF, PDFPlumber|
|BIM連携|ifcopenshell, xBIM, speckle|
|土木API連携|pyautocad, AutoLISP, Forge|
|RAGフレーム|LangChain, LlamaIndex|