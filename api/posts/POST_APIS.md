### **1. CreatePostResource**

```http
POST /api/posts/
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description       |
| -------- | ---- |----------|-----------------|-------------------|
| title   | str  | Yes      | -               | Head of Post      |
| description     | str  | Yes      | -               | Post content      |


**Example response:**

```json
{
"ok": true,
    "description": "Post created",
    "result": {
        "id": 169,
        "title": "Example",
        "description": "example"
    }
}
```


### **2. PostLikeResource**

```http
POST /api/<int:post_id>/like
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description       |
| -------- | ---- |----------|-----------------|-------------------|


**Example response:**

```json
{
"ok": true,
    "description": "You Liked it!",
    "result": {
        "id": 100,
        "title": "Random Title",
        "description": "Random Description"
    }
}
```

### **3. PostDislikeResource**

```http
POST /api/<int:post_id>/dislike
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description       |
| -------- | ---- |----------|-----------------|-------------------|


**Example response:**

```json
{
"ok": true,
    "description": "You Disliked it!",
    "result": {
        "id": 100,
        "title": "Random Title",
        "description": "Random Description"
    }
}
```

### **3. AnalyticsResource**

```http
GET /api/post/<int:post_id>/analytics
```

- Authorization: Access token

**Params:**

| Name     | Type | Required | Values(default) | Description |
| -------- | ---- |----------|-----------------|-------------|
| date_from_str   | str  | Yes      | -               | From date   |
| date_to_str     | str  | Yes      | -               | To date     |
```http
GET http://127.0.0.1:5000/api/post/100/analytics?date_from=2023-01-01&date_to=2023-12-31
```


**Example response:**
```json
{
    "likes_count": 5
}

```