from activity_periods_api.models import Member, ActivityPeriod
from rest_framework import serializers

class ActivityPeriodSerializer(serializers.ModelSerializer):
  """ 
  To Serialize the Data of 'ActivityPeriod' Model
  """
  class Meta:
      model = ActivityPeriod
      fields = ['start_time', 'end_time']


class MemberSerializer(serializers.ModelSerializer):
  """
  To Serialize the Data of 'Member' Model
  """
  activity = serializers.SerializerMethodField('get_activity_details')
      
  class Meta:
    model = Member
    fields = ('real_name', 'time_zone', 'activity')

  def get_activity_details(self,obj):
    return ActivityPeriodSerializer(obj.get_activities(), many =True).data



