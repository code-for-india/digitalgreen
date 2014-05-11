from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.models import VideoView
from lib import exotel
from django.conf import settings
from pprint import pprint
from django.utils import timezone

@api_view(['GET'])
def hasInterest(request):
	print request.QUERY_PARAMS
	video_id = request.QUERY_PARAMS['CustomField']
	mobile_no = request.QUERY_PARAMS['From'][1:]
	recording_url = request.QUERY_PARAMS.get('RecordingUrl')
	print mobile_no, video_id
	try:
		video_view = VideoView.objects.get(video_id=video_id, mobile_no=mobile_no)
		video_view.has_interest = False
		video_view.has_implemented = False
		video_view.survey_at = timezone.now()
		video_view.recording_url = recording_url
		video_view.save()
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	return Response("hasInterest", status=status.HTTP_200_OK);

@api_view(['GET'])
def hasImplemented(request):
	print request.QUERY_PARAMS
	video_id = request.QUERY_PARAMS['CustomField']
	mobile_no = request.QUERY_PARAMS['From'][1:]
	recording_url = request.QUERY_PARAMS.get('RecordingUrl')

	try:
		video_view = VideoView.objects.get(video_id=video_id, mobile_no=mobile_no)
		video_view.has_interest = True
		video_view.has_implemented = True
		video_view.survey_at = timezone.now()
		video_view.recording_url = recording_url
		video_view.save()

	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	return Response("hasImplemented", status=status.HTTP_200_OK);

@api_view(['GET'])
def survey(request, video_id, mobile_no):
	try:
		video_view = VideoView.objects.get(video_id=video_id, mobile_no=mobile_no)
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	r = exotel.survey(
		settings.sid, settings.token,
		# agent_no="9718935868",
		#customerNo="9718935868",
		#customerNo="9972532929",
		#customerNo=mobile_no,
		customerNo=mobile_no,
		callerid="08033013384",
		url='http://my.exotel.in/exoml/start/23637',
		timelimit="500",  # This is optional
		timeout="500",  # This is also optional
		calltype="trans",  # Can be "trans" for transactional and "promo" for promotional content
		videoId=video_id

	)
	return Response(r.json(), status=r.status_code);