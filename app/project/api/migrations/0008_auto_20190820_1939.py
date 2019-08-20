# Generated by Django 2.2.4 on 2019-08-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_source_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='current_balance',
        ),
        migrations.AddField(
            model_name='artist',
            name='known_balance',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=10, verbose_name='Current Balance'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('source', models.ManyToManyField(to='api.Source')),
                ('vendor', models.ManyToManyField(to='api.Vendor')),
            ],
        ),
    ]