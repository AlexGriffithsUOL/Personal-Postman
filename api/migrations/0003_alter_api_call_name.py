# Generated by Django 5.0.3 on 2024-07-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_remove_api_call_api_endpoint_remove_api_call_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="api_call",
            name="name",
            field=models.TextField(default="GET Api Call", verbose_name="Name"),
        ),
    ]