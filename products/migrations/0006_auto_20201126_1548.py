# Generated by Django 3.1.3 on 2020-11-26 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.country'),
        ),
    ]
