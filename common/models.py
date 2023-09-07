from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models.deletion import RestrictedError


class BaseModel(models.Model):
    """
    A base model for common fields and methods shared among other models.

    This abstract base model includes the following fields:
    - `created_at`: A DateTimeField representing the date and time when the object was created.
    - `updated_at`: A DateTimeField representing the date and time when the object was last updated.
    - `is_active`: A BooleanField indicating whether the object is active (default is True).
    - `is_deleted`: A BooleanField indicating whether the object is logically deleted (default is False).

    It also provides a custom `delete` method that handles object deletion by catching
    a `RestrictedError` exception and raising it with a warning message if applicable.

    Attributes:
        created_at (DateTimeField): The date and time when the object was created.
        updated_at (DateTimeField, optional): The date and time when the object was last updated.
        is_active (BooleanField): Indicates whether the object is active (True) or not (False).
        is_deleted (BooleanField): Indicates whether the object is logically deleted (True) or not (False).

    Meta:
        abstract = True
    """
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """
        Override the default delete method to handle exceptions.

        This method attempts to delete the object using the parent class's delete method.
        If a `RestrictedError` exception is raised during deletion, it's caught and re-raised
        with a warning message and information about restricted objects.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.

        Raises:
            RestrictedError: If a restricted object prevents deletion.
        """
        try:
            super().delete(*args, **kwargs)
        except RestrictedError as e:
            warning_message = '[Cannot delete]'
            raise RestrictedError(warning_message, e.restricted_objects)
