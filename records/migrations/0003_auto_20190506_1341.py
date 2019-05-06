# Generated by Django 2.2.1 on 2019-05-06 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_record_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='image',
        ),
        migrations.AlterField(
            model_name='record',
            name='note',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='メモ'),
        ),
    ]
