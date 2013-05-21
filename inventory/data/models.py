from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Equipment(models.Model):
	model_num = models.IntegerField()
	serial_num = models.IntegerField()
	equip_type = models.ForeignField()
	location = models.ForeignField()
	description = models.TextField()

	def __unicode__(self):
		return unicode(model_num)

class Location(models.Model):
	room = models.CharField(max_length=4)
	building = models.CharField(max_length=2)
	def __unicode__(self):
		return unicode(self.building + self.room)
