#!/bin/usr/python3

import requests

TOKEN_VALUE = 'Token DEFECTDOJO_TOKEN' #do not forget to use environment variable here
url = "http://13.38.200.191:8080/api/v2/import-scan/"
scan_type = "scan_type_value"

#scan_payload
payload = {
	"headers": {"Authorization":f"{TOKEN_VALUE}"},
	"required_value":{
	"scan_type": f"{scan_type}",
	"engagement":1,
	"minimum_severity":"Info",
	"active":True,
	"verified":True,
	"deduplication_on_engagement":True,
	},
	"files": {'file': open('file_to_import')}
}

#importing
print(f"Importing {scan_type}")
req_import_scan = requests.post(url,files=payload['files'], headers=payload['headers'],data=payload['required_value'])
print(req_import_scan.status_code)
print(req_import_scan.text)
