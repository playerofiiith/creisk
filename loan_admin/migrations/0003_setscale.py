# Generated by Django 3.0.4 on 2020-04-09 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_admin', '0002_feature_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='SetScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.IntegerField()),
                ('green', models.IntegerField()),
            ],
        ),
    ]
