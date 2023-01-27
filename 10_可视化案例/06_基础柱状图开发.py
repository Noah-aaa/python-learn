from pyecharts.charts import *
from pyecharts.options import *
bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"),color="red" )
bar.reversal_axis()
bar.render("中英美三国GDP柱状图.html")