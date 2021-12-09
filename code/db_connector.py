import pandas as pd
import sqlalchemy as sqla
import threading
from dir_path_resolver import PathResolver
from endpoint_type import EndpointType

db_protocol = "sqlite:///"
data_dir = PathResolver.data_dir
db_filename = "influenza_data.sqlite"
db_file_fullpath = data_dir.joinpath(db_filename)
db_conn_str = db_protocol + str(db_file_fullpath)

class DBConnector():
    """
    A class for access created database.
    """

    mutex = threading.Lock()

    def __init__(self) -> None:
        self.db_conn = sqla.create_engine(db_conn_str)

    def write(self, 
              df: pd.DataFrame, 
              endpoint_type: EndpointType, 
              if_exists = "replace"
    ):
        """
        Write passed in dataframe to 
        corresponding table in the db
        according to endpoint type.

        Keyword Argument:

        df -- the dataframe to save.

        endpoint_type -- the endpoint you want to save.

        if_exists -- define the behavior if the content already exists (default replace)
        
        Note:
        This method is concurrenct safe.
        """
        table_name = DBConnector.resolveTableName(endpoint_type)
        
        if (len(df) == 0):
            return
        
        DBConnector.mutex.acquire()
        df.to_sql(table_name, self.db_conn, if_exists=if_exists, index=False)
        DBConnector.mutex.release()

    def read(self, query: str) -> pd.DataFrame:
        '''
        Read dataframe out based on passed in query from database.

        Parameter:

        query -- the query for fetch data.
        '''
        try:
            return pd.read_sql_query(query, self.db_conn)
        except:
            return pd.DataFrame()

    def get_table_name(endpoint_type: EndpointType) -> str:
        '''
        Helper function that wraps `DBConnector.resolveTableName`
        '''
        return DBConnector.resolveTableName(endpoint_type)

    @staticmethod
    def resolveTableName(endpoint_type: EndpointType) -> str:
        '''
        Return the table name based on given endpoint type.

        Parameter:

        endpoint_type -- the endpoint you want to use.
        '''
        if endpoint_type == EndpointType.FLUSURV:
            return "flusurv"
        if endpoint_type == EndpointType.FLUVIEW:
            return "fluview"
        if endpoint_type == EndpointType.GFT:
            return "gft"
        if endpoint_type == EndpointType.WIKI:
            return "wiki"
