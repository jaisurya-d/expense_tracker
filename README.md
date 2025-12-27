# 📘 Django Day 2 -- Understanding HTTP Responses & URL Routing

## 📌 Lesson Overview

Day 2 focuses on how Django handles **HTTP requests and responses** and
how **URLs are mapped to views**. This lesson helps beginners understand
how Django sends data back to the browser or client.

------------------------------------------------------------------------

## 🎯 Topics Covered

-   Django Views
-   URL routing using `urls.py`
-   Project URL vs App URL
-   HTTP Response Types:
    -   HttpResponse
    -   JsonResponse
    -   HttpResponseNotFound (404)

------------------------------------------------------------------------

## 📊 HTTP Response Types Explained

  Response Type                   Status Code   Use Case
  ------------------------------- ------------- ----------------------
  HttpResponse                    200           Normal HTML response
  JsonResponse                    200           API / JSON response
  HttpResponseRedirect            302           Temporary redirect
  HttpResponsePermanentRedirect   301           Permanent redirect
  HttpResponseNotFound            404           Page not found
  HttpResponseForbidden           403           Access denied
  HttpResponseBadRequest          400           Invalid request
  HttpResponseServerError         500           Server error

------------------------------------------------------------------------

## 📁 Important Files

    expense_tracker/
    │
    ├── expense_tracker/
    │   └── urls.py
    │
    ├── app/
    │   ├── views.py
    │   └── urls.py

------------------------------------------------------------------------

## 🧠 Views Explanation (`app/views.py`)

### HttpResponse Example

``` python
def httpresponse(request):
    return HttpResponse('<h1>Hello All</h1>')
```

✔ Returns HTML content\
✔ Status Code: 200

------------------------------------------------------------------------

### JsonResponse Example

``` python
def jsonresponse(request):
    return JsonResponse({
        "status": "Success",
        "message": "hello all welcome to our course"
    })
```

✔ Used for API responses\
✔ Returns JSON data

------------------------------------------------------------------------

### 404 Not Found Example

``` python
def not_found_view(request):
    return HttpResponseNotFound("Page not found")
```

✔ Manually returns a 404 response

------------------------------------------------------------------------

## 🔗 App URLs (`app/urls.py`)

``` python
urlpatterns = [
    path('httpresponse/', httpresponse, name='httpresponse'),
    path('jsonresponse/', jsonresponse, name='jsonresponse'),
    path('', not_found_view, name='not_found_view'),
]
```

------------------------------------------------------------------------

## 🌐 Project URLs (`expense_tracker/urls.py`)

``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
```

------------------------------------------------------------------------

## ▶️ How to Run the Project

``` bash
python manage.py runserver
```

### Test URLs in Browser

-   http://127.0.0.1:8000/httpresponse/
-   http://127.0.0.1:8000/jsonresponse/
-   http://127.0.0.1:8000/

------------------------------------------------------------------------

## ✅ Day 2 Learning Outcomes

By the end of this lesson, students will be able to: - Understand Django
views - Connect URLs to views - Return HTML and JSON responses - Handle
404 errors

------------------------------------------------------------------------

🚀 **Next Lesson:** Django Models & Database (Day 3)
