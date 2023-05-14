from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class MainMenu(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='main_menu_children', verbose_name='Категория')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Главное меню'

    def __str__(self):
        return self.name


class SecondaryMenu(MPTTModel):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='secondary_menu_children', verbose_name='Категория')

    class MPTTMeta:
        order_insertion_by = ['name']
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Дополнительное меню'

    def __str__(self):
        return self.name