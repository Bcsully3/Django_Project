# Generated by Django 4.2.5 on 2023-09-29 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='New Portfolio', max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('contact_email', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='major',
            field=models.CharField(choices=[('CSCI-BS', 'BS in Computer Science'), ('CPEN-BS', 'BS in Computer Engineering'), ('BIGD-BI', 'BI in Game Design and Development'), ('BICS-BI', 'BI in Computer Science'), ('BISC-BI', 'BI in Computer Security'), ('CSCI-BA', 'BA in Computer Science'), ('DASE-BS', 'BS in Data Analytics and Systems Engineering')], max_length=200),
        ),
        migrations.CreateModel(
            name='ProjectInPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.project')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='portfolio',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
    ]
