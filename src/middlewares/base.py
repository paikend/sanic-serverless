from sanic_cors import CORS, cross_origin

def CorsMiddleware(app):
  cors = CORS(app, resources={r"/*": {"origins": "*"}})
  return cors