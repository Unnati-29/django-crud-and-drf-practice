from django.contrib import admin
from .models import ChaiVariety, ChaiReview, Store, ChaiOrder

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'chai_variety', 'quantity', 'order_date')
    list_filter = ('order_date',)


admin.site.register(ChaiVariety, ChaiVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiOrder, ChaiOrderAdmin)
