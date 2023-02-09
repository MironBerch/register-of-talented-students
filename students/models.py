from django.db import models


class StudentsBase(models.Model):
    file = models.FileField(upload_to='students/')


class Student(models.Model):
    PARALLEL_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
    )
    CLASS_CHOICES = (
        ('а', 'а'),
        ('б', 'б'),
        ('в', 'в'),
    )
    full_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='student full name',
    )
    school_parallel = models.CharField(
        choices=PARALLEL_CHOICES,
        max_length=2,
        verbose_name='school parallel',
    )
    school_сlass = models.CharField(
        choices=CLASS_CHOICES,
        max_length=2,
        verbose_name='school сlass',
    )

    def __str__(self):
        return self.full_name