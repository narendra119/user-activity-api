from django.core.management.base import BaseCommand
from activity_periods_api.models import Member, ActivityPeriod

import uuid
from datetime import datetime, timedelta
from random import randint

from random import randrange

class Command(BaseCommand):
  help = "Adding member objects to our db"

  def add_arguments(self, parser):
      parser.add_argument('total_act_count', type=int, help="number of activities to be created")

  def _create_time_zone(self, total):
    help = "Creating the time periods"
    

    for i in range(total):
      mem_count = Member.objects.all().count()
      x = randrange(mem_count)
      member = Member.objects.all()[x]
      
      if i%2 == 0:
        start = datetime.now() + timedelta(days = randint(1,10)) 
      else:
        start = datetime.now() - timedelta(days = randint(1,10))

      print(f'start the obj{i} creation')
      
      act_obj = ActivityPeriod(
        member = member,
        start_time = start,
        end_time = start + timedelta(minutes = randint(1,60)),
      )
      act_obj.save()
      print(f'obj{i} created')

  def handle(self, *args, **options):
    total = options['total_act_count']
    self._create_time_zone(total)
    
