from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),   # 👈 VERY IMPORTANT
    path('workouts/', include('workouts.urls')),
]
