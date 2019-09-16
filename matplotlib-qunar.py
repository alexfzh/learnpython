# -*- coding: utf-8 -*-
# @Time    : 2019/9/15/0015 22:22
# @Author  : Alex_fei
# @File    : matplotlib-qunar.py

import pymysql
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，不然无法显示中文

conn = pymysql.connect('localhost', 'root', 'a123456a', 'doubanbook')
cursor = conn.cursor()
sql = """select * from qunar order by salespermonth desc limit 0,15 """
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    conn.commit()
except:
    # 如果发生错误则回滚
    conn.rollback()
results = cursor.fetchall()
# for result in results:
#     print(result)

# x,y轴数据
x_arr = []  # 景区名称
y_arr = []  # 销量
for i in results:
    x_arr.append(i[1])
    y_arr.append(i[3])

"""
去哪儿月销量排行榜
"""
plt.bar(x_arr, y_arr, color='rgb')  # 指定color，不然所有的柱体都会是一个颜色
plt.gcf().autofmt_xdate()  # 旋转x轴，避免重叠
plt.xlabel(u'景点名称')  # x轴描述信息
plt.ylabel(u'月销量')  # y轴描述信息
plt.title(u'景点月销量统计表')  # 指定图表描述信息
plt.ylim(0, 50000)  # 指定Y轴的高度
plt.savefig('去哪儿月销售量排行榜')  # 保存为图片
plt.show()
