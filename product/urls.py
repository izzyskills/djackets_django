from django.urls import path
from . import views

urlpatterns = [
    path("latest-products/", views.LatestProductList.as_view()),
    path("products/search/", views.search),
    path(
        "products/<slug:category_slug>/<slug:product_slug>/",
        views.ProductDetail.as_view(),
    ),
    path("products/<slug:category_slug>/", views.CategoryDetail.as_view()),
]
