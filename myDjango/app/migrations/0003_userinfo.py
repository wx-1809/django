# Generated by Django 4.0.3 on 2022-03-24 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_test_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
