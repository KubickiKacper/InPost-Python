from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('pc/', views.product_pc_list_view),
    path('pc/<int:code>', views.product_pc_view, name='pc'),
    path('pc_create/', views.pc_create_view, name='pc_create'),
    path('pc_csv/', views.pc_csv, name='pc_csv'),
    path('laptop/', views.product_laptop_list_view),
    path('laptop/<int:code>', views.product_laptop_view, name='laptop'),
    path('laptop_create/', views.laptop_create_view, name='laptop_create'),
    path('laptop_csv/', views.laptop_csv, name='laptop_csv'),
    path('printer_create/', views.printer_create_view, name='printer_create'),
    path('printer/<int:code>', views.product_printer_view, name='printer'),
    path('promos/', views.promo_list_view),
    path('promo_create/', views.promo_create_view, name='promo_create'),
    path('promo_csv/', views.promo_csv, name='promo_csv'),
    path('product_create_select/', views.product_create_select),
    path('type_check/<str:model_name>', views.type_check_route, name='type_check'),
    path('printer_code_check/<str:model_name>', views.printer_code_check_route, name='printer_code_check'),
]
