'''
This script is used to collect all data from different endpoint.
'''

import threading
import requests
import pandas as pd
import requests_cache
from dir_path_resolver import PathResolver
from db_connector import DBConnector
from utils import Utils

from endpoint_type import EndpointType

cache_path = PathResolver.data_dir.joinpath("req_cache")
requests_cache.install_cache(cache_path)

# param = FluSurvParams(["202003", "202004"], [FluSurvRegion.CA])

class DataFetcher():
    sem = threading.Semaphore(20)
    db_connector = DBConnector()

    @staticmethod
    def fetch(endpoint: EndpointType, param, does_store: bool = True):
        DataFetcher.sem.acquire()
        base_url = str(endpoint)
        json = requests.get(base_url, param.query()).json()
        DataFetcher.sem.release()

        result_df = Utils.extract_epidata(json)

        if does_store:
            DataFetcher.store_without_dup(result_df, endpoint)

        return result_df

    @staticmethod
    def store_without_dup(df: pd.DataFrame, endpoint_type: EndpointType):
        '''
        This function is not memory efficient, use it with caution.
        '''

        db_query = f"""
        select * from {DBConnector.resolveTableName(endpoint_type)}
        """
        existing_db = DataFetcher.db_connector.read(db_query)
        concat_df = pd.concat(
            [existing_db, df], 
            ignore_index=True
        )
        no_dup_df = concat_df.drop_duplicates(ignore_index=True)

        DataFetcher.db_connector.write(no_dup_df, endpoint_type)
        

# print(EndpointType.FLUSURV == EndpointType.FLUSURV)

# print(DataFetcher.fetch(EndpointType.FLUSURV, param))

