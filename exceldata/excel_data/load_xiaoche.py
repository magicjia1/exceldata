from datetime import datetime

import pandas as pd
import recard

# 读取包含表头的Excel文件
file_path = "../description\西安校车导出考勤明细-10月.xlsx"
year = 2023  # 年份
month = 10  # 月份

def loadxiaoche(file_path,year,month):
    # 自动推断表头并读取数据
    df = pd.read_excel(file_path)  # 如果不想使用第一行作为表头


    # 将数据按照人员分组
    grouped = df.groupby("姓名")
    res = []
    # 构建字典
    result_dict = {}
    for name, group in grouped:
        calendar = recard.generate_calendar(name, year, month)
        # print(calendar)
        # print(name, group)
        for index, row in group.iterrows():

            date = row['考勤日期']
            for key, value in calendar[str(name)].items():

                if datetime.strptime(key, '%Y-%m-%d').date() == datetime.strptime(date, '%Y-%m-%d').date():
                    calendar[str(name)][key] = 1

        res.append(calendar)


    # 打印前几行数据查看
    # 遍历并按行打印
    for i in res:
        print(i)
    return res

if __name__ == '__main__':
    load_xiaoche(file_path, year, month)
