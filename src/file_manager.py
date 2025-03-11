import pandas as pd
import json
import polars as pl


def read_csv(file, delimiter=',', header=0):
    return pd.read_csv(file, delimiter=delimiter, header=header)

def read_orc(file):
    return pd.read_orc(file)

def read_parquet(file): 
    return pl.read_parquet(file)

def read_avro(file):
    df = pl.read_avro(file)
    json_obj = df.to_dicts() 
    return json_obj # I'm returning a json object for avro because it has nested structures

def read_json(file):
    return json.load(file)



FILE_HANDLERS = {
    ".csv": {
        "reader": read_csv,
        "options": {"header": 0, "delimiter": ","}, 
    },
    ".orc": {
        "reader": read_orc,
        "options": {}
    },
    ".parquet": {
        "reader": read_parquet,
        "options": {}
    },
    ".avro": {
        "reader": read_avro,
        "options": {}
    },
    ".json": {
        "reader": read_json,
        "options": {}
    }
}

def is_supported(file_type):
    return file_type in FILE_HANDLERS

def read_file(file, file_type, **kwargs):    
    if file_type in FILE_HANDLERS:
        return FILE_HANDLERS[file_type]["reader"](file, **kwargs)
    return None