import os
import requests

class build:
    def __init__(self,filename):
        code = open('build.pyon','r').read()
        try:
            os.mkdir('JSbuild/')
            print('building')
        except:
            print('rebuilding')
        os.chdir('JSbuild/')
    def builder(self):
        directory = '/path/to/your/directory'
        files_and_dirs = os.listdir(directory)
        for file in files_and_dirs:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if file_path.endswith(".pyact") or file_path.endswith(".py"):
                    print(file_path)
                    self.buildFile(file_path)
    def buildFile(self,path):
        url = "https://api.extendsclass.com/convert/python/es6"
        headers = {
            "Content-Type": "text/plain;charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
        }
        file = open('path','r').read()
        data = {
            "body": file
        }

        response = requests.post(url, headers=headers, data=data)

        if response.ok:
            data = response.json()
            js =  data['stdout']
        else:
            print("Error fetching data:", response.status_code, response.reason)
        open('')