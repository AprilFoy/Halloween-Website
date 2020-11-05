from django.urls import path
from . import views

urlpatterns = [
    path("", views.storefront_index, name="storefront_index"),
    path("index/", views.index_page, name="index_page"),
    path("<int:pk>/", views.storefront_detail, name="storefront_detail"),
    path("<category>/", views.storefront_category, name="storefront_category"),
]
