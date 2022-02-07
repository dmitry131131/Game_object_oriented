import pygame  # импорт библиотеки

# инициализируем окно игры
pygame.init()
pygame.mixer.init()  # включаем звук
screen = pygame.display.set_mode((400, 400))  # выставляем ширину и высоту
pygame.display.set_caption("Game")  # название окна(сверху)
clock = pygame.time.Clock()  # запуск внутреигрового времени

# основной игровой цикл
run = True
while run:
    clock.tick(30)  # установка фиксированного FPS
    # обработчик событий
    for ev in pygame.event.get():
        # проверка на закрытие окна
        if ev.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # после отрисовки всего показывает результат пользователю(переворачивает экран)

pygame.quit()
