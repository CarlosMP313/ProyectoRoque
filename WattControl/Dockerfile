# filepath: c:\Users\carlo\Documents\Laptop Gris\RESPALDO MEMORIA COSA CARLOS\Proyecto Programacion Web\WattControl-1\Dockerfile
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install wait-for-it
ADD https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Copy the entire project into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["sh", "-c", "/wait-for-it.sh db:3306 -- python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]