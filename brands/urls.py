from django.urls import path

from brands.views import (
    BrandCreateView,
    BrandDeleteView,
    BrandDetailView,
    BrandListView,
    BrandUpdateView,
)

app_name = "brands"

urlpatterns = [
    path("", BrandListView.as_view(), name="list"),
    path("create/", BrandCreateView.as_view(), name="create"),
    path("<slug:slug>/detail/", BrandDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", BrandUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", BrandDeleteView.as_view(), name="delete"),
]
