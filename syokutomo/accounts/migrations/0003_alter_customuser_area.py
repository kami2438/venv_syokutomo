# Generated by Django 3.2 on 2021-11-26 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.t10_area', verbose_name='エリア'),
        ),
    ]