from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile_no']



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    cpassword = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['name', 'mobile_no', 'password', 'cpassword']

    def save(self):
        user = User(
            name=self.validated_data['name'],
            mobile_no=self.validated_data['mobile_no'],
                )
        password = self.validated_data['password']
        password2 = self.validated_data['cpassword']

        if password != password2:
            raise serializers.ValidationError({'password': 'password should match'})
        user.set_password(password)
        user.save()
        return user


# class UserRegistrationSerializer(serializers.ModelSerializer):
#     #cpassword = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['name','mobile_no', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}  # not to be shown in api view
#         }
#
#     def save(self):
#         user = User(
#             name=self.validated_data['name'],
#             mobile_no=self.validated_data['mobile_no'],
#             email=self.validated_data['email'],
#         )
#         password = self.validated_data['password']
#         #cpassword = self.validated_data['password2']
#
#         # if password != password2:
#         #     raise serializers.ValidationError({'password': 'password should match'})
#         user.set_password(password)
#         user.save()
#         return user

