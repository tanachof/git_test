import csv
import time
from PIL import ImageGrab

def take_screenshot_from_csv(csv_file, cell_range, file_name):
    # CSVファイルを開く
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        
        # セル範囲の情報を解析
        start_row, start_col, end_row, end_col = cell_range
        
        # スクリーンショットを撮影する範囲を指定（左上の座標と右下の座標）
        (x1, y1, x2, y2) = (100, 100, 500, 500)
        screenshot_area = (x1, y1, x2, y2)
        
        # セル範囲のスクリーンショットを取得
        for row_index, row in enumerate(reader):
            if start_row <= row_index <= end_row:
                for col_index, cell in enumerate(row):
                    if start_col <= col_index <= end_col:
                        # スクリーンショットを撮影して保存
                        screenshot = ImageGrab.grab(bbox=screenshot_area)
                        screenshot.save(file_name)
                        print(f"スクリーンショットを保存しました: {file_name}")
                        return
    
    print(f"指定したセル範囲が見つかりませんでした")

# 複数のCSVファイルからセル範囲のスクリーンショットを取得する例
csv_files = ["file_c.csv"]
start_row = 1
start_col = 1
end_row = 3
end_col = 3
cell_range = (start_row, start_col, end_row, end_col)
file_name = "screenshot.png"

for csv_file in csv_files:
    take_screenshot_from_csv(csv_file, cell_range, file_name)
    time.sleep(1)  # 次の処理までの待機時間（秒）
