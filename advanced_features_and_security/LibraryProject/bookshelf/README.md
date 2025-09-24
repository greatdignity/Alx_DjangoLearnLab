# LibraryProject Permissions & Groups Setup

This Django project demonstrates custom permissions and groups.

## Custom Permissions
- `can_create` – allows creating new Book records
- `can_edit` – allows editing existing Book records
- `can_delete` – allows deleting Book records

These permissions are added in `bookshelf/models.py` in the `Book` model.

## Groups
We created groups in the admin:
- **Editors** – can create and edit
- **Viewers** – can only view
- **Admins** – can create, edit and delete

## Views
Views such as `book_list` and `book_create` use the `@permission_required` decorator to enforce access control.

## Testing
Create users, assign them to groups, and try accessing the restricted views to verify permissions.

