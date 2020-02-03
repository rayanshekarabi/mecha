# Generated by Django 3.0.2 on 2020-01-30 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sniper', models.IntegerField(default=0)),
                ('assault', models.IntegerField(default=0)),
                ('engineer', models.IntegerField(default=0)),
                ('support', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_kill', models.IntegerField(default=0)),
                ('total_death', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('rank', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.IntegerField(default=0)),
                ('extra_health', models.IntegerField(default=0)),
                ('special_attacks', models.IntegerField(default=0)),
                ('bullet', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Bullet')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nickname', models.TextField(default='guest')),
                ('phone_number', models.TextField(default='000000000', unique=True)),
                ('token', models.TextField(default='', unique=True)),
                ('last_code_send', models.IntegerField(default=0, null=True)),
                ('avatar_url', models.URLField(default='#')),
                ('profile', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Profile')),
                ('wallet', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Wallet')),
            ],
        ),
    ]