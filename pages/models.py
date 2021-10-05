from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from ckeditor.fields import RichTextField


from django.contrib.auth import get_user_model


class Resume(models.Model):
    headline = models.CharField(verbose_name='Headline', max_length=120)
    about = RichTextField(verbose_name='About Me', blank=True)
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
    tag = models.ManyToManyField(to=SkillsTag, related_name='tags')

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
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)
    current = models.BooleanField(verbose_name='Currently employed', default=False)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='work')

    def __str__(self):
        return self.employer

    class Meta(object):
        ordering = ['-end_date']


class Education(models.Model):
    course = models.CharField(max_length=100, verbose_name='Degree/Certificate')
    institute = models.CharField(max_length=100, verbose_name='Place of study')
    description = RichTextField(verbose_name='Course description', blank=True)
    start_date = models.DateField(verbose_name='Start Date')
    end_date = models.DateField(verbose_name='End Date', null=True, blank=True)
    current = models.BooleanField(verbose_name='Currently enrolled', default=False)
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='education')

    def __str__(self):
        return self.course


class Portfolio(models.Model):
    title = models.CharField(max_length=100, verbose_name='Project Titles')
    description = RichTextField(verbose_name='Portfolio Description', blank=True)
    topic = models.CharField(max_length=100, verbose_name='Topics')
    resume = models.ForeignKey(Resume, null=True, blank=True, on_delete=models.CASCADE, related_name='portfolio')
    portfolio_pic = models.ImageField(verbose_name='Portfolio Picture', null=True, upload_to='portfolio_pics/')
    tag = models.ManyToManyField(to=SkillsTag, related_name='skilltags')
    problem = RichTextField(verbose_name='The Problem', blank=True)
    solution = RichTextField(verbose_name='The Solution', blank=True)
    repo_url = models.URLField(verbose_name="Repository Url", blank=True, null=True)

    def __str__(self):
        return self.title

    def get_topics(self):
        top = self.topic.split(',')
        return ' / '.join(top)


class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(verbose_name='Feature')
    portfolio = models.ForeignKey(to=Portfolio, related_name='features', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return self.title


class PortfolioImages(models.Model):
    alt = models.CharField(max_length=50, verbose_name='Alt Description')
    portfolio_image = models.ImageField(upload_to='portfolio_pics/')
    portfolio = models.ForeignKey(to=Portfolio, related_name='images', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ['order']

    def __str__(self):
        return self.alt
