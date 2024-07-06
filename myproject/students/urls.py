from django.urls import path
from . import views
urlpatterns = [
    path('create-student/',views.StudentAPIView.as_view()),
    path('create-student/<int:pk>/',views.StudentAPIView.as_view()),

    path('standard-api/',views.StandardAPIView.as_view()),
    path('standard-api/<int:pk>/',views.StandardAPIView.as_view()),

]
