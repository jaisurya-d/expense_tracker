### Django Day 2 – Understanding HTTP Responses & URLs

This project demonstrates basic Django response types and URL routing.
It is designed for beginners to understand how Django handles different kinds of HTTP responses.

### Topics Covered

- Django URL configuration
- HttpResponse
- JsonResponse
- HttpResponseNotFound (404)
- Basic project and app URL integration

### Response Types Explained

| Response Type                 | Status Code | Use Case             |
| ----------------------------- | ----------- | -------------------- |
| HttpResponse                  | 200         | Normal HTML response |
| JsonResponse                  | 200         | API / JSON response  |
| HttpResponseRedirect          | 302         | Temporary redirect   |
| HttpResponsePermanentRedirect | 301         | Permanent redirect   |
| HttpResponseNotFound          | 404         | Page not found       |
| HttpResponseForbidden         | 403         | Access denied        |
| HttpResponseBadRequest        | 400         | Invalid request      |
| HttpResponseServerError       | 500         | Server error         |

### Views (app/views.py)
- HttpResponse Example
- JsonResponse Example
- 404 Not Found Response

### App URLs (app/urls.py)
    path('httpresponse/', httpresponse, name='httpresponse'),
    path('jsonresponse/', jsonresponse, name='jsonresponse'),
    path('', not_found_view, name='not_found_view')

### Project URLs (expense_tracker/urls.py)
     path('', include('app.urls'))

### How to Check
  Run the server
    
    python manage.py runserver

  Open in browser:

    http://127.0.0.1:8000/httpresponse/
    http://127.0.0.1:8000/jsonresponse/
    http://127.0.0.1:8000/


### Day 2 Learning Objectives

By the end of Day 2, you should be able to:
- Understand what a view is in Django
- Understand what a URL is and how Django connects URLs to views
- Use different HTTP response types
- Return HTML and JSON responses
- Handle a 404 – Page Not Found response
