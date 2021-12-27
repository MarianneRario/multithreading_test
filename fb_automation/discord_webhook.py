import requests
import json

from pyngrok import ngrok

webhook_url = ""

public_url = ngrok.connect(5000).public_url
# print(public_url)


def webhook(url, thread_id, url_extension):
    data = {"content": public_url + url_extension, "username": "MR.Ario",
            "embeds": [
                {
                    "description": "Request output",
                    "title": f"Output for Thread ID {thread_id}",
                    "url": url
                }
            ]}
    result = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

