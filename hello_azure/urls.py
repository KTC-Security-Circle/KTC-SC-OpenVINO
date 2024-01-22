from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('obj_demo', views.obj_demo, name='obj_demo'),
    path('obj_result', views.obj_result, name='obj_result'),
    path('seg_demo', views.seg_demo, name='seg_demo'),
    path('seg_result', views.seg_result, name='seg_result'),
]
    