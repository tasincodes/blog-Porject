# Generated by Django 4.2.3 on 2023-07-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0003_alter_employee_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='ph',
            field=models.CharField(default='+880', max_length=10),
        ),
    ]