#!/usr/bin/env python3
#antuor:Alan


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lyerp.settings")


import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()


from productlist.models import Product
import xlrd

data= xlrd.open_workbook('testupload.xlsx') #打开文件
table = data.sheet_by_index(0) #获取工作表
WorkList = []
nrows = table.nrows #行数
ncols = table.ncols #列数
for i in range(1,nrows):
    row = table.row_values(i) #获取每行值
    WorkList.append(
        Product(
            category = row[0],
            image = row[1],
            sku = row[2],
            name = row[3],
            price = row[4],
            weight = row[5],
            volume = row[6],
            cn_us_cost = row[7],
            us_second_cost = row[8],
            cn_uk_cost = row[9],
            uk_second_cost = row[10],
            cn_de_cost = row[11],
            de_second_cost = row[12],
            cn_au_cost = row[13],
            au_second_cost = row[14],

        )
    )
Product.objects.bulk_create(WorkList)
print ('数据导入成功')