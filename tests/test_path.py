from nose.tools import *

from tests import test_app

def test_home():
  result = test_app.get('/')
  eq_(result.data, "Hello World!")
  eq_(result.status_code, 200)

def test_name():
  result = test_app.get('/Yohannes')
  eq_(result.data, "Hello Yohannes!")
  eq_(result.status_code, 200)