# Generated by Django 3.0.4 on 2020-03-30 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_officer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=10)),
                ('ml', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='SavedModel',
        ),
    ]
