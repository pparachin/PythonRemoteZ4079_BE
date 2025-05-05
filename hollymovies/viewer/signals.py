from django.db.models.signals import m2m_changed, post_delete, post_save, pre_save
from django.dispatch import receiver
from django.db.models import F

from .models import Actor, Director, Movie

@receiver(m2m_changed, sender=Movie.actor.through)
def update_actor_movie_count(action, pk_set, sender, instance, **kwargs):
    if action == "post_add":
        Actor.objects.filter(pk__in=pk_set).update(movie_count=F('movie_count') + 1)
    elif action == "post_remove":
        Actor.objects.filter(pk__in=pk_set).update(movie_count=F('movie_count') - 1)

"""
  Před uložením ziskáme původního režiséra.
"""
@receiver(pre_save, sender=Movie)
def movie_pre_save(sender, instance, **kwargs):
    # Kontrolujeme zda se jedná o založení nového filmu
    if not instance.pk:
        instance._old_director_id = None
    else:
        # V případě že se jedná o změnu u existujícího filmu
        try:
            movie = sender.objects.get(pk=instance.pk)
            instance._old_director_id = movie.director.id
        except sender.DoesNotExist:
            instance._old_director_id = None

"""
Po uložení filmu:
- Zjistíme jestli je režisér nový, v případě že ano musíme novému přičíst 1
- Pokud se jedná pouze o update zkontrolujeme jestli se změnilo id režiséra a pokud ano, tak přičteme 1
"""
@receiver(post_save, sender=Movie)
def movie_post_save(sender, instance, created, **kwargs):
    # Získání ids nového a aktulního režiséra
    new_director_id = instance.director_id
    old_director_id = getattr(instance, '_old_director_id', None)

    # Zkontrolujeme zda se jedná o vytváření nového záznamu
    if created:
        # Kontrola zda došlo k přiřazení hodnoty do new_id (tedy existuje "nový" režisér)
        if new_director_id:
            Director.objects.filter(pk=new_director_id).update(
                movie_count=F('movie_count') + 1
            )
    else:
        if new_director_id != old_director_id:
            if new_director_id:
                Director.objects.filter(pk=new_director_id).update(
                    movie_count=F('movie_count') + 1
                )
            if old_director_id:
                Director.objects.filter(pk=old_director_id).update(
                    movie_count=F('movie_count') - 1
                )


@receiver(post_delete, sender=Movie)
def movie_post_delete(sender, instance, **kwargs):
    if instance.director_id:
        Director.objects.filter(pk=instance.director_id).update(
            movie_count=F('movie_count') - 1
        )
