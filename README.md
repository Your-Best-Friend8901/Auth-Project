Auth-Project

📌 Description:
The project provides a secure and convenient authentication system — both via the classic method (username and password) and through OAuth using external services where the user is already authenticated (Google, GitHub). After successful authentication, the user receives JWT tokens, which indicate that the user is logged in.

⚙️🧰 Technical Details

🔥 How the Project Was Implemented

The project is built with Django REST Framework (DRF) and integrates several frameworks:
dj-rest-auth + django-allauth + SimpleJWT — to provide production-ready authentication endpoints that are already tested and widely used in commercial projects.

🧩 What is dj-rest-auth?

dj-rest-auth is a framework that provides ready-to-use authentication endpoints.
It combines multiple frameworks and takes the best parts from each to offer secure and convenient tools.

The framework does not build logic from scratch. Instead, it uses other frameworks as a foundation to create ready-made components like RegisterView and RegisterSerializer, where it only handles validation logic.

For example, when it comes to user registration, dj-rest-auth does not implement its own saving logic — it uses allauth's internal mechanisms (adapters). It simply passes the validated data to allauth, which then handles the actual user creation.

Why?
Because dj-rest-auth was created after allauth. To avoid reinventing the wheel, it leverages allauth's battle-tested and reliable user management operations.
As a result, dj-rest-auth is dependent on other frameworks — without them, it cannot run.

🔍 Why I Chose dj-rest-auth

Just like dj-rest-auth didn't want to reinvent the wheel and used allauth, I also didn't want to build authentication from scratch.

dj-rest-auth already provides:
    Production-ready, secure tools
    Battle-tested components
    Easy customization — if someone needs custom behavior, they can simply inherit from the existing classes and extend the parent logic with their own.

There's no point in building a custom auth system when a secure, flexible, and proven solution already exists.

🏭 The Lifecycle of an Authentication Request
text
```
Middleware -> DRF -> URLs -> Ready-made Auth Tool -> Class Object -> dispatch() method -> actual method (e.g., POST for login)
```
🔑 What Happens After Login (When Data Is Valid)

Once dj-rest-auth validates the user's credentials, it identifies the user from the database and creates a JWT token — a pointer that contains the user's data. This token allows us to identify the user among many.

The token is sent to the user's browser with the HttpOnly flag, which means:
    "No one can access this data except our domain."
On every subsequent request, we simply verify the token's signature. If it's valid, we immediately know who the user is — without an extra database query, unlike session-based authentication.
