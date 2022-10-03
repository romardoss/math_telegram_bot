import requests

def main(message):
    headers = {"content-type": "application/json"}
    data = {}
    data["expr"] = message
    data["precision"] = 14
    
    result = requests.post("https://api.mathjs.org/v4/", json = data, headers=headers).text
    result = result.replace('{"result":"', '')
    result = result.replace('","error":null}', '')
    
    print(result + "\n")

    if result[0] == "{":
        return "error"
    return result
