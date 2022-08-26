from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics

from .models import Film, Comment, Profile
from .serializers import FilmSerializers, CommentSerializers, ProfileSerializers, UserSerializer, RegisterSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class UserDetailAPI(APIView):
    def get(self,request,username,*args,**kwargs):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['POST'])
def updateUser(request, pk):
    User.objects.filter(id=pk).update(first_name = request.data['firstName'], last_name = request.data['lastName'])
    user = User.objects.get(id = pk)
    serializer = UserSerializer(user, many=False)
    return Response((serializer.data), status=status.HTTP_200_OK)

@api_view(['GET'])
def getFilm(request, pk):
    try:
        film = Film.objects.get(film_id = pk)
    except:
        return Response({'error': 'film not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FilmSerializers(film, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def getAllFilmIsWatch(request, pk):
    film = Film.objects.filter(is_watch = True, user=pk).order_by('-updated')
    serializers = FilmSerializers(film, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllFilmIsLike(request, pk):
    film = Film.objects.filter(is_liked = True, user=pk).order_by('-updated')
    serializers = FilmSerializers(film, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def createFilm(request):
    if Film.objects.filter(film_id = request.data['film_id']).exists():  
        return Response({'detail': 'Film is exist !'})
    print('request: ', request.data)
    serializer = FilmSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Created is failure !'}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def updateFilm(request, pk):
    try:
        film = Film.objects.get(film_id = pk)
    except:
        return Response({'error': 'Film not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = FilmSerializers(film, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
def updateLikeFilm(request, pk):
    Film.objects.filter(film_id=pk).update(is_liked=True)
    return Response({'detail': 'Like Successfully'})

@api_view(['POST'])
def updateUnLikeFilm(request, pk):
    Film.objects.filter(film_id=pk).update(is_liked=False)
    return Response({'detail': 'UnLike Successfully'})



@api_view(['POST'])
def createComment(request):
#     try:
#         film = Film.objects.get(film_id=request.data['film_id'])
#     except:
#         return Response({'detail': 'Id film unvalid !'})
#     serializerFilm = FilmSerializers(film, many=False)
#     request.data['film_id'] = serializerFilm.data['id']
    print(request.data)
    serializer = CommentSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': 'Create comment is failure !'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getComment(request, pk):
    try:
        comments = Comment.objects.get(id=pk)
    except:
        return Response({'error': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CommentSerializers(comments, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def getAllCommentFilm(request, pk):
    try:
        comments = Comment.objects.filter(film_id = pk).order_by('-updated')
    except:
        return Response({'error': 'Film not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CommentSerializers(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def updateComment(request, pk):
    try:
        comment = Comment.objects.get(id = pk)
    except:
        return Response({'detail': 'Id Comment not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CommentSerializers(comment, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Data error'})

@api_view(['GET'])
def getProfile(request, pk):
    try:
        profile = Profile.objects.get(user_id = pk)
    except:
        return Response({'detail': 'UserID not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ProfileSerializers(profile, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def updateProfile(request, pk):
    Profile.objects.filter(id=pk).update(bio = request.data['bio'], location=request.data['location'])
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializers(profile, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)
