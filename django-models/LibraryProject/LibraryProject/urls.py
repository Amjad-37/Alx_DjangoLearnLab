from django.contrib import admin
from django.urls import path, include  # <-- اتأكد إن include موجودة

urlpatterns = [
    path('admin/', admin.site.urls),

    # <-- السطر ده بيوصل كل حاجة
    path('', include('relationship_app.urls')),
]
