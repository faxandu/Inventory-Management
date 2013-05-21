from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Inventory(models.Model):
	modelNum = models.CharField(max_length=200)
	def __unicode__(self):
		return self.modelNum

class Serial(models.Model):
	inventory = models.ForeignKey(Inventory)
	serialNum = models.CharField(max_length=200)
	def __unicode__(self):
		return self.serialNum

class Description(models.Model):
	inventory = models.ForeignKey(Inventory)
	descript = models.CharField(max_length=255)
	def __unicode__(self):
		return self.descript

class Location(models.Model):
	inventory = models.ForeignKey(Inventory)
	room = models.CharField(max_length=3)
	building = models.CharField(max_length=2)
	def __unicode__(self):
		return self.building + self.room