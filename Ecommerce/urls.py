from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name="home"),
    path("<int:pk>/", product_detail_page, name="detail")
]