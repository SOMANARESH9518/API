from .serializers import APIUserSerializer
from myapp.models import APIUser
from rest_framework import generics
from rest_framework import permissions
from django.http import JsonResponse


def index(request):
    api_user_list = list(APIUser.objects.values())
    return JsonResponse(api_user_list, safe=False)


class CreateView(generics.ListCreateAPIView):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
