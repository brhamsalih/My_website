from django.shortcuts import render

# Create your view
def Index(requst):
    req = 1234
    return render(requst,'projects/index.html',{'req':req})
