# Generated by Django 5.0.3 on 2024-03-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
