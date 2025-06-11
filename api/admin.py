from django.contrib import admin

# Register your models here.

from .models import FitnessClass, Booking

@admin.register(FitnessClass)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'instructor', 'available_slots')
    search_fields = ('name', 'instructor')
    list_filter = ('instructor',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email', 'fitness_class')
    search_fields = ('client_name', 'client_email')
    list_filter = ('fitness_class',)