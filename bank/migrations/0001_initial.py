# Generated by Django 4.0.2 on 2022-03-22 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=100, verbose_name='Счёт клиента')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(verbose_name='Значение')),
                ('transaction_type', models.CharField(choices=[('DP', 'Зачисление'), ('WD', 'Вывод')], max_length=10, verbose_name='Тип операции (зачисление/вывод)')),
                ('comment', models.CharField(max_length=100, verbose_name='Комментарий')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.balance')),
            ],
            options={
                'verbose_name': 'Транзкция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]