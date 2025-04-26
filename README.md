# **BookCart Automation** 

This project contains Selenium automation scripts for testing basic functionalities on the [BookCart](https://bookcart.azurewebsites.net/) website.

---

## **Project Structure**

| File/Folder | Description |
| :---- | :---- |
| `functions.py` | Contains all reusable functions for login, search, wishlist, cart, checkout, etc. |
| `test_flow.py` | Script to run a complete test flow by calling functions from `functions.py`. |

---

## **Requirements**

* Python 

* Selenium library installed

* Google Chrome browser installed

* Latest version of ChromeDriver (matching your Chrome browser version)

To install Selenium, run:

`pip install selenium`

---

## **Configuration**

Before running the tests:

1. Open `functions.py`.

2. **Update the `driver_path` variable** to match the location of your `chromedriver` executable on your system.

✅ **Important:**  
Make sure your ChromeDriver version matches the installed version of your Chrome browser. You can download the latest ChromeDriver from the official website: [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/) 

---

**How to Run**

After setting the correct `driver_path`, simply run:

`python test_flow.py`

This will automatically:

* Open the website

* Log in

* Search for a book

* Add a book to wishlist

* Add the book to the cart

* Proceed to checkout

* Place an order

* Clear the wishlist

---

## **Notes**

* Tests are written using **Python \+ Selenium**.

* Chrome options are configured to disable sandbox and dev-shm usage issues.

* You can adjust sleep times or WebDriverWait timeouts based on your internet speed or system performance.  
