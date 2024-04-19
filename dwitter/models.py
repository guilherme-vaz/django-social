from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
#Decorator que pode ser usado no lugar de post_save.connect
@receiver(post_save, sender=User)
# Ao criar um usuário cria também um perfil automaticamente
def create_profile(sender, instance, created, **kwargs):
    if created:
        #O user é passado como instância para o construtor de Profile (pq tem relacionamento One to One)
        user_profile = Profile(user=instance)
        #Cria o perfil/usuário
        user_profile.save()
        #Adiciona o perfil a lista de seguindo para que o usuário possa ver os pŕoprios Dweets
        user_profile.follows.add(instance.profile)
        #Salva novamente
        user_profile.save()

# Execute create_profile() every time the User model executes .save(). You do this by passing User as a keyword argument to sender.
# post_save.connect(create_profile, sender=User)