# Generated by Django 4.1.1 on 2023-01-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0017_alter_questionans_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionans',
            name='question',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]