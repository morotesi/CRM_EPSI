# Generated by Django 4.0.5 on 2022-06-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0004_rename_id_acheteur_voiture_pk_acheteur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
