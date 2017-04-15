


import sys
import boto3
from boto3.session import Session



sns = boto3.resource('sns')
topic_arn='topic arn'
topic = sns.Topic(topic_arn)

mess_text = sys.argv[1] 

response = topic.publish(
 
    topic_arn,
    Message=mess_text
)
 
 


