from app.dll.netflix_agg import data_count

# this is designed like this so that if hulu (or another streaming service) is added
# the data can come from a source other than the database (3rd party api) but still aggregated

def agg_data(column):
    # hulu calls can be configured in DLL
    # data then parsed and aggregated here
    return data_count(column)
