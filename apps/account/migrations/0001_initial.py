# Generated by Django 4.0.6 on 2022-08-07 22:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
