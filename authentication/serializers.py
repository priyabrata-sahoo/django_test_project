from datetime import datetime
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        # fields = ("first_name", "last_name", "password", "email")
        fields= "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data.pop("email")
        password = validated_data.pop('password')
        # phone = validated_data.pop('phone')

        user = User.objects.create_user(
            email=email,
            password=password,
            **validated_data
        )
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        # Calculate expires_in
        expires_in_timestamp = refresh.access_token.payload["exp"]
        expires_in_datetime = datetime.fromtimestamp(expires_in_timestamp)
        expires_in_seconds = int((expires_in_datetime - datetime.now()).total_seconds())

        return {
            "user": user,
            "refresh_token": str(refresh),
            "access_token": access_token,
            "expires_in": expires_in_seconds,
        }

class UserResponseSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    refresh_token = serializers.CharField()
    access_token = serializers.CharField()
    expires_in = serializers.IntegerField()


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = User.objects.filter(email=email).first()

        if user is None:
            raise serializers.ValidationError("User not found.")

        if not user.check_password(password):
            raise serializers.ValidationError("Invalid password.")

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        # Calculate expires_in
        expires_in_timestamp = refresh.access_token.payload["exp"]
        expires_in_datetime = datetime.fromtimestamp(expires_in_timestamp)
        expires_in_seconds = int((expires_in_datetime - datetime.now()).total_seconds())

        return {
            "user": user.id,
            "access_token": access_token,
            "refresh_token": str(refresh),
            "expires_in": expires_in_seconds,
        }


class UserLogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def logout_user(self):
        refresh_token = self.validated_data['refresh_token']

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            raise serializers.ValidationError('Invalid refresh token')

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    def create(self, validated_data):
        isinstance = {}
        return isinstance
    
    def validate(self, data):
        old_password = data.get('old_password')
        new_password = data.get('new_password')
        confirm_password = data.get('confirm_password')

        # Get the user making the request
        user = self.context['request'].user

        # Check if the old password is correct
        if not user.check_password(old_password):
            raise serializers.ValidationError('Old password is incorrect.')

        # Check if the new password and confirmation match
        if new_password != confirm_password:
            raise serializers.ValidationError('New passwords do not match.')

        # Change password logic
        user.set_password(new_password)
        user.save()

        return data