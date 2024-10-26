# Project 40 - Cookie Handling in Django

In this project, I implemented cookie management in Django, demonstrating how to set, retrieve, and delete both **regular** and **signed cookies**.

## Key Features:
- **Set Regular Cookies:** Set a cookie with a specified expiration time using `response.set_cookie()`.
- **Retrieve Regular Cookies:** Retrieve a cookie using `request.COOKIES.get()` with a fallback value to handle cases where the cookie is not present.
- **Delete Regular Cookies:** Delete a cookie with `response.delete_cookie()`.

### Signed Cookies:
- **Set Signed Cookies:** Securely store cookie values using `response.set_signed_cookie()` to prevent data tampering.
- **Retrieve Signed Cookies:** Retrieve signed cookies using `request.get_signed_cookie()` with added salt for extra security.
  
The project highlights the use of cookies for temporary storage of client-side data and ensures the security of sensitive information using Django's built-in mechanisms.
