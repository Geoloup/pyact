import os

class build:
    def __init__(self,filename):
        code = open('build.pyon','r').read()
        try:
            os.mkdir('JSbuild/')
            print('building')
        except:
            print('rebuilding')
        os.chdir('JSbuild/')