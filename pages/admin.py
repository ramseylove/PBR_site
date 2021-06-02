from django.contrib import admin

from .models import Resume, Skills, SkillsTag, WorkExperience, Education, Portfolio


class SkillsAdmin(admin.StackedInline):
    model = Skills
    filter_horizontal = ('tag',)
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


class PortfolioAdmin(admin.StackedInline):
    model = Portfolio
    verbose_name_plural = 'Portfolio'
    fk_name = 'resume'
    extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = (SkillsAdmin, WorkExperienceAdmin, EducationAdmin, PortfolioAdmin)
    model = Resume

    list_display = ('get_name', 'created_at', 'modified_at')

    def get_name(self, obj):
        return obj.user.userprofile.name
    get_name.short_description = 'Resume'
    get_name.admin_order_field = 'get_name'


class SkillsTagAdmin(admin.ModelAdmin):
    model = SkillsTag
    verbose_name_plural = 'Skill Tags'


admin.site.register(SkillsTag, SkillsTagAdmin)
admin.site.register(Resume, ResumeAdmin)
