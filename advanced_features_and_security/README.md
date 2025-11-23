# Advanced Features and Security

## Permissions and Groups

### Custom Permissions (In bookshelf app)
- can_view
- can_create
- can_edit
- can_delete

### Views
- bookshelf/views.py handles the permission checks.


## Security Review (Task 3)

### HTTPS Configuration
We have enforced HTTPS for all connections to ensure data confidentiality and integrity.
- `SECURE_SSL_REDIRECT`: Redirects HTTP requests to HTTPS.
- `SECURE_HSTS_...`: Enables HTTP Strict Transport Security to prevent man-in-the-middle attacks.

### Secure Cookies
- `SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE` are set to `True` to prevent cookie interception over insecure connections.

### Secure Headers
- `X_FRAME_OPTIONS = 'DENY'`: Protects against Clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents MIME-type sniffing vulnerabilities.
- `SECURE_BROWSER_XSS_FILTER`: Activates browser-side XSS protection.
