# Excel文件导入mysql数据库
# 1.构建UI界面
# 2.进行excel数据获取
# 3.进行数据导入
# 第一版完成功能  version 0.0.1
import base64
# -*- coding: UTF-8 -*-
import demjson as json
import numpy as np
import pandas as pd
import pymysql as pm
import tkinter as tkk
import tkinter.messagebox as mb
from threading import Thread
from tkinter import filedialog, END

# 创建主窗口
tk = tkk.Tk()
tk.title("ExcelImportForMysqlDB")  # 标题设置
tk.geometry('950x370')  # 设置窗口大小为900x600 横纵尺寸

var = tkk.StringVar()

var.set(
    {"url": "192.168.10.241", "username": "root", "password": "yegoo@123",
     "database": "zhuanke2.0", "tablename": "psi_sale"})

sourceData = ""
sourceDbData = ""
execCount = 0
dataArray = []


def open_msg_box():
    mb.showinfo("this exe info", "===启动成功===")


def open_err_box():
    mb.showinfo("this exe info", "===启动失败===")


def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    global sourceData
    sourceData = filename
    filepath.insert('insert', filename)


def insert_text():
    var = e.get()
    global sourceDbData
    global sourceData
    t.delete(0.0, END)
    t.insert('insert', sourceData + '\n')
    t.insert('insert', var + '\n')
    sourceDbData = var
    execThisExe()


# 业务处理
def execThisExe():
    if (sourceData == '') or (sourceDbData == ''):
        error = '源文件信息与数据源信息不可为空'
        t.insert('insert', error, 'warning')
    if (sourceData != '') and (sourceDbData != ''):
        error = '信息获取成功,开始读取Excel\n'
        t.insert('insert', error, 'info')
        try:
            # 处理excel
            global dataArray
            sheet = pd.read_excel(sourceData, keep_default_na=False)
            dataArray = np.array(sheet)
            dataArray = dataArray.tolist()
            info = "共获取" + str(len(dataArray)) + "条数据\n"
            t.insert("insert", info, "info")
            info = "开始进行插入数据,请稍等.......\n"
            t.insert("insert", info, "info")
            t1 = Thread(target=importForDb)
            t1.start()
        except Exception as error:
            t.insert('insert', "error：" + str(error), 'error')


def importForDb():
    dbinfo = json.decode(sourceDbData)
    db_saas = {
        "host": dbinfo["url"],
        "user": dbinfo["username"],
        "password": dbinfo["password"],
        "db": dbinfo["database"],
        "charset": "utf8",
        "ssl": {'ssl': {}}  # 很屎虽然什么都没填但是必须有这项配置
    }
    mysqlDb = pm.connect(**db_saas)
    # mysqlDb = pm.connect(host=dbinfo["url"], user=dbinfo["username"], password=dbinfo["password"],
    #                      db=dbinfo["database"], ssl={'ssl': {}})
    cursor = mysqlDb.cursor()
    try:
        for data in dataArray:
            value = ''
            for val in data:
                if val == '':
                    value += 'NULL' + ','
                elif str(val) == 'NaT':
                    value += 'NULL' + ','
                else:
                    value += "'" + str(val) + "'" + ","
            value = value[0: len(value) - 1]
            sql = "insert into " + dbinfo["tablename"] + " values(" + value + ")"
            print(sql)
            count = cursor.execute(sql)
            global execCount
            execCount += count
            mysqlDb.commit()
        info = "执行成功，共计执行" + str(execCount) + "条记录"
        t.insert('insert', info, 'success')
    except Exception as error:
        mysqlDb.rollback()
        t.insert('insert', "error：" + str(error), 'error')
    finally:
        cursor.close()
        mysqlDb.close()


# 数据库连接信息
tkk.Label(tk, text="数据库连接信息：").grid(row=0, column=0)
e = tkk.Entry(tk, textvariable=var, width=90)
e.grid(row=0, column=1)
# 选择文件
tkk.Label(tk, text="请选择Excel：").grid(row=5, column=0)
file = tkk.Button(tk, text='选择文件', command=UploadAction)
file.grid(row=5, column=1, padx=10, pady=5)
filepath = tkk.Text(tk, height=1, width=40)
filepath.grid(row=6, column=1)
# 选择数据库
tkk.Label(tk, text="请确认请求：").grid(row=7, column=0)
db = tkk.Button(tk, text="确认数据库连接信息，only for mysql", width=35, height=1, command=insert_text)
db.grid(row=7, column=1, padx=10, pady=5)
# 日志信息
tkk.Label(tk, text="日志信息").grid(row=8, column=0)
t = tkk.Text(tk, height=10, width=70)
t.grid(row=8, column=1)
t.tag_config('error', background="red", foreground="black")
t.tag_config('warning', background="yellow", foreground="red")
t.tag_config('info', background="green", foreground="black")
t.tag_config('success', background="blue", foreground="black")
# 宣传图片
gzh = tkk.StringVar()
gzh.set("https://www.helloimg.com/image/Z80K5Y")
tkk.Entry(tk, textvariable=gzh, width=20).grid(row=10, column=0)
tkk.Label(tk, text="左边是我的公众号，新创建，复制到浏览器，动动小手点个关注\n 欢迎访问我的博客 zhonghanlu.club",
          font=('Arial', 20),
          fg='red').grid(row=10, column=1)
# 调用主事件循环，让窗口程序保持运行。
tk.mainloop()
