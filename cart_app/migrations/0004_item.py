# Generated by Django 4.1.1 on 2022-12-18 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0003_userdetails_address_userdetails_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default=None, max_length=100)),
                ('item_price', models.IntegerField(default=None)),
                ('item_img', models.ImageField(default=None, upload_to='media/')),
                ('quantitie', models.CharField(default=None, max_length=30)),
                ('brand_name', models.CharField(default=None, max_length=100)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cart_app.productcategory')),
            ],
        ),
    ]
