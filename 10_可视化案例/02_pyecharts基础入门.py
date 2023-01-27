"""
pyecharts 官网 pyecharts.org 图表参照完整gallery.pyecharts.org
生成图
"""
# 导包
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,VisualMapOpts
# 构建Line对象创建折线图对象
line = Line()
# 给折线图对象添加x轴的数据
line.add_xaxis(["中国", "美国", "日本"])
# 给折线图对象添加y轴的对象
line.add_yaxis("GDP", [10, 20, 10])
# 设置全局配置
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True)
)
# 通过render方法，将代码生成为图像
line.render()
