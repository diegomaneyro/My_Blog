# Generated by Django 5.1.5 on 2025-02-05 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_post', '0003_rename_user_article_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='Articles'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='Categories'),
        ),
    ]
