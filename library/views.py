from django.shortcuts import render

from rest_framework import mixins, generics

from .models import Library
from api.serializers import LibrarySerializer

# Create your views here.
class LibraryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class LibraryDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)