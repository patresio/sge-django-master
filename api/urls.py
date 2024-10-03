from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from api.views import BrandCreateListAPIView, BrandRetrieveUpdateDestroyAPIView

app_name = "api"

urlpatterns = [
    ### VERSION 1 API
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("v1/token/verify", TokenVerifyView.as_view(), name="token_verify"),
    ### Brands
    path(
        "v1/brands/",
        BrandCreateListAPIView.as_view(),
        name="brand-create-list-api-view",
    ),
    path(
        "v1/brands/<int:pk>/",
        BrandRetrieveUpdateDestroyAPIView.as_view(),
        name="brand-detail-api-view",
    ),
]
