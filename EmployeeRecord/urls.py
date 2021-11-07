from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from employee.views import signup
from employee.views import index
from employee.views import login
from employee.views import employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login', login, name="login"),
    path('signup', signup, name="signup"),
    path('employee', employee, name="employee"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
