# Generated by Django 3.2 on 2021-05-15 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal_library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('pages', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=250)),
                ('url', models.URLField()),
                ('holder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal_library.userinformation')),
            ],
        ),
    ]
