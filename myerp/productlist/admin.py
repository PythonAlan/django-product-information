from django.contrib import admin

# Register your models here.
from productlist.models import Product
import productlist.config as pd  #参数
from django.contrib.admin.models import LogEntry

LogEntry.objects.all().delete()

class ProductAdmin(admin.ModelAdmin):
    def us_sale_price_10(self, obj) :
        first_class_cost_us = obj.weight*pd.first_class_rate['first_class_rate_us']/pd.exchange_rate['us']
        second_class_cost_us = obj.us_second_cost
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_10 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.72
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_10,1)
    us_sale_price_10.short_description = u'US(空)10%$'
    us_sale_price_10.allow_tags = True

    def cn_us_sale_price_10(self, obj) :
        first_class_cost_us = 0
        second_class_cost_us = obj.cn_us_cost
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_10 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.72
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_10,1)
    cn_us_sale_price_10.short_description = u'US(本)10%$'
    cn_us_sale_price_10.allow_tags = True


    def us_sea_sale_price_10(self,obj):
        first_class_cost_us = obj.volume*pd.sea['us_fee']/pd.exchange_rate['us']
        second_class_cost_us = obj.us_second_cost
        purchase_price = obj.price/pd.exchange_rate['us']
        sale_price_10 = (first_class_cost_us+second_class_cost_us+purchase_price)/0.72
        return u'<span style="color:red;font-weight:bold">%s</span>' % round(sale_price_10,1)
    us_sea_sale_price_10.short_description = u'US(海)10%$'
    us_sea_sale_price_10.allow_tags = True


    def uk_sale_price_10(self, obj) :
        first_class_cost_uk = obj.weight*pd.first_class_rate['first_class_rate_uk']/pd.exchange_rate['uk']
        second_class_cost_uk = obj.uk_second_cost
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_10 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.70
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_10,1)
    uk_sale_price_10.short_description = u'UK(空)10%£'
    uk_sale_price_10.allow_tags = True

    def cn_uk_sale_price_10(self, obj) :
        first_class_cost_uk = 0
        second_class_cost_uk = obj.cn_uk_cost
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_10 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.70
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_10,1)
    cn_uk_sale_price_10.short_description = u'UK(本)10%£'
    cn_uk_sale_price_10.allow_tags = True

    def uk_sea_sale_price_10(self,obj):
        first_class_cost_uk = obj.volume*pd.sea['uk_fee']/pd.exchange_rate['uk']
        second_class_cost_uk = obj.uk_second_cost
        purchase_price = obj.price/pd.exchange_rate['uk']
        sale_price_10 = (first_class_cost_uk+second_class_cost_uk+purchase_price)/0.70
        return u'<span style="color:green;font-weight:bold">%s</span>' % round(sale_price_10,1)
    uk_sea_sale_price_10.short_description = u'UK(海)10%$'
    uk_sea_sale_price_10.allow_tags = True



    def de_sale_price_10(self, obj) :
        first_class_cost_de = obj.weight*pd.first_class_rate['first_class_rate_de']/pd.exchange_rate['de']
        second_class_cost_de = obj.de_second_cost
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_10 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.70
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_10,1)
    de_sale_price_10.short_description = u'DE(空)10%€'
    de_sale_price_10.allow_tags = True

    def cn_de_sale_price_10(self, obj) :
        first_class_cost_de = 0
        second_class_cost_de = obj.cn_de_cost
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_10 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.70
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_10,1)
    cn_de_sale_price_10.short_description = u'DE(本)10%€'
    cn_de_sale_price_10.allow_tags = True

    def de_sea_sale_price_10(self, obj) :
        first_class_cost_de = obj.volume*pd.sea['de_fee']/pd.exchange_rate['de']
        second_class_cost_de = obj.de_second_cost
        purchase_price = obj.price/pd.exchange_rate['de']
        sale_price_10 = (first_class_cost_de+second_class_cost_de+purchase_price)/0.70
        return u'<span style="color:blue;font-weight:bold">%s</span>' % round(sale_price_10,1)
    de_sea_sale_price_10.short_description = u'DE(海)10%€'
    de_sea_sale_price_10.allow_tags = True


    def au_sale_price_10(self, obj) :
        first_class_cost_au = obj.weight*pd.first_class_rate['first_class_rate_au']/pd.exchange_rate['au']
        second_class_cost_au = obj.au_second_cost
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_10 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.70
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_10,1)
    au_sale_price_10.short_description = u'AU(空)10%$'
    au_sale_price_10.allow_tags = True

    def cn_au_sale_price_10(self, obj) :
        first_class_cost_au = obj.weight*pd.first_class_rate['first_class_rate_au']/pd.exchange_rate['au']
        second_class_cost_au = obj.cn_au_cost
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_10 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.70
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_10,1)
    cn_au_sale_price_10.short_description = u'AU(本)10%$'
    cn_au_sale_price_10.allow_tags = True

    def au_sea_sale_price_10(self, obj) :
        first_class_cost_au = obj.volume*pd.sea['au_fee']/pd.exchange_rate['au']
        second_class_cost_au = obj.de_second_cost
        purchase_price = obj.price/pd.exchange_rate['au']
        sale_price_10 = (first_class_cost_au+second_class_cost_au+purchase_price)/0.70
        return u'<span style="color:orange;font-weight:bold">%s</span>' % round(sale_price_10,1)
    au_sea_sale_price_10.short_description = u'AU(海)10%$'
    au_sea_sale_price_10.allow_tags = True


    def preview(self,obj):    #show photos in admin

        return '<img src="%s" height="64" width="64" />' %(obj.image)

    preview.allow_tags = True

    preview.short_description = "图片"







   #show in admin
    list_display = (
        'category',
        'sku',
        'preview',
        'owner',
        'name',
        'price',
        'weight',
        'volume',
        'cn_us_sale_price_10',
        'us_sale_price_10',
        'us_sea_sale_price_10',
        'cn_uk_sale_price_10',
        'uk_sale_price_10',
        'uk_sea_sale_price_10',
        'cn_de_sale_price_10',
        'de_sale_price_10',
        'de_sea_sale_price_10',
        'cn_au_sale_price_10',
        'au_sale_price_10',
        'au_sea_sale_price_10',


    )
    #edited
    fields = (
        'category',
        'image',
        'sku',
        'name',
        'price',
        'weight',
        'volume',
        'cn_us_cost',
        'us_second_cost',
        'cn_uk_cost',
        'uk_second_cost',
        'cn_de_cost',
        'de_second_cost',
        'cn_au_cost',
        'au_second_cost',

    )

    search_fields = ('sku','name',)
    ordering = ('sku',)
    list_filter = ('category',)
    list_per_page = 10





class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product,ProductAdmin)
admin.site.site_header = "产品信息系统"
admin.site.index_title = "eBayA组产品最低售价表"
#LogEntry.objects.all().delete()#delete recent actions