# Generated by Django 3.1 on 2021-06-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0016_auto_20210613_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnotes',
            name='unit_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], default='1', max_length=256),
        ),
    ]
