from django.urls import path
from base import views


urlpatterns=[

    path('test/', views.webscrap.as_view(), name='test'),
]