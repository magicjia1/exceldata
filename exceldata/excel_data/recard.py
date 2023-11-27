from datetime import datetime, timedelta


def generate_calendar(name, year, month):
    result_dict = {name: {}}

    # 获取指定年月的第一天
    date = datetime(year, month, 1)

    # 获取下个月的第一天
    next_month = date.replace(day=28) + timedelta(days=4)  # 转到下个月的第一天
    last_day_of_month = next_month - timedelta(days=next_month.day)

    # 生成该月的所有日期
    while date <= last_day_of_month:
        date_str = date.strftime('%Y-%m-%d')
        result_dict[name][date_str] = 0
        date += timedelta(days=1)

    return result_dict
# 调用函数并获取特定人员特定年月的日期字典
name = "John Doe"  # 人员名字
year = 2023  # 年份
month = 10  # 月份

# calendar = generate_calendar(name, year, month)
# print(calendar)
