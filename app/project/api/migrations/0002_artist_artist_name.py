# Generated by Django 2.2.4 on 2019-08-20 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_name',
            field=models.CharField(default='TBD', max_length=150, verbose_name='Artist Name'),
            preserve_default=False,
        ),
    ]
