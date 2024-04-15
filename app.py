import pandas as pd
import streamlit as st

def check_excel_format(file_path):
    try:
        df = pd.read_excel(file_path)
        # 在這裡加入你的格式驗證邏輯，這只是一個示例
        # 例如，檢查特定欄位是否符合特定的格式
        # 如果檢查通過，返回 True，否則返回 False
        # 這邊只是示例，你需要根據你的需求定義檢查邏輯
        # 以下示例檢查是否有空值
        if df.isnull().values.any():
            return False, "Excel 中包含空值"
        else:
            return True, "Excel 格式正確"
    except Exception as e:
        return False, f"發生錯誤: {str(e)}"

def main():
    st.title("Excel 格式驗證程式")

    # 讓用戶上傳 Excel 檔案
    uploaded_file = st.file_uploader("請上傳 Excel 檔案", type=["xls", "xlsx"])

    if uploaded_file is not None:
        # 顯示上傳的檔案資訊
        st.write("已上傳檔案:", uploaded_file.name)

        # 執行格式驗證
        is_valid, message = check_excel_format(uploaded_file)
        if is_valid:
            st.success(message)
        else:
            st.error(message)

if __name__ == "__main__":
    main()
