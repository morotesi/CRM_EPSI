# Generated by Django 4.0.5 on 2022-06-20 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0003_role_employee_commande'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prix',
            options={'verbose_name': 'Prix', 'verbose_name_plural': 'Prix'},
        ),
    ]