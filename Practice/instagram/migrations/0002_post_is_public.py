# Generated by Django 4.0 on 2023-12-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_public",
            field=models.BooleanField(default=False, verbose_name="공개여부"),
        ),
    ]