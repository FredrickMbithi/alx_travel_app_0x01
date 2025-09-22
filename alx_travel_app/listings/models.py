#!/usr/bin/env python3
"""
Django models for the travel app.
This file defines the main database tables: Listing, Booking, and Review.
Each model maps to a table and includes relationships & constraints.
"""

import uuid
from django.db import models
from django.contrib.auth.models import User


class Listing(models.Model):
    """
    A property (hotel, apartment, cabin, etc.) available for booking.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Booking(models.Model):
    """
    A booking record made by a user for a listing.
    Connects User → Listing with start/end dates.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.listing.title}"


class Review(models.Model):
    """
    A user review for a listing.
    Stores rating + optional comment.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review {self.rating}/5 for {self.listing.title}"
