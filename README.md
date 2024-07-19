# Calculator Application

## Overview

The Calculator Application is a sophisticated desktop tool built using Python and the `customtkinter` library. It offers a sleek, modern interface for performing a wide range of arithmetic and mathematical operations. The application supports fundamental calculations, advanced mathematical functions, and provides robust input management features.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Mathematical Functions**: Square root, square, reciprocal (1/x), and negation (+/-).
- **User-Friendly Interface**: Designed with `customtkinter` for a modern and intuitive user experience.
- **Dynamic Input Handling**: Includes features for input validation, formatting, and error handling.

## Installation

To set up and run the Calculator Application on your local environment, follow these steps:

1. **Clone the Repository**:
   Retrieve the project repository using Git:
   ```bash
   git clone https://github.com/amariwan/calculator-app.git
   cd calculator-app
   ```

2. **Create a Virtual Environment** (Recommended):
   Set up a virtual environment to manage dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   Start the application by executing the `main.py` script:
   ```bash
   python main.py
   ```

## Usage

### Basic Operations

- **Input Numbers**: Use the number buttons to enter digits.
- **Perform Calculations**: Click on arithmetic operation buttons (`+`, `-`, `X`, `/`) to define the operation. Click the `=` button to compute and display the result.

### Advanced Operations

- **Square Root**: Click the `√x` button to compute the square root of the current input.
- **Square**: Click the `x²` button to square the current input.
- **Reciprocal**: Click the `1/x` button to compute the reciprocal (1 divided by the current input).
- **Negation**: Click the `+/-` button to invert the sign of the current input.

### Input Management

- **Clear Entry (`CE`)**: Clears the current input field.
- **Clear All (`C`)**: Resets both the current input and the operation.
- **Delete Last Character (`<x`)**: Removes the last character from the current input.

### Calculation

- **Result (`=`)**: Evaluates the expression and displays the result.

## Project Structure

### `main.py`

- **Description**: Serves as the entry point for the application. It initializes and runs the `Calculadora` class.
- **Usage**: Execute this script to launch the calculator application.

### `calculadora/`

- **Purpose**: Contains the core functionality of the application.

  - **`__init__.py`**: Initializes the `calculadora` package. It can be used to include package-level configurations or documentation.
  - **`__main__.py`**: Provides an entry point for the package, allowing it to be run as a module.
  - **`calculos.py`**: Defines mathematical functions used by the calculator:
    - **`pow_square(n)`**: Returns the square of the number.
    - **`sqrt(n)`**: Computes the square root of the number.
    - **`one_divided_n(n)`**: Returns the reciprocal of the number.
    - **`negative(n)`**: Returns the negation of the number.

### `requirements.txt`

- **Description**: Lists the necessary Python packages required for the application.
- **Usage**: Install dependencies using `pip`:
  ```bash
  pip install -r requirements.txt
  ```

## Contributing

Contributions to the project are welcome. To contribute:

1. **Fork the Repository**: Create a personal copy of the repository by forking it on GitHub.
2. **Create a Branch**: Develop your changes on a new branch.
3. **Submit a Pull Request**: Open a pull request with a detailed explanation of your changes and improvements.

## License

This project is licensed under the MIT License. For more details, refer to the [LICENSE](LICENSE) file.

## Contact

For inquiries or support, please contact:

- **Email**: dev@tasiomind.de
- **GitHub Profile**: [amariwan](https://github.com/amariwan)
