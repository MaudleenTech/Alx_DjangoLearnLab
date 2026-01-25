## Permissions & Groups Setup (Task 1)

### Custom permissions (relationship_app.Book)
- can_view
- can_create
- can_edit
- can_delete

### Groups (created in Django admin)
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: can_view, can_create, can_edit, can_delete

### Protected endpoints
- /perm/view/  -> requires can_view
- /perm/create/ -> requires can_create
- /perm/edit/ -> requires can_edit
- /perm/delete/ -> requires can_delete


## Security Best Practices (Task 2)

### Settings applied (settings.py)
- DEBUG = False
- SECURE_BROWSER_XSS_FILTER = True
- SECURE_CONTENT_TYPE_NOSNIFF = True
- X_FRAME_OPTIONS = "DENY"
- CSRF_COOKIE_SECURE = True
- SESSION_COOKIE_SECURE = True

### CSRF protection
- Forms include `{% csrf_token %}` in templates.

### SQL injection prevention
- Used Django ORM filters (e.g., title__icontains) instead of raw SQL or string formatting.

### Content Security Policy (CSP)
- Added middleware that sets: `Content-Security-Policy: default-src 'self'`
