# Generated by Django 5.0.3 on 2024-10-21 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_page', '0002_auto_20240315_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
