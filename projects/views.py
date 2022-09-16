from django.shortcuts import render
from .import models
# Create your view
def Index(requst):
    req = object.get.all(models.Category)
    return (requst,'part/index.html',{'req':req})
