from app.dll.netflix_report import get_report_data


# this is designed like this so that if hulu (or another streaming service) is added
# the data can come from a source other than the database (3rd party api) but still aggregated


def report(sort_column, sort_dir, page_length, start, filter_by):
    return get_report_data(sort_column, sort_dir, page_length, start, filter_by)
