# Generated by Django 4.2.17 on 2025-01-08 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.CharField(max_length=100, unique=True)),
                ('lead_date', models.DateTimeField(blank=True, null=True)),
                ('lead_check_in', models.DateTimeField(blank=True, null=True)),
                ('lead_check_out', models.DateTimeField(blank=True, null=True)),
                ('meeting_id', models.CharField(blank=True, max_length=100, null=True)),
                ('boom_score', models.FloatField(blank=True, null=True)),
                ('boom_score_delta', models.FloatField(blank=True, null=True)),
                ('conversation', models.CharField(blank=True, max_length=100, null=True)),
                ('language_code', models.CharField(blank=True, max_length=10, null=True)),
                ('home_city', models.CharField(blank=True, max_length=100, null=True)),
                ('home_country', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
    ]
