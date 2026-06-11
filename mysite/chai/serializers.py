from rest_framework import serializers
from .models import ChaiReview, ChaiVariety


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = ChaiReview
        fields = '__all__'

class ChaiSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = ChaiVariety
        fields = '__all__'
        extra_kwargs = {
            'image': {'required': False}
        }