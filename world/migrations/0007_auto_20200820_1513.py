# Generated by Django 3.1 on 2020-08-20 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0006_auto_20200820_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='owned_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decks', to='world.base'),
        ),
    ]
