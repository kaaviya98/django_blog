# Generated by Django 4.1.2 on 2022-11-01 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_category_post_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.CharField(max_length=255),
        ),
    ]
