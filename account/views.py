from account.serializers import UserRegistarationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer = UserRegistarationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({'msg':'Registration Successfull'},
            status =status.HTTP_201_CREATED) 
        return Response(serializer.errors,
        status=status.HTTP_400_BAD_REQUEST)
