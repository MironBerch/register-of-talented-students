from django.db import models

from users.models import User
from students.models import Student


class Contest(models.Model):
    SUBJECT_CHOICES = (
        ('Русский язык', 'Русский язык'),
        ('Литературное чтение', 'Литературное чтение'),
        ('Математика', 'Математика'),
        ('Окружающий мир', 'Окружающий мир'),
        ('Музыка', 'Музыка'),
        ('ИЗО', 'ИЗО'),
        ('Технология', 'Технология'),
        ('Физическая культура', 'Физическая культура'),
        ('Английский язык', 'Английский язык'),
        ('ОРКСЭ', 'ОРКСЭ'),
        ('Литература', 'Литература'),
        ('История', 'История'),
        ('Обществознание', 'Обществознание'),
        ('География', 'География'),
        ('Биология', 'Биология'),
        ('ОБЖ', 'ОБЖ'),
        ('Экономика', 'Экономика'),
        ('Технология', 'Технология'),
        ('Химия', 'Химия'),
        ('Физика', 'Физика'),
        ('Информатика', 'Информатика'),
        ('Проектная деятельность', 'Проектная деятельность'),
    )
    STAGE_CHOICES = (
        ('Школьный', 'Школьный'),
        ('Районный', 'Районный'),
        ('Городской', 'Городской'),
        ('Региональный', 'Региональный'),
        ('Всероссийский', 'Всероссийский'),
        ('Международный', 'Международный'),
    )
    DIRECTION_CHOICES = (
        ('Спорт', 'Спорт'),
        ('Образование', 'Образование'),
        ('Исскуство', 'Исскуство'),
        ('Культура', 'Культура'),
        ('Социальное', 'Социальное'),
        ('Олимпиада', 'Олимпиада'),
    )
    RESULT_CHOICES = (
        ('1 место', '1 место'),
        ('2 место', '2 место'),
        ('3 место', '3 место'),
        ('Призёр', 'Призёр'),
        ('Победитель', 'Победитель'),
        ('Лауреат', 'Лауреат'),
        ('Участник', 'Участник'),
        ('Дипломат', 'Дипломат'),
    )
    contest_creater = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    event_date = models.DateField(editable=True,)
    title = models.CharField(max_length=100)
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    other = models.TextField(
        blank=True,
        null=True,
        verbose_name='teacher comment',
    )
    teachers_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    stage = models.CharField(
        choices=STAGE_CHOICES,
        max_length=25,
    )
    direction = models.CharField(
        choices=DIRECTION_CHOICES,
        max_length=25,
    )
    subject = models.CharField(
        choices=SUBJECT_CHOICES,
        max_length=25,
    )
    scan_diploma = models.FileField(
        upload_to='diplom_scans/',
        null=True,
        blank=True,
    )
    result = models.CharField(
        choices=RESULT_CHOICES,
        max_length=25,
    )