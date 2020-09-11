# Generated by Django 3.1 on 2020-09-06 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_teacher_subj_teacher_timetable_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('s_name', models.CharField(max_length=100)),
                ('s_email', models.EmailField(max_length=50)),
                ('s_specialization', models.CharField(max_length=50)),
                ('s_rollno', models.IntegerField(max_length=7, primary_key='True', serialize=False)),
                ('s_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameModel(
            old_name='teacher_subj',
            new_name='teacher_class',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='UserForm',
        ),
        migrations.AlterField(
            model_name='teacher_class',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_timetable',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='teacher_timetable_link',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]