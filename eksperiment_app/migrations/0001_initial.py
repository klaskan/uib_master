# Generated by Django 2.2.5 on 2020-01-14 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eksperiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deklarert_inntekt', models.DecimalField(decimal_places=2, max_digits=4)),
                ('revidert', models.BooleanField(default=False)),
                ('utbetalt', models.DecimalField(decimal_places=2, max_digits=4)),
                ('faktisk_utbetaling', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]
