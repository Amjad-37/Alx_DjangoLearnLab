from django.contrib import admin
from .models import Book

# بنعمل كلاس عشان نتحكم في شكل الموديل في صفحة الأدمن
class BookAdmin(admin.ModelAdmin):
    # الحقول اللي هتظهر في القايمة
    list_display = ('title', 'author', 'publication_year')

    # فلاتر هتظهر في الجنب
    list_filter = ('publication_year', 'author')

    # عشان يضيف خانة بحث (هيبحث في العنوان والمؤلف)
    search_fields = ('title', 'author')

# هنا بنسجل الموديل بتاعنا (Book) مع الكلاس اللي عملناه (BookAdmin)
admin.site.register(Book, BookAdmin)
