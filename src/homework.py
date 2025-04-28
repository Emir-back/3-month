import flet as ft
from database_hw import Database
from pprint import pprint

def main(page: ft.Page):
    database_hw = Database("database.sqlite")
    database_hw.create_tables()
    products = database_hw.get_products()
    pprint(products)

    page.title = "My first app"
    Title_text = ft.Text("Общая сумма:", size=20)
    total_text = ft.Text(str(database_hw.total_expenses()), size=20)
    head = ft.Text("Список покупок", size=30, weight=ft.FontWeight.BOLD)

    def get_color(cost):
        if cost <= 100:
            return ft.colors.GREEN
        elif cost <= 1000:
            return ft.colors.PINK
        elif cost <= 10_000:
            return ft.colors.RED
        else:
            return ft.colors.PURPLE

    def save(e):
        cost = second_input.value
        title = first_input.value
        if not cost.isdigit():
            print("Введите положительное число")
            return
        cost = int(cost)

        database_hw.add_name(title, cost)  # исправлено на add_name
        total_text.value = str(database_hw.total_expenses())  # исправлено на total_expenses

        color = get_color(cost)
        area.controls.append(
            ft.Row(
                controls=[
                    ft.Text(title + ":"),
                    ft.Text(str(cost), color=color),
                    ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.YELLOW_400),
                    ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED_400),
                ]
            )
        )
        page.update()

    first_input = ft.TextField(label="Введите товар")
    second_input = ft.TextField(label="Введите сумму товара")

    button = ft.ElevatedButton("Добавить", on_click=save)
    area = ft.Column(expand=True, scroll="always")

    for title, cost in products:
        color = get_color(cost)
        area.controls.append(
            ft.Row(
                controls=[
                    ft.Text(title + ":"),
                    ft.Text(str(cost), color=color),
                    ft.IconButton(ft.icons.EDIT, icon_color=ft.colors.YELLOW_400),
                    ft.IconButton(ft.icons.DELETE, icon_color=ft.colors.RED_400),
                ]
            )
        )

    page.add(
        head,
        ft.Row([first_input, second_input, button]),
        area,
        ft.Row([Title_text, total_text])
    )

ft.app(target=main)
