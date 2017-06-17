import jester, asyncdispatch, json


proc handle_push_event(req: Request): string =
  echo req.body
  result = ""


routes:
  post "/github_webhook":
    try:
      resp handle_push_event(request)
    except:
      resp Http400, "Unable to parse JSON payload"

runForever()