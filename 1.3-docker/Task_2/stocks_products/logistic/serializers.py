from rest_framework import serializers
from .models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = "product", "quantity", "price"


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = "address", "positions"

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = Stock.objects.create(**validated_data)
        for position in positions:
            product = position.pop("product")
            StockProduct.objects.create(stock=stock, product=product, **position)
        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop("positions")

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)
        for position in positions:
            product = position.pop("product")
            StockProduct.objects.update_or_create(
                stock=instance,
                product=product,
                defaults={
                    "quantity": position.get("quantity"),
                    "price": position.get("price"),
                },
            )
        return stock
