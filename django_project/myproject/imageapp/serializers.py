
from rest_framework import serializers


from .models import SwiperContent

class SwiperContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwiperContent
        fields = '__all__'