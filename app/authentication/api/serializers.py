from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields= ('id','email','firstname','lastname','password','name')

        extra_kwargs = {
            'password': {'write_only': True, 'min_length': 4},
            'firstname':{'write_only':True},
            'lastname':{'write_only':True}
        }

    def get_name(self,obj):
        name = obj.firstname
        if name=='':
            name = obj.email
        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    clinic_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= User
        fields= ['id','email','name','token','clinic_id']

    def get_token(self,obj):
        token = RefreshToken.for_user(obj)
        return str(token)

    def get_clinic_id(self,obj):
        clinic = obj.clinic_set.get()
        if(clinic):
            return clinic.id
        else:
            return 0




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        clinic = user.clinic_set.get()
        if clinic:
            token["clinic_id"]=clinic.id


        # Add custom claims
        token['name'] = user.firstname
        token["test"] = "test"
        # ...

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data

        for k,v in serializer.items():
            data[k]=v

        return data

