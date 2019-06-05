# Generated by Django 2.0 on 2019-03-01 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0005_pendingquery'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsweredQueries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qsn', models.CharField(max_length=10000)),
                ('ans', models.CharField(max_length=10000)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reviews.College')),
            ],
        ),
    ]
