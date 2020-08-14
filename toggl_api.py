# https://github.com/toggl/toggl_api_docs/blob/master/toggl_api.md
# https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request

# https://github.com/toggl/toggl_api_docs/blob/master/reports.md

import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode
from env_variables import get_variables


def get_full_url(endpoint, params, reports=False):
    api_url = "https://www.toggl.com/"

    api_version = 8
    reports_api_version = 2

    if reports:
        api_url += "reports/api/v{}".format(reports_api_version)
    else:
        api_url += "api/v{}".format(api_version)

    endpoint_url = "{api}/{endpoint}".format(api=api_url, endpoint=endpoint)

    if len(params):
        return endpoint_url + "?" + urlencode(params)
    else:
        return endpoint_url


def get(endpoint, params, reports=False):
    url = get_full_url(endpoint, params, reports)
    api_key = get_variables()["toggl_api_key"]

    print("url", url)
    print("api_key", api_key)

    request = requests.get(url,
                           headers={'content-type': 'application/json'},
                           auth=HTTPBasicAuth(api_key, 'api_token'))

    return request.content


def get_weekly_report():
    return get("weekly", {"user_agent": "wildeastengineer@gmail.com",
                          "workspace_id": 1519631}, True)


print(get_weekly_report())
