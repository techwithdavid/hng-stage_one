# HNG internship stage one task

## Description

Backend Stage One Task

An endpoint that takes two GET request query parameters and return specific information in JSON format.

The returned response includes the following:
- Slack name
- Current day of the week
- Current UTC time (with validation of +/-2)
- Track
- The GitHub URL of the file being run
- The GitHub URL of the full source code.
- A Status Code of Success (200)

JSON
```
 {
   "slack_name": "example_name",
   "current_day": "Monday",
   "utc_time": "2023-08-21T15:04:05Z",
   "track": "backend",
   "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
   "github_repo_url": "https://github.com/username/repo",
   "status_code": 200
}
```
