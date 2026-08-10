# Python - Network #1

This project builds on the basics of HTTP by fetching and manipulating
internet resources directly from Python, first with `urllib` and then
with the much simpler `requests` package.

## Topics covered

- Fetching internet resources with `urllib`
- Decoding a `urllib` body response
- Fetching internet resources with `requests`
- Making HTTP GET and POST requests
- Fetching and parsing JSON resources
- Manipulating data from an external service (the GitHub API)

## Files

- `0-hbtn_status.py` - fetches the ALU intranet status page with `urllib`
- `1-hbtn_header.py` - prints the `X-Request-Id` response header (`urllib`)
- `2-post_email.py` - sends a POST request with an email parameter (`urllib`)
- `3-error_code.py` - prints the body or `Error code: <status>` (`urllib`)
- `4-hbtn_status.py` - fetches the ALU intranet status page with `requests`
- `5-hbtn_header.py` - prints the `X-Request-Id` response header (`requests`)
- `6-post_email.py` - sends a POST request with an email parameter
  (`requests`)
- `7-error_code.py` - prints the body or `Error code: <status>`
  (`requests`)
- `8-json_api.py` - searches the `search_user` API and prints `[id] name`
- `10-my_github.py` - prints a GitHub user's id via Basic Authentication

## Requirements

- Each script starts with `#!/usr/bin/python3`, has a module docstring,
  and only runs its logic under `if __name__ == "__main__":`
- Dictionary values are accessed with `.get()`
- Tasks 2, 3, 6, 7, and 8 are tested against a web server on port 5000

## Notes

These exercises are part of the ALU higher level programming curriculum
and focus on `urllib`, `requests`, and consuming HTTP/JSON APIs from
Python.
