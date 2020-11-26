# Generated by Django 3.1.3 on 2020-11-22 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview_Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('profile_pic', models.ImageField(upload_to='images/newsfeed')),
                ('date', models.DateField()),
                ('job_title', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('difficulty', models.CharField(max_length=10)),
                ('experience', models.CharField(max_length=255)),
                ('questions', models.CharField(max_length=255)),
            ],
        ),
    ]
