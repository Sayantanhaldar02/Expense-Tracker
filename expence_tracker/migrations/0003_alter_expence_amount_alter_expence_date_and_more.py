# Generated by Django 5.0.4 on 2024-05-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expence_tracker', '0002_rename_name_expence_expence_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expence',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expence',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='expence',
            name='expence_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]