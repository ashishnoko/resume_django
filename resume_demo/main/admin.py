from pickle import READONLY_BUFFER
from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user')


admin.site.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp','user')

admin.site.register(Testimonial)
class Testimonial(admin.ModelAdmin):
    list_display = ('id','name','is_active')

admin.site.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)


admin.site.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id','name')

admin.site.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','name','score')


