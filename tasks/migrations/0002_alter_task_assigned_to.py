# Generated by Django 5.1.3 on 2024-12-08 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyMembers', '0001_initial'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='familyMembers.familymember'),
        ),
    ]