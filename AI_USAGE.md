# AI_USAGE.md

## 1. AI Tool Used

- Tool: ChatGPT
- Purpose: Learning Django, understanding the assignment, debugging errors, improving the box recommendation logic, and preparing documentation.

## 2. How AI Was Used

ChatGPT was used for guidance during project development.

The following tasks were completed with AI assistance:

- Understanding Django project setup.
- Creating and understanding Django models.
- Developing the box recommendation service.
- Creating API views and URL routes.
- Writing automated test cases.
- Improving the recommendation logic with weight and volume checks.
- Preparing README documentation.

## 3. Example Prompts Used

The following are examples of prompts used during the actual development conversation:

1. "Guide me step by step to develop the AI-Assisted Box Selection System using Django."
2. "Explain how to create the Django models for products, boxes, and orders."
3. "Help me implement the box recommendation logic."
4. "Help me add test cases for the box recommendation system."
5. "Explain how to improve the logic for multiple products."
6. "Help me prepare a beginner-friendly README for Windows 10."

Check these examples against your actual ChatGPT conversation and replace or remove any prompt that you did not use.

## 4. AI Suggestions Accepted and Modified

- Used guidance for Django project setup and application structure.
- Used suggestions for product, box, order, and order-item models.
- Used guidance to create the recommendation API.
- Modified the recommendation logic to check total weight and combined product volume.
- Added automated tests and verified them by running Django tests.

## 5. AI Suggestions and Limitations

The initial recommendation logic checked whether each product could fit individually inside a box. It did not verify the combined product volume.

This limitation was identified and the logic was improved with a combined-volume check.

The current algorithm is still an approximation. It does not guarantee exact 3D packing of multiple products.

## 6. Verification

I tested the project locally on Windows 10 using Python and Django.

Command used:

```powershell
python manage.py test box_selector
```

Actual result:

```text
Found 10 test(s).
System check identified no issues (0 silenced).
..........
Ran 10 tests
OK
```

The API was also tested using the browser, and it returned the expected JSON response for Order ID 1.

## 7. Developer's Responsibility

I reviewed the AI suggestions, implemented the code in my local Django project, and tested the application.

AI was used as a learning and development assistant. The final implementation and testing were performed in my local environment.