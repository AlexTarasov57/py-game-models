# Generated by Django 4.0.2 on 2024-09-10 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guild',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='guild',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='db.guild'),
        ),
        migrations.AlterField(
            model_name='player',
            name='nickname',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
