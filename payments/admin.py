from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.TabularInline):
    """display a list of the editable line items in the same
    page so we don't have to go to inlineitem seccion admin"""
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """Register the models to the admin"""
    inlines = (OrderLineItemAdmin,)

    readonly_fields = ('order_number',
                       'date',
                       'order_total',
                       'grand_total',
                       'original_bag',
                       'stripe_pid',
                       )

    fields = ('order_number',
              'user_profile',
              'date',
              'first_name',
              'last_name',
              'email',
              'phone_number',
              'order_total',
              'grand_total',
              'original_bag',
              'stripe_pid',
              )

    list_display = ('order_number',
                    'date',
                    'first_name',
                    'last_name',
                    'order_total',
                    'grand_total',
                    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)