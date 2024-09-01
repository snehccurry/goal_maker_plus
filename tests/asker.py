# this is asker, it asks user to add something for next hour if empty or else like
import flet as ft
from exit_handlers import  *


def main(page: ft.page):

    page.window.bgcolor = ft.colors.TRANSPARENT
    page.title = "Next Hour Plan"
    # page.bgcolor = ft.colors.TRANSPARENT
    #page.window.title_bar_hidden = False
    #page.window.frameless = True
    page.window.height = 500
    page.window.width = 500
    page.window.prevent_close = False
    #page.window.movable = True
    #page.window.title_bar_buttons_hidden = False
    page.window.alignment = ft.alignment.center_right




    def add_to_goals(e):
        print(f"added {e.data} to goals")
        pass



    # Text field/ text input field that will accept the

    Heading = ft.Text("What would you like to do in the next hour? ", style=ft.TextStyle(size=23))
    text_field = ft.TextField(autofocus=True, on_submit= add_to_goals, hint_text= "example: learn Rust/read/complete a task.")

    def add_to_goals():
        s= text_field.value
        try:
            print(f"added {s} to goals")

        except:
            print("Something went wrong, try again")

    time_taken_will_be = "expected time for completion will be: 0 mins"
    def update_time(t):
        time_taken_will_be = f"expected time for completion will be: {t} mins"
        page.update()




    # a row of buttons that shows time in minutes

    row_of_time = ft.Row( wrap= True,scroll= True,spacing = ft.MainAxisAlignment.SPACE_AROUND,  controls=[
        ft.ElevatedButton("5 mins",on_click= lambda _ : update_time(5)),
        ft.ElevatedButton("10 mins", on_click=lambda _: update_time(10)),
        ft.ElevatedButton("15 mins", on_click=lambda _: update_time(15)),
        ft.ElevatedButton("30 mins", on_click=lambda _: update_time(30)),
        ft.ElevatedButton("45 mins", on_click=lambda _: update_time(45)),
        ft.ElevatedButton("60 mins", on_click=lambda _: update_time(60)),
        ft.ElevatedButton("120 mins", on_click=lambda _: update_time(120)),
        ft.ElevatedButton("240 mins", on_click=lambda _: update_time(240)),
    ])





    #Sized_box_mid_gap = ft.Container(height= 60)
    add_goal_button=  ft.Container(content = ft.ElevatedButton(content= ft.Text("Add Goal!", style= ft.TextStyle(size= 18)), on_click= lambda _: add_to_goals(), ),)
    add_goal_button.alignment = ft.alignment.bottom_right





    page.window.on_event = lambda e: print_event(e, page)
    page.on_keyboard_event = lambda e: on_escape_event(e, page)
    Main_frame = ft.Column(controls=[Heading,ft.Container(height=20),text_field, ft.Container(height=5), ft.Text(time_taken_will_be),row_of_time, ft.Container(height=50), add_goal_button], spacing= ft.MainAxisAlignment.SPACE_BETWEEN)
    page.add(Main_frame)

ft.app(main)