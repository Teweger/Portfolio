from django.urls import path
from pages import views

urlpatterns = [
    path('download_pdf/<str:p>/', views.download_pdf, name="download_pdf"),
    path("", views.home, name='home'),
]
