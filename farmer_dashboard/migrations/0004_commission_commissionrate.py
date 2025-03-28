# Generated by Django 5.1.7 on 2025-03-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer_dashboard', '0003_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('rental', 'Pond Rental'), ('sales', 'Fish Sales')], max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('transaction', models.CharField(help_text='Related transactoin ID or reference', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommissionRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_rate', models.DecimalField(decimal_places=2, default=10.0, help_text='Commission percentage for pond rentals', max_digits=5)),
                ('sales_rate', models.DecimalField(decimal_places=2, default=5.0, help_text='Commission percentage for fish sales', max_digits=5)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
