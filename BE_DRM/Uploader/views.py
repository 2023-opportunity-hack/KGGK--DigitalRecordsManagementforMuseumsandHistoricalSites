import boto3
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def upload_to_s3(request):
    file = request.FILES['file']
    uploadedAt = request.data['uploadedAt']
    keyWords = request.data['keyWords']
    try:
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        s3.upload_fileobj(file, settings.AWS_STORAGE_BUCKET_NAME, file.name)
        s3Url = f'https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file.name}'
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        table = dynamodb.Table('DRM')
        response = table.put_item(
            Item = {
                'id': 1,
                'fileName': file.name,
                's3Url': s3Url,
                'uploadedAt': uploadedAt,
                'keyWords': keyWords
            }
        )
        return Response({
            'success': True,
            'metaData': response,
            'message': 'File uploaded successfully'
        })
    except Exception as e:
        return Response({
            'success': False, 
            'message': str(e)
        })

@api_view(['GET'])
def searchFile(request):
    try:
        searchText = request.GET['searchText']
        dynamodb = boto3.client(
            'dynamodb',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )
        response = dynamodb.scan(
            TableName = 'DRM',
            FilterExpression = 'contains(keyWords, :value)',
            ExpressionAttributeValues = {
                ':value': {'S' : searchText}
            }
        )
        return Response({
            'success': False, 
            'metaData': response,
            'message': 'Data search completed successfully'
        })
    except Exception as e:
        return Response({
            'success': False, 
            'message': str(e)
        })