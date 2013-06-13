from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

#number is implied
class Equip_Type(models.Model):
	eType = models.CharField(max_length=20, unique=True)

	def __unicode__(self):
		return unicode(self.eType)

class Location(models.Model):
	room = models.CharField(max_length=4)
	building = models.CharField(max_length=2)
	def __unicode__(self):
		return unicode(self.building + self.room)

class Equipment(models.Model):
	model_num = models.IntegerField()
	serial_num = models.IntegerField()
	equip_type = models.ForeignKey(Equip_Type)
	location = models.ForeignKey(Location)
	description = models.TextField()

	def __unicode__(self):
		return unicode(self.description)


class Computer(Equipment):
	ram = models.IntegerField()
	max_ram = models.IntegerField()