## Permissions & Groups Setup

This app uses Django’s permission system to restrict access:

### Custom Permissions (Book Model)
- `can_view`: Can view books
- `can_create`: Can create books
- `can_edit`: Can edit books
- `can_delete`: Can delete books

### Groups
- **Viewers**: Assigned `can_view` only
- **Editors**: Assigned `can_view`, `can_edit`, `can_create`
- **Admins**: All permissions

### Views Protection
Views are protected using `@permission_required` decorator:
- `book_list`: requires `can_view`
- `book_create`: requires `can_create`
- `book_edit`: requires `can_edit`
- `book_delete`: requires `can_delete`

### How to Test
1. Create users in the admin panel.
2. Assign them to the appropriate group (Viewers, Editors, Admins).
3. Log in as each user and try to access different URLs to confirm permissions work.
