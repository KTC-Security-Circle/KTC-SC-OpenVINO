from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import IndexView , obj_result
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('seg_result/', views.seg_result, name='seg_result'),
    path('seg_demo/', views.seg_demo, name='seg_demo'),
    path('obj_demo/', IndexView.as_view(), name='obj_demo'),
    path('obj-result/', obj_result, name='obj_result'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
