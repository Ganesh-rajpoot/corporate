from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.http import Http404
from .models import *




class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserDetailView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            # Perform login logic here if needed
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MentorListView(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorCreateView(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorDetailView(APIView):
    def get_object(self, pk):
        try:
            return Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        mentor = self.get_object(pk)
        serializer = MentorSerializer(mentor)
        return Response(serializer.data)

    def put(self, request, pk):
        mentor = self.get_object(pk)
        serializer = MentorSerializer(mentor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mentor = self.get_object(pk)
        mentor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ContactUsCreateView(generics.CreateAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def index(request):
    return render(request, 'app/index.html')
def about(request):
    return render(request, 'app/about.html')
def services(request):
    return render(request, 'app/services.html')
def contact(request):
    return render(request, 'app/contact.html')

def registration(request):
    return render(request, 'app/registration.html')