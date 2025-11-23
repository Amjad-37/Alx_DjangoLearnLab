from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Author, Library, Librarian, UserProfile

# إعدادات الـ Admin لليوزر الجديد
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # إضافة الحقول الجديدة للعرض في الفورم
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    # إضافة الحقول الجديدة عند إنشاء يوزر
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# تسجيل الموديلات
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
