# Generated by Django 4.0.6 on 2023-12-03 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure_content', '0002_alter_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=500)),
                ('lastname', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
