# Generated by Django 3.1 on 2021-06-13 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0018_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classnotes',
            name='topic_name',
        ),
        migrations.AddField(
            model_name='classnotes',
            name='description',
            field=models.CharField(default='This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.', max_length=1000),
        ),
    ]
