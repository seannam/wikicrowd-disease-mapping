from django.urls import path

from .import views

urlpatterns = [
  path(r'', views.index, name='index'),
  path('diseases/', views.DiseaseListView.as_view(), name='diseases'),
  path('diseases/<int:pk>', views.DiseaseDetailView.as_view(), name='disease-detail'),
]
