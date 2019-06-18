from django.urls import path

from mdb.api.viewsets import ExampleViewset

urlpatterns = [
    path('movie/', ExampleViewset.as_view({'get': 'list', 'post': 'create'}), name='movie-list-actions'),
    path('movie/<int:pk>/',
         ExampleViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'}),
         name='movie-detail-actions'),
]