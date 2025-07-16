from fastapi import FastAPI, Query # Import FastAPI and Query
from pydantic import BaseModel # Import BaseModel for data validation
from fastapi.middleware.cors import CORSMiddleware # Import CORS middleware for handling cross-origin requests

class BMIOutput(BaseModel): # Define a Pydantic model for the BMI output
    bmi: float # Field for BMI value
    message: str # Field for message based on BMI value

app = FastAPI() # Create an instance of FastAPI

# Add CORS middleware to allow requests from any origin
app.add_middleware(CORSMiddleware,
    allow_origins=["*"], # Allow all origins
    allow_credentials=True, # Allow credentials
    allow_methods=["*"], # Allow all HTTP methods
    allow_headers=["*"], # Allow all headers
)

@app.get("/") # Define a route for the root path
def read_root(): # Define the root path handler
    return {"Hello": "World"}

# Run the application using the command:
# uvicorn main:app --reload
# uvicorn is an ASGI server that serves FastAPI applications
# Make sure you have uvicorn installed in your environment
# You can install it using pip:
# pip install uvicorn
# main is the file name (without .py) and app is the FastAPI instance
# The command specifies the module name (main) and the FastAPI instance (app)
# The --reload option enables auto-reloading of the server when code changes are detected


# This will start the FastAPI application and you can access it at http://localhost:8000
# You can also access the interactive API documentation at http://localhost:8000/docs

@app.get("/calculate_average_grade") # Define a route for the calculate path
def calculate_average_grade(total: float = Query(..., gt= 0, lt= 1000, description= "Total grade points earned"), num_subjects: int = Query(..., gt= 0, description= "Number of subjects taken")): # Define the function to calculate average grade
    # ... means that this parameter is required
    # gt=0 and lt=1000 ensure that the total is a positive number and not too large
    average = total / num_subjects
    
    if average >= 90:
        message = "Your grade is: A"
    elif average >= 80:
        message = "Your grade is: B"
    elif average >= 70:
        message = "Your grade is: C"
    elif average >= 60:
        message = "Your grade is: D"
    else:
        message = "Your grade is: F"
    return BMIOutput(bmi=average, message=message)
# This function calculates the average grade based on the total grade points and number of subjects

# This function can be called with query parameters like:
# http://localhost:8000/calculate_average_grade?total=270&num_subjects=3
# You can also use automatic API documentation to test this endpoint by navigating to http://localhost:8000/docs
# This will allow you to input the total and number of subjects directly in the browser interface
# The response will be a JSON object containing the average grade and the corresponding message