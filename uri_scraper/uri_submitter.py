# -*- coding: utf-8 -*-
import requests
from lxml import html

USERNAME = "rdcmdev@gmail.com"
PASSWORD = "10c07230"
LOGIN_URL = "https://www.urionlinejudge.com.br/judge/en/login"
SUBMISSION_URL = "https://www.urionlinejudge.com.br/judge/en/runs/add"


session_requests = requests.session()

# Get login csrf token
result = session_requests.get(LOGIN_URL)
tree = html.fromstring(result.text)

form_token_data = {
    "_csrfToken": tree.xpath("//input[@name='_csrfToken']/@value")[0],
    "_Token[fields]": tree.xpath("//input[@name='_Token[fields]']/@value")[0],
    "_Token[unlocked]": tree.xpath("//input[@name='_Token[unlocked]']/@value")[
        0
    ],
}

# Perform login
result = session_requests.post(
    LOGIN_URL,
    data={
        "email": USERNAME,
        "password": PASSWORD,
        **form_token_data,
    },
)

# Submit
result = session_requests.post(
    SUBMISSION_URL,
    data={
        "problem_id": "1000",
        "language_id": "20",
        "source_code": 'print("Hello World!")',
        "template": "1",
        **form_token_data,
    },
)
