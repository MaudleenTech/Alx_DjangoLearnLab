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
