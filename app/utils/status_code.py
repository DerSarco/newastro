class Status:
  HTTP_OK = 200
  HTTP_CREATED = 201
  HTTP_NO_CONTENT = 204
  HTTP_MOVED_PERMANENTLY = 301
  HTTP_FOUND = 302
  HTTP_NOT_MODIFIED = 304
  HTTP_BAD_REQUEST = 400
  HTTP_UNAUTHORIZED = 401
  HTTP_FORBIDDEN = 403
  HTTP_NOT_FOUND = 404
  HTTP_METHOD_NOT_ALLOWED = 405
  HTTP_INTERNAL_SERVER_ERROR = 500
  HTTP_NOT_IMPLEMENTED = 501

  @classmethod
  def get_message(self, status_code):
    """Get message from status code."""
    return {
      self.HTTP_OK: "OK",
      self.HTTP_CREATED: "Created",
      self.HTTP_NO_CONTENT: "No Content",
      self.HTTP_MOVED_PERMANENTLY: "Moved Permanently",
      self.HTTP_FOUND: "Found",
      self.HTTP_NOT_MODIFIED: "Not Modified",
      self.HTTP_BAD_REQUEST: "Bad Request",
      self.HTTP_UNAUTHORIZED: "Unauthorized",
      self.HTTP_FORBIDDEN: "Forbidden",
      self.HTTP_NOT_FOUND: "Not Found",
      self.HTTP_METHOD_NOT_ALLOWED: "Method Not Allowed",
      self.HTTP_INTERNAL_SERVER_ERROR: "Internal Server Error",
      self.HTTP_NOT_IMPLEMENTED: "Not Implemented",
    }.get(status_code, "Unknown")
