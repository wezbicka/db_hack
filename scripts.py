import logging
import sys

from datacenter.models import Schoolkid
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('Как назвать логгер?')


def get_kid_by_name(child_name: str) -> Schoolkid:
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except MultipleObjectsReturned as exeption:
        logger.error(f'{exeption}.Найдено больше одного ученика')
        sys.exit()
    except ObjectDoesNotExist as exeption:
        logger.error(f'{exeption}.Не найдено учеников с таким именем')
        sys.exit()
    else:
        logger.info(f'Ученик по имени "{child.full_name}" найден.')
        return child



