# Generated by Django 5.0.6 on 2024-05-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp1', '0002_curso_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
            ],
        ),
    ]