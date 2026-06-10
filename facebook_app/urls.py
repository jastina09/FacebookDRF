from django.urls import path,include
from rest_framework import routers
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'favorite',FavoriteViewSet)
router.register(r'favorite_item', FavoriteItemViewSet)
router.register(r'hashtag',HashtagViewSet)
router.register(r'location',LocationViewSet)
router.register(r'comment_like',CommentLikeViewSet)
router.register(r'post_create', PostCreateViewSet)





urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserprofileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserprofileDetailAPIView.as_view(), name='user_detail'),
    path('commet/', CommentAPIView.as_view(), name='comments'),
    path('comment_create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('follow/', FollowViewSet.as_view(), name='follow'),
    path('post/', PostListAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailAPIView.as_view(), name='user_detail'),
    path('post_content/', PostContentViewSet.as_view(), name='post_content'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]