from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('asis-list/', views.asisList, name="asis-list"),
    path('asis-list-date/', views.asisListDate, name="asis-list-date"),
    path('asis-detail/<int:pk>/', views.asisDetail, name="asis-Detail"),
    path('asis-create/', views.asisCreate, name="asis-Create"),
]