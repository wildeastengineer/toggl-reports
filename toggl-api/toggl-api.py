# https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md
# https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request

# https://github.com/toggl/toggl_api_docs/blob/master/reports.md

import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode


api_url = "https://www.toggl.com/api"
api_version = 8

api_token = ""
headers = {'content-type': 'application/json'}


def get_full_url(endpoint, params):
    endpoint_url = "{api}/v{version}/{endpoint}".format(api=api_url, version=api_version, endpoint=endpoint)

    if len(params):
        return endpoint_url + "?" + urlencode(params)
    else:
        return endpoint_url


url = get_full_url("time_entries", {'time_entry': {'start': '2020-02-05T15:42:46+02:00',
                                                   'duration': '1200'}})

print("url", url)

request = requests.get(url, headers=headers, auth=HTTPBasicAuth(api_token, 'api_token'))

print(request.content)
