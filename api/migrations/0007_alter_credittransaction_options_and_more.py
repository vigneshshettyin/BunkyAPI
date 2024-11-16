# Generated by Django 5.0.3 on 2024-11-16 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_product_options_customer_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='credittransaction',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['created_at']},
        ),
        migrations.RenameField(
            model_name='credittransaction',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='credittransaction',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_modified',
            new_name='updated_at',
        ),
        migrations.AddField(
            model_name='credittransaction',
            name='date',
            field=models.DateField(default='2024-11-16'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='is_fuel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='Change Me', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DailyLubeSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StockInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField()),
                ('date', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
                'abstract': False,
            },
        ),
    ]
