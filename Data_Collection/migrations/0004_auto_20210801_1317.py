# Generated by Django 3.2.5 on 2021-08-01 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_Collection', '0003_auto_20210801_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='ownership_type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='pacel',
            name='existing_use',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pacel',
            name='institution',
        ),
        migrations.AddField(
            model_name='pacel',
            name='institution',
            field=models.ManyToManyField(to='Data_Collection.Institution'),
        ),
        migrations.AlterField(
            model_name='pacel',
            name='proposed_use',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pacel',
            name='topology',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]