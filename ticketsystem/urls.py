from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_view, name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('hall/', views.hall_index, name='hall_index'),
    path('hall/add/', views.create_hall, name='create_hall'),
    path('hall/<int:hall_id>/', views.get_hall, name='get_hall'),
    path('event/', views.event_index, name='event_index'),
    path('event/<int:event_id>/', views.get_event, name='get_event'),
    path('event/add/', views.create_event, name='create_event'),
    path('event/<int:event_id>/add/', views.create_day, name='create_day'),
    path('day/<int:day_id>/', views.get_day, name='get_day'),
    path('day/<int:day_id>/sell/', views.sell, name='sell'),
    path('day/<int:day_id>/cancel/', views.cancel, name='cancel'),
    path('day/<int:day_id>/cancel_count/', views.cancel_count, name='cancel_count'),
    path('day/<int:day_id>/reserve/', views.reserve, name='reserve'),
    path('day/<int:day_id>/dereserve/', views.dereserve, name='dereserve'),
    path('day/<int:day_id>/click/<int:ticket_id>/', views.reserve_toggle, name='reserve_toggle'),
    path('log/', views.log_index, name='log_index'),
    path('log/<int:day_id>/search/', views.lookup_log, name='lookup_log'),
    path('log/<int:day_id>/', views.get_log, name='get_log'),

]
