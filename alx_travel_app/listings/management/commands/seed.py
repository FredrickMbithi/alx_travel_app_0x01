#!/usr/bin/env python3
"""
Custom Django management command to seed the database.
Run it with: python manage.py seed
It creates a few sample listings for testing.
"""

from django.core.management.base import BaseCommand
from listings.models import Listing


class Command(BaseCommand):
    help = "Seeds the database with sample listings."

    def handle(self, *args, **kwargs):
        sample_data = [
            {"title": "Cozy Beach House", "description": "Beautiful seaside view.", "price_per_night": 120.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Peaceful retreat in the mountains.", "price_per_night": 85.00, "location": "Mt. Kenya"},
            {"title": "City Apartment", "description": "Modern apartment in the city center.", "price_per_night": 150.00, "location": "Nairobi"},
        ]

        for data in sample_data:
            Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "price_per_night": data["price_per_night"],
                    "location": data["location"],
                },
            )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded with sample listings!"))
