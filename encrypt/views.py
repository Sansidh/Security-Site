from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import hashlib
from .forms import MD5Form
# Create your views here.

def hello(request, num):
   text = """<h1>welcome to my app !: %s</h1>"""%num
   num3 = float(num)**(1/2)
   text+="\nThe sqaure root of given number is %f"%num3
   return render(request, "hello.html", {"num3" : num3})

def home(request):
	text ="Welcome to my Homepage"
	return render(request, "home.html")

def hashing(request, input):
	result = hashlib.md5()
	result.update(input.encode('utf-8'))
	output = result.hexdigest()
	return HttpResponse("The md5 hash of the given input is : %s "%output)
# def home1(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = MD5Form(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             output = form.process()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/%s'%output)

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = MD5Form(request.GET)
#         form.hashed == form.process()

#     return render(request, 'test.html', {'form': form})