# Generated by Django 5.0.6 on 2024-05-10 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_star_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Crochets', 'Crochets'), ('Crochet Bundles', 'Crochet Bundles')], default='Vegetables', max_length=25),
        ),
    ]
