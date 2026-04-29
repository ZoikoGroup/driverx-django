from rest_framework import serializers


class EditProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=False, max_length=150)
    last_name = serializers.CharField(required=False, max_length=150)
    password = serializers.CharField(write_only=True, required=False, min_length=8)
    confirm_password = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        password = attrs.get('password')
        confirm = attrs.pop('confirm_password', None)

        if password and not confirm:
            raise serializers.ValidationError(
                {"confirm_password": "Please confirm your password."}
            )
        if password and password != confirm:
            raise serializers.ValidationError(
                {"confirm_password": "Passwords do not match."}
            )
        return attrs

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance