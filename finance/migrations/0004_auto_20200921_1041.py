# Generated by Django 3.0.8 on 2020-09-21 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
        ('employees', '0001_initial'),
        ('finance', '0003_auto_20200921_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employees.Student'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='exams',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.Exams'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount_paid',
            field=models.IntegerField(verbose_name='Costo Examen'),
        ),
    ]
