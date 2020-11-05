from django.contrib import admin
from storefront.models import Store, Category

class StoreAdmin(admin.ModelAdmin):
    fields = ('item', 'description', 'categories', 'price')

class StoreAdmin(admin.ModelAdmin):
    exclude = ('image',)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Store, StoreAdmin)
admin.site.register(Category,StoreAdmin)
