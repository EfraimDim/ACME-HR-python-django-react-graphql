# # Generated by Django 4.0.3 on 2022-03-08 13:47

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_no', models.CharField(
                    max_length=4, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': settings.IS_TESTING,
            },
        ),

        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_no', models.BigIntegerField(
                    primary_key=True, serialize=False)),
                ('birth_date', models.DateField()),
                ('first_name', models.CharField(max_length=14)),
                ('last_name', models.CharField(max_length=16)),
                ('gender', models.TextField()),
                ('hire_date', models.DateField()),
            ],
            options={
                'db_table': 'employees',
                'managed': settings.IS_TESTING,
            },
        ),

        migrations.CreateModel(
            name='DeptEmp',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING,
                to='backend.employee')),
                ('dept_no', models.ForeignKey(db_column='dept_no',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='backend.department')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'dept_emp',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='DeptManager',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING,
                to='backend.employee')),
                ('dept_no', models.ForeignKey(db_column='dept_no',
                 on_delete=django.db.models.deletion.DO_NOTHING, to='backend.department')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'dept_manager',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING,
                 to='backend.employee')),
                ('salary', models.BigIntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
            options={
                'db_table': 'salaries',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('emp_no', models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING,
                 to='backend.employee')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'titles',
                'managed': settings.IS_TESTING,
            },
        ),
        migrations.AlterUniqueTogether(
            name='deptmanager',
            unique_together={('emp_no', 'dept_no')},
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together={('emp_no', 'dept_no')},
        ),
        migrations.AlterUniqueTogether(
            name='salary',
            unique_together={('emp_no', 'from_date')},
        ),
        migrations.AlterUniqueTogether(
            name='title',
            unique_together={('emp_no', 'title', 'from_date')},
        ),
    ]