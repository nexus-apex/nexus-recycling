from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/create/', views.collection_create, name='collection_create'),
    path('collections/<int:pk>/edit/', views.collection_edit, name='collection_edit'),
    path('collections/<int:pk>/delete/', views.collection_delete, name='collection_delete'),
    path('recyclematerials/', views.recyclematerial_list, name='recyclematerial_list'),
    path('recyclematerials/create/', views.recyclematerial_create, name='recyclematerial_create'),
    path('recyclematerials/<int:pk>/edit/', views.recyclematerial_edit, name='recyclematerial_edit'),
    path('recyclematerials/<int:pk>/delete/', views.recyclematerial_delete, name='recyclematerial_delete'),
    path('collectionroutes/', views.collectionroute_list, name='collectionroute_list'),
    path('collectionroutes/create/', views.collectionroute_create, name='collectionroute_create'),
    path('collectionroutes/<int:pk>/edit/', views.collectionroute_edit, name='collectionroute_edit'),
    path('collectionroutes/<int:pk>/delete/', views.collectionroute_delete, name='collectionroute_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
