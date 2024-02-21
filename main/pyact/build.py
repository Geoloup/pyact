import os
import requests
import threading

class build:
    def __init__(self,filename):
        try:
            os.mkdir('JSbuild/')
            print('building')
        except:
            print('rebuilding')
        #os.chdir('JSbuild/')
        self.builder(filename)
    def builder(self,filepath):
        directory = filepath
        files_and_dirs = os.listdir(directory)
        for file in files_and_dirs:
            file_path = os.path.join(directory, file)
            if os.path.isfile(file_path):
                if file_path.endswith(".pyact") or file_path.endswith(".py"):
                    print(file_path)
                    self.buildFile(file_path)
                else:
                    self.BuildFolder().start()
    def BuildFolder():
        class folderT(threading):
            def __init__(self,builderT):
                super()
                self.builderT = builderT
            def run(self,folderPath):
                directory = folderPath
                builderT = self.builderT
                files_and_dirs = os.listdir(directory)
                for file in files_and_dirs:
                    file_path = os.path.join(directory, file)
                    if os.path.isfile(file_path):
                        if file_path.endswith(".pyact") or file_path.endswith(".py"):
                            print(file_path)
                            buildFile(file_path)
                    else:
                        builderT(builderT).start()
        folderT(folderT).run()
                        

    def buildFile(self,path):
        url = "https://api.extendsclass.com/convert/python/es6"
        headers = {
            "Content-Type": "text/plain;charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
        }
        file = open(path,'r').read()
        data = {
            "body": file
        }
        response = requests.post(url, headers=headers, data=data)
        if response.ok:
            data = response.json()
            js =  data['stdout']
        else:
            print("Error fetching data:", response.status_code, response.reason)
        try:
            n = open('JSbuild/' + path,'w')
        except:
            n = open('JSbuild/' + path,'w')
        n.write(js)
        n.close()