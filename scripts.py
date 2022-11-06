from __future__ import annotations
import logging
import sys
import random

from datacenter.models import Schoolkid, Mark, \
    Chastisement, Lesson, Commendation


COMPLIMENTS = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!",
        "Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!",
    ]


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('DataBases')


def get_kid_by_name(child_name: str) -> Schoolkid:
    try:
        child = Schoolkid.objects.get(full_name__contains=child_name)
    except Schoolkid.MultipleObjectsReturned as exeption:
        logger.error(f'{exeption}.Найдено больше одного ученика')
        sys.exit()
    except Schoolkid.DoesNotExist as exeption:
        logger.error(f'{exeption}.Не найдено учеников с таким именем')
        sys.exit()
    else:
        logger.info(f'Ученик по имени "{child.full_name}" найден.')
        return child


def fix_marks(child_name: str) -> None:
    schoolkid = get_kid_by_name(child_name)
    bad_marks = Mark.objects.filter(
        schoolkid=schoolkid,
        points__lte=3,
    )
    if bad_marks:
        marks_count = bad_marks.update(points=random.randint(4,5))
        logger.info(f"Оценки исправлены в количестве {marks_count} шт.") 
    else:
        print("У ученика нет плохих оценок!")


def remove_chastisements(child_name: str) -> None:
    schoolkid = get_kid_by_name(child_name)
    сhastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    сhastisements.delete()


def create_commendation(child_name, subject, commendations=COMPLIMENTS):
    schoolkid = get_kid_by_name(child_name)
    lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject,
    )
    lesson_of_subject = lessons.order_by('-date').first()
    commendation = random.choice(commendations)
    Commendation.objects.create(
        text=commendation,
        created=lesson_of_subject.date,
        schoolkid=schoolkid,
        subject=lesson_of_subject.subject,
        teacher=lesson_of_subject.teacher,
    )
