import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    # HTTP event variables
    raw_path = event.get("rawPath") or event.get("path", "")
    method = event.get("requestContext", {}).get("http", {}).get("method") or event.get("httpMethod", "")

    # Clean path
    stage = event.get("requestContext", {}).get("stage")
    path = raw_path
    if stage and raw_path.startswith(f"/{stage}"):
        path = raw_path[len(stage)+1:]

    logger.info("=== LAMBDA START ===")
    logger.info(f"Got request {json.dumps(event)}")
    logger.info(f"Got request method: {method} | path: {path}")

    try:
        return {
            "statusCode": 200,
            "body": json.dumps({"response":"hello from GitHub Actions lab!"}),
        }
    except Exception:
        logger.exception("Unexpected server error")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Unexpected server error"}),
        }
