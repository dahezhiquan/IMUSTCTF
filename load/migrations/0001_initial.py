# Generated by Django 3.2.9 on 2022-02-17 13:55

from django.db import migrations, models

# CTF工具权限数据表结构
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usertool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolname', models.CharField(max_length=20)),
                ('toolpassword', models.CharField(max_length=50)),
                ('uid', models.CharField(max_length=50)),
            ],
        ),
    ]
