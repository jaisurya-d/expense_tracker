# Day 3 -- Django Models & Admin Panel

## Overview

In this lesson, we learned how to: - Create a Django model - Understand
different Django field types - Register a model in the Django admin
panel - View and manage data using Django Admin

## Files Explained

### `models.py`

This file defines the database structure using Django models.

We created an **Expense** model with the following fields: - `category`
-- Expense category (Food, Travel, etc.) - `amount` -- Expense amount
using DecimalField - `date` -- Date of the expense - `comment` -- Short
description - `created_at` -- Automatically stores record creation time

The `__str__` method helps display readable data in the admin panel.

### `admin.py`

This file registers the Expense model so it can be managed via Django
Admin.

``` python
admin.site.register(Expense)
```

## Commands Used

``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Result

You can now add, view, edit, and delete expenses from the Django Admin
Panel.

------------------------------------------------------------------------

Happy Learning 🚀
