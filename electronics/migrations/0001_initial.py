# Generated by Django 3.1 on 2021-06-04 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Unit_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.IntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='unit_images/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Video_lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_file', models.FileField(upload_to='Video_lectures')),
                ('title', models.CharField(max_length=100)),
                ('topic_name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject')),
                ('unit_number', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='electronics.unit_info')),
            ],
        ),
        migrations.CreateModel(
            name='Course_outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_outcome_number', models.IntegerField()),
                ('course_outcome', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Classnotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes_file', models.FileField(upload_to='Classnotes')),
                ('title', models.CharField(max_length=100)),
                ('topic_name', models.CharField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject')),
                ('unit_number', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='electronics.unit_info')),
            ],
        ),
    ]
