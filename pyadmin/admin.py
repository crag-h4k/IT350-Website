from django.contrib import admin

from .models import Customer, Account, Shipping, Billing, Meal_History, Employee, Order, Meal, Meal_Review

admin.site.register(Customer)
admin.site.register(Account)
admin.site.register(Shipping)
admin.site.register(Billing)
admin.site.register(Meal_History)
admin.site.register(Employee)
admin.site.register(Order)
admin.site.register(Meal)
admin.site.register(Meal_Review)
