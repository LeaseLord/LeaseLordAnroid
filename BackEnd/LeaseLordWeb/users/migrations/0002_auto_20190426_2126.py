# Generated by Django 2.1.5 on 2019-04-27 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='propertymanager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='users.PropertyManager'),
        ),
    ]