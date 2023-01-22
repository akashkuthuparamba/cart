# Generated by Django 4.1.1 on 2022-12-18 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0007_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=30)),
                ('price', models.CharField(default=None, max_length=10)),
                ('quantitie', models.CharField(default=None, max_length=30)),
                ('date', models.DateField(default=None)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
