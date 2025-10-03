from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Listing instances.
    Provides CRUD operations: list, create, retrieve, update, destroy
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['location', 'price_per_night']
    search_fields = ['title', 'description', 'location']
    ordering_fields = ['price_per_night', 'created_at']

class BookingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Booking instances.
    Provides CRUD operations: list, create, retrieve, update, destroy
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['listing', 'user', 'status']
    ordering_fields = ['check_in', 'created_at']