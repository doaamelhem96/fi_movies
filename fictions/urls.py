from django.urls import path
from .views import ListsViews, DetailsViews, CreatesViews, UpdatesViews, DeletesViews

urlpatterns = [
    path('', ListsViews.as_view(), name='listmovie'),
    path('<int:pk>/', DetailsViews.as_view(), name='fiction_detail'),
    path('create/', CreatesViews.as_view(), name='fiction_create'),
    path('<int:pk>/update/', UpdatesViews.as_view(), name='fiction_update'),
    path('<int:pk>/delete/', DeletesViews.as_view(), name='fiction_delete'),
]
