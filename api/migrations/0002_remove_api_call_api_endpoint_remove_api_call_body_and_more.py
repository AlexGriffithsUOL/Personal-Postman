# Generated by Django 5.0.3 on 2024-07-06 13:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="api_call",
            name="API Endpoint",
        ),
        migrations.RemoveField(
            model_name="api_call",
            name="Body",
        ),
        migrations.RemoveField(
            model_name="api_call",
            name="Headers",
        ),
        migrations.RemoveField(
            model_name="api_call",
            name="Name",
        ),
        migrations.AddField(
            model_name="api_call",
            name="api_type",
            field=models.TextField(
                choices=[
                    ("ge", "GET"),
                    ("po", "POST"),
                    ("pa", "PATCH"),
                    ("pu", "PUT"),
                    ("de", "DELETE"),
                ],
                default="ge",
                max_length=2,
            ),
        ),
        migrations.AddField(
            model_name="api_call",
            name="endpoint",
            field=models.TextField(blank=True, verbose_name="API Endpoint"),
        ),
        migrations.AddField(
            model_name="api_call",
            name="body",
            field=models.TextField(blank=True, null=True, verbose_name="Body"),
        ),
        migrations.AddField(
            model_name="api_call",
            name="headers",
            field=models.TextField(blank=True, null=True, verbose_name="Headers"),
        ),
        migrations.AddField(
            model_name="api_call",
            name="name",
            field=models.TextField(default="e", verbose_name="Name"),
            preserve_default=False,
        ),
    ]
