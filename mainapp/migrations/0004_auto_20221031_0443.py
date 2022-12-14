# Generated by Django 3.2.16 on 2022-10-31 04:43

from django.db import migrations
from random import randint
from datetime import date
import mainapp

def populate_tables(apps, schema_editor):
    # Populate EmployeePosition table
    EmployeePosition = apps.get_model('mainapp', 'EmployeePosition')
    position_titles = ('Worker', 'Accountant', 'System administrator', 'Director')
    employee_positions = []
    for position_title in position_titles:
        employee_positions.append(EmployeePosition.objects.create(title=position_title))

    # Populate Department table
    Department = apps.get_model('mainapp', 'Department')
    departments = []
    departments.append(Department.objects.create(name='Factory 1', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 2', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 3', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 4', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 5', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 6', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 7', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 8', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 9', level=0, lft=0, rght=0, tree_id=0))
    departments.append(Department.objects.create(name='Factory 10', level=0, lft=0, rght=0, tree_id=0))
    for i in range(0, 10):
        production = Department.objects.create(
            name='Production',
            parent=departments[i],
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        accounting = Department.objects.create(
            name='Accounting',
            parent=departments[i],
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        purchasing = Department.objects.create(
            name='Purchasing',
            parent=departments[i],
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        sweets_production_zone = Department.objects.create(
            name='Sweets production zone',
            parent=production,
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        candy_bar_production_line = Department.objects.create(
            name='Candy bar production line',
            parent=sweets_production_zone,
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        candy_bar_test_area = Department.objects.create(
            name='Candy bar test area',
            parent=candy_bar_production_line,
            level=0,
            lft=0,
            rght=0,
            tree_id=0
        )
        departments += [
            production,
            accounting,
            purchasing,
            sweets_production_zone,
            candy_bar_production_line,
            candy_bar_test_area
        ]
    mainapp.models.Department.objects.rebuild()

    # Populate Employee table
    Employee = apps.get_model('mainapp', 'Employee')    
    last_names = ['Ivanov', 'Petrov', 'Novoselov', 'Vanushkov', 'Gavrin']
    first_names = ['Ivan', 'Vitaliy', 'Evgeniy', 'Artem', 'Konstantin']
    middle_names = ['Viktorovich', 'Alekseevich', 'Ivanovich', 'Pavlovich', 'Aleksandrovich']
    for i in range(0, 50000):
        Employee.objects.create(
            last_name=last_names[randint(0, len(last_names) - 1)],
            first_name=first_names[randint(0, len(first_names) - 1)],
            middle_name=middle_names[randint(0, len(middle_names) - 1)],
            position=employee_positions[randint(0, len(employee_positions) - 1)],
            hire_date=date(2022, 1, 15),
            salary=randint(1000, 2000),
            department=departments[randint(0, len(departments) - 1)]
        )

class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20221030_0759'),
    ]

    operations = [
        migrations.RunPython(populate_tables),
    ]
