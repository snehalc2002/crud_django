from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'instructor', 'credits')
    search_fields = ('title', 'instructor')
    list_filter=('credits',)