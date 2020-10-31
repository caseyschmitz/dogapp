from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'dogs'
urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('dogs/', views.DogList.as_view(), name='dog-list'),
    path('dogs/<int:pk>', views.DogDetail.as_view(), name='dog-detail'),
    path('breeds/', views.BreedList.as_view(), name='breed-list'),
    path('breeds/<int:pk>', views.BreedDetail.as_view(), name='breed-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)