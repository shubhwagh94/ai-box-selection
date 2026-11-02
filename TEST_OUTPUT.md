# TEST_OUTPUT.md

## Project Testing

**Testing Framework:** Django Test Framework

**Operating System:** Windows 10

**Command Executed:**

```powershell
python manage.py test box_selector
```

## Actual Test Output

```text
Found 10 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.177s

OK
Destroying test database for alias 'default'...
```

## Test Summary

- Total test cases: 10
- Passed: 10
- Failed: 0
- System check errors: 0

**Result:** All 10 automated tests passed successfully.

## API Verification

The recommendation API was tested in the browser.

Endpoint:

```text
http://127.0.0.1:8000/api/orders/1/recommend-box/
```

Expected result:

- Order ID: 1
- Total Weight: 1.3 kg
- Recommended Box: Small Box
- Box Cost: 20.00

**Result:** API returned the expected JSON response.