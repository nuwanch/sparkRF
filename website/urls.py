from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<str:pk>', views.customer_record, name='record'),
    path('delete_record/<str:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('site_update/<str:site_alpha>', views.site_update, name='site_update'),
    path('update_record/<str:sitealpha>', views.update_record, name='update_record'),
    path('download/', views.download, name='download'),
    path('download_xl/<str:pk>', views.download_xl, name='download_xl'),
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
    path('common_booking_view', views.common_booking_view, name='common_booking_view'),
    path('reserve_alphacode', views.reserve_alphacode, name='reserve_alphacode'),
    path('test_pass', views.test_pass, name='test_pass'),
    path('work_request_list', views.work_request_list, name='work_request_list'),
    path('create_work_request', views.create_work_request, name='create_work_request'),
    path('request_record/<int:pk>', views.request_record, name='request_record'),
    path('site_configuration_form_step1', views.site_configuration_form_step1, name='site_configuration_form_step1'),
    path('site_configuration_form_step2', views.site_configuration_form_step2, name='site_configuration_form_step2')

    
]
