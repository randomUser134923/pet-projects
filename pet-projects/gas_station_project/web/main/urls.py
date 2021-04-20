from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduction', views.introductionview, name='introduction'),
    path('faq',views.faqview , name='faq'),
    path('product',views.productview, name='product'),
    
]