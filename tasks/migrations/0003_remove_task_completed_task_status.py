# Generated by Django 5.1.3 on 2024-12-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_assigned_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('CO', 'Completed'), ('AC', 'Accepted'), ('PE', 'Pending'), ('RE', 'Rejected')], default='CO', max_length=2),
            preserve_default=False,
        ),
    ]