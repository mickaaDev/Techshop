# Generated by Django 3.0.8 on 2020-07-18 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_product_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to=settings.AUTH_USER_MODEL, verbose_name='Продавец'),
        ),
    ]
