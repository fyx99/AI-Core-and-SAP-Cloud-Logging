from ai_api_client_sdk.ai_api_v2_client import AIAPIV2Client
import requests


AICORE_AUTH_URL =  "https://testd070430.authentication.sap.hana.ondemand.com"
AICORE_CLIENT_ID = "sb-c169cc1b-a141-4861-9af7-bee90cd06200!b13079|xsuaa_std!b77089"
AICORE_CLIENT_SECRET = "cec821ba-09d5-4435-ab77-a36d0d3aa8fb$QX666MHlGjwiuB7MlC--SOI2-7qUw-F5_MtXAAcB310="
AICORE_RESOURCE_GROUP = "generative-ai-hub"
AICORE_BASE_URL = "https://api.ai.internalprod.eu-central-1.aws.ml.hana.ondemand.com/v2"

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