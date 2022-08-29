from app.dll.netflix_titles import get_details, insert_new_title


# this is designed like this so that if hulu (or another streaming service) is added
# the data can come from a source other than the database (3rd party api) but still aggregated
def title_details(title):
    return get_details(title)


def add_title(fields):
    insert_new_title(fields)
    return


def update_title(title, fields):
    return
