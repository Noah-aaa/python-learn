import json
from pyecharts.charts import *
from pyecharts.options import *
f_us = open("D:\BaiduNetdiskDownload\资料\资料\资料\可视化案例数据\折线图数据\美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
f_jp = open("D:\BaiduNetdiskDownload\资料\资料\资料\可视化案例数据\折线图数据\日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("D:\BaiduNetdiskDownload\资料\资料\资料\可视化案例数据\折线图数据\印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()

us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

us_data = us_data[:-2:1]
jp_data = jp_data[:-2:1]
in_data = in_data[:-2:1]
# print(us_data)
# print(in_data)
# print(jp_data)
# 将json数据转为python中的字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
# print(json.loads(us_data))

# 回去trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取x,y坐标
us_x_data = us_trend_data['updateDate'][:314]
us_y_data = us_trend_data['list'][0]['data'][:314]

jp_x_data = jp_trend_data['updateDate'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

in_x_data = in_trend_data['updateDate'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]
# 生成图标


line = Line()

# 设置全局变量
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)
# 添加x轴数据
line.add_xaxis(us_x_data)
line.add_xaxis(jp_x_data)
line.add_xaxis(in_x_data)
# 添加y轴数据
line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))

# 生成图表

line.render()
f_us.close()
f_in.close()
f_jp.close()



