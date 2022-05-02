# import required module
import requests
import json
import seatbelt
'''refrence 
https://www.geeksforgeeks.org/send-text-messages-to-any-mobile-number-using-fast2sms-api-in-python/?ref=rp'''

# mention url
url = "https://www.fast2sms.com/dev/bulk"


# create a dictionary
my_data = {
	# Your default Sender ID
	'sender_id': 'FSTSMS',
	
	# Put your message here!
	'message': 'This is a test message',
	
	'language': 'english',
	'route': 'p',
	
	# You can send sms to multiple numbers
	# separated by comma.
	'numbers': '9540609984'	
}

# create a dictionary
headers = {
	'authorization': 'na',
	'Content-Type': "application/x-www-form-urlencoded",
	'Cache-Control': "no-cache"
}

####NYX6I7e4HGrmjPBnUTwOvb09FoCa5SsxuZtJz3WiMgEKLph8fd7OXMlxSQIpAb9r2atGNekzhcPURyBu#####


# make a post request
response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)
#
#load json data from source
returned_msg = json.loads(response.text)
  
# print the send message
print(returned_msg['message'])