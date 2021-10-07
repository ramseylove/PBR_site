from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminMixin

from .models import Resume, Skills, SkillsTag, WorkExperience, Education, Portfolio, PortfolioImages, Feature


class SkillsAdmin(admin.TabularInline):
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


class PortfolioImagesAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = PortfolioImages
    verbose_name_plural = 'Images'
    fk_name = 'portfolio'
    extra = 0


class FeatureAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = Feature
    verbose_name_plural = 'Features'
    fk_name = 'portfolio'
    extra = 0


class PortfolioAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (FeatureAdmin, PortfolioImagesAdmin,)
    model = Portfolio
    verbose_name_plural = 'Portfolio'
    fk_name = 'resume'
    list_display = ('title', 'resume')
    # extra = 0


class ResumeAdmin(admin.ModelAdmin):
    inlines = (SkillsAdmin, WorkExperienceAdmin, EducationAdmin)
    model = Resume

    list_display = ('get_name', 'created_at', 'modified_at')

    def get_name(self, obj):
        return obj.user.userprofile.name
    get_name.short_description = 'Resume'
    get_name.admin_order_field = 'get_name'


class SkillsTagAdmin(SortableAdminMixin, admin.ModelAdmin):
    model = SkillsTag
    verbose_name_plural = 'Skill Tags'


admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(SkillsTag, SkillsTagAdmin)
admin.site.register(Resume, ResumeAdmin)
