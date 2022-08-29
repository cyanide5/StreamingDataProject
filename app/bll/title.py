from app.dll.netflix_titles import get_details, insert_new_title


def title_details(title):
    return get_details(title)


def add_title(fields):
    insert_new_title(fields)
    return


def update_title(title, fields):
    return
