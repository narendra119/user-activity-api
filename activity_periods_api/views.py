from activity_periods_api.models import Member
from activity_periods_api.serializers import  MemberSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# View to show the api data
@api_view(['GET'])
def work_view(self):
  
  response_data = {}
  members = Member.objects.all()
  response_data['data'] = MemberSerializer(members, many = True).data
  
  return Response(response_data, status = status.HTTP_200_OK)
