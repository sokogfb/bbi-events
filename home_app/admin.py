from django.contrib import admin

# Register your models here.
from home_app.models import gallery, passed_weddings


class GAdmin(admin.ModelAdmin):
    list_filter = ("date", "name", "picture")
    search_fields = ("name",)
    list_display = ("date", "name", "picture")
    list_per_page = 20
    list_max_show_all = True


class PWAdmin(admin.ModelAdmin):
    list_filter = ("date", "name", "bride", "groom")
    search_fields = ("name", "bride", "groom")
    list_display = ("date", "name", "bride", "groom", "picture")
    list_per_page = 20
    list_max_show_all = True


admin.site.register(gallery, GAdmin)
admin.site.register(passed_weddings, PWAdmin)
