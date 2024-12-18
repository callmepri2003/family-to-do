# Generated by Django 5.1.3 on 2024-12-09 04:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familyMembers', '0001_initial'),
        ('tasks', '0002_alter_task_assigned_to'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigned_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasked_assigned_to_others', to='familyMembers.familymember'),
        ),
    ]
