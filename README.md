# Agro-py

Agro-py is a collection of Python projects aimed at providing solutions for various agricultural needs. Each project focuses on a specific aspect of agriculture, leveraging the power of Python to simplify and automate tasks.

## Installation
To install the API, clone the repository and install the required dependencies:
```bash
git clone https://github.com/josehenriqueroveda/it_services_api.git
cd it_services_api
pip install -r requirements.txt

python -m spacy download pt_core_news_sm
```

## Projects

### Find Nearest Weather Station

This project is designed to find the nearest weather station given a specific latitude and longitude. This can be particularly useful for farmers who want to get the most accurate weather data for their specific location.

The main function in this subproject is `find_nearest_station(lat, lon, stations_df, station_col)`. This function takes in a latitude and longitude, along with a DataFrame of weather stations (which includes their coordinates), and returns the name of the nearest weather station.

Here's an example of how to use it:

```python
df['nearest_station'] = df.apply(
    lambda row: find_nearest_station(row['lat'], row['long'], stations_df, 'STATION_NAME'), axis=1
)
```


---

## License
This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
If you find a bug or have a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository and submit a pull request.

Before submitting a pull request, please make sure that your code adheres to the following guidelines:
 - Follow the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide.
 - Write docstrings for all functions and classes.
 - Write unit tests for all functions and classes.
 - Make sure that all tests pass by running pytest.
 - Keep the code simple and easy to understand.
