## Endpoints

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
    "comment": {}
  },
  "response": {
    "success": {
      "topicId": "topic-id",
      "commentId": "commentId"
    },
    "error": {
      "error": true,
      "message": "Error message"
    }
  }
}
```
