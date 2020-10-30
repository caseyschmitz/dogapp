from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'dogs'
urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.DogList.as_view(), name='doglist'),
    path('dogs/', views.DogList.as_view(), name='doglist'),
    path('dogs/<int:pk>/', views.DogDetail.as_view(), name='dogdetail'),
    path('breeds/', views.BreedList.as_view(), name='breedlist'),
    path('breeds/<int:pk>/', views.BreedDetail.as_view(), name='breeddetail')
]

urlpatterns = format_suffix_patterns(urlpatterns)