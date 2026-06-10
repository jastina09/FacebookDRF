from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = ('username', 'email', 'password', 'first_name', 'last_name')
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
    user = UserProfile.objects.create_user(**validated_data)
    return user

  def to_representation(self, instance):
    refresh = RefreshToken.for_user(instance)
    return {
      'user': {
        'username': instance.username,
        'email': instance.email,
      },
      'access': str(refresh.access_token),
      'refresh': str(refresh),
    }


class UserLoginSerializer(serializers.Serializer):
  username = serializers.CharField()
  password = serializers.CharField(write_only=True)

  def validate(self, data):
    user = authenticate(**data)
    if user and user.is_active:
      return user
    raise serializers.ValidationError("Неверные учетные данные")

  def to_representation(self, instance):
    refresh = RefreshToken.for_user(instance)
    return {
      'user': {
        'username': instance.username,
        'email': instance.email,
      },
      'access': str(refresh.access_token),
      'refresh': str(refresh),
    }


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username','avatar']


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username','avatar']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','avatar','first_name','last_name','birth_date','bio','is_official','user_type','date_register']


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id','follower','following']


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['hashtag_name']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_name']


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','music','create_date']



class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostContentDetailSerializer(serializers.ModelSerializer):
    post = UserProfileDetailSerializer()
    class Meta:
        model = PostContent
        fields = ['id','file','post']

class PostNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','author','music','description','hashtag','user','location','create_date']


class CommentNameSerializer(serializers.ModelSerializer):
    user = UserProfileNameSerializer()
    post = PostNameSerializer()
    class Meta:
        model = Comment
        fields = ['text','user','post','parent','create_date']


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserProfileNameSerializer()
    post = PostNameSerializer()
    class Meta:
        model = Comment
        fields = ['text','user','post','parent','create_date']


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserProfileNameSerializer()
    comment = CommentNameSerializer()
    class Meta:
        model = CommentLike
        fields = ['user','comment','like']


class PostDetailSerializer(serializers.ModelSerializer):
    post_comment = CommentNameSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','author','music','description','hashtag','user','location','create_date','post_comment']


class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='favorite.user.username')
    class Meta:
        model = Favorite
        fields = ['user']


class FavoriteItemSerializer(serializers.ModelSerializer):
    favorite = FavoriteSerializer()
    post = PostNameSerializer()
    class Meta:
        model = FavoriteItem
        fields = ['favorite','post']