# API Documentation
---
## Basics
---
- Json responses

### Default route
---
### Test
### POST/GET /test

- **Params**
    - None
- **Response** 
    - Message: {Method} request

### employee route
---
#### /new

#### Request Body
- **firstName** (string): First name of the nurse.
- **lastName** (string): Last name of the nurse.
- **nick** (string): Unique nickname for the nurse.
- **password** (string): Password for the nurse's account.
- **dateOfBirth** (string): Date of birth of the nurse (format: YYYY-MM-DD).
- **isAdmin** (boolean): Indicates whether the nurse has administrative privileges.

#### Example Request
```json
{
    "firstName": "John",
    "lastName": "Doe",
    "nick": "johnny",
    "password": "securepassword",
    "dateOfBirth": "1990-05-15",
    "isAdmin": false
}
```
Responses

Success Response:
    Code: 200 OK
    Content:

```json
    {
        "message": "Nurse added successfully!"
    }
```

Error Response:

    Code: 400 Bad Request
    Content:

```json
{
    "message": "No, or incorrect params given!"
}
```

Code: 409 Conflict
Content:

```json
{
    "message": "Someone already has this nickname!"
}
```