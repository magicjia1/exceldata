import math

import numpy
import pandas as pd
import calendar
from datetime import datetime, timedelta
import numpy as np
import re

# 读取包含表头的Excel文件
file_path = '../description\\10月太仓.xlsx'
year=2023
month=10

def loadtaichang(file_path,year,month):
    # 自动推断表头并读取数据
    df = pd.read_excel(file_path, header=None)  # 如果不想使用第一行作为表头

    res_taichang = []

    start_date_str, end_date_str = "", ""
    for index, row in df.iterrows():
        if index == 2:
            table_time = row[23]
            # print(table_time)
            match = re.search(r'\d{4}-\d{2}-\d{2}～\d{4}-\d{2}-\d{2}', table_time)

            if match:
                date_range = match.group()
                start_date_str, end_date_str = date_range.split('～')



        if isinstance(row[0], str):
            row_dict = row.to_dict()
            # print(row_dict)
            res = row
            for i in range(1, len(row)):
                if str(row[i]) == "nan":

                    res[i] = 0
                else:
                    res[i] = 1

            res_dict = res.to_dict()




            # print(res_dict)
            # 将起始日期字符串转换为日期对象

            start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

            # 给定的字典

            # 获取第一个键值对
            first_key, first_value = next(iter(res_dict.items()))

            # 分离第一个键值对和其余的键值对
            rest_of_dict = {key: value for key, value in res_dict.items() if key != 0}
            # 构建新的字典，以日期作为键
            new_dict = {
                str((start_date + timedelta(days=key - 1)).date()): value for key, value in rest_of_dict.items()
            }


            missing_end_date = ((start_date + timedelta(days=- 1)).date())
            missing_start_date = (datetime(year, month, 1).date())

            # 生成缺失日期的键
            missing_dates = [(missing_start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in
                             range((missing_end_date - missing_start_date).days + 1)]

            missing_dates_dict = {}

            for date in missing_dates:
                missing_dates_dict[date] = 1

            for name in new_dict:
                for key, value in new_dict.items():
                    missing_dates_dict[key] = value


            # print(first_value,new_dict)

            final_dict = {first_value: missing_dates_dict}
            res_taichang.append(final_dict)

            # # print(res_dict)

    for i in res_taichang:
        print(i)
    return res_taichang
