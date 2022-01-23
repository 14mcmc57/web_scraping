from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)
from rest_framework import status




# Create your views here.
class Schedule(viewsets.ModelViewSet):
    def get_queryset(self):
        try:
            print("============")
            return Response({'massage': 'Created successfully','status': True})
        except Exception as e:
            logger.error('Something Went Wrong' + str(e))
            context = {'status': False, 'error': {'message': ['Something Went Wrong']}}
            return Response(context, status=status.HTTP_200_OK)
