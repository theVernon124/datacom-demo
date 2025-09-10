# Datacom Technical Exam - QA Practice Bugs Form Tests

This repository contains an automated test suite for [QA Practice Bugs Form](https://qa-practice.netlify.app/bugs-form), built using Playwright and Pytest, as my submission for the Datacom Technical Exam for the Senior Quality Assurance Automation Engineer role.

## Project Structure

- `data/`: Contains modules for generating test data (`data_generator.py`) and predefined user data scenarios (`user_data.py`).
- `pages/`: Implements the Page Object Model for the Bugs Form (`bugs_form_page.py`)
- `tests/`: Contains the actual test cases (`test_bugs_form.py`).
- `.github/workflows/playwright.yml`: GitHub Actions workflow for CI, building a Docker image, and running tests.
- `Dockerfile`: Defines the Docker image.
- `requirements.txt`: Lists all Python dependencies.
- `pytest.ini`: Pytest configuration file.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Docker (optional, for containerized execution)

### Local Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/theVernon124/datacom-demo.git
    cd datacom-demo
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Playwright browsers:**
    ```bash
    playwright install
    ```

## Running Tests

### Locally

To run all tests:

```bash
pytest
```

### Using Docker

1.  **Build the Docker image:**

    ```bash
    docker build . --tag datacom-demo
    ```

2.  **Run tests in a Docker container:**
    ```bash
    docker run --name datacom-demo-container datacom-demo
    ```

## Continuous Integration

The project uses GitHub Actions to automatically run tests on `push` and `pull_request` events to the `main` branch. The workflow builds the Docker image and executes the tests within the container. Playwright traces are uploaded as artifacts.
