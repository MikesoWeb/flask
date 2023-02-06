# Flask Hello World Application

A simple Flask application that returns a greeting message to the user.

## Usage

The application listens on `http://127.0.0.1:5000/` and takes an optional query parameter `name`. If `name` is provided, the greeting will include the value of `name`.

For example:
- `http://127.0.0.1:5000/` returns `Hello, !`
- `http://127.0.0.1:5000/?name=Tom` returns `Hello, <p style="color:red; text-align:center">Tom</p>!`

## Code Explanation

The code uses Flask to define a simple web application. It has a single endpoint `"/"` that is implemented in the `hello` function. The function retrieves the value of `name` from the query parameters of the request and formats it as a string. The result of the function is then returned as the response to the request.

## How to Run

1. Clone the repository to your local machine
2. Install the required packages using `pip install -r requirements.txt`
3. Run the application using `python app.py`

## Copyright and License

Copyright (c) 2021 Michael Tereshov

This code is licensed under the MIT License.
