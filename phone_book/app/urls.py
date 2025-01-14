from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:pk>/edit/', views.edit_contact, name='edit_contact'),
    path('contact/<int:pk>/delete/', views.delete_contact, name='delete_contact'),
    path('contact/<int:pk>/call/', views.call_page, name='call_page'),
    path('add/', views.add_contact, name='add_contact'),
]
