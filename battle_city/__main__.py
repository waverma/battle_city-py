import os

from battle_city.graphic_elements.graphic_utils import GraphicUtils
from battle_city.graphic_elements.texture_provider import TextureProvider
from battle_city.game_loop import GameLoop


# TODO убрать -py из названия пакетов [сделано]
# TODO 1) четыре типа врагов(
#  бронированный(2 хп/ это текущий),
#  простой(1 хп),
#  скорострельный(1 хп, более скорострельный),
#  хилящийся танк(по истечении 3 секунд между получением урона, хилит себя)
#  )
# TODO 2) новые препятствия(
#  кирпич(есть),
#  бетон(есть),
#  кусты(добавить. Сковозь них можно ехать),
#  текстура урона(огонь(гореть) или вода(тонуть)),
#  грязь(замедляет)
#  )
# TODO 3) четыре уровня(
#  чем выше, тем разнообразнее.
#  лимит у спавнера(например, каждый спавнер должен обязательно заспавнить
#                   разные типы танков)
#  )
# TODO 4) внутриигровая табличка с показателями(
#  бонусы,
#  очки,
#  жизнь,
#  скорость
#  )
# TODO 5) чит коды(последовательность кнопок, как в ГТА:СА)(
#  хилл,
#  увилечение урона,
#  неуязвимость
#  )
# TODO убрать магические числа из логики в,
#  например, класс с константами игрового мира
# TODO убрать константы графики в graphic_utils
# TODO в файле томл удалить coverage report [cделано]

if __name__ == "__main__":
    TextureProvider.set_textures(
        os.path.normpath(
            os.path.dirname(os.path.abspath(__file__)) + os.sep + os.pardir
        )
    )
    GameLoop(
        GraphicUtils.DEFAULT_WINDOW_SIZE[0],
        GraphicUtils.DEFAULT_WINDOW_SIZE[1]
    ).run()
