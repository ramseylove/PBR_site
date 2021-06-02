from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ckeditor.fields import RichTextField

from django.contrib.auth import get_user_model


class Resume(models.Model):
    headline = models.CharField(verbose_name='Headline', max_length=120)
    about = RichTextField(verbose_name='About Me')
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='Modified At', null=True, blank=True)

    def __str__(self):
        return self.user.userprofile.name


class SkillsTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Skills(models.Model):
    name = models.CharField(max_length=50)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                help_text='Enter percentage represented as whole numbers 0 to 100')
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='skills')
    tag = models.ManyToManyField(to=SkillsTag, related_name='tag')

    def get_level(self):
        if self.level <= 50:
            return "Novice"
        elif self.level <= 65:
            return "Advanced"
        elif self.level <= 85:
            return "Expert"
        else:
            return "Master"

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, verbose_name='Job Title')
    employer = models.CharField(max_length=100, verbose_name='Employer')
    description = RichTextField(verbose_name='Job Description')
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date', null=True)
    current = models.BooleanField(verbose_name='Currently employed', default=False)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='workexperiences')

    def __str__(self):
        return self.employer


class Education(models.Model):
    course = models.CharField(max_length=100, verbose_name='Degree/Certificates')
    institute = models.CharField(max_length=100, verbose_name='Place of study')
    description = RichTextField(verbose_name='Course description', blank=True, null=True)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date', null=True)
    current = models.BooleanField(verbose_name='Currently enrolled', default=False)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='education')

    def __str__(self):
        return self.institute


class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Project Titles')
    description = RichTextField(verbose_name='Portfolio Description', blank=True, null=True)
    topic = models.CharField(max_length=100, verbose_name='Topics')
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='portfolio')
    portfolio_pic = models.ImageField(verbose_name='Portfolio Picture', null=True, upload_to='portfolio_pics/')

    def __str__(self):
        return self.title

    def get_topics(self):
        top = self.topic.split(',')
        return ' / '.join(top)


