import urllib2
import json 

data =  {

        "Inputs": {

                "input1":
                {
                    "ColumnNames": ["zip", "Corporation", "LLC*Limited Liability Co", "Sole Proprietor", "Partnership", "LLP*Limited Liability Partners", "Other", "Corporation/Nonprofit", "PLLC*Prof Limited Liability Co", "Municipal", "Partnership/Nonprofit", "Crime", "Landmarks", "Parks", "Libraries", "High Schools", "Traffic Cameras", "Picnic Sites", "Childrens Play Areas", "Hospitals", "Schools"],
                    "Values": [ [ "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], [ "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0" ], ]
                },        },
            "GlobalParameters": {
}
    }

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/b3cd0145cd0e4b0ba66a00d5ee5c0233/services/ab6c186ce5be4c60812701cf87aefb93/execute?api-version=2.0&details=true'
api_key = 'YGktXXGjUVY84rfw1F6dXEuZg0E9enlHCamRghBI1tEa6vd8xQ3iz1VBn71hFgB1Z+0kr4x2eNnaJCTQ75+iEg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib2.Request(url, body, headers) 

try:
    response = urllib2.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib2.HTTPError, error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))                 