# Generated by Django 4.2.3 on 2023-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0004_alter_employee_ph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dept',
            field=models.CharField(max_length=10),
        ),
    ]