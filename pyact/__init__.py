# api for the html element for pycharm for exemple
import inspect

class element:     
  def customElement(func):
      def inner1(*args, **kwargs):
          returned_value = func(*args, **kwargs)
          return returned_value
           
      return inner1
