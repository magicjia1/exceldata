
from datetime import datetime, timedelta
import pandas as pd
import recard

# 读取包含表头的Excel文件
file_path = '../description/启翔楼.xlsx'
year = 2023  # 年份
month = 10  # 月份

def loadqixiang(file_path,year,month):
    a=[]
    # 自动推断表头并读取数据
    df = pd.read_excel(file_path,sheet_name=0,header=None,skiprows=3)  # 如果不想使用第一行作为表头



    # 输出每一行数据
    for index, row in df.iterrows():
        # print(row.to_dict())
        res = row
        for i in range(2, len(row)):
            if str(row[i]) == "nan":

                res[i] = 0
            else:
                res[i] = 1

        # print(res.to_dict())
        res_dict = res.to_dict()
        # 分离第一个键值对和其余的键值对
        rest_of_dict = {key: value for key, value in res_dict.items() if key >= 4}
        name= row[1]
        # 构建新的字典，以日期作为键
        # 获取指定年月的第一天
        start_date = datetime(year, month, 1)
        new_dict = {
            str((start_date + timedelta(days=key - 4)).date()): value for key, value in rest_of_dict.items()
        }
        final_dict = {name: new_dict}

        a.append(final_dict)
        print(final_dict)
    return a

if __name__ == '__main__':
    loadqixiang(file_path,year,month)