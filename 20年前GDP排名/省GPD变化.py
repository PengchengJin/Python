from pyecharts.charts import Bar,Timeline
from pyecharts.options import *


#打开文件
f = open("分省年度数据.csv", "r", encoding="GB2312")
#读取数据，字符串列表
date_lines = f.readlines()
#关闭文件
f.close()

#date_lines_1 = date_lines.split(',')

#文件首行去除“年”字符，并以“，”分列
date_line_year = date_lines[0].replace("年", "").split(',')
i = 1
j = 1
#创建数据字典
date_dict = {}
num = len(date_line_year)
#遍历数据，按年份将各省数据放入字典，key为年份，数据为各省数据
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
#将字典内以key为关键子排序
sorted_year_list = sorted(date_dict.keys())

#创建时间线
timeline = Timeline()
#数据处理，分别获取X轴和Y轴数据
for year in sorted_year_list:
    date_dict[year].sort(key=lambda element: element[1], reverse=True)
    #获取排名前20名省份
    year_date = date_dict[year][:20]
    x_date = []
    y_date = []
    for province_gdp in year_date:
        x_date.append(province_gdp[0])
        y_date.append(province_gdp[1])
    #X轴和Y轴数据逆序
    x_date.reverse()
    y_date.reverse()
    #创建柱状图对象，并将对象赋值
    bar = Bar()
    bar.add_xaxis(x_date)
    bar.add_yaxis("GDP", y_date, label_opts=LabelOpts(position="right"))
    #柱状图X轴、Y轴翻转
    bar.reversal_axis()
    #柱状图添加到时间线
    timeline.add(bar, str(year))
#时间轴配置
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)
#以时间线生成图表
timeline.render()

