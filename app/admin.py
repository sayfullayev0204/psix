from django.contrib import admin
from .models import Guide,Music,Test, Video,Books

admin.site.register(Guide)
admin.site.register(Music)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    pass