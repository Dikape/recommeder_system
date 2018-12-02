from django.contrib import admin
from django import forms
from .models import Material, MaterialTitleTranslate, \
    MaterialType, RedactorReview, Advertisement, UserComment


# @admin.register(MaterialTitleTranslate)
class MaterialTitleTranslateAdmin(admin.StackedInline):
    model = MaterialTitleTranslate
    extra = 0
    min_num = 0


# @admin.register(RedactorReview)
class RedactorReviewAdmin(admin.StackedInline):
    model = RedactorReview
    extra = 0
    min_num = 0

# @admin.register(Advertisement)
class AdvertisementAdmin(admin.StackedInline):
    model = Advertisement
    extra = 0
    min_num = 0

class MaterialForm(forms.ModelForm):
  class Meta:
    model = Material
    widgets = {
      'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
    }
    fields = '__all__'


class MaterialTypeForm(forms.ModelForm):
  class Meta:
    model = Material
    widgets = {
      'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
    }
    fields = '__all__'


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    form = MaterialForm
    inlines = [MaterialTitleTranslateAdmin, RedactorReviewAdmin, AdvertisementAdmin]


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    form = MaterialTypeForm


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    pass
