from django.urls import path

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('upload/<int:request_id>', views.UploadFileView.as_view(), name='upload'),
    path('client/<int:client_id>', views.ClientView.as_view(), name='client')
]