# lab-githubactions-srobles

A lab project for learning GitHub Actions, by Sergio Robles.

This is a small **AWS Lambda** project: an HTTP API that replies with a hello
message on **any endpoint**. It's used as a sandbox to experiment with CI/CD
workflows and automation using GitHub Actions.

## How it works

The Lambda handler in [main.py](main.py) (`main.handler`) is designed for an
API Gateway / Lambda Function URL proxy integration. Whatever path or method is
requested, it returns a `200` JSON response:

```json
{
  "message": "Hello from lab-githubactions-srobles!",
  "method": "GET",
  "path": "/"
}
```

It understands both the API Gateway **REST** (`path` / `httpMethod`) and
**HTTP API v2** (`rawPath` / `requestContext.http.method`) event shapes.

## Running locally

Invoke the handler directly with a sample event:

```bash
uv run python main.py
```

## Testing

```bash
uv run pytest tests/
```

## Deploying

Package `main.py` and configure the Lambda handler as `main.handler`, then put
an API Gateway (HTTP API) or a Lambda Function URL in front of it with a
catch-all route so every endpoint reaches the function.
