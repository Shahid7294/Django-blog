from django.contrib import admin
from .models import About,SocialLink

# Register your models here.
class AboutBlog(admin.ModelAdmin):
    def has_add_permission(self, request):
        about=About.objects.all().count()
        if about != 0:
            return False
        return True

    list_display=('about_heading','about_description','updated_at')
admin.site.register(About,AboutBlog)
admin.site.register(SocialLink)