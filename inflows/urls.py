from django.urls import path

from inflows.views import InflowCreateView, InflowDetailView, InflowListView

app_name = "inflows"

urlpatterns = [
    path("", InflowListView.as_view(), name="list"),
    path("create/", InflowCreateView.as_view(), name="create"),
    path("<slug:slug>/detail/", InflowDetailView.as_view(), name="detail"),
]
