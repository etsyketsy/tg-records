# Generated by Django 2.2.4 on 2019-09-25 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20190828_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Release',
            fields=[
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Release Name')),
                ('release_number', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Release Number')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('artist', models.ManyToManyField(to='api.Artist')),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='album',
        ),
        migrations.RemoveField(
            model_name='income',
            name='album',
        ),
        migrations.RemoveField(
            model_name='product',
            name='album',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.AddField(
            model_name='expense',
            name='release',
            field=models.ManyToManyField(blank=True, to='api.Release'),
        ),
        migrations.AddField(
            model_name='income',
            name='release',
            field=models.ManyToManyField(blank=True, to='api.Release'),
        ),
        migrations.AddField(
            model_name='product',
            name='release',
            field=models.ManyToManyField(blank=True, to='api.Release'),
        ),
    ]