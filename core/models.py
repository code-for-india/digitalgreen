from django.db import models

# Create your models here.

class Address(models.Model):
	id = models.AutoField(primary_key=True)
	country = models.CharField(max_length=3)
	state = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	village = models.CharField(max_length=100)
	block = models.CharField(max_length=100)
	pincode = models.CharField(max_length=10)
	lat = models.DecimalField(max_digits=9, decimal_places=6)
	lan = models.DecimalField(max_digits=9, decimal_places=6)
	preferred_language = models.CharField(max_length=10)

	# ...
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.block

class Farmer(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=200)
	mobile_no = models.CharField(max_length=10, primary_key=True)
	address = models.ForeignKey(Address)
	image_url = models.URLField()
	preferred_language = models.CharField(max_length=10)

	# ...
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.mobile_no
		
class Video(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200)
	url = models.URLField(null=True, blank=True)
	info = models.TextField(null=True, blank=True)
	language = models.CharField(max_length=10, null=True, blank=True)

	# ...
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.name

class VideoView(models.Model):
	id = models.AutoField(primary_key=True)
	mobile_no = models.ForeignKey(Farmer)
	video = models.ForeignKey(Video)
	watch_at = models.DateTimeField(null=True)
	survey_at = models.DateTimeField(null=True)
	has_interest = models.NullBooleanField()
	has_implemented = models.NullBooleanField()
	recording_url = models.URLField(null=True, blank=True)

	# ...
	def __unicode__(self):  # Python 3: def __str__(self):
		return '{mobile_no}, {video_id}, {has_interest}, {has_implemented}'.format(mobile_no=self.mobile_no,video_id=self.video_id, has_interest=self.has_interest, has_implemented=self.has_implemented)
