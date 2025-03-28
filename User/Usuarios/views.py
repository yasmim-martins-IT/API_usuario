from django.shortcuts import render 
from .models import UserAbs
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from .serializer import UsersSerializer


@api_view(['POST'])
def criar_superUser(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not all ([username, password , email, idade,endereco]):
        return Response({'error' : 'informações insuficientes para criar o usuario'}, status= status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(username = username).exists():
        return Response({'error' : 'Já existe um usuario com esse nome'}, status= status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(email = email).exists():
         return Response({'error' : 'Já existe um usuario com esse e-mail'}, status= status.HTTP_400_BAD_REQUEST)
        
    try: 
       usuario = UserAbs.objects.create_superuser(
           username= username,
           password = password,
           email = email,
           biografia = biografia ,
           idade = idade ,
           telefone = telefone ,
           endereco = endereco ,
           escolaridade = escolaridade,
           animais = animais

       )
       return Response({'Mensagem': 'SuperUser criado com sucesso'}, status=status.HTTP_201_CREATED)     
    except Exception as e:
        return Response({'error': f'Erro ao criar usuário: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def criar_User(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    animais = request.data.get('animais')

    if not all ([username, password , email, idade,endereco]):
        return Response({'error' : 'informações insuficientes para criar o usuario'}, status= status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(username = username).exists():
        return Response({'error' : 'Já existe um usuario com esse nome'}, status= status.HTTP_400_BAD_REQUEST)
    if UserAbs.objects.filter(email = email).exists():
         return Response({'error' : 'Já existe um usuario com esse e-mail'}, status= status.HTTP_400_BAD_REQUEST)
        
    try: 
       usuario = UserAbs.objects.create_user(
           username= username,
           password = password,
           email = email,
           biografia = biografia ,
           idade = idade ,
           telefone = telefone ,
           endereco = endereco ,
           escolaridade = escolaridade,
           animais = animais

       )
       return Response({'Mensagem': 'User criado com sucesso'}, status=status.HTTP_201_CREATED)     
    except Exception as e:
        return Response({'error': f'Erro ao criar usuário: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # Create your views here.

@api_view(['POST'])
def logar(request):
    username = request.data.get('username')
    password =request.data.get('password')

    if not username or not password :
        return Response({'Erro' : 'Informações insuficientes para fazer o login'}, status= status.HTTP_200_OK)
    
    user = authenticate(username = username , password = password)

    if user :
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }, status=status.HTTP_200_OK)
    return Response({'Acesso negado'}, status= status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_usuarios(request):
    usuarios = UserAbs.objects.all()

    serializer = UsersSerializer(usuarios, many = True )

    return Response(serializer.data)

  
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def atualizar(request , pk):
  try :
    evento_atualizado = UserAbs.objects.get(pk=pk)
  except UserAbs.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  serializer =UsersSerializer(evento_atualizado,data = request.data , partial = True)
  
  if serializer.is_valid():
    serializer.save()
    
    return Response(serializer.data , status=status.HTTP_200_OK)
  return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete (request,pk):
    try :
        evento_atualizado = UserAbs.objects.get(pk=pk)
    except UserAbs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    try:
        evento_atualizado.delete()

        return Response(status= status.HTTP_404_NOT_FOUND)
    except :
        return Response({'Erro' :'Não foi possivel deletar o usuario'},status = status.HTTP_500_INTERNAL_SERVER_ERROR)