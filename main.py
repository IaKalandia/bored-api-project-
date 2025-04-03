import requests

url = "https://www.boredapi.com/api/activity/"

response = requests.get(url)

# print status code and response before decoding
print(f"status code: {response.status_code}")
print("Row response text:")
print(response.text[:100]) # only show first 100 chars for readability

#only try to decode if the response is ok

if response.status_code == 200:
    try: 
        data = response.json()
        print("here is something to do:")
        print(f"{data['activity']}")
    except ValueError:
        print("failed to decode json response")

else:
    print(f"failed to fetch data: {response.status_code}")

