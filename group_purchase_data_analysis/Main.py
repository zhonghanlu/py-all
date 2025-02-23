from collections import defaultdict
from decimal import Decimal

from group_purchase_data_analysis.data_connect import get_mysql_connection
from group_purchase_data_analysis.data_render import zs,zz

# 获取分类数据信息
def get_category_data():
    # 获取数据库连接
    connection = get_mysql_connection()
    # 创建游标对象
    cursor = connection.cursor()

    cursor.execute("SELECT sc.category_name,SUM(sop.quantity) "
                   "FROM shop_category sc "
                   "LEFT JOIN shop_sku_spu_product sssp ON sssp.category_id = sc.id "
                   "LEFT JOIN shop_order_product sop ON sssp.id = sop.product_id "
                   "GROUP BY sc.category_name,sop.quantity")

    return cursor.fetchall()

# 初始化 xy  基础数据
categoryQuantity = defaultdict(Decimal)
# 处理分类的 xy 轴数据
def handler_category_x_y_data(data):
    for category,quantity in data:
        if quantity is None:
            categoryQuantity[category] += 0
        else:
            categoryQuantity[category] += quantity
    return categoryQuantity

if __name__ == '__main__':
    # 分类商品销售数量数据获取
    categoryData = get_category_data()
    # 数据展示
    # 清洗数据、获取x，y轴数据
    xyDataDict = handler_category_x_y_data(categoryData)
    # 柱装
    zz(xyDataDict.keys(),xyDataDict.values(),"分类销售量","个")

    # 折线
    # zs(xyDataDict.keys(),xyDataDict.values(),"月份销售折线","元")
