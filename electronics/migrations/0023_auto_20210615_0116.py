# Generated by Django 3.1 on 2021-06-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0022_subject_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]