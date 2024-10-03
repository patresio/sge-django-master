from rest_framework.serializers import ModelSerializer

from brands.models import Brand
from categories.models import Category
from inflows.models import Inflow
from outflows.models import Outflow
from products.models import Product
from suppliers.models import Supplier


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class InflowSerializer(ModelSerializer):
    class Meta:
        model = Inflow
        fields = "__all__"


class OutflowSerializer(ModelSerializer):
    class Meta:
        model = Outflow
        fields = "__all__"
