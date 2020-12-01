from django.contrib import admin
from .models import Site, Article, Feature, Product, SiteProduct, PricingRecord, Price, Redirect, TrackingClick, DestinationGeo, OtaDestinationScore

# Register your models here.


class PricingRecordAdmin(admin.ModelAdmin):
    list_display = ('productname', 'site', 'price7days')
    list_filter = ('site',)


class DestinationGeoAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)


admin.site.register(Site)
admin.site.register(Article)
admin.site.register(Feature)
admin.site.register(Product)
admin.site.register(SiteProduct)
admin.site.register(PricingRecord, PricingRecordAdmin)
admin.site.register(Price)
admin.site.register(Redirect)
admin.site.register(TrackingClick)
admin.site.register(DestinationGeo, DestinationGeoAdmin)
admin.site.register(OtaDestinationScore)
