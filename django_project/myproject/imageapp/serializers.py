
from rest_framework import serializers


from .models import ImageContent,AudioContent

class ImageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageContent
        fields = '__all__'



class AudioContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioContent
        fields = '__all__'
