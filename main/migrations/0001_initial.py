# Generated by Django 4.1.2 on 2022-10-16 05:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFiles',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='media/csv')),
                ('date_added', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'verbose_name': 'csv',
                'verbose_name_plural': 'csvs',
                'db_table': 'csv_generated',
                'ordering': ('-date_added',),
            },
        ),
    ]
