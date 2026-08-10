# Python - Network #0

This project covers the basics of HTTP and the network layer of the web:
URLs, requests, responses, headers, methods, status codes, and using
`curl` from the command line to interact with a web server.

## Topics covered

- What a URL is, how to read one, and the HTTP scheme
- Domain names, sub-domains, and port numbers
- Query strings
- HTTP requests and responses: headers, body, methods, and status codes
- HTTP cookies
- Making requests with `curl`

## Files

- `0-body_size.sh` - displays the size (in bytes) of a response body
- `1-body.sh` - displays the body of a response, only if the status is 200
- `2-delete.sh` - sends a `DELETE` request and displays the response body
- `3-methods.sh` - displays all HTTP methods a server accepts
- `4-header.sh` - sends a GET request with a custom header and displays
  the response body
- `5-post_params.sh` - sends a POST request with `email` and `subject`
  parameters and displays the response body

## Requirements

- Each script is exactly 3 lines long: shebang, a comment explaining the
  script, and the `curl` command (with `-s` for silent mode)
- Scripts are tested against a web server running on port 5000

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on the fundamentals of HTTP and `curl`.
