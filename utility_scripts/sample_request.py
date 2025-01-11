from ai_api_client_sdk.ai_api_v2_client import AIAPIV2Client
import requests


AICORE_AUTH_URL =  "https://<auth_tenant>.authentication.sap.hana.ondemand.com"
AICORE_CLIENT_ID = "<client_id>"
AICORE_CLIENT_SECRET = "<client_secret>"
AICORE_RESOURCE_GROUP = "<resource_group>"
AICORE_BASE_URL = "https://api.ai.<region>.ml.hana.ondemand.com/v2"

ai_api_v2_client = AIAPIV2Client(
    base_url=AICORE_BASE_URL + "/lm", 
    auth_url=AICORE_AUTH_URL + "/oauth/token", 
    client_id=AICORE_CLIENT_ID,
    client_secret=AICORE_CLIENT_SECRET, 
    resource_group=AICORE_RESOURCE_GROUP
)



def get_response():
    res = requests.post(
        f"https://api.ai.internalprod.eu-central-1.aws.ml.hana.ondemand.com/v2/inference/deployments/dfe12a3f001337b6/v2/predict/",
        json={},
        headers={
            "Authorization": ai_api_v2_client.rest_client.get_token(),
            "ai-resource-group": AICORE_RESOURCE_GROUP,
            "Content-Type": "application/json"
        })
    if res.status_code != 200:
        raise Exception("ERROR WITH DEPLOYMENT " + str(res.status_code) + " " + str(res.content))
    print(res.json())
    return res.json()



if __name__ == "__main__":
    get_response()