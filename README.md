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

<img width="1506" alt="Screenshot 2023-10-24 at 10 57 15 PM" src="https://github.com/bettychen87/Fetch-take-home-assignment/assets/65417079/127ed42c-f54e-4390-b93f-6ca39<img width="1511" alt="Screenshot 2023-10-24 at 10 57 37 PM" src="https://github.com/bettychen87/Fetch-take-home-assignment/assets/65417079/61d627a1-9256-4e1b-bb43-ddd170181013">
e80b423">

<img width="1511" alt="Screenshot 2023-10-24 at 10 57 37 PM" src="https://github.com/bettychen87/Fetch-take-home-assignment/assets/65417079/a5c9567a-4361-40b1-bc48-b5c61ce4de64">

- tester.py can also be used to test the API.
```
python3 tester.py
```
