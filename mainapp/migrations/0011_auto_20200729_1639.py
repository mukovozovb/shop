# Generated by Django 3.0.8 on 2020-07-29 16:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата заказа'),
        ),
    ]
