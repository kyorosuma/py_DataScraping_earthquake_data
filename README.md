# DataScraping_earthquake_data
 
# 設計書

## 基本設計

**概要:** このプログラムは、指定された Python コードファイルを解析し、関数・クラスの情報を抽出して設計書を自動生成するシステムです。解析結果をもとに、設計書を JSON 形式で出力します。

**入力:** 解析対象の Python ファイル (.py) のパスを入力

**出力:** 設計書ファイル（JSON 形式）

**使用技術:** Python 3.x, Selenium, WebDriverManager, JSON 処理

**主要ライブラリ:** selenium, webdriver_manager, time

## 詳細設計

### 関数一覧
- **setup_webdriver**: WebDriver をセットアップする関数。ChromeDriver を使用し、指定された URL を開いてページをロードする。
- **get_earthquake_data**: 地震情報のテーブルからデータを取得し、earthquake_data.txt ファイルに書き込む関数。
- **main**: プログラムのエントリーポイント。セットアップとデータ取得の流れを制御する。

### クラス一覧

### メモ
各関数は特定の役割を持ち、セットアップからデータ取得、ファイル書き込みまでの一連の処理を担当する。エラーハンドリングやログ出力などの補足機能が必要。
