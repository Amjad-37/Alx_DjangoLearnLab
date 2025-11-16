from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # السطر ده هو اللي ناقص عندك
    # هو ده اللي بيربط المشروع بالـ app
    path('', include('relationship_app.urls')),
]
