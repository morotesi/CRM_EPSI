# Generated by Django 4.0.5 on 2022-06-23 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0010_commande_id_voiture_alter_voiture_id_marque'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commande',
            old_name='id_client',
            new_name='pk_client',
        ),
        migrations.RenameField(
            model_name='commande',
            old_name='id_employee',
            new_name='pk_employee',
        ),
    ]
