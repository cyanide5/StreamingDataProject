from app.dll.netflix_agg import data_count


def agg_data(column):
    # hulu calls can be configured in DLL
    # data then parsed and aggregated here
    return data_count(column)
