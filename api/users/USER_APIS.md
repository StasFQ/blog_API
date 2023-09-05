### **1. UserRegistrationResource**

```http
POST /api/register
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description |
|----------| ---- |----------|-----------------|-------------|
| email    | str  | Yes      | -               | your email  |
| password | str  | Yes      | -               | password    |


**Example response:**
```json
{
    "ok": true,
    "description": "",
    "result": {
        "message": "User registration successful",
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MzkyNjc2NywianRpIjoiMmZkZTBiNTMtZTA0Yy00MGM4LTkyMGYtZGUyMGRjOGU4OTU3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6NTksIm5iZiI6MTY5MzkyNjc2NywiZXhwIjoxNjkzOTMzOTY3fQ.VKHJSLs4ACJo5wCsNr6j_zVmsdqkpvuw9sEDu6m_t9s"
    }
}
```

### **2. LoginResource**

```http
POST /api/login
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description |
|----------| ---- |----------|-----------------|-------------|
| email    | str  | Yes      | -               | your email  |
| password | str  | Yes      | -               | password    |


**Example response:**
```json
{
    "ok": true,
    "description": "Logged in successfully",
    "result": {
        "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MzkyNjgzNiwianRpIjoiYWM5ZmIyOWYtMmVmNS00NzMwLThhMzYtYzMyNTYxYmMxZDE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6OCwibmJmIjoxNjkzOTI2ODM2LCJleHAiOjE2OTM5MzQwMzZ9.8uZmKq7Tm4hezX053WyYJJk2Ylj8lYOgG4HgJym2Urk",
        "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MzkyNjgzNiwianRpIjoiMDQ4MTQ1NzctZjE4Ny00OTI5LWFiYmItYzQ4ZTI3NzA5YjY0IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjgsIm5iZiI6MTY5MzkyNjgzNiwiZXhwIjoxNjk0MDEzMjM2fQ.C3p1AxzqpCl4XAC-c20wzDVzge530vQEYnPEMgFAogc"
    }
}
```

### **3. LoginResource**

```http
POST /api/user/<int:user_id>/activity
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description |
|----------| ---- |----------|-----------------|-------------|



**Example response:**
```json
{
    "ok": true,
    "description": "Got user activity data",
    "result": {
        "last_login_date": "2023-09-05 11:12:27",
        "last_request_date": "2023-09-05 11:12:27"
    }
}
```