import matplotlib.pyplot as plt
# windows
# plt.rcParams['font.family'] = 'SimHei'

# MacOs
plt.rcParams['font.family'] = 'Heiti TC'

# 折线图
def zs(x,y,title,label):
    # 数据
    # 创建图形
    plt.figure(figsize=(8, 4))
    # 绘制折线图
    plt.plot(x, y, marker='o', linestyle='-', color='b', label=label)
    # 添加标题和标签
    plt.title(title)
    plt.xlabel('X 轴')
    plt.ylabel('Y 轴')
    # 添加图例
    plt.legend()
    # 显示图形
    plt.show()

# 柱装图
def zz(x,y,title,label):
    # 创建图形
    plt.figure(figsize=(8, 4))
    # 绘制柱状图
    plt.bar(x, y, color='g', label=label)
    # 添加标题和标签
    plt.title(title)
    plt.xlabel('类别')
    plt.ylabel('值')
    # 添加图例
    plt.legend()
    # 显示图形
    plt.show()
