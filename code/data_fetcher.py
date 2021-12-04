'''
This script is used to collect all data from different endpoint.
'''

import threading
import requests
import pandas as pd
import numpy as np
import sqlalchemy as sqla
import requests_cache
from sqlalchemy.sql.expression import true
from db_connector import DBConnector
from utils import Utils
from fluview_params import FluViewParams
from flusurv_params import FluSurvRegion
from flusurv_params import FluSurvParams

from endpoint_type import EndpointType
requests_cache.install_cache('data_cache')

param = FluSurvParams(["202001", "202002"], [FluSurvRegion.CA])

class DataFetcher():
    sem = threading.Semaphore(20)
    db_connector = DBConnector()

    @staticmethod
    def fetch(endpoint: EndpointType, param, does_store: bool = true):
        DataFetcher.sem.acquire()
        base_url = str(endpoint)
        json = requests.get(base_url, param.query()).json()
        DataFetcher.sem.release()

        result_df = Utils.extract_epidata(json)

        if does_store:
            DataFetcher.store_without_dup()

        return result_df

    @staticmethod
    def store_without_dup(df: pd.DataFrame, endpoint_type: EndpointType):
        # TODO
        DataFetcher.db_connector.read()

# print(EndpointType.FLUSURV == EndpointType.FLUSURV)

print(DataFetcher.fetch(EndpointType.FLUSURV, param))

