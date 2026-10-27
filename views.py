from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        return Response(DoctorSerializer(doctors, many=True).data)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DoctorDetail(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        return Response(DoctorSerializer(doctor).data)

    def put(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        if doctor.created_by != request.user:
            return Response(
                {"detail": "You can only edit doctors added by you"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        if doctor.created_by != request.user:
            return Response(
                {"detail": "You can only delete doctors added by you"},
                status=status.HTTP_403_FORBIDDEN,
            )
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
