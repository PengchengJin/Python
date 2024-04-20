from pyecharts.charts import Bar,Timeline
from pyecharts.options import *


#打开文件
f = open("分省年度数据.csv", "r", encoding="GB2312")
#读取数据，字符串列表
date_lines = f.readlines()
#关闭文件
f.close()

#date_lines_1 = date_lines.split(',')


date_line_year = date_lines[0].replace("年", "").split(',')
i = 1
j = 1
date_dict = {}
num = len(date_line_year)
while i < num:
    year = int(date_line_year[i])
    j = 1
    while j < len(date_lines):
        province = date_lines[j].split(',')[0]
        gdp = float(date_lines[j].split(',')[i])
        try:
            date_dict[year].append([province, gdp])
        except KeyError:
            date_dict[year] = []
            date_dict[year].append([province, gdp])
        j += 1
    i += 1

sorted_year_list = sorted(date_dict.keys())


timeline = Timeline()
for year in sorted_year_list:
    date_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_date=date_dict[year][:20]
    x_date = []
    y_date = []
    for province_gdp in year_date:
        x_date.append(province_gdp[0])
        y_date.append(province_gdp[1])
    x_date.reverse()
    y_date.reverse()
    bar = Bar()
    bar.add_xaxis(x_date)
    bar.add_yaxis("GDP", y_date, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    timeline.add(bar, str(year))
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render()

