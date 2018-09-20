from django.db import models

# Create your models here.


class Lecturer(models.Model):
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Feedback(models.Model):

    SATISFACTION = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    AUDIBILTY = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    SUBJECT_CLARITY = (
        ('EXCELLENT', 'EXCELLENT'),
        ('GOOD', 'GOOD'),
        ('BAD', 'BAD'),
        ('WORST', 'WORST')
    )
    ANY_PARTIALITY = (
        ('NO PARTIALITY', 'NO PARTIALITY'),
        ('SOMETIMES', 'SOMETIMES'),
        ('ALL THE TIME', 'ALL THE TIME')
    )
    HOMEWORK = (
        ('NO HOMEWORKS', 'NO HOMEWORKS'),
        ('SOMETIMES', 'SOMETIMES'),
        ('REGULARLY', 'REGULARLY')
    )
    PUNCTUALITY = (
        ('NEVER LATE', 'NEVER LATE'),
        ('OCCASIONALLY LATE', 'OCCASIONALLY LATE'),
        ('ALWAYS LATE', 'ALWAYS LATE')
    )
    ANOTHER_CLASS = (
        ('YES', 'YES'),
        ('NO', 'NO')
    )
    satisfied = models.CharField(choices=SATISFACTION, max_length=200)
    audibility = models.CharField(choices=AUDIBILTY, max_length=200)
    clarity = models.CharField(choices=SUBJECT_CLARITY, max_length=200)
    partiality = models.CharField(choices=ANY_PARTIALITY, max_length=200)
    homework = models.CharField(choices=HOMEWORK, max_length=200)
    punctuality = models.CharField(choices=PUNCTUALITY, max_length=200)
    another_class = models.CharField(choices=ANOTHER_CLASS, max_length=200)
    lecturer = models.ForeignKey(
        Lecturer, on_delete=models.CASCADE, default='')
