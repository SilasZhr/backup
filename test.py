import requests
import json



list = []
with open("links", "r") as f:
    for i in f.readlines():
        code = i.strip().split('/')[-1]
        #print(code)
        list.append({"id":code})
url = 'https://us-central1-cedge-poap.cloudfunctions.net/app/add-poap-codes?event=cedge'
print(list)
payload = json.dumps(list)
headers = {
  'Authorization': 'OAuth oauth_consumer_key="74EhuXTeRyQjwzNkKYzE5VbQB",oauth_token="765768616893640704-70B3XeoLnpL11Wisi60Ezl7KDwCamUn",oauth_signature_method="HMAC-SHA1",oauth_timestamp="1624253558",oauth_nonce="4KtDy2fawyQ",oauth_version="1.0",oauth_signature="GylFEdmFzxIvZ869pfFv9AtTqWo%3D"',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
