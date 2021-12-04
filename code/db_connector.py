import pandas as pd
import sqlalchemy as sqla
import threading
from endpoint_type import EndpointType

db_protocol = "sqlite:///"
db_filename = "../data/influenza_data.sqlite"
db_conn_str = db_protocol + db_filename

class DBConnector():
    mutex = threading.Lock()

    def __init__(self) -> None:
        self.db_conn = sqla.create_engine(db_conn_str)

    def write(self, df: pd.DataFrame, endpoint_type: EndpointType):
        table_name = DBConnector.resolveTableName(endpoint_type)
        
        DBConnector.mutex.acquire()
        df.to_sql(table_name, self.db_conn, if_exists="append")
        DBConnector.mutex.release()

    def read(self, query: str) -> pd.DataFrame:
        pd.read_sql_query(query, self.db_conn)

    def get_table_name(endpoint_type: EndpointType) -> str:
        return DBConnector.resolveTableName(endpoint_type)

    @staticmethod
    def resolveTableName(endpoint_type: EndpointType) -> str:
        if endpoint_type == EndpointType.FLUSURV:
            return "flusurv"
        if endpoint_type == EndpointType.FLUVIEW:
            return "fluview"
        if endpoint_type == EndpointType.GFT:
            return "gft"
        if endpoint_type == EndpointType.WIKI:
            return "wiki"
