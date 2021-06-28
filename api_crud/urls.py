
from django.contrib import admin
from django.urls import include, path


# urls
urlpatterns = [
    path('emp', include('employee.urls')),
    path('admin/', admin.site.urls),
]