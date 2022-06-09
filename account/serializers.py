from rest_framework import serializers
from account.models import User

class UserRegistarationSerializer(serializers.ModelSerializer):
    # we are writing this because we need password confirmation field in our Registration Request
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'name', 'password', 'password2', 'tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }

# Validating password and confirm password while Registration
def validate(self,attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
        raise serializers.ValidationError("Password and confirm password doesn't match")
    return attrs

def create(self, validate_data):
    return User.objects.create_user(**validate_data)