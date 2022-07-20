import os
import json
import requests

iexec_out = os.environ['IEXEC_OUT']
api_key = os.environ["IEXEC_APP_DEVELOPER_SECRET"]
recipient = os.environ["IEXEC_REQUESTER_SECRET_1"]
message = os.environ["IEXEC_REQUESTER_SECRET_2"]

url = 'https://api.mailjet.com/v4/sms-send'
headers = {
    'Authorization': 'Bearer %s' % api_key,
    'content-type': 'application/json'
}
data = {
    "From": "Secret",
    "To": recipient,
    "Text": message
}

response = requests.post(url, headers=headers, data=json.dumps(data))

with open(iexec_out + '/result.txt', 'w+') as fout:
    fout.write(str(json.loads(response.content)["Status"]))

with open(iexec_out + '/computed.json', 'w+') as f:
    json.dump({"deterministic-output-path": iexec_out + '/result.txt'}, f)
