from pyecharts.charts import *
from pyecharts.options import*
from pyecharts.globals import*
f = open("D:/BaiduNetdiskDownload/资料/资料/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
f.close()
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])  # 年份
    country = line.split(",")[1]  # 国家
    gdp = float(line.split(",")[2])  # gdp数据
    try:
        data_dict[year].append([country,gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country,gdp])

print(data_dict)


# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# # 排序年份
#
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key = lambda element:element[1], reverse=True)
    # 去除本年份排名前八
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0]) # x轴添加
        y_data.append(country_gdp[1]/100000000)  # y轴添加

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球前八GDP数据"))
    timeline.add(bar,str(year))

# 设置自动播放
timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)

timeline.render("1960~2019全球前八GDP动态柱状图.html")



