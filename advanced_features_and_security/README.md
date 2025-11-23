# Advanced Features and Security

## Permissions and Groups Setup

We have implemented custom permissions and groups to manage access control in the application.

### Custom Permissions
Defined in the `Book` model within `relationship_app/models.py`:
- `can_view`: Allows a user to view a book instance.
- `can_create`: Allows a user to create a new book.
- `can_edit`: Allows a user to edit an existing book.
- `can_delete`: Allows a user to delete a book.

### Groups
- **Admins**: Have all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).
- **Editors**: Can create and edit books (`can_create`, `can_edit`).
- **Viewers**: Can only view books (`can_view`).

### Views Enforcing Permissions
Located in `relationship_app/views.py`, we utilize the `@permission_required` decorator:
- `book_list`: Requires `relationship_app.can_view`
- `add_book`: Requires `relationship_app.can_create`
- `edit_book`: Requires `relationship_app.can_edit`
- `delete_book`: Requires `relationship_app.can_delete`
