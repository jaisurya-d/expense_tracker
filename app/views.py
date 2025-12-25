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
        expense_id = request.POST.get('expense_id',None)
        c_date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        comment = request.POST.get('comment')

        print("c_date --",c_date,"category --",category,'amount --',amount,'comment --',comment,"-----------------------------------",expense_id)
        if expense_id is None or expense_id == "":
        # Save to database
            Expense.objects.create(
                date=c_date,
                category=category,
                amount=amount,
                comment=comment,
            )
            return redirect('expense_register')  # reload page after saving
        else:
            Expense.objects.filter(id = expense_id).update( date=c_date,
                category=category,
                amount=amount,
                comment=comment,)
            return redirect('expense_register')  # reload page after saving



        # Fetch all expenses
    # if request.method == "GET":
    expenses = Expense.objects.all().order_by('-date')
    for expense in expenses:
        expense.date = expense.date.isoformat()     

    context = {'expenses': expenses}

    return render(request,'expense_register.html',context)

def delete_expense(request):
    if request.method == "POST":
        expense_id = request.POST.get('id')
        check = Expense.objects.filter(id = expense_id).delete()
        if check:
            return JsonResponse({"Status":"Success","Message":"Expense Deleted Successfully"})
        else:
            return JsonResponse({"Status":"Failed","Message":"Expense Not Deleted"})
    
