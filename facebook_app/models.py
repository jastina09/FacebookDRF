from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    avatar = models.ImageField(null=True, blank=True, upload_to='ava')
    user_link = models.URLField(null=True,blank=True)
    birth_date = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    is_official = models.BooleanField(default=False)
    TypeChoices = (
    ('blog','blog'),
    ('beauty', 'beauty'),
    ('sport','sport'),
    ('shopping','shopping')
    )
    user_type = models.CharField(max_length=30, choices=TypeChoices)
    date_register = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.username},{self.first_name}'

class Follow(models.Model):
    follower = models.ForeignKey(UserProfile, on_delete=models.CASCADE ,related_name='follower')
    following = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f'{self.following},{self.follower}'

class Hashtag(models.Model):
    hashtag_name = models.CharField()

    def __str__(self):
        return self.hashtag_name

class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='author')
    description = models.TextField(null=True, blank=True)
    hashtag = models.ManyToManyField(Hashtag, blank=True, related_name="posts")
    music = models.FileField(upload_to='music', null=True, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='users')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True,blank=True)
    create_date = models.DateField(auto_now_add=True)



class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField(upload_to='file_post_content')

class PostLike(models.Model):
    user = models.ForeignKey(UserProfile,related_name='like',on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post,related_name='likies',on_delete=models.CASCADE, null=True)
    like = models.BooleanField()

    class Meta:
        unique_together = ('user','post')

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='post_comment')
    text = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text

class CommentLike(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user','comment')


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class FavoriteItem(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Chat(models.Model):
    person = models.ManyToManyField(UserProfile)
    create_date = models.DateField(auto_now_add=True)


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='chat_img', null=True,blank=True)
    text = models.TextField(null=True,blank=True)
    video = models.FileField(upload_to='videos', null=True,blank=True)
    create_date = models.DateField(auto_now_add=True)