from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from api.serializers import (
    BrandSerializer,
    CategorySerializer,
    InflowSerializer,
    OutflowSerializer,
    ProductSerializer,
    SupplierSerializer,
)
from brands.models import Brand
from categories.models import Category
from inflows.models import Inflow
from outflows.models import Outflow
from products.models import Product
from suppliers.models import Supplier


class BrandCreateListAPIView(ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryCreateListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class InflowCreateListAPIView(ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class InflowRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer


class OutflowCreateListAPIView(ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer


class OutflowRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer


class ProductCreateListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SupplierCreateListAPIView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
