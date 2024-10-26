
# Django User Authentication and Profile Management with saperate interface for Admin and norma user

This project is a Django application for user authentication and profile management, with differentiated functionalities for admin and normal users. The application includes user registration, login, profile viewing, editing, and password change features.

---

## Features

1. **User Registration**: Allows new users to sign up and create an account.
2. **User Login and Logout**: Authenticated login and secure logout functionality.
3. **User Profile Display**:
   - Admin users can view profiles of all registered users.
   - Normal users can only view their profile information.
4. **Password Change Options**:
   - Change password with the old password.
   - Change password without requiring the old password.
5. **Profile Editing**:
   - Admin users can edit their profile and access all user profiles.
   - Normal users can edit only their own profile.

---

## Implementation Details

### 1. Views

- **sign_up**: Renders the sign-up page for new users.
- **user_login**: Authenticates users, with redirection based on login status.
- **user_profile**: Displays profile details based on user type.
  - Admins see an editable form with a list of all users.
  - Normal users see a read-only version of their profile form.
- **user_logout**: Logs the user out and redirects to login.
- **user_change_pass** and **user_change_pass1**: Allow password change with or without the old password.
- **user_edit_profile**: Lets users update their profile details.
- **user_detail**: Allows admins to view details of any user.

### 2. Forms

- **signUpForm**: Extends `UserCreationForm` to include fields like username, email, etc.
- **EditUserProfileForm**: Used by normal users to view and edit their profile.
- **EditAdminProfileForm**: Admin-specific form allowing full control over user data fields.

---


## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   - Go to `http://127.0.0.1:8000/` to access the application.

---

## Usage

- **Register a User**: Create an account from the signup page.
- **Login**: Log in to view the user profile page.
- **Profile Page**:
   - Admin users can view all users and edit user profiles.
   - Normal users can only view and edit their own profiles.
- **Change Password**: Users can change their password with or without the old password.

---
