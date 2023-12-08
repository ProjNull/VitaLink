# API Documentation
## Basics

    JSON responses

### Default route
---
### Test
#### POST/GET /test
### Request Body
- None
### Return
    Message: {Method} request

### Nurses Route
---
### Add Nurse
#### POST /nurses/new
### Request Body


- firstName (string): First name of the nurse.
- lastName (string): Last name of the nurse.
- nick (string): Unique nickname for the nurse.
- password (string): Password for the nurse's account.
- email (string): Email address of the nurse.
- dateOfBirth (string): Date of birth of the nurse (format: YYYY-MM-DD).
- isAdmin (boolean): Indicates whether the nurse has administrative privileges.

Example Request
```json
{
    "firstName": "John",
    "lastName": "Doe",
    "nick": "johnny",
    "password": "securepassword",
    "email": "john.doe@example.com",
    "dateOfBirth": "1990-05-15",
    "isAdmin": false
}
```
Responses

Success Response:
- Code: 200 OK
- Content:
```json
{
    "message": "Nurse added successfully!"
}
```
Error Responses:

- Code: 400 Bad Request
- Content:
```json
{
    "message": "No, or incorrect params given!"
}
```
- Code: 409 Conflict
- Content:
```json
{
    "message": "Someone already has this email!"
}
```

### Get Nurse
#### GET /nurses/get
### Request Body

- idEmployee (integer): ID of the nurse.

Example Request

```json
{
    "idEmployee": 1
}
```

Responses

Success Response:
- Code: 200 OK
- Content:

```json
{
    "idEmployee": 1,
    "firstName": "John",
    "lastName": "Doe",
    "nick": "johnny",
    "password": "securepassword",
    "email": "john.doe@example.com",
    "dateOfBirth": "1990-05-15",
    "isAdmin": false
}
```
Error Response:
- Code: 404 Not Found
- Content:

```json
{
    "message": "Employee not found"
}
```