from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from activity_periods_api.models import Member 

import uuid
import random
import pytz

TIMEZONES = list(pytz.all_timezones)

class Command(BaseCommand):
  help = "Adding member objects to our db"

  def add_arguments(self, parser):
    parser.add_argument('total_mem_count',type=int, help="Number of members to be created" )

  def _create_members(self, total):
      for i in range(total):
        print('started creating member object')
        member = Member(
          uid = uuid.uuid4(),
          real_name = f'mem_{get_random_string()}',
          time_zone = random.choice(TIMEZONES),
        )
        print('Saving member object')
        member.save()
        print('Member object saved!')

  def handle(self, *args, **options):
    total = options['total_mem_count']
    self._create_members(total)
    
