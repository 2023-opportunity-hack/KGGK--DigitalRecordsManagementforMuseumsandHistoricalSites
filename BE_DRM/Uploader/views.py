import boto3
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def upload_to_s3(request):
    file = request.FILES['file']
    # address = request.address
    # uploadedAt = request.uploadedAt
    # keyWords = request.keyWords
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
        # s3Url = "https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file.name}"
        return Response({
            'success': True,
            'message': 'File uploaded successfully'
        })
    except Exception as e:
        return Response({
            'success': False, 
            'message': str(e)
        })

@api_view(['GET'])
def searchFile(request):
    print('hello', request.GET)
    try:
        return Response({
            'success': False, 
            'message': 'Working!!!'
        })
    except Exception as e:
        return Response({
            'success': False, 
            'message': str(e)
        })