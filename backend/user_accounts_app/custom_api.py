from rest_framework.views import APIView
from rest_framework import  viewsets,pagination, response, permissions,status
from rest_framework.response import Response

from .serializers_custom_users import *
from .model_custom_user import *
from django.contrib.auth.models import User

class Gondor_mgmt_me_APIVIEW(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.method == 'GET':
            # print(request.user)
            # # print(User._meta.fields())
            # # print(Gondor_mgmt.objects.all()[0])
            # gondor_rcd = User.objects.filter(id=request.user.id)
            # print(gondor_rcd.values())
            # user_info_serializer = Gondor_mgmt_full_user_serializer(gondor_rcd)
            user_info_serializer = custom_UserSerializer(request.user)
            # print(user_info_serializer.data)
            return Response(user_info_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)