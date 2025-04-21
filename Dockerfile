# Use the officail python base image
FROM python:3.10-slim


#Set the working directory inside the container
WORKDIR /app


# Copy the current directory contents into the conatiner
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose streamlit's default port \
Expose 8501

# Define env variables if needed \

# run the streamlit app
CMD ["streamlit", "run", "app/main.py", "--server.port=8501", "--server.enableCORS=false"]