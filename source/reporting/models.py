from django.db import models


class Contest(models.Model):
    creation_date = models.DateField(editable=True, auto_now_add=True)
    event_date = models.DateField(editable=True,)
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
    title = models.CharField(max_length=100)
    students_name = models.CharField(max_length=100)
    other = models.TextField()
    teachers_name = models.CharField(max_length=100)
    stage = models.CharField(choices=STAGE_CHOICES, max_length=25)
    direction = models.CharField(choices=DIRECTION_CHOICES, max_length=25)
    subject = models.CharField(max_length=100)
    school_сlass = models.CharField(max_length=100)
    result = models.CharField(choices=RESULT_CHOICES, max_length=25)