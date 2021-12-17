# function to write sql query into folder of flat files

from sqlalchemy import create_engine
from pathlib import Path
import pandas as pd
import re

import Configurations as config


def write_sql_query_to_folder():

    # connect to sql db
    engine = create_engine(
        "mssql+pyodbc://"
        + config.DB["servername"]
        + "/"
        + config.DB["database"]
        + "?"
        + config.DB["driver"]
    )
    conn = engine.connect().execution_options(stream_results=True)

    # check folder is empty and throw an exception if not
    if Path(config.DATAREADS).exists():
        if any(Path(config.DATAREADS).iterdir()):
            raise Exception(
                f"Please empty the folder {config.DATAREADS} and run file again."
            )
    else:
        Path(config.DATAREADS).mkdir()

    # create regex object to remove quotes and bars
    quoteBarRegex = re.compile(r'["|]')

    # write new files
    for batch, chunk_dataframe in enumerate(
        pd.read_sql(config.SELECTQUERY, conn, chunksize=config.NUMBEROFROWS)
    ):

        # check progress
        print(f"Dataframe {batch+1} has {len(chunk_dataframe)} rows")

        # open new file
        f = open(Path(config.DATAREADS) / f"dataread_{batch+1}.csv", "w", newline="")

        # apply regex object
        chunk_dataframe["column_name"] = chunk_dataframe["column_name"].apply(
            lambda x: quoteBarRegex.sub("", x)
        )

        # write csv
        chunk_dataframe.to_csv(f, sep="|", header=False, index=False)

    # Clean up
    f.close()
    conn.close()


if __name__ == "__main__":
    write_sql_query_to_folder()

### END


# NOTES:
# need inputs for the following in Configurations:
#
# # connecting to SQL
# DB = {
#     "servername": "MY_SERVER_NAME",
#     "database": "MY_DATABASE_NAME",
#     "driver": "driver=ODBC Driver 17 for SQL Server",
# }
#
# SCHEMA = "MY_SCHEMA_NAME"
#
# OUTPUTTABLENAME = "MY_OUTPUT_TABLE_NAME"
#
# select query
# SELECTQUERY = "SELECT * FROM MYTABLE"
#
# folder for data reads
# DATAREADS = r"folder to save data reads to"
# DATAOUTPUT = r"folder to save output data to"
#
# NUMBEROFROWS = 500000