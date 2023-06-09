# Generated by Django 4.2.1 on 2023-05-14 17:09

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecondaryMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_menu_children', to='tree_menu.secondarymenu', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Пункт меню',
                'verbose_name_plural': 'Дополнительное меню',
            },
        ),
    ]
