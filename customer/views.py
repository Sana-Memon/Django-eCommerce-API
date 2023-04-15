from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from customer.serializers import CustomerSerializer
from customer.models import Customer

# Create your views here.
class ListCustomerAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CreateCustomerAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class UpdateCustomerAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DeleteCustomerAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
