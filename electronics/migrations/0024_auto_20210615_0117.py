# Generated by Django 3.1 on 2021-06-14 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('electronics', '0023_auto_20210615_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classnotes',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='classnotes',
            name='doc_type',
            field=models.CharField(choices=[('PDF', 'PDF'), ('Word Doc', 'Word Doc'), ('PPT', 'PPT')], max_length=256),
        ),
        migrations.AlterField(
            model_name='classnotes',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject'),
        ),
        migrations.AlterField(
            model_name='classnotes',
            name='unit_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=256),
        ),
        migrations.AlterField(
            model_name='laboratory_videos',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_full_form',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='video_lectures',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.subject'),
        ),
        migrations.AlterField(
            model_name='video_lectures',
            name='unit_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='electronics.unit_info'),
        ),
    ]
