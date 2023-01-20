from django.db import models
from users.models import User 


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
    contest_creater = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    event_date = models.DateField(editable=True,)
    title = models.CharField(max_length=100)
    students_name = models.CharField(max_length=100)
    other = models.TextField(blank=True, null=True)
    teachers_name = models.CharField(max_length=100, blank=True, null=True)
    stage = models.CharField(choices=STAGE_CHOICES, max_length=25)
    direction = models.CharField(choices=DIRECTION_CHOICES, max_length=25)
    subject = models.CharField(choices=SUBJECT_CHOICES, max_length=25)
    school_parallel = models.CharField(choices=PARALLEL_CHOICES, max_length=2)
    school_сlass = models.CharField(choices=CLASS_CHOICES, max_length=2)
    result = models.CharField(choices=RESULT_CHOICES, max_length=25)