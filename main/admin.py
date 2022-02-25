from django.contrib import admin
from main.models import Nate

# admin.site.register(Nate)


class NateAdmin(admin.ModelAdmin):
    list_display= ('title', 'content', 'created_at', 'updated_ar')


admin.site.register(Nate, NateAdmin)