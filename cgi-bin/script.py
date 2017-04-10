#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
import sys
import boto3
from boto3.session import Session

rds = boto3.setup_default_session(region_name='us-east-1')
client = boto3.client('sns')
sns = boto3.resource('sns')
topic_arn='arn:aws:sns:us-east-1:022267260148:166class'
topic = sns.Topic(topic_arn)


form = cgi.FieldStorage() 

# Get data from fields
thenumber = form.getvalue('number')



response = topic.subscribe(Protocol='sms', Endpoint=thenumber) 










print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "</head>"
print "<body>"
print "</body>"
print "</html>"
