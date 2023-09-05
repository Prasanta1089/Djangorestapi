from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from home.models import Persion
from home.serializers import PeopleSerializer , LoginSerilizer , RegisterSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class LoginApi(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerilizer(data = data)
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST)
        print(serializer.data)
        user = authenticate(username = serializer.data['username'] , password = serializer.data['password'])
        print(user)
        if not user:
            return Response({
                'status': False,
                'message': 'invalid condition'
            }, status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user = user)   
        print(token)
        return Response({'status' : True , 'message':'user login' , 'token':str(token)}, status.HTTP_201_CREATED)
        
class RegisterAPI(APIView):
    def post(self , request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        
        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status.HTTP_400_BAD_REQUEST )
            
        serializer.save()
        return Response({'status':True , 'message': 'user created'}, status.HTTP_201_CREATED)



@api_view(["GET", "POST","PUT"])

def index(request):
    if request.method=="GET":
        Biodata = {
            "Name":"Prasanta",
            "Age":"23",
            "Profesion":"Python developer",
            "Skilss":"Python, Django , Fastapi, Html, Css, Boot strap , Mongo DB",
            "Sellary":25000
            
        }
        
        return Response(Biodata)
    
    else :
        data = request.data 
        print(data)
        
        Biodata={
            "Name":"Raja",
            "Age":"23",
            "Profesion":"Python developer",
            "Skilss":"Python, Django , Fastapi, Html, Css, Boot strap , Mongo DB",
            "Sellary":30000
        }
        return Response(Biodata)

@api_view(['POST'])
def login(request):
    data = request.data
    serilizer = LoginSerilizer(data=data)
    
    if serilizer.is_valid():
        data = serilizer.data
        print(data)
        return Response({'message': 'success'})
    return Response(serilizer.errors)

class PersonAPI(APIView):
    
    def get(self , request):
        objs = Persion.objects.filter(color__isnull=False)
        serializer = PeopleSerializer(objs , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        data = request.data 
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self , request):
        data = request.data 
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
    
    def patch(self , request):
        data = request.data 
        obj = Persion.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj , data = data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self , request):
        data = request.data 
        obj = Persion.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' :'person deleted'})
    

    
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
    if request.method == "GET":
       objs = Persion.objects.filter(color__isnull=False)
       serializer = PeopleSerializer(objs , many = True)
       return Response(serializer.data)
    
   
    elif request.method == 'POST':
        data = request.data 
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif  request.method == "PUT":
        data = request.data 
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
   
   
   
    elif request.method == 'PATCH':
        data = request.data 
        obj = Persion.objects.get(id = data['id'])
        serializer = PeopleSerializer(obj , data = data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    else:
        data = request.data 
        obj = Persion.objects.get(id = data['id'])
        obj.delete()
        return Response({'message' :'person deleted'})
    
    
    


class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Persion.objects.all()
    
    