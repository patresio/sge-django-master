from django.urls import path

from products.views import (
    ProductCreateView,
    ProductDeleteView,
    ProductDetailView,
    ProductListView,
    ProductUpdateView,
)

app_name = "products"

urlpatterns = [
    path("", ProductListView.as_view(), name="list"),
    path("create/", ProductCreateView.as_view(), name="create"),
    path("<slug:slug>/detail/", ProductDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", ProductUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", ProductDeleteView.as_view(), name="delete"),
]
