from django.contrib import admin
from . models import blog

# Register your models here.
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','content','photo']
