from django.shortcuts import render
from django.http import Http404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.decorators import APIView
from rest_framework import status
from .models import Requirements, Report,LeadsManagement
from .serializer import RequirementsSerializer, ReportSerializer, LeadsSerializer
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
        check_queryset = Requirements.objects.filter(month=month, business_type=bus_type)
        if check_queryset:
            error_res = dict(error='Already requirement Present')
            return Response(error_res, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class RequirementsEdit(APIView):
    def get_object(self, pk):
        try:
            data = Requirements.objects.get(pk=pk)
            print(data)
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
            required = self.get_object(pk)
            required.delete()
            return Response({"msg": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Requirements.DoesNotExist:
            raise Http404


class ReportDetails(APIView):
    # permission_classes = [IsAdminUser]

    def get(self, request):
        page_id = request.GET.get('page_id')
        data = Report.objects.filter(page_id=page_id)
        serial = ReportSerializer(data, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)


class ReportEdit(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serial = ReportSerializer(data=request.data)
        print(serial)
        month = request.data['month']
        bus_type = request.data['business_type']
        check_queryset = Report.objects.filter(month=month, business_type=bus_type)
        if check_queryset:
            error_res = dict(error='Already requirement Present')
            return Response(error_res, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            data = Report.objects.get(pk=pk)
            return data

        except Report.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        required = self.get_object(pk)
        serial = ReportSerializer(required)
        return Response(serial.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        required = self.get_object(pk)
        serial = ReportSerializer(required, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_200_OK)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        required = self.get_object(pk)
        serial = ReportSerializer(required, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            required = self.get_object(pk)
            required.delete()
            return Response({"msg": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Report.DoesNotExist:
            raise Http404


class LeadManageMixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = LeadsManagement.objects.all()
    serializer_class = LeadsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class LeadsEditMixin(mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = LeadsManagement.objects.all()
    serializer_class = LeadsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

