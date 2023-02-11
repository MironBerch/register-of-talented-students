from django.db import models


class StudentsBase(models.Model):
    file = models.FileField(upload_to='students/')


class Class(models.Model):
    school_class = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.school_class


class Student(models.Model):
    full_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='student full name',
    )
    school_сlass = models.ForeignKey(
        Class,
        on_delete=models.PROTECT,
    )
    is_learns = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name