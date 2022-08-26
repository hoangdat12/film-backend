from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import MyTokenObtainPairView, UserDetailAPI, RegisterUserAPIView
from .views import getFilm, createFilm, updateFilm, getAllFilmIsWatch, getAllFilmIsLike, updateLikeFilm, updateUnLikeFilm
from .views import createComment, getAllCommentFilm, getComment, updateComment
from .views import getProfile, updateProfile
from .views import updateUser

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<str:username>', UserDetailAPI.as_view()),
    path('register/', RegisterUserAPIView.as_view()),

    path('user/update/<int:pk>', updateUser),

    path('film/get/<int:pk>', getFilm),
    path('film/get/<int:pk>/is-watched', getAllFilmIsWatch),
    path('film/get/<int:pk>/is-liked', getAllFilmIsLike),
    path('film/create', createFilm),
    path('film/update/<int:pk>', updateFilm),
    path('film/update-like/<int:pk>', updateLikeFilm),
    path('film/update-unlike/<int:pk>', updateUnLikeFilm),

    path('comment/create', createComment),
    path('comment/get-all/<int:pk>', getAllCommentFilm),
    path('comment/get/<int:pk>', getComment),
    path('comment/update/<int:pk>', updateComment),

    path('profile/<int:pk>',getProfile),
    path('profile/update/<int:pk>', updateProfile),
]