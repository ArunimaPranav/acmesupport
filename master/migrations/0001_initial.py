# Generated by Django 4.1.5 on 2023-01-15 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('priority', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], null=True)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=500)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Last_Updated_at', models.DateTimeField(auto_now=True)),
                ('Created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='createdby', to='accounts.account')),
            ],
        ),
    ]