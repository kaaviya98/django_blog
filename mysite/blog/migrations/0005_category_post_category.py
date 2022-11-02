# Generated by Django 4.1.2 on 2022-11-01 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_post_created_post_publish_post_updated"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.CharField(default="uncategorised", max_length=255),
        ),
    ]