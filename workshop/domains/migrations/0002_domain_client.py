# Generated by Django 2.1 on 2018-08-10 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('domains', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='domains.Client'),
            preserve_default=False,
        ),
    ]
