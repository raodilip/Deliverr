from rest_framework import serializers
from Catalog.models import Item

COLOR_CHOICES = [
    ("RED", "RED"),
    ("BLUE", "BLUE"),
]

class ItemSerializer(serializers.Serializer):
    
    product_id = serializers.IntegerField(read_only=True)
    sku = serializers.CharField(required=True, allow_blank=False, max_length=200)
    title = serializers.CharField(required=True, allow_blank=False, max_length=100)
    isDigital = serializers.BooleanField()
    color = serializers.CharField(required=True, allow_blank=False,max_length=50)


    def create(self, validated_data):
        """
        Create and return a new `Item` instance, given the validated data.
        """
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Item` instance, given the validated data.
        """
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.sku = validated_data.get('sku', instance.sku)
        instance.title = validated_data.get('title', instance.title)
        instance.isDigital = validated_data.get('isDigital', instance.isDigital)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance