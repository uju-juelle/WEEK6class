# Generated by Django 4.2 on 2023-04-20 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('GENERAL', 'GENERAL')], max_length=100)),
                ('image', models.ImageField(default='product.jpg', upload_to='product_images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
