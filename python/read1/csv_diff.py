import csv

def subtract_csv_files(file_a, file_b, output_file):
    data_a = []
    data_b = []
    
    # ファイルAを読み込む
    with open(file_a, 'r',encoding="utf-8-sig", ) as file:
        reader = csv.reader(file)
        data_a = list(reader)
    
    # ファイルBを読み込む
    with open(file_b, 'r' ,encoding="utf-8-sig",) as file:
        reader = csv.reader(file)
        data_b = list(reader)
    
    # 引き算を行い、結果を格納する
    result = []
    for row_a, row_b in zip(data_a, data_b):
        result_row = []
        for cell_a, cell_b in zip(row_a, row_b):
            try:
                cell_a = float(cell_a)
                cell_b = float(cell_b)
                result_row.append(str(cell_b - cell_a))  # 引き算を行い、結果を文字列として格納
            except ValueError:
                result_row.append('')  # 数値でないセルは空文字として格納
        result.append(result_row)
    
    # 結果をcsvファイルCに書き込む
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(result)

# 使用例
subtract_csv_files('C:\\Users\\t36co\\Documents\\b.csv', 'C:\\Users\\t36co\\Documents\\a.csv', 'file_c.csv')