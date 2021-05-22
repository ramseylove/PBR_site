from django.contrib import admin

from .models import Resume, Skills, WorkExperience, Education


class SkillsAdmin(admin.StackedInline):
    model = Skills
    verbose_name_plural = 'Skills'
    fk_name = 'resume'
    extra = 0


class WorkExperienceAdmin(admin.StackedInline):
    model = WorkExperience
    verbose_name_plural = 'Work Experience'
    fk_name = 'resume'
    extra = 0


class EducationAdmin(admin.StackedInline):
    model = Education
    verbose_name_plural = 'Education'
    fk_name = 'resume'
    extra = 0

class ResumeAdmin(admin.ModelAdmin):
    inlines = (SkillsAdmin, WorkExperienceAdmin, EducationAdmin)

    model = Resume


admin.site.register(Resume, ResumeAdmin)