from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['created_at']
    
    def validate(self, data):
        # Add custom validation (e.g., check-in before check-out)
        if data.get('check_in') and data.get('check_out'):
            if data['check_in'] >= data['check_out']:
                raise serializers.ValidationError(
                    "Check-out date must be after check-in date"
                )
        return data