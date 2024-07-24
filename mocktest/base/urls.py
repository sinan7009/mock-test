from django.urls import path
from . import views

urlpatterns = [
    path('', views.base , name="base"),
    path('create_question/',views.create_question , name= "create_question"),
    path('mocktext/<uuid:pk>/<str:name>',views.exam,name="exam"),
    path('modules/', views.modules,name="modules"),
    path('login/', views.login, name='login'),
    path('exam/complete/', views.exam_complete, name='exam_complete'),


]