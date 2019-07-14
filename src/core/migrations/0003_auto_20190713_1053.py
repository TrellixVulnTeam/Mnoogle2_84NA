# Generated by Django 2.1.7 on 2019-07-13 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190713_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='category',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='company',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='employmentType',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='views',
        ),
        migrations.AddField(
            model_name='jobs',
            name='Company',
            field=models.TextField(default='Not Available', max_length=250),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='Address',
            field=models.TextField(default='Not available', max_length=250),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
    ]