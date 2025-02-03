# Generated by Django 5.1.5 on 2025-01-28 05:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecartApp', '0002_cart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=250)),
                ('phone', models.PositiveBigIntegerField(default=1234657890)),
                ('status', models.CharField(choices=[('order-placed', 'order-placed'), ('cancelled', 'cancelled'), ('delivered', 'delivered'), ('dispatched', 'dispatched'), ('out-for-delivery', 'out-for-delivery')], default='order-placed', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecartApp.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
