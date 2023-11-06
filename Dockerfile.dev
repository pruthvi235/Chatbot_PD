# Use a base Python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy your application code into the container
COPY . /app

# Install required Python packages
RUN pip install streamlit streamlit_chat langchain sentence_transformers

# Expose the port on which your Streamlit app will run
EXPOSE 8501

# Specify the command to run your Streamlit app
CMD ["streamlit", "run", "main.py"]
