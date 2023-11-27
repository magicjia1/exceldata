import os
from datetime import datetime, timedelta


import pandas as pd

from exceldata.excel_data import load_qixiang, load_taichang, load_xiaoche

conunt = 0
def gen_day_excel(file_path1,file_path2,file_path3,year,month):
    # 指定要创建的文件夹路径
    folder_name = "./out"

    # 如果文件夹不存在，则创建
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
    else:
        print(f"Folder '{folder_name}' already exists.")

    a = load_qixiang.loadqixiang(file_path1, year, month)
    print(1)
    b = load_taichang.loadtaichang(file_path2, year, month)
    print(2)
    c = load_xiaoche.loadxiaoche(file_path3, year, month)
    result = {}



    def merge(a):
        global conunt

        # global result
        for i in a:
            # 获取第一个键值对
            first_key, first_value = next(iter(i.items()))
            # print(first_key)
            if first_key in result:
                # print("to merged",first_value)
                # print("to merge",result[first_key])
                # 合并两个字典
                # for key in first_value:
                #     if key in result[first_key] and first_value[key] == 1:
                #         result[first_key][key] = 1

                conunt += 1
                # print('值在字典的键中')
            else:
                result[first_key] = first_value


    merge(a)

    merge(b)

    merge(c)
    # 验证数目是否正确
    #
    print(len(a)+len(b)+len(c)-conunt)
    print(len(result))

    print(result)

    df = pd.DataFrame(result).transpose()
    df.index.name = 'Name'
    df.columns.name = 'Date'
    print(df)

    final_week = []

    # 导出为 Excel 文件
    df.to_excel(f'{folder_name}/output_day_{year}_{month}.xlsx')


    #todo

    rs=[]
    date0 = df.columns[0]
    start_date = datetime.strptime(date0, '%Y-%m-%d')

    rs = []

    for index, row in df.iterrows():
        per_week = []
        count_sign = 0
        start_date = datetime(year, month, 1)  # 假设这是你的起始日期

        for i in range(0, len(row)):
            if start_date.weekday() != 6:  # 如果不是周日
                count_sign += row.iloc[i]
            else:  # 如果是周日
                count_sign += row.iloc[i]
                per_week.append(count_sign)
                count_sign = 0

            start_date += timedelta(days=1)

        rs.append({index: per_week})

    print(rs)

    new_dict = {}

    for item in rs:
        for name, weeks in item.items():
            week_dict = {}
            for i, count in enumerate(weeks):
                week_dict[f'第{i+1}周'] = count
            new_dict[name] = week_dict

    print(new_dict)

    df2 = pd.DataFrame(new_dict).transpose()
    df2.index.name = 'Name'
    df2.columns.name = 'Week'
    print(df2)


    # 将 DataFrame 保存为 Excel 文件
    df2.to_excel(f'{folder_name}/output_week_{year}_{month}.xlsx')

if __name__ == '__main__':

    file_path1 = '../description/启翔楼.xlsx'
    file_path2 = '../description/10月太仓.xlsx'
    file_path3 = "../description/西安校车导出考勤明细-10月.xlsx"
    year = 2023
    month = 10

    gen_day_excel(file_path1,file_path2,file_path3,year,month)