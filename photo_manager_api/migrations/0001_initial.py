# Generated by Django 4.1.5 on 2023-01-12 20:29

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
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to='media/uploads/')),
                ('location', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('people_on_photo', models.TextField()),
                ('user_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]