# Generated by Django 4.2.5 on 2023-09-29 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_portfolio_project_alter_student_major_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='portfolio',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.portfolio'),
        ),
        migrations.DeleteModel(
            name='ProjectInPortfolio',
        ),
    ]
