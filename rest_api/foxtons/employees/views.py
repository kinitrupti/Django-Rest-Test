from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import requests   # To use request package in current program 

url = 'https://reqres.in/api/users' #fetching data from the url

@api_view(['GET', 'POST'])
def employee_list(request): #Get the list of employees
	if request.method == 'GET':
                response = requests.get(url)
                return Response(response.json())
                return Response(response.json(), status=status.HTTP_404_ERROR)

	elif request.method == 'POST':
                data = {} 
                response = requests.post('https://reqres.in/api/users', data)
                return Response(response.json(), status=status.HTTP_201_CREATED)
		
@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, id): #Performs operations like Create, Update, Delete
        
        url = 'https://reqres.in/api/users/%s' % id
        response = requests.get(url)
        
        if request.method == 'GET':
                return Response(response.json())
        elif request.method == 'POST':
                data = {}
                response = requests.post('https://reqres.in/api/users', data=data)
                return Response(response.json(), status=status.HTTP_201_CREATED)
        elif request.method == 'PUT':
                data = {}
                response = requests.put('https://reqres.in/api/users', data=data)
                return Response(response.json())
        elif request.method == 'DELETE':
                response=requests.delete(url)
                return Response(response.status_code)   
            
@api_view(['GET', 'POST'])
def employee_unknown(request): #Get list of jobs
        if request.method == 'GET':
                url = 'https://reqres.in/api/unknown'
                response = requests.get(url)
                return Response(response.json())

@api_view(['GET', 'POST'])
def employee_register(request): 
        if request.method == 'GET':
                url = 'https://reqres.in/api/register'
                response = requests.get(url)
                return Response(response.json())
