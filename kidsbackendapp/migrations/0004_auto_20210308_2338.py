# Generated by Django 3.1.7 on 2021-03-08 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kidsbackendapp', '0003_auto_20210308_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodconfiguration',
            name='lastSelected',
        ),
        migrations.AddField(
            model_name='foodconfiguration',
            name='lastEaten',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='foodconfiguration',
            name='food',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kidsbackendapp.food'),
        ),
        migrations.AlterField(
            model_name='foodconfiguration',
            name='foodConfigurationName',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='foodconfiguration',
            name='foodOption',
            field=models.ManyToManyField(blank=True, to='kidsbackendapp.FoodOption'),
        ),
    ]