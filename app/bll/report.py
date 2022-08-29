from app.dll.netflix_report import get_report_data


def report(sort_column, sort_dir, page_length, start, filter_by):
    return get_report_data(sort_column, sort_dir, page_length, start, filter_by)



