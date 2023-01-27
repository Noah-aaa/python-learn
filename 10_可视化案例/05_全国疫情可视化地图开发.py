import json
from pyecharts.charts import *
from pyecharts.options import*
# 打开文件
f = open("D:\BaiduNetdiskDownload\资料\资料\资料\可视化案例数据\地图数据\疫情.txt", "r", encoding="UTF-8")

# 获取数据
data = f.read()

# 文件关闭
f.close()

# 数据处理将json数据转换为python字典
data_dict = json.loads(data)

# 获取省份信息
data_list = []
data_dict_list = data_dict["areaTree"][0]["children"]
for province_data in data_dict_list:
    province_name = province_data['name'] # 省份名字
    province_confirm = province_data["total"]["confirm"]  # 确诊人数
    data_list.append((province_name,province_confirm))  # 元组地图省份信息，确诊人数。地图需要

print(data_list)
map = Map()  # 构建地图对象
map.add("各省份确诊人数", data_list, "china")

# 全局选项
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(is_show=True,
                                 is_piecewise=True,
                                 pieces=[
                                     {"min": 1, "max": 99,"label": "1~99人", "color": "blue"},
                                     {"min": 100, "max": 999,"label": "100~999人", "color": "yellow"},
                                     {"min": 1000, "max": 9999,"label": "10000~9999人", "color": "white"},
                                     {"min": 10000, "max": 99999,"label": "100000~99999人", "color": "black"},
                                     {"min": 100000, "max": 99999,"label": "1000000~999999人", "color": "pink"},
                                     {"min": 1000000, "max": 99999,"label": "10000000~9999999人", "color": "green"}
                                 ])
)
map.render("全国疫情地图.html")

