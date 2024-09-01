def on_escape_event(e, page):
    if (e.key == "Escape"):
        print("initializing exit")
        page.window.close()


def print_event(e, page):
    if (e.data == "blur"):
        page.window.close()
