from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # Um perfil tem um usuário
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        # Users can follow someone without them following back
        symmetrical=False,
        # Users don’t need to follow anyone. The follows field can remain empty.
        blank=True
    )

    def __str__(self):
        return self.user.username
