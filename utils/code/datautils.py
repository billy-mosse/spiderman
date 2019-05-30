"""This function does something.

    Args:
       name (str):  The name to use.

    Kwargs:
       state (bool): Current state to be in.

    Returns:
       int.  The return code::

          0 -- Success!
          1 -- No good.
          2 -- Try again.

    Raises:
       AttributeError, KeyError

    A really great idea.  A way you might use me is

    >>> print public_fn_with_googley_docstring(name='foo', state=None)
    0

    BTW, this always returns 0.  **NEVER** use with :class:`MyPublicClass`.

    """

import pandas as pd
import numpy as np
import os
import requests
import geopandas as gpd
import mplleaflet
import zipfile

def download_file(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(response.content)



def load_csv(year):
    """
    This function returns a pandas dataframe of the #year dataset in the data.buenosaires.gob.ar dataset
    """
    try:
        return pd.read_csv('data/bici%d_cdn.csv' % year)

    except FileNotFoundError:
        url="http://cdn.buenosaires.gob.ar/datosabiertos/datasets/bicicletas-publicas/recorridos-realizados-%d.csv" % year
        filename = os.path.join("data", "bici%d_cdn.csv" % year)
        download_file(url, filename)

        return load_csv(year)


def load_2018_csv():
    """
    This function returns a pandas dataframe of the 2018 dataset in the data.buenosaires.gob.ar dataset
    """
    return load_csv(2018)



def load_estaciones(): 
    """ESTA NO ANDA"""
    if os.path.isfile('data/estaciones_de_bicicletas.shp'):
        return gpd.read_file('data/estaciones_de_bicicletas.shp')
    else:
        download_file("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/estaciones-bicicletas-publicas/estaciones-de-bicicletas-zip.zip", "data/estaciones_de_bicicletas.shp")
        download_file("http://cdn.buenosaires.gob.ar/datosabiertos/datasets/estaciones-bicicletas-publicas/estaciones-de-bicicletas-publicas.csv", "data/estaciones-de-bicicletas-publicas.csv")

        #zip_ref = zipfile.ZipFile("data/estaciones_de_bicicletas.zip", 'r')
        #zip_ref.extractall("data")
        #zip_ref.close()

        return load_estaciones()

print(load_estaciones().head())