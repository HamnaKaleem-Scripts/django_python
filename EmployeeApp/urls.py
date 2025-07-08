from EmployeeApp import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department$', views.departmentapi),
    url(r'^department/([0-9]+)$', views.departmentapi),

    url(r'^employee$', views.employeesapi),
    url(r'^employee/([0-9]+)$', views.employeesapi),

    url(r'^employee/savefile$', views.savefile),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)