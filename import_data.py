import pandas as pd

# 讀取 Excel 文件
excel_file = 'test_case.xlsx'
sheet_name = '帳戶資料'
df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

# 將 DataFrame 轉換為 JSON
json_data = df.to_json(orient='records', force_ascii=False, indent=4)

# 保存到 JSON 文件中
json_file = 'data.json'
with open(json_file, 'w', encoding='utf-8') as file:
    file.write(json_data)

print(f"Excel 文件已成功轉換為 JSON，保存為 {json_file}")
