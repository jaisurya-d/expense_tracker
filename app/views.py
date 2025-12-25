from django.http import JsonResponse,HttpResponse,HttpResponseNotFound
from django.shortcuts import render,redirect
from .models import Expense

from django.contrib.auth.models import User 

from django.contrib import messages

from django.contrib.auth import authenticate, login, logout as auth_logout

from django.contrib.auth.decorators import login_required   
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

@login_required(login_url='/home_page/')
def expense_register(request):
    if request.method == "POST":
        # Get data manually from POST
        expense_id = request.POST.get('expense_id',None)
        c_date = request.POST.get('date')
        category = request.POST.get('category')
        amount = request.POST.get('amount')
        comment = request.POST.get('comment')

        print("c_date --",c_date,"category --",category,'amount --',amount,'comment --',comment,"-----------------------------------",expense_id)
        if expense_id is None:
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

@login_required(login_url='/home_page/')
def delete_expense(request):
    if request.method == "POST":
        expense_id = request.POST.get('id')
        check = Expense.objects.filter(id = expense_id).delete()
        if check:
            return JsonResponse({"Status":"Success","Message":"Expense Deleted Successfully"})
        else:
            return JsonResponse({"Status":"Failed","Message":"Expense Not Deleted"})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Account created successfully. Please login.")
        # return HttpResponse("User Created Successfully")
        return render('login')

    return render(request, "auth/registration.html")
    
def login_page(request):
    # ✅ If already logged in → go to index
    if request.user.is_authenticated:
        return redirect("expense_register")

    # # ✅ AJAX POST (login)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request,'invalid credentials')
            return redirect('login')

        login(request, user)

        return redirect('expense_register')

    # ✅ Normal GET → show login page
    return render(request, "auth/login.html")

@login_required(login_url='/home_page/')
def logout(request):
    auth_logout(request)
    return redirect("/home_page/")