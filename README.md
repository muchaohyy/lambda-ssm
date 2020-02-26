# lambda-ssm
This is to demo how to access ssm from lambda<br>
#### 1. Log into AWS account
#### 2. Search for KMS and click through
#### 3. Create a customied key with key type = 'Symmetric', give a name as 'ssm-custom', choose key administrators as the user you are using. But at this stage, do not give any usage permission. You can review your key policy at the end and leave it as it is.
#### 4. In AWS console,search for AWS Systems Manager and click through
#### 5. Choose Parameter Store and create parameter, and create three parameters called username, password, pwd-custom
username -- choose String
password -- choose SecureString and choose aws managed key aws/ssm
pwd-cust -- choose SecureString and choose customer managed key ssm-custom
#### 6. In AWS console, search lambda and click through
#### 7. Create a lambda in python3.8 with all default set up
#### 8. Copy the code into lambda
#### 9. Modify the parameter name if you are using different name.
#### 10. Run the lambda and check the result.
The result will not show the value of username, password or pwd-cust<br>
The reason is by default lambda does not have permission to access ssm
#### 11. In the role that your lambda using, simply modify it by adding AmazonSSMReadOnlyAccess
#### 12. Run the lambda again and check the result
The result will show the value of username, password but not pwd-cust<br>
The reason is you need the key in KMS to decrypt your SecureString in ssm; however, by default AWS managed key can be accessed but not for customized key<br>
You need to modify the policy of customized key and let it be used by your lambda
#### 13. In AWS console, search KMS and click through
#### 14. Click your customized key, add your lambda role into key user and save
#### 15. Run the lambda again and check the result
In this time, you should be able to see all the values of username, password and pwd-cust
