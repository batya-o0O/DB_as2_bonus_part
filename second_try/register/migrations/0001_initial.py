# Generated by Django 4.1.3 on 2022-11-21 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('disease_code', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('pathogen', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseType',
            fields=[
                ('did', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=60, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=40)),
                ('salary', models.IntegerField()),
                ('phone', models.CharField(max_length=20)),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.country')),
            ],
        ),
        migrations.CreateModel(
            name='Specialize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.diseasetype')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_deaths', models.IntegerField()),
                ('total_patients', models.IntegerField()),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.disease')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users')),
            ],
        ),
        migrations.CreateModel(
            name='PublicServant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users')),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=20)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.users')),
            ],
        ),
        migrations.AddField(
            model_name='disease',
            name='did',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.diseasetype'),
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.country')),
                ('disease_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.disease')),
            ],
        ),
    ]
