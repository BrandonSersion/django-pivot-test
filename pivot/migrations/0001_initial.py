# Generated by Django 2.1 on 2018-08-03 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kingdom', models.CharField(max_length=30)),
                ('phylum', models.CharField(max_length=30)),
                ('class_name', models.CharField(max_length=30)),
                ('order', models.CharField(max_length=30)),
                ('family', models.CharField(max_length=30)),
                ('genus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AnimalCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pivot.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Zoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('entry_fee', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='animalcount',
            name='zoo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pivot.Zoo'),
        ),
    ]
