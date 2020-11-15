from django.contrib import admin
from .models import Site, Article, Feature, Product, SiteProduct, PricingRecord, Price

# Register your models here.


class PricingRecordAdmin(admin.ModelAdmin):
    list_display = ('productname', 'site', 'price7days')
    list_filter = ('site',)


admin.site.register(Site)
admin.site.register(Article)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(SiteProduct)
admin.site.register(PricingRecord, PricingRecordAdmin)
admin.site.register(Price)
