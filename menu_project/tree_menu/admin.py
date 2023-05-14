from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import MainMenu, SecondaryMenu


class MainMenuMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('pk', 'name', 'parent')
    list_display_links = ('pk', 'name')
    mptt_level_indent = 20


class SecondaryMenuMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('pk', 'name', 'parent')
    list_display_links = ('pk', 'name')
    mptt_level_indent = 20


admin.site.register(MainMenu, MainMenuMPTTModelAdmin)
admin.site.register(SecondaryMenu, SecondaryMenuMPTTModelAdmin)
