from django.contrib import admin
from .models import Google
from .models import Write, Category, Choice


# Register your models here.
admin.site.register(Google)
admin.site.register(Write)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Choice)