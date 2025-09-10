FROM mcr.microsoft.com/playwright/python:v1.54.0-noble

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN python -m playwright install

# Run pytest when the container launches
CMD ["pytest"]
