# Generated by Django 3.0.4 on 2020-03-30 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_officer', '0003_savedstate_statandml'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('columns', models.CharField(max_length=1000000)),
                ('nominal_features', models.CharField(max_length=1000000)),
            ],
        ),
    ]
