# Generated by Django 5.0.3 on 2024-11-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_credittransaction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['code']},
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
