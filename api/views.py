from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer, BookingRequestSerializer

class ClassListView(APIView):
    def get(self, request):
        classes = FitnessClass.objects.all()
        serializer = FitnessClassSerializer(classes, many=True)
        return Response(serializer.data)

class BookClassView(APIView):
    def post(self, request):
        serializer = BookingRequestSerializer(data=request.data)
        if serializer.is_valid():
            class_id = serializer.validated_data['class_id']
            try:
                fitness_class = FitnessClass.objects.get(id=class_id)
            except FitnessClass.DoesNotExist:
                return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

            if fitness_class.available_slots <= 0:
                return Response({'error': 'No slots available'}, status=status.HTTP_400_BAD_REQUEST)

            Booking.objects.create(
                fitness_class=fitness_class,
                client_name=serializer.validated_data['client_name'],
                client_email=serializer.validated_data['client_email'],
            )
            fitness_class.available_slots -= 1
            fitness_class.save()

            return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookingListView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        bookings = Booking.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

