from datacenter.models import Schoolkid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def get_kid_by_name(child_name: str) -> Schoolkid:
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except MultipleObjectsReturned:
        print("Найдено больше одного ученика")
    except ObjectDoesNotExist:
        print("Не найдено учеников с таким именем")
    return child