from django.urls import path

from outflows.views import OutflowCreateView, OutflowDetailView, OutflowListView

app_name = "outflows"

urlpatterns = [
    path("", OutflowListView.as_view(), name="list"),
    path("create/", OutflowCreateView.as_view(), name="create"),
    path("<slug:slug>/detail/", OutflowDetailView.as_view(), name="detail"),
]
