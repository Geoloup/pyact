# Welcome to *pyact*
**pyact is a web framework made in python for python dev. 
Simplicity first.**
## installation
just do in terminal : `pip install pyract`
## Api    
All the api class
> window
> 
> Document
> 
> Element

To import the api you can do this `from pyact.api import *` or `import pyact.api as pyact`

## Build the files

first make a setup.py .
Then in this file do `import pyact.build` and `pyact.build.build('main/')` change 'main.py' by the main directory
**or**
go to `.github/workflows/build.yml` and copy the file content in you're main branch 
 
Build api
> Build

 **please note that build pyact does not support class in class.*
