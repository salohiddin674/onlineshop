from django.shortcuts import render
from main.models import User
from main.serializers import UserSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.contrib.auth import logout, authenticate, login
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def signin_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        usr = authenticate(username=username,password=password)
        try:
            if usr is not None:
                login(request,usr)
                status = 200
                data = {
                    'status':status,
                    'username':username,
                }
            else:
                status = 403
                message = " Invalid Password or Username!"
                data = {
                    'status':status,
                    'message':message,
                }
        except User.DoesNotExist:
            status = 404
            message = 'This User is not defined'
            data = {
                'status':status,
                'message':message,
            }
        return Response(data)
    except Exception as err:
            return Response(f'{err}')



@api_view(['POST'])
def signup_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    phone_number = request.POST.get('phone_number')
    new = User.objects.create_user(
        username=username,
        password=password,
        phone_number=phone_number,
    )
    ser = UserSerializer(new)
    return Response(ser.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'data':'sucses'})



@api_view(['PUT'])
def edit_user_view(request,pk):
    try:
        user = User.objects.get(pk=pk)
        try:
            username = request.data.get('username')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            email = request.data.get('email')
            phone_number = request.data.get('phone_number')
            password = request.data.get('password')
            if username is not None:
                user.username = username
            if first_name is not None:
                user.first_name = first_name
            if last_name is not None:
                user.last_name = last_name
            if email is not None:
                user.email = email
            if phone_number is not None:
                user.phone_number = phone_number
            if password is not None:
                user.set_password(password)
            user.save()
            ser = UserSerializer(user)
            return Response(ser.data)

        except:
            status = 400
            message = ' Request failed '
            data = {
                'status':status,
                'message':message,
            }
    except:
        status = 404
        message = 'User not found'
        data = {
            'status':status,
            'message':message,
        }
    return Response(data)


@api_view(['DELETE'])
def delete_user(request,pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
        data= {
            'message':'User succesfuly'
        }
    except:
        status = 404
        message = 'User not found'
        data = {
            'status':status,
            'message':message,
        }
    return Response(data)



