# Generated by Django 3.2.14 on 2022-07-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('grade', models.CharField(blank=True, max_length=100)),
                ('roll_no', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('gender', models.BooleanField()),
            ],
        ),
    ]
