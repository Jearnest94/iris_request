import os
import requests
import json
import time

def response_to_json(response, name, calltype):
    i = 0
    while os.path.exists(f"./json/{name}_{calltype}_%s.json" % i):
        i += 1
    with open(f'./json/{name}_{calltype}_%s.json' % i, 'w') as f:
        json.dump(response, f)
        
def iris_request():
    url = f""
    response = requests.get(url, headers="").json()
    response_to_json(response, 'iris', f'test')
    return response


def main():
    pass

if __name__ == '__main__':
    main()
