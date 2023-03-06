from django.contrib.auth import authenticate

from rest_framework.serializers import ModelSerializer, Serializer, CharField, ValidationError
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import UserModel, VolunteerModel, ImageModel


class LoginSerializer(ModelSerializer):
    username = CharField()
    password = CharField()

    class Meta:
        model = UserModel
        fields = ['username', 'password']

    def validate(self, attrs):
        print(attrs)
        username = attrs.get('username', '')
        password = attrs.get('password', '')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise AuthenticationFailed('Invalid credentials, try again')
            if not user.is_active:
                raise AuthenticationFailed('Account disabled, contact admin')

            return {
                'user': user,
            }
        else:
            raise ValidationError(
                "Username and password are required"
            )


class UserModelSerializerMeta(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id',
                  'username',
                  'email',
                  'name',
                  'phone',
                  'is_user',
                  'is_volunteer',
                  ]


class UserModelSerializer:
    class Write(UserModelSerializerMeta):
        password = CharField(write_only=True)

        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'password',
            ]
            read_only_fields = ['id', 'password']

        def validate(self, attrs):
            password = attrs.get('password', '')
            is_user = attrs.get('is_user', False)
            is_volunteer = attrs.get('is_volunteer', False)
            if not is_user and not is_volunteer:
                raise ValidationError(
                    "User must be either player or agent"
                )
            if is_user and is_volunteer:
                raise ValidationError(
                    "User cannot be both player and agent"
                )
            if len(password) < 6:
                raise ValidationError(
                    "Password must be at least 6 characters"
                )
            return attrs

        def save(self, **kwargs):
            password = self.validated_data.pop('password')
            user = UserModel.objects.create(**self.validated_data)
            user.set_password(password)
            user.password_plain = password
            user.save()
            return user

    class List(UserModelSerializerMeta):
        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields + [
                'is_admin',
            ]

    class Lite(UserModelSerializerMeta):
        class Meta(UserModelSerializerMeta.Meta):
            fields = UserModelSerializerMeta.Meta.fields


class LogoutSerializer(Serializer):
    refresh = CharField()

    default_error_messages = {
        'bad_token': 'Token is expired or invalid'
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')


class ImageModelSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class VolunteerSerializerMeta(ModelSerializer):
    class Meta:
        model = VolunteerModel
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'whatsapp',
            'social_media',
            'gender',
            'pronouns',
            'date_of_birth',
            'country',
            'nationality',
            'sector',
            'mode_of_communication',
            'photo_sharing_consent',
            'nominee1_name',
            'nominee1_social_media',
            'nominee1_country',
            'nominee1_contact',
            'nominee2_name',
            'nominee2_social_media',
            'nominee2_country',
            'nominee2_contact',
        ]


class VolunteerSerializer:
    class Write(VolunteerSerializerMeta):
        class Meta(VolunteerSerializerMeta.Meta):
            fields = VolunteerSerializerMeta.Meta.fields + [
                'id',
            ]

    class List(VolunteerSerializerMeta):
        class Meta(VolunteerSerializerMeta.Meta):
            fields = VolunteerSerializerMeta.Meta.fields + [
                'created_at',
            ]
