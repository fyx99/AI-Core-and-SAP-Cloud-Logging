from ai_api_client_sdk.ai_api_v2_client import AIAPIV2Client
import requests


ai_api_v2_client = AIAPIV2Client(
    base_url=AICORE_BASE_URL + "/lm", 
    auth_url=AICORE_AUTH_URL + "/oauth/token", 
    client_id=AICORE_CLIENT_ID,
    client_secret=AICORE_CLIENT_SECRET, 
    resource_group=AICORE_RESOURCE_GROUP
)



def get_response():
    res = requests.post(
        f"https://api.ai.internalprod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/dd57ca34bd22438c/v2/hello/",
        json={},
        headers={
            "Authorization": ai_api_v2_client.rest_client.get_token(),
            "ai-resource-group": AICORE_RESOURCE_GROUP,
            "Content-Type": "application/json"
        })
    if res.status_code != 200:
        raise Exception("ERROR WITH DEPLOYMENT " + str(res.status_code) + " " + str(res.content))
    return res.json()



if __name__ == "__main__":
    get_response()