from rest_framework import serializers
from .models import Persion , Color 
from django.contrib.auth.models import User



class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def validate(self, data):
        
        if data['username']:
            if User.objects.filter(username = data ['username']).exists():
                raise serializers.ValidationError('username is taken')
            
            
            if data['email']:
                if User.objects.filter(email = data ['email']).exists():
                   raise serializers.ValidationError('email is taken')
            return data
        
    
    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'] , email= validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)
        
 

class LoginSerilizer(serializers.Serializer):
    username = serializers.CharField()
    pasword = serializers.CharField()
    


class ColorSerilzer(serializers.ModelSerializer):
    
    class Meta:
        model = Color 
        fields = ['color_name']

class PeopleSerializer(serializers.ModelSerializer):
    color = ColorSerilzer()
    color_info = serializers.SerializerMethodField()
    
    
    
    class Meta:
        model = Persion
        fields = '__all__'
        depth = 1
        
    def get_color_info(self , obj):
        color_obj = Color.objects.get(id = obj.color.id)
        return {'color_name': color_obj.color_name , 'hex_code': '#000'}
        
    def validate(self, data):
        special_character = "~!@#$%^&*()/"
        if any(c in special_character for c in data["Name"]):
            raise serializers.ValidationError('name does not contain any special character')
        
        
        #if data['age'] < 18:
        #   raise serializers.ValidationError('age should be greator than 18')
        return data
            