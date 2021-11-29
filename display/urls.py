from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [

    path('tv1',views.tv1),

    path('tv2',views.tv2),

    path('tv2_1',views.tv2_1),

    path('tv2_2',views.tv2_2),



]