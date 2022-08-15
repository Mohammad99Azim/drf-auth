from dataclasses import field
from rest_framework.serializers import (ModelSerializer,CharField,PrimaryKeyRelatedField,CurrentUserDefault)

from .models import Names_Gender
class NamesSerializer(ModelSerializer):
    user_name = CharField(source = 'user.username' , read_only=True)
    user = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())
    class Meta:
        model = Names_Gender
        fields = ['id','user','user_name','the_name','gender','accurate','data_created_at','data_updated_at']