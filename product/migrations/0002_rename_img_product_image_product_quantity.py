# Generated by Django 4.2.6 on 2023-10-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='img',
            new_name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=5),
        ),
    ]
