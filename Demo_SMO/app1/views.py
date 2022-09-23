from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework import status
from .models import Requirements, Report
from .serializer import RequirementsSerializer, ReportSerializer
from django.db.models import Q


class RequirementsInfo(APIView):
    def get(self, request):
        page_id = request.GET.get('page_id')
        data = Requirements.objects.filter(page_id=page_id)
        serial = RequirementsSerializer(data, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    def post(self, request):
        serial = RequirementsSerializer(data=request.data)
        month = request.data['month']
        bus_type = request.data['business_type']
        check_queryset = Requirements.objects.filter(month =month,business_type=bus_type)
        if check_queryset:
            error_res = dict(error='Already requirement Present')
            return Response(error_res,status=status.HTTP_400_BAD_REQUEST)
        else:
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self,request):
        pass

class RequirementsEdit(APIView):
    def get_object(self, pk):
        try:
            data = Requirements.objects.get(pk=pk)
            return data

        except Requirements.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        required = self.get_object(pk)
        serial = RequirementsSerializer(required)
        return Response(serial.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        required = self.get_object(pk)
        serial = RequirementsSerializer(required, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        required = self.get_object(pk)
        serial = RequirementsSerializer(required, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            data = Requirements.objects.get(pk=pk)
            data.delete()
            return Response({"msg": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Requirements.DoesNotExist:
            raise Http404






