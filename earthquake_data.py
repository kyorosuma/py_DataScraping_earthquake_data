from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriverのセットアップ
options = webdriver.ChromeOptions()
options.headless = True  # ヘッドレスモードでブラウザを表示せず実行

# ChromeDriverの設定
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 指定されたURLを開く
url = "https://www.data.jma.go.jp/multi/quake/index.html?lang=jp"
driver.get(url)

# ページが完全にロードされるのを待つ
time.sleep(5)  # 必要に応じて調整

# 地震情報のテーブルを取得
earthquake_table = driver.find_element(By.ID, 'quakeindex_table')

# テーブル内のすべての行を取得
rows = earthquake_table.find_elements(By.TAG_NAME, 'tr')

# ファイルにデータを書き込む
with open('earthquake_data.txt', 'w', encoding='utf-8') as file:
    # ヘッダー行を除外してテーブルデータをファイルに書き込む
    for row in rows[1:]:  # 最初の行はヘッダーなのでスキップ
        columns = row.find_elements(By.TAG_NAME, 'td')
        if columns:  # もし列が存在すれば、テーブルデータを取得
            row_data = [column.text.strip() for column in columns]  # 各列のテキストを取得し、余分なスペースを削除
            file.write("\t".join(row_data) + "\n")  # タブ区切りでファイルに書き込む

# ブラウザを閉じる
driver.quit()
