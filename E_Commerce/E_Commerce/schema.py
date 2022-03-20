import graphene
from graphene_django import DjangoObjectType

from CRM.models import *

class ShopType(DjangoObjectType):
    class Meta:
        model = Shop
        fields = ("id", "shop_name", "shop_description", "shop_rating", "user_id")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "product_name", "product_type", "product_description", "product_price", "shop_id")

class Query(graphene.ObjectType):
    all_shop = graphene.List(ShopType)
    product_by_name = graphene.Field(ProductType, name=graphene.String(required=True))

    def resolve_all_shop(root, info):
        # We can easily optimize query count in the resolve method
        return Shop.objects.all()

    def resolve_product_by_name(root, info, name):
        try:
            return Product.objects.get(product_name=name)
        except Product.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)