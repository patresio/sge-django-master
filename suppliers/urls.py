from django.urls import path

from suppliers.views import (
    SupplierCreateView,
    SupplierDeleteView,
    SupplierDetailView,
    SupplierListView,
    SupplierUpdateView,
)

app_name = "suppliers"

urlpatterns = [
    path("", SupplierListView.as_view(), name="list"),
    path("create/", SupplierCreateView.as_view(), name="create"),
    path("<slug:slug>/detail/", SupplierDetailView.as_view(), name="detail"),
    path("<slug:slug>/update/", SupplierUpdateView.as_view(), name="update"),
    path("<slug:slug>/delete/", SupplierDeleteView.as_view(), name="delete"),
]
