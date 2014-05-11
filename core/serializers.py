from core.models import Address, Farmer, Video, VideoView
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = ('id', 'country', 'state', 'district', 'village', 'block', 'lat', 'lan', 'preferred_language')

class FarmerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Farmer
		fields = ('id', 'name', 'mobile_no', 'address', 'image_url', 'preferred_language')

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = ('id', 'name', 'url', 'info', 'language')

class VideoViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = VideoView
		fields = ('id', 'mobile_no', 'video', 'watch_at', 'survey_at', 'has_interest', 'has_implemented', 'recording_url')