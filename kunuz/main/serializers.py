from rest_framework import serializers
from .models import Categories, Articles


class BaseModelSerializer(serializers.Serializer):
    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CategorySerializer(BaseModelSerializer):
    title = serializers.CharField()
    link = serializers.CharField()

    class Meta:
        model = Categories


class ArticlesSerializer(BaseModelSerializer):
    title = serializers.CharField()
    description = serializers.CharField()
    categories = serializers.CharField()

    class Meta:
        model = Articles
