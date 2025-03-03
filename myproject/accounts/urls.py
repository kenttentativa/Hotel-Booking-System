from django.urls import path, include
from . import views  # ✅ Correct way
from .views import view_bookings, add_booking

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms/', views.view_rooms, name='view_rooms'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('add_room/', views.add_room, name='add_room'),
    path('delete_room/<int:room_id>/', views.delete_room, name='delete_room'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("dashboard/", views.home, name="dashboard"),
    path('bookings/', views.view_bookings, name='view_bookings'),
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('bookings/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
]
