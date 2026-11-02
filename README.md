# ai-box-selection
AI-Assisted Box Selection System using Python and Django
# AI-Assisted Box Selection System

## 1. Project Overview

The AI-Assisted Box Selection System is a Django-based web application
that recommends a suitable, cost-effective shipping box for an ecommerce
order.

The current recommendation logic checks:

-   Total order weight against the box's maximum weight.
-   Whether each product can fit inside the box, allowing rotation by
    comparing sorted dimensions.
-   Whether the combined product volume is within the box's internal
    volume.
-   The cost of suitable boxes, and selects the lowest-cost option.

> **Important limitation:** The volume check is an approximation. It
> does not perform exact 3D bin packing and cannot guarantee that
> multiple products can physically be arranged together without overlap.

## 2. Technologies Used

-   Python
-   Django 5.2.18
-   SQLite (default Django database)
-   Django Admin
-   Django `JsonResponse` API
-   Windows 10
-   Visual Studio Code (if used)

## 3. Project Structure

``` text
ai-box-selection/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── box_selector/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── services.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── venv/                 # Local virtual environment; do not upload to GitHub
├── db.sqlite3            # Local development database; usually do not upload
├── manage.py
├── README.md
└── AI_USAGE.md           # Add this file with your actual AI-use record
```

## 4. Requirements

-   Windows 10
-   Python installed and available from PowerShell (`python --version`)
-   pip (comes with most Python installations)
-   Internet connection for installing Django

## 5. Setup Instructions (Windows 10 / PowerShell)

Open **Windows PowerShell** or the VS Code terminal using PowerShell.

### Step 1: Open the project folder

If you have already downloaded or extracted the project:

``` powershell
cd "C:\Users\YOUR_USERNAME\Desktop\Assignment\ai-box-selection"
```

Replace `YOUR_USERNAME` with your Windows account folder name.

### Step 2: Create a virtual environment

``` powershell
python -m venv venv
```

### Step 3: Activate the virtual environment

``` powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks script activation, run the following command once
for your current Windows user:

``` powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

If prompted, confirm the change, then activate the environment again:

``` powershell
.\venv\Scripts\Activate.ps1
```

When activated, `(venv)` should appear at the beginning of the
PowerShell prompt.

### Step 4: Install Django

``` powershell
python -m pip install --upgrade pip
python -m pip install Django==5.2.18
```

### Step 5: Apply database migrations

``` powershell
python manage.py migrate
```

### Step 6: Create an admin user

``` powershell
python manage.py createsuperuser
```

Follow the prompts to set the username, email (if requested), and
password.

### Step 7: Start the development server

``` powershell
python manage.py runserver
```

Open the following address in your browser:

-   Application server: http://127.0.0.1:8000/
-   Django Admin: http://127.0.0.1:8000/admin/

The root page (`/`) may show Django's 404 page because no home-page
route has been configured. Use the API endpoint below to test the
application.

To stop the server, press `CTRL + C` in PowerShell.

## 6. Add Sample Data Through Django Admin

1.  Open http://127.0.0.1:8000/admin/.
2.  Sign in using the superuser account.
3.  Add products under **Products**.
4.  Add shipping boxes under **Box**.
5.  Create an order under **Orders**.
6.  Add one or more order items and set each product quantity.

Product fields: - Name - Length - Width - Height - Weight

Box fields: - Name - Length - Width - Height - Maximum weight - Cost

Use consistent measurement units for all dimensions and weights. The
sample data used during development uses centimetres for dimensions,
kilograms for weight, and the cost in the chosen currency.

## 7. API Endpoint

**Method:** `GET`

**Endpoint:**

``` text
http://127.0.0.1:8000/api/orders/1/recommend-box/
```

Replace `1` with the actual order ID.

The API returns the order ID, total order weight, recommended box
details, and a status message.

### Example successful response

``` json
{
    "order_id": 1,
    "total_weight": 1.3,
    "recommended_box": {
        "name": "Small Box",
        "cost": "20.00",
        "dimensions": {
            "length": 30.0,
            "width": 25.0,
            "height": 15.0
        }
    },
    "message": "Suitable box found successfully"
}
```

If no suitable box is found, `recommended_box` is `null` and the message
is `No suitable box found`.

If the order ID does not exist, the API returns HTTP 404.

## 8. Run Automated Tests

Stop the development server if it is running, then run:

``` powershell
python manage.py test box_selector
```

The test suite checks recommendation logic and API behaviour. The
current development test run completed with **10 tests passing**.

## 9. Recommendation Logic and Assumptions

1.  The system retrieves the products and quantities in an order.
2.  It calculates total order weight.
3.  It calculates the combined product volume, including quantities.
4.  It checks each product's dimensions against the box dimensions.
    Sorting the dimensions allows the product to be rotated.
5.  It rejects boxes that exceed weight capacity, cannot fit an
    individual product, or have insufficient total volume.
6.  It selects the suitable box with the lowest cost.
7.  An empty order returns no recommendation.

### Known limitation

This is a simplified box-selection approach, not an exact 3D packing
solver. A total-volume check and individual dimension checks are
necessary filters, but they are not sufficient to prove that all
products can be physically arranged inside one box. This limitation
should be considered before using the system in a real warehouse.

## 10. GitHub Submission Notes

Before uploading the project to GitHub:

-   Include the Django source code, migrations, `README.md`,
    `AI_USAGE.md`, test files, and the required actual exported chat
    transcript.
-   Do not upload the `venv/` folder.
-   Do not upload passwords, secret keys, or other credentials.
-   Normally exclude the local `db.sqlite3` file unless the assignment
    instructions specifically require a sample database.
-   Add a `requirements.txt` file so dependencies can be installed
    consistently:

``` powershell
python -m pip freeze > requirements.txt
```

Then another user can install the listed dependencies using:

``` powershell
python -m pip install -r requirements.txt
```

Update this README if the implementation, dependencies, or API behaviour
changes.
