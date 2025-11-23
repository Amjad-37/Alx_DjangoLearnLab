from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# إعداد الـ Router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # الرابط القديم بتاع التاسك اللي فات
    path('books/', BookList.as_view(), name='book-list'),

    # إضافة روابط الـ Router الجديدة (CRUD كامل)
    path('', include(router.urls)),
]
