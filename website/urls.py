from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('download/', views.download, name='download'),
    path('download_xl/<int:pk>', views.download_xl, name='download_xl'),
    path('add_phy_info', views.add_phy_info, name='add_phy_info'),
    path('reserve_alphacode', views.reserve_alphacode, name='reserve_alphacode'),
    path('view_siteinfo', views.view_siteinfo, name='view_siteinfo'),
    path('create_rfreport', views.create_rfreport, name='create_rfreport'),
    path('create_tnet', views.create_tnet, name='create_tnet'),
    path('create_celldata', views.create_celldata, name='create_celldata'),
    path('book_resource', views.book_resource, name='book_resource'),
    path('view_bookings', views.view_bookings, name='view_bookings'),
    path('booking_record/<int:pk>', views.booking_record, name='booking_record'),
    path('update_booking/<int:pk>', views.update_booking, name='update_booking'),
    path('delete_booking/<int:pk>', views.delete_booking, name='delete_booking'),
    

    
   
   
]
