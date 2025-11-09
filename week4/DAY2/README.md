### Week4

# プロジェクト名

FastAPIとSQLiteを使ったDB連携タスク管理API

# 概要

このプロジェクトでは、FastAPIとSQLAlchemyを用いて、SQLiteデータベースと連携するタスク管理APIを作成しました。
タスク（Task）には「名前（name）」「期限（deadline）」「説明（description）」を設定でき、API経由で作成・取得・更新・削除（CRUD）を行えます。
データベース操作はSQLAlchemy ORMで行い、直接SQLを書くことなくPythonコード上でテーブルやデータを扱えるようにしています。

# 学習の目的

データベース連携の基本構造を理解し、FastAPIアプリとDBのやり取り（CRUD処理）を一通り実装できるようにすることを目的としました。
外部APIの利用に続き、今度はアプリ内部でデータを永続化する仕組み（DB連携）を学び、Webアプリケーションの裏側でどのようにデータが保存・更新されるのかを理解しました。

# 使用技術

・FastAPI
・SQLAlchemy
・SQLite

# 主な実装内容

1. **データベース設定（database.py）**

   * `create_engine`でSQLiteに接続し、`SessionLocal`でDB操作用のセッションを作成。
   * `Base = declarative_base()`で全モデルの基底クラスを定義しました。

2. **モデル定義（models.py）**

   * `Task`クラスを作成し、テーブル名`tasks`と各カラム（`id`, `name`, `deadline`, `description`）を定義。
   * SQLAlchemyの`Column`を使用してテーブル構造をPythonで表現。

3. **CRUD処理（crud.py）**

   * データの作成・取得・更新・削除をそれぞれ関数で実装。
   * `db.query(models.Task).all()`や`db.add()`などを用いてORM的に操作。

4. **FastAPI連携（main.py）**

   * `Depends(get_db)`でDBセッションを自動生成し、エンドポイント関数内で使用可能に。
   * `/tasks/`エンドポイントを通して、タスクのCRUDを実行可能。
   * `HTTPException`で例外処理を行い、存在しないタスク操作時には404エラーを返すように実装。

# 学んだこと

* **ORMの仕組み**：SQLを書かずにPythonコードでDB操作ができることを体験。
* **依存関係注入（Dependency Injection）**：`Depends(get_db)`により、エンドポイントごとにDBセッションを安全に使い回す仕組みを理解。
* **アプリ構成の分離**：`database.py`, `models.py`, `crud.py`, `main.py`を役割ごとに分けることで、コードの保守性が高まる構成を学びました。

# 今後の課題

* タスクに「完了フラグ」や「優先度」を追加し、より実用的な管理機能に拡張する。
* Pydanticモデルを使って、リクエスト・レスポンスのバリデーションを実装する。
* テストコード（pytest）を導入し、API動作の自動検証を行う。

# 学習記録

本プロジェクトは、FastAPI学習の**Week4**として作成しました。
外部API利用から一歩進み、データをアプリ内部に保存・編集できる**バックエンドAPIの基礎構造**を理解しました。
これにより、データ永続化を伴うWebアプリケーション開発の流れを一通り体験しました。

学習経過はQiitaで記録しています。
- DB接続方法の基礎理解

https://qiita.com/nanakato/items/7bbf97a811e9feb4232e


- SQLAlchemyとSQLiteでタスク管理アプリを構築

https://qiita.com/nanakato/items/9022283c3160288aca11