from django.db import models


class StudentsBase(models.Model):
    """Students excel table"""
    file = models.FileField(upload_to='students/')

    class Meta:
        verbose_name = 'Список учащихся'
        verbose_name_plural = "Списки учащихся"


class Class(models.Model):
    school_class = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Школьный класс',
    )

    def __str__(self):
        return self.school_class

    class Meta:
        verbose_name = 'Школьный класс'
        verbose_name_plural = 'Школьные классы'


class Student(models.Model):
    full_name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='ФИО ученика',
    )
    school_сlass = models.ForeignKey(
        Class,
        on_delete=models.PROTECT,
        related_name='school_сlass',
        verbose_name='Школьный класс',
    )
    is_learns = models.BooleanField(
        default=True,
        verbose_name='Проходит обучение',
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'