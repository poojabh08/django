from django.contrib import admin

# Register your models here.
from home.models import Student,library,Section,Teacher,books
'''admin.site.register(Student)
admin.site.register(library)
admin.site.register(Section)
admin.site.register(Teacher)
admin.site.register(books)'''
@admin.register(books)
class booksAdmin(admin.ModelAdmin):
    pass
 
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('student_name','department','teacher')
    list_filter=('student_name','department','timestamp')
    fields=('student_name','department')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(library)
class libraryAdmin(admin.ModelAdmin):
    pass
