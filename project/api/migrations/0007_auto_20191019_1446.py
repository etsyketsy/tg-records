# Generated by Django 2.0.3 on 2019-10-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20191009_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='ffo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='release',
            name='upc',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]