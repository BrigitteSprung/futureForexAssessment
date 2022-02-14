from django.urls import path
from django.conf.urls.static import static

from futureForexAssessment import settings

from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('upload/<int:request_id>', views.UploadFileView.as_view(), name='upload'),
    path('client/<int:client_id>', views.ClientView.as_view(), name='client'),
    path('clients/', views.ClientsView.as_view(), name='clients'),
    path('request/<int:client_id>', views.RequestView.as_view(), name='request'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
