from django.db import models
import uuid
# Create your models here.


class Member(models.Model):
  """the Member model """
  
  uid = models.UUIDField(uuid.uuid4)
  real_name = models.CharField(max_length = 100)
  time_zone = models.CharField(max_length = 100)

  def get_activities(self):
    return self.activity_periods.all()

  class Meta:
    db_table = 'api_member'

  def __str__(self):
    return self.real_name

class ActivityPeriod(models.Model):
  """this model stores the activities of each member"""
  
  member = models.ForeignKey(Member, on_delete = models.CASCADE, related_name='activity_periods', null = False)

  start_time = models.DateTimeField()
  end_time = models.DateTimeField()
  
  class Meta:
    db_table = 'api_activity_period'
  
  def __str__(self):
    return f'{self.member.real_name}s activity Period'

