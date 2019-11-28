from django.contrib import admin
from .models import User, Contact, ConfirmEmailToken, Shop, Category, Product, Parameter,\
    ProductParameter, Order, OrderItem

admin.site.register(User)
admin.site.register(Contact)
admin.site.register(ConfirmEmailToken)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Parameter)
admin.site.register(ProductParameter)
admin.site.register(Order)
admin.site.register(OrderItem)