import json
import boto3

def lambda_handler(event, context):
    
    ssm = boto3.client('ssm')
    username = ssm.get_parameter(Name='/username')
    print(username['Parameter']['Value'])
    password = ssm.get_parameter(Name='/password', WithDecryption=True)
    print(password['Parameter']['Value'])
    pwdcustom = ssm.get_parameter(Name='/pwd-custom', WithDecryption=True)
    print(pwdcustom['Parameter']['Value'])
