from django.shortcuts import render

# Create your view
def Index(requst):
    return (requst,'index.html',{'req':req})
