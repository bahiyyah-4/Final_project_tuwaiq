# Generated by Django 4.1.3 on 2022-11-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_options_prodect'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodect',
            options={'ordering': ('-created_at',)},
        ),
        migrations.AddField(
            model_name='prodect',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/product_images/'),
        ),
    ]