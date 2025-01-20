import boto3
from src.modules.challenge.app.compose_email_charles import compose_email_charles
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from base64 import b64encode, b64decode
import io
import boto3

def lambda_handler(event, context):

    s3 = boto3.client('s3')

    result = s3.get_object(Bucket='challenge-storage-devcommunitymaua', Key='kick buttowski.png')
    
    result_body = result["Body"].read()

    pic_64 = str(b64encode(result_body))[2:-1]

    charles_email_html = compose_email_charles(pic_64)

    client_ses = boto3.client('ses', region_name="sa-east-1")

    response = client_ses.send_email(
                Destination={
                    'ToAddresses': [
                        "mcapaldo.devmaua@gmail.com",
                        "22.01082-3@maua.br"
                    ],
                    'CcAddresses': [
                        "21.01444-2@maua.br",
                        "vgsoller@gmail.com",
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': "UTF-8",
                            'Data': charles_email_html,
                        },
                    },
                    'Subject': {
                        'Charset': "UTF-8",
                        'Data': "Email do Charles",
                    },
                },
                Source="contato@devmaua.com",
            )
    
    return LambdaHttpResponse(status_code=200, body=response)