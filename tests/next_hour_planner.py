# this is asker widget frame.

import flet as ft
from exit_handlers import *
import time

# Page settings (commented out)
# page.window.bgcolor = ft.colors.TRANSPARENT
# page.title = "Next Block Plan"
# page.window.height = 700
# page.window.width = 400
# page.window.prevent_close = False
# page.scroll = ft.ScrollMode.HIDDEN
# page.window.movable = True
# page.window.title_bar_buttons_hidden = False
# page.window.alignment = ft.alignment.center_right

def add_to_goals(e):
    if e.data.strip() != "":
        print(f"added {e.data} to goals")
    else:
        print("modal saying: the field is empty, consider writing a goal in that text field")

# Text field/ text input field that will accept the goal
Heading = ft.Text("What would you like to do in the next block? ", style=ft.TextStyle(size=23))
text_field = ft.TextField(
    autofocus=True,
    on_submit=add_to_goals,
    hint_text="add something productive for next hour...",
    border_color=ft.colors.BLUE_ACCENT,
    hint_style=ft.TextStyle(color=ft.colors.WHITE54)
)

def add_to_goals():
    s = text_field.value
    if s.strip() != "":
        try:
            print(f"added {s} to goals")
        except:
            print("Something went wrong, try again")
    else:
        print("modal saying: the field is empty, consider writing a goal in that text field")

time_selected = "Time for completion: 0 mins"
time_for_completion = ft.Text(value=time_selected, size=18)

def update_time(e):
    time_for_completion.value = f"Time for completion: {e} mins"
    # time_for_completion.style = ft.TextStyle(color=ft.colors.BLUE_ACCENT_700)
    time_for_completion.update()

# A row of buttons that shows time in minutes
row_of_time = ft.Row(
    wrap=True,
    scroll=True,
    spacing=ft.MainAxisAlignment.SPACE_AROUND,
    controls=[
        ft.ElevatedButton("5 mins", on_click=lambda e: update_time(5)),
        ft.ElevatedButton("10 mins", on_click=lambda e: update_time(10)),
        ft.ElevatedButton("15 mins", on_click=lambda e: update_time(15)),
        ft.ElevatedButton("30 mins", on_click=lambda e: update_time(30)),
        ft.ElevatedButton("45 mins", on_click=lambda e: update_time(45)),
        ft.ElevatedButton("60 mins", on_click=lambda e: update_time(60)),
        ft.ElevatedButton("120 mins", on_click=lambda e: update_time(120)),
        ft.ElevatedButton("240 mins", on_click=lambda e: update_time(240)),
    ]
)

# Add goal button
add_goal_button = ft.Container(
    content=ft.ElevatedButton(
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=24)),
        content=ft.Text("Add Goal!", style=ft.TextStyle(color=ft.colors.WHITE)),
        bgcolor=ft.colors.BLUE_ACCENT_700,
        on_click=lambda _: add_to_goals()
    ),
    alignment=ft.alignment.bottom_right,
    padding=ft.padding.all(20)
)

def add_a_break(break_time):
    print(f"break added of {break_time} mins")

# Break buttons
add_a_break_after_goal_completion = "Time for completion: 0 mins"
time_for_completion = ft.Text(value=time_selected, size=18)

take_a_short_break_button = ft.Container(content=ft.ElevatedButton(text="take 9 min break", color=ft.colors.with_opacity(0.7, ft.colors.WHITE), on_click=lambda _: add_a_break(10)))
take_a_medium_break_button = ft.Container(content=ft.ElevatedButton(text="take 20 min break", color=ft.colors.with_opacity(0.7, ft.colors.WHITE), on_click=lambda _: add_a_break(20)))
take_a_long_break_button = ft.Container(content=ft.ElevatedButton(text="take 60 min break", color=ft.colors.with_opacity(0.7, ft.colors.WHITE), on_click=lambda _: add_a_break(30)))
take_a_one_day_break_button = ft.Container(content=ft.ElevatedButton(text="take 1 day break", color=ft.colors.with_opacity(0.7, ft.colors.WHITE), on_click=lambda _: add_a_break(1440)))

all_breaks_row = ft.Container(content=ft.Row(wrap=True, controls=[take_a_short_break_button, take_a_medium_break_button, take_a_long_break_button, take_a_one_day_break_button]))


def next_hour_planner_widget(visible = False):
    # Main frame
    Main_frame = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        controls=[
            Heading,
            ft.Container(height=20),
            text_field,
            ft.Container(height=10),
            ft.Container(height=10),
            time_for_completion,
            row_of_time,
            ft.Container(height=50),
            all_breaks_row,
            ft.Container(height=20),
            add_goal_button
        ],
        spacing=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    Main_frame.visible = visible

    return Main_frame

































# # this is asker, it asks user to add something for next hour if empty or else like
# import flet as ft
# from exit_handlers import  *
# import time
#
#
# def main(page: ft.page):
#
#     page.window.bgcolor = ft.colors.TRANSPARENT
#     page.title = "Next Block Plan"
#     # page.bgcolor = ft.colors.TRANSPARENT
#     #page.window.title_bar_hidden = False
#     #page.window.frameless = True
#     page.window.height = 700
#     page.window.width = 400
#     page.window.prevent_close = False
#     page.scroll = ft.ScrollMode.HIDDEN
#
#     #page.window.movable = True
#     #page.window.title_bar_buttons_hidden = False
#
#     page.window.alignment = ft.alignment.center_right
#
#
#
#
#
#     def add_to_goals(e):
#         if(e.data.strip()!=""):
#             print(f"added {e.data} to goals")
#
#         else:
#             print("modal saying: the field is empty, consider writing a goal in that text field")
#
#
#
#     # Text field/ text input field that will accept the
#
#     Heading = ft.Text("What would you like to do in the next block? ", style=ft.TextStyle(size=23))
#     text_field = ft.TextField(autofocus=True, on_submit= add_to_goals, hint_text= "add something productive for next hour...", border_color= ft.colors.BLUE_ACCENT, hint_style=ft.TextStyle(color=ft.colors.WHITE54))
#
#     def add_to_goals():
#         s= text_field.value
#         if(s.strip()!=""):
#             try:
#                 print(f"added {s} to goals")
#
#             except:
#                 print("Something went wrong, try again")
#         else:
#             print("modal saying: the field is empty, consider writing a goal in that text field")
#
#
#
#     time_selected = "Time for completion: 0 mins"
#     time_for_completion = ft.Text(value = time_selected, size =18)
#     def update_time(e):
#         time_for_completion.value  = f"Time for completion: {e} mins"
#         #time_for_completion.style = ft.TextStyle(color=ft.colors.BLUE_ACCENT_700)
#         time_for_completion.update()
#
#
#
#
#
#
#     # a row of buttons that shows time in minutes
#
#     row_of_time = ft.Row( wrap= True,scroll= True,spacing = ft.MainAxisAlignment.SPACE_AROUND,  controls=[
#         ft.ElevatedButton("5 mins",on_click= lambda e : update_time(5)),
#         ft.ElevatedButton("10 mins", on_click=lambda e: update_time(10)),
#         ft.ElevatedButton("15 mins", on_click=lambda e: update_time(15)),
#         ft.ElevatedButton("30 mins", on_click=lambda e: update_time(30)),
#         ft.ElevatedButton("45 mins", on_click=lambda e: update_time(45)),
#         ft.ElevatedButton("60 mins", on_click=lambda e: update_time(60)),
#         ft.ElevatedButton("120 mins", on_click=lambda e: update_time(120)),
#         ft.ElevatedButton("240 mins", on_click=lambda e: update_time(240)),
#     ])
#
#
#
#
#
#     #Sized_box_mid_gap = ft.Container(height= 60)
#     add_goal_button=  ft.Container(content = ft.ElevatedButton(style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=24)),content= ft.Text("Add Goal!", style= ft.TextStyle(color=ft.colors.WHITE)),bgcolor=ft.colors.BLUE_ACCENT_700, on_click= lambda _: add_to_goals(), ),)
#     add_goal_button.alignment = ft.alignment.bottom_right
#     add_goal_button.padding = ft.padding.all(20)
#
#
#
#     def add_a_break(break_time):
#         print(f"break added of {break_time} mins")
#
#
#     add_a_break_after_goal_completion = "Time for completion: 0 mins"
#     time_for_completion = ft.Text(value=time_selected, size=18)
#
#     take_a_short_break_button = ft.Container(content=ft.ElevatedButton(text="take 9 min break",  color=ft.colors.with_opacity(0.7,ft.colors.WHITE), on_click=add_a_break(10)))
#     take_a_medium_break_button = ft.Container(content=ft.ElevatedButton(text="take 20 min break",  color=ft.colors.with_opacity(0.7,ft.colors.WHITE),on_click=add_a_break(20)))
#     take_a_long_break_button = ft.Container(content=ft.ElevatedButton(text="take 60 min break",  color=ft.colors.with_opacity(0.7,ft.colors.WHITE),on_click=add_a_break(30)))
#     take_a_one_day_break_button = ft.Container(content=ft.ElevatedButton(text="take 1 day break", color=ft.colors.with_opacity(0.7, ft.colors.WHITE),on_click=add_a_break(1440)))
#
#
#
#     all_breaks_row = ft.Container(content=ft.Row(wrap=True,controls=[take_a_short_break_button, take_a_medium_break_button, take_a_long_break_button, take_a_one_day_break_button]))
#
#
#     #page.window.on_event = lambda e: print_event(e, page)
#     page.on_keyboard_event = lambda e: on_escape_event(e, page)
#     Main_frame = ft.Column(scroll=ft.ScrollMode.ALWAYS,controls=[Heading,ft.Container(height=20),text_field, ft.Container(height=10) ,ft.Container(height=10),time_for_completion,row_of_time, ft.Container(height=50),  all_breaks_row, ft.Container(height=20), add_goal_button], spacing= ft.MainAxisAlignment.SPACE_BETWEEN)
#     page.add(Main_frame)
#     def fade_in(Main_frame):
#         opacity = 0.0
#         f=1
#         while opacity < 0.9:
#             opacity += 0.02 # this is how fast the window will increase it's opactiy
#             Main_frame.opacity = opacity
#             Main_frame.update()
#             time.sleep(0.05)
#             if (f == 1):
#                 time.sleep(0.3)
#                 f=0
#
#     #fade_in(Main_frame)
#
# ft.app(main)