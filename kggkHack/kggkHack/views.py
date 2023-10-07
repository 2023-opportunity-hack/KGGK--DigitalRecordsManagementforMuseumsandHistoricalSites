import os
import boto3
from django.conf import settings
from django.http import JsonResponse


def upload_to_s3(request):
    # if request.method == 'POST':
        
        print("hello from fun")
        s3 = boto3.client(
            's3',
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            region_name=settings.AWS_S3_REGION_NAME
        )

        try:
            file_path = '/Users/khiladi/Documents/GitHub/KGGK--DigitalRecordsManagementforMuseumsandHistoricalSites/kggkHack/pages/file1.pdf'
            filename = os.path.basename(file_path)
            with open(file_path, 'rb') as file_obj:
                s3.upload_fileobj(file_obj, settings.AWS_STORAGE_BUCKET_NAME,filename )
            return JsonResponse({'success': True, 'message': 'File uploaded successfully'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})



# result = upload_to_s3()
# if result['success']:
#     print("File uploaded successfully")
# else:
#     print("File upload failed. Error: ", result['message'])
