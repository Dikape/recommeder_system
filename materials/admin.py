from django.contrib import admin
from .models import Material, MaterialTitleTranslate, \
    MaterialType, RedactorReview, Advertisement, UserComment


# @admin.register(MaterialTitleTranslate)
class MaterialTitleTranslateAdmin(admin.StackedInline):
    model = MaterialTitleTranslate


# @admin.register(RedactorReview)
class RedactorReviewAdmin(admin.StackedInline):
    model = RedactorReview


# @admin.register(Advertisement)
class AdvertisementAdmin(admin.StackedInline):
    model = Advertisement


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    inlines = [MaterialTitleTranslateAdmin, RedactorReviewAdmin, AdvertisementAdmin]


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(UserComment)
class UserCommentAdmin(admin.ModelAdmin):
    pass
