import gzip
import os
from fitparse import FitFile
import pandas as pd
from datetime import datetime, timedelta

def read_fit_file(file_path):
    with gzip.open(file_path,'rb') as gz_file:
        fit_data = gz_file.read()

    fitfile = FitFile(fit_data)

    records = []
    for record in fitfile.get_messages("record"):
        record_data = {}
        for record_data_entry in record:
            record_data[record_data_entry.name] = record_data_entry.value
        records.append(record_data)
    
    df = pd.DataFrame(records)
    return df

foo = read_fit_file('../Data/activities/12098685657.fit.gz')

print(foo)
