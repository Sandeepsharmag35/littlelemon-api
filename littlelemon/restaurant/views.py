from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

def home(request):
    return render(request, "index.html", {})

def about(request):
    return render(request, "about.html", {})

def menu_page(request):
    menu = Menu.objects.all()
    return render(request, "menu.html", {"menu": menu})

def display_menu_item(request, pk=None): 
    if pk: 
        menu_item = Menu.objects.get(pk=pk) 
    else: 
        menu_item = "" 
    return render(request, 'menu_item.html', {"menu_item": menu_item}) 


def book_page(request):
    bookings = Booking.objects.all()
    return render(request, "book.html", {})

class MenuView(APIView):
    def get(self, request):
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})


class BookingView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
