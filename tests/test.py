from flet import *
from exit_handlers import *
from next_hour_planner import *

def main(page: Page):
    page.update()
    page.on_keyboard_event = lambda e: on_escape_event(e, page)
    page.window.bgcolor = colors.TRANSPARENT
    page.title = "Next Block Plan"
    # page.bgcolor = ft.colors.TRANSPARENT
    #page.window.title_bar_hidden = False
    #page.window.frameless = True
    page.window.height = 750
    page.window.width = 400
    page.window.prevent_close = False
    page.scroll = ScrollMode.HIDDEN

    #page.window.movable = True
    #page.window.title_bar_buttons_hidden = False

    page.window.alignment = alignment.center_right

    def changetab(e):
        # GET INDEX TAB
        my_index = e.control.selected_index
        tab_1.visible = True if my_index == 0 else False
        tab_2.visible = True if my_index == 1 else False
        tab_3.visible = True if my_index == 2 else False
        page.update()

    page.navigation_bar = CupertinoNavigationBar(
        on_change=changetab,
        selected_index=0,
        destinations=[
            NavigationBarDestination(icon="home", label="All Goals"),
            NavigationBarDestination(icon="explore", label = "Planner"),
            NavigationBarDestination(icon="settings", label = "Settings"),
        ]
    )

    tab_1 = Text("Tab 1", size=30, visible=True)
    tab_2 = next_hour_planner_widget(visible=False)
    tab_3 = Text("Tab 3", size=30, visible=False)

    page.add(
        Container(
            # margin=margin.only(
            #     top=page.window.height / 2,
            #     left=50
            #
            # ),
            content=Column([
                tab_1,
                tab_2,
                tab_3

            ])

        )

    )


app(target=main)
