from rest_framework import serializers
from models import Restaurant

class RestaurantSerializer(serializers.Serializer):
    # fields = ('_id', 'email', 'password', );
    # id = serializers.CharField(required=True, max_length=50)
    email = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=False, max_length=20)

    def restore_object(self, attrs, instance=None):
        if instance:
            # instance.id = attrs.get('id', instance.id)
            instance.email = attrs.get('email', instance.email)
            instance.password = attrs.get('password', instance.password)
            return instance

        return Restaurant(attrs.get('email'),attrs.get('password'))

