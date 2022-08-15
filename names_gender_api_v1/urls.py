from django.urls import path,include

from .views import NamesListView,NamesDetailView
urlpatterns = [
    path('',NamesListView.as_view(), name='names'),
    path('<int:pk>/',NamesDetailView.as_view(), name='names_detail'),
    path('api-auth/', include('rest_framework.urls')),
]