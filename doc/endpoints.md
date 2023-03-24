## Endpoints

GET /health

```json
{
  "method": "GET",
  "path": "/health",
  "description": "Health of the server",
  "response": {
    "success": {
      "message": "Server is healthy"
    },
    "error": {
      "error": true,
      "message": "Server is not healthy"
    }
  }
}
```

GET /comments

```json
{
  "method": "GET",
  "path": "/comments/:topic-id",
  "description": "Responses with all the comments for given topic id",
  "response": {
    "success": {
      "topicId": "topic-id",
      "comments": []
    },
    "error": {
      "error": true,
      "message": "Error message"
    }
  }
}
```

POST /add-comment

```json
{
  "method": "POST",
  "path": "/add-comment",
  "description": "Adds comment to given topic",
  "body": {
    "topicId": "topic-id",
    "comment": ""
  },
  "response": {
    "success": {
      "topic-id": "topic-id",
      "comment-id": "comment-id",
      "total_comments": 232
    },
    "error": {
      "error": true,
      "message": "Error message"
    }
  }
}
```
