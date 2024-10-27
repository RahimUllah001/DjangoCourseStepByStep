# Django Session Management Project

## Overview

This project demonstrates the use of Django's session management features. It covers setting, retrieving, and deleting session data, as well as checking session expiry details.

## Features

1. **Setting a Session (`setsession` view)**:
   - The session stores a user's name (`'Rahim'`) in `request.session['name']`.
   - Template `setsession.html` displays a message confirming the session is set.

2. **Retrieving a Session (`getsession` view)**:
   - This view retrieves the session value associated with the key `'name'`.
   - If the session exists, the name is displayed.
   - The view also displays session expiry information:
     - `request.session.get_cookie_age`: The lifespan of the session cookie in seconds.
     - `request.session.get_expiry_age`: Remaining time before session expiry.
     - `request.session.get_expiry_date`: The exact date and time when the session will expire.
   - If the session has expired or does not exist, it returns a message: "Your Session has been Expired."

3. **Deleting a Session (`delsession` view)**:
   - The `delsession` view removes all session data using `request.session.flush()`.
   - Additionally, it clears expired sessions from the database with `request.session.clear_expired()`.

## HTML Template (`getsession.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Get Session</title>
</head>
<body>
    <h4>Session Information</h4>
    <p>Name: {{name}}</p>
    <p>Cookie Age: {{request.session.get_cookie_age}}</p>
    <p>Expiry Age: {{request.session.get_expiry_age}}</p>
    <p>Expiry Date: {{request.session.get_expiry_date}}</p>
</body>
</html>
```

## Key Functions and Methods:

- **Session Setting (`setsession`)**:
   - `request.session['name'] = 'Rahim'`: Sets a session key-value pair.
   
- **Session Retrieval (`getsession`)**:
   - `request.session.get('name')`: Safely retrieves the session data for the key `'name'`.
   - `request.session.modified = True`: Forces the session to be saved, even if the data has not changed.
   - `request.session.get_cookie_age`: Retrieves the lifespan of the session cookie.
   - `request.session.get_expiry_age`: Retrieves the remaining time before the session expires.
   - `request.session.get_expiry_date`: Gets the exact date and time when the session expires.

- **Session Deletion (`delsession`)**:
   - `request.session.flush()`: Clears all session data for the current session.
   - `request.session.clear_expired()`: Removes expired session data from the database.

## Conclusion

This project demonstrates how to manage user sessions in Django. By using session data, you can create persistent user-specific information, control session duration, and provide feedback to users regarding their session status. The session expiry and metadata display feature also aids in debugging and enhancing session management practices.

