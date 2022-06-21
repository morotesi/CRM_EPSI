# Generated by Django 4.0.5 on 2022-06-19 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bdd', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=56)),
                ('description', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_nom', models.CharField(max_length=56)),
                ('employee_prenom', models.CharField(max_length=56)),
                ('email', models.CharField(max_length=56)),
                ('no_tel', models.CharField(max_length=56)),
                ('id_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd.role')),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_commande', models.DateField(blank=True, null=True)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd.client')),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bdd.employee')),
            ],
        ),
    ]
