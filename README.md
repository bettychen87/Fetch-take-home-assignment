# Fetch-take-home-assignment

## Setup and Running Instructions

1. Prequisites:
- Ensure that you have [Docker](https://www.docker.com/) installed on your machine.
- Clone the project repository

2. Build Docker Image:
- Navigate to the project directory
```
cd fetch-take-home-assignment
```
- Run the following command to build the Docker image:
```
docker build -t receipt-processor .
```
3. Run Docker Container:
- Run the following command to start the container:
```
docker run -d -p 8000:8000 receipt-process
```
4. Accessing the Application:
- The application can be accessed at http://localhost:8000
- http://localhost:8000/receipts/process for receipt processing
- http://localhost:8000/receipts/{receipt_id}/points for getting points

5. Testing Application
- [Postman](https://www.postman.com/) can be used to make sure the the endpoints work.
- tester.py can also be used to test the API.
```
python3 tester.py
```
