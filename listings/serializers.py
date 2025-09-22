#!/usr/bin/env python3
"""
Serializers for travel app models.
They transform Django model instances into JSON responses for APIs.
"""

from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listing model.
    Converts a Listing object → JSON.
    """
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at']


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for Booking model.
    Converts a Booking object → JSON.
    """
    class Meta:
        model = Booking
        fields = ['id', 'user', 'listing', 'start_date', 'end_date', 'created_at']
