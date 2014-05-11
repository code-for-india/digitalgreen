from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from core.models import Video, Farmer, Address, VideoView
from core.serializers import VideoSerializer, FarmerSerializer, AddressSerializer, VideoViewSerializer
from rest_framework import permissions

#@permission_classes((permissions.IsAuthenticated,))

@api_view(['GET', 'POST'])
def video_list(request):
	"""
	List all video, or create a new video.
	"""
	if request.method == 'GET':
		videos = Video.objects.all()
		serializer = VideoSerializer(videos, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = VideoSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@permission_classes((permissions.IsAuthenticated,))

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk):
	"""
	Retrieve, update or delete a video.
	"""
	try:
		video = Video.objects.get(pk=pk)
	except Video.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = VideoSerializer(video)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = VideoSerializer(snippet, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		video.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def farmer_list(request):
	"""
	List all polls, or create a new farmer.
	"""
	if request.method == 'GET':
		farmers = Farmer.objects.all()
		serializer = FarmerSerializer(farmers, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = FarmerSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@permission_classes((permissions.IsAuthenticated,))

@api_view(['GET', 'PUT', 'DELETE'])
def farmer_detail(request, pk):
	"""
	Retrieve, update or delete a farmer.
	"""
	try:
		farmer = Farmer.objects.get(pk=pk)
	except Farmer.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = FarmerSerializer(farmer)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = FarmerSerializer(snippet, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		farmer.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def farmer_list_by_videoid(request, video_id):
	"""
	Get all farmers.
	?? How is get able to return multiple objects
	"""
	try:
		farmers = Farmer.objects.get(video_id=video_id)
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = VideoViewSerializer(farmers, many=True)
		return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def video_view(request, video_id, mobile_no):
	"""
	Retrieve, update or delete a video_view.
	"""
	try:
		video_view = VideoView.objects.get(video_id=video_id, mobile_no=mobile_no)
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = VideoViewSerializer(video_view)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = VideoViewSerializer(video_view, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		video_view.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def video_view_list_by_video_id(request, video_id):
	"""
	Get all a video_view.
	"""
	try:
		video_views = VideoView.objects.filter(video_id=video_id)
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = VideoViewSerializer(video_views, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def video_view_list_by_mobile_no(request, mobile_no):
	"""
	Get all a video_view.
	"""
	try:
		video_views = VideoView.objects.filter(mobile_no=mobile_no)
	except VideoView.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = VideoViewSerializer(video_views, many=True)
		return Response(serializer.data)

@api_view(['GET'])
def video_view_list(request):
	"""
	Get all a video_view.
	"""
	video_views = VideoView.objects.all()
	serializer = VideoViewSerializer(video_views, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def video_detail_with_context(request):
	"""
	Get all a video_view.
	"""
	response = []

	video_views = VideoView.objects.all()
	#serializer = VideoViewSerializer(video_views, many=True)
	for video_view in video_views:
		farmer = Farmer.objects.get(pk=video_view.mobile_no)
		video = Video.objects.get(pk=video_view.video_id)
		address = Address.objects.get(pk=farmer.address_id)
		response.append({'video_view': VideoViewSerializer(video_view).data, 'farmer': FarmerSerializer(farmer).data, 'video': VideoSerializer(video).data, 'address': AddressSerializer(address).data})
	return Response(response)