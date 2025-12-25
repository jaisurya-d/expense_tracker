from django.http import JsonResponse,HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect
from .models import Expense

# Create your views here.
"""
| Response Type                 | Status Code | Use Case           |
| ----------------------------- | ----------- | ------------------ |
| HttpResponse                  | 200         | Normal response    |
| JsonResponse                  | 200         | API response       |
| HttpResponseRedirect          | 302         | Temporary redirect |
| HttpResponsePermanentRedirect | 301         | Permanent redirect |
| HttpResponseNotFound          | 404         | Not found          | Page not found
| HttpResponseForbidden         | 403         | Forbidden          | You are not allowed here
| HttpResponseBadRequest        | 400         | Bad request        | Invalid request
| HttpResponseServerError       | 500         | Server error       | Server error occurred
"""

# def httpresponse(request):
#     print('Hello all welcome to our course')
#     return HttpResponse('<h1>hello all</h1>')

# def jsonresponse(request):
#         return JsonResponse({
#         "status": "Success",
#         "message": "hello all welcome to our course"
#     })

# def not_found_view(request):
#     return HttpResponseNotFound("Page not found")

def index(request):
    return render(request,'index.html')

def home_page(request):
    return render(request,'home_page.html',{'user':"Jaisurya"})

def expense_register(request):
    if request.method == "POST":
        # Get data manually from POST
        c_date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        comment = request.POST.get('comment')

        print("c_date --",c_date,"category --",category,'amount --',amount,'comment --',comment)

    return render(request,'expense_register.html')