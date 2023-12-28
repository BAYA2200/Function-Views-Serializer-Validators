from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def validate(self, data):
        if "!@#$%^&*" in data["name"]:
            raise ValidationError('You cannot use special characters')
        return data


class ItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ['id', 'name', 'price', 'qr', 'category_id']

    def validate(self, data):
        print(data)
        a = "{}C{}P{}I".format(data['category_id'], data['price'], data['id'])
        print(a)
        if data['qr'] != "{}C{}P{}I".format(data['category_id'].id, data['price'], data['id']):
            raise serializers.ValidationError("QR код не соответствует стандартам")

        return data
