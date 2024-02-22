from django.contrib import admin

from shop_app.models import Product, Client, Order, OrderItem


class ClientAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'phone', 'address', 'date_registered']
    search_fields = ['name']
    ordering = ['-date_registered']
    list_filter = ['address', 'email']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Данные о контактах покупателя',
                'fields': ['email', 'phone']
            },
        ),
        (
            'Адрес',
            {
                'description': 'Адрес',
                'fields': ['address'],
            }
        ),
    ]


class ProductAdmin(admin.ModelAdmin):
    @admin.action(description="Обнуление количества продукта")
    def reset_quantity(modeladmin, request, queryset):
        queryset.update(quantity=0)

    list_display = ['name', 'description', 'price', 'quantity']
    search_fields = ['name']
    ordering = ['-price']
    list_filter = ['name']
    actions = [reset_quantity]

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Данные о продукте',
                'fields': ['description', 'price']
            },
        ),

        (
            'Количество товара',
            {
                'description': 'Количество',
                'fields': ['quantity'],
            }
        ),
    ]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_ordered', 'total_price')
    inlines = [OrderItemInline]

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = 'Общая цена'


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
