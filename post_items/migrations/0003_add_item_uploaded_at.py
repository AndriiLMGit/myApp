# Generated by Django 3.0.2 on 2020-04-05 18:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post_items', '0002_add_item_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='add_item',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
