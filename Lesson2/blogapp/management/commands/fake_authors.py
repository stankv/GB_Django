from django.core.management.base import BaseCommand
from blogapp.models import Author


class Command(BaseCommand):
    help = "Заполнение таблицы тестовыми данными: Авторы."

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            author = Author(name=f'name{i}',
                            surname=f'surname{i}',
                            email=f'user{i}@mail.ru',
                            biography=f'биография{i}',
                            birthday=f'2000-01-0{i}'
                            )
            author.save()
        self.stdout.write('Введены 10 авторов!')