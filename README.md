# Django CSV Data Visualization Project

This project is aimed at visualizing CSV data using Django and Plotly.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Python (version 3.6 or higher)
- You have installed Django (version 3.0 or higher)
- You have installed Plotly (version 4.0 or higher)
- You have installed any other dependencies listed in the `requirements.txt` file

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository to your local machine:
    ```
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```
    cd django-csv-visualization
    ```

3. Install the project dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Apply the database migrations:
    ```
    python manage.py migrate
    ```

5. Run the Django development server:
    ```
    python manage.py runserver
    ```

6. Open a web browser and go to `http://localhost:8000/` to view the project.

## Usage

- To import CSV data, go to `http://localhost:8000/import-csv/` and upload a CSV file.
- To view the visualizations of the imported data, go to `http://localhost:8000/visualize-data/`.

##Watch a Quick Demo
https://drive.google.com/file/d/1irECF5iQrlkW2iN-ijUZlEarn-XWp30r/view?usp=sharing
