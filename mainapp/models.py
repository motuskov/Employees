from django.db import models

class EmployeePosition(models.Model):
    '''
    The EmployeePosition object represents a position that an
    employee can hold in a company.

    Attributes:
        title (models.CharField): Title of an employee position
    '''
    title = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.title

class Department(models.Model):
    '''
    The Department object represents a department of a compony.

    Attributes:
        name (models.CharField): Name of a department
        parent_department (models.ForeignKey): Superior department (if exists)
    '''
    name = models.CharField(
        max_length=100
    )
    parent_department = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child_departments'
    )

    def __str__(self):
        return self.name

class Employee(models.Model):
    '''
    The Employee objects represent an employee of a company.

    Attributes:
        last_name (models.CharField): Last name of the employee
        first_name (models.CharField): First name of the employee
        middle_name (models.CharField): Middle name of the employee
        position (models.ForeignKey): Employee position in a company
        hire_date (models.DateField): Date the employee was hired
        salary (models.DecimalField): Employee's salary
        department (models.ForeignKey): Department where the employee works
    '''
    last_name = models.CharField(
        max_length=30
    )
    first_name = models.CharField(
        max_length=30
    )
    middle_name = models.CharField(
        max_length=30,
        blank=True
    )
    position = models.ForeignKey(
        EmployeePosition,
        on_delete=models.CASCADE,
        related_name='employees'
    )
    hire_date = models.DateField()
    salary = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='employees'
    )

    class Meta:
        indexes = [
            models.Index(fields=[
                'last_name',
                'first_name',
                'middle_name'
            ])
        ]

    def __str__(self):
        if self.middle_name:
            return f'{self.last_name} {self.first_name} {self.middle_name}'
        else:
            return f'{self.last_name} {self.first_name}'
