
import requests
import json
import random


Challannumber = random.randint(12345, 987654 ) 
#https://www.geeksforgeeks.org/send-text-messages-to-any-mobile-number-using-fast2sms-api-in-python/

# mention url
url = "https://www.fast2sms.com/dev/bulk"


# create a dictionary
my_data = {
	# Your default Sender ID
	'sender_id': 'FSTSMS',
	
	# Put your message here!
	'message': 'your challan number is 53636363683 pls pay on paytm or google pay or contact on 73231422',
	
	'language': 'english',
	'route': 'p',
	
	
	'numbers': '9540609984'	
}

# create a dictionary
headers = {
	'authorization': 'NYX6I7e4HGrmjPBnUTwOvb09FoCa5SsxuZtJz3WiMgEKLph8fd7OXMlxSQIpAb9r2atGNekzhcPURyBu',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache" 
}
	

def Response():
	requests.request("POST",
							url,
							data = my_data,
							headers = headers)

#load json data from source

#returned_msg = json.loads(Response.text)

# print the send message