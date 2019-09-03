from django.shortcuts import render, redirect
from django.contrib import messages

from classes.models import Classroom

from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,CreateAPIView,DestroyAPIView
from .serializers import ClassDetailSerializer,ClassListSerializer,CreateSerializer


class ClassRoomView(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassListSerializer

class DetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class CreateView(CreateAPIView):
		serializer_class = CreateSerializer

		def perform_create(self, serializer):
			serializer.save(teacher=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = CreateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'


class DeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'