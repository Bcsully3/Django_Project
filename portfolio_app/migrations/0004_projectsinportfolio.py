# Generated by Django 4.2.5 on 2023-09-29 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0003_project_portfolio_delete_projectinportfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectsInPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.project')),
            ],
        ),
    ]
