# Generated by Django 3.2.11 on 2022-10-11 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animalslist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sittinglist',
            name='breeds_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sitting_breeds_list', to='animalslist.breedlist'),
        ),
    ]