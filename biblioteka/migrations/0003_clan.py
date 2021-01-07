# Generated by Django 3.1.5 on 2021-01-07 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteka', '0002_auto_20210107_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=20)),
                ('prezime', models.CharField(max_length=20)),
                ('knjige', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteka.knjiga')),
            ],
        ),
    ]