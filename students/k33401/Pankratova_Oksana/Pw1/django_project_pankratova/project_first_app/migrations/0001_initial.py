# Generated by Django 4.1.7 on 2023-04-03 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gos_number', models.CharField(max_length=15)),
                ('mark', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=20)),
                ('color', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Motorist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField()),
                ('end', models.DateField(blank=True, null=True)),
                ('id_auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.automobile')),
                ('id_motorist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.motorist')),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
                ('license_type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('A1', 'A1'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('M', 'M'), ('BE', 'Be'), ('CE', 'Ce'), ('DE', 'De')], max_length=3)),
                ('given', models.DateField()),
                ('motorist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.motorist')),
            ],
        ),
        migrations.AddField(
            model_name='automobile',
            name='owning',
            field=models.ManyToManyField(through='project_first_app.Ownership', to='project_first_app.motorist'),
        ),
    ]
