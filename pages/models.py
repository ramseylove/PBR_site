from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.contrib.auth import get_user_model


class Resume(models.Model):
    about = models.TextField(verbose_name='About Me')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)


class Skills(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                help_text='Enter percentage represented as whole numbers 0 to 100')
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE)


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    employer = models.CharField(max_length=100, verbose_name='Employer')
    description = models.TextField(verbose_name='Job Description')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date', null=True)
    current = models.BooleanField(verbose_name='Currently employed', default=0)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE)


class Education(models.Model):
    course = models.CharField(max_length=100, verbose_name='Course/Degree/Certificates')
    institute = models.CharField(max_length=100, verbose_name='Place of study')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateTimeField(verbose_name='End Date', null=True)
    current = models.BooleanField(verbose_name='Currently enrolled', default=0)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE)

