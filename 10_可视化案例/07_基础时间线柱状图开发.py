from pyecharts.charts import *
from pyecharts.options import *
from pyecharts.globals import *
bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"),color="red" )
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 40, 30], label_opts=LabelOpts(position="right"),color="red" )
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [90, 80, 60], label_opts=LabelOpts(position="right"),color="red" )
bar3.reversal_axis()

timeline = Timeline({"theme": ThemeType.LIGHT})
timeline.add(bar1, "点1")
timeline.add(bar2, "点2")
timeline.add(bar3, "点3")


# 自动播放设置
timeline.add_schema(play_interval=1000,
                    is_timeline_show=True,
                    is_auto_play=True,
                    is_loop_play=True)

timeline.render("基础时间线图.html")
