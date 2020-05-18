from rest_framework import serializers
from .models import Product, News


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('id', 'name', 'details', 'cost', 'discount', 'discount_type', 'percent')
        # fields = '__all__'
        read_only_fields = ['id']
        exclude = ['created_at']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        exclude = ['arrival_date']