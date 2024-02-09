import turtle
import math

# Рекурсивна функція для відображення дерева Піфагора
def draw_pifagoras_tree(t, length, level):
    if level == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pifagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.right(90)
    draw_pifagoras_tree(t, length * math.sqrt(2) / 2, level - 1)
    t.left(45)
    t.backward(length)

def main():
    # Введення рівня рекурсії
    print("Фрактал 'Дерево Піфагора'")
    level = int(input("Введіть рівень рекурсії: "))

    # Ініціалізація та налаштування екрану
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.title("Фрактал 'Дерево Піфагора'")

    # Підготовка відображення дерева Піфагора
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)

    # Виклик функції для відображення дерева Піфагора
    draw_pifagoras_tree(t, 150, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
