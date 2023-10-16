import pandas as pd
from scipy.spatial.distance import cdist


def find_nearest_station(
    lat: float, lon: float, stations_df: pd.DataFrame, station_col: str
) -> str:
    """
    Given a latitude and longitude, find the nearest weather station
    from a dataframe of weather stations and their coordinates.

    Parameters:
    lat (float): Latitude of the point of interest
    lon (float): Longitude of the point of interest
    stations_df (pd.DataFrame): DataFrame of weather stations with 'latitude', 'longitude', and 'STATION_NAME' columns

    Returns:
    str: The name of the nearest weather station

    Example:
    >>> df['nearest_station'] = df.apply(
    ...     lambda row: find_nearest_station(row['lat'], row['long'], stations_df), axis=1
    ... )
    """
    distances = cdist(
        [(lat, lon)], stations_df[["latitude", "longitude"]].values, metric="euclidean"
    )
    closest_station_idx = distances.argmin()

    return stations_df.iloc[closest_station_idx][station_col]
