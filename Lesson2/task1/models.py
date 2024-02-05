from django.db import models

# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или решка.
# Также запоминайте время броска.
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.


class Coin(models.Model):
    game_time = models.DateTimeField(auto_now_add=True)
    side = models.CharField(choices=(('орел', 'орел'), ('решка', 'решка')), max_length=5)

    @staticmethod
    def count_throw():
        coin = Coin.objects.all()
        dict_coin = {'Орел': 0, 'Решка': 0}
        for item in coin:
            if item.side == 'Орел':
                dict_coin['Орел'] += 1
            else:
                dict_coin['Решка'] += 1
        return dict_coin


    def __repr__(self):
        return f'{self.side}, {self.pk}'
