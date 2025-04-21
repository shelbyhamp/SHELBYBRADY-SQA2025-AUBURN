from hypothesis import given, settings, strategies as st
import json
import pandas as pd
from io import StringIO

from main import getCountFromAnalysis
import scanner  # Make sure scanner.runScanner() can accept string paths
import constants

import csv
import os

# Ensure results directory exists
os.makedirs("integration-test-results", exist_ok=True)

# Create fuzz_report.csv with headers
with open("integration-test-results/fuzz_report.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Function", "Input", "Error"])

def log_crash(func_name, input_val, error):
    with open("integration-test-results/fuzz_report.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            func_name,
            str(input_val).replace(",", ";"),
            str(error).replace(",", ";")
        ])


# 1. Test getCountFromAnalysis with random list of tuples
@given(
    st.lists(
        st.tuples(
            st.text(),  # dir_name
            st.text(),  # script_name
            st.tuples(
                st.lists(st.text()),  # unameDict
                st.lists(st.text()),  # passwordDict
                st.lists(st.text()),  # tokenDict
            ),
            st.lists(st.text()),  # templa_secret
            st.lists(st.text()),  # taint_secret
            st.dictionaries(st.text(), st.text()),  # privilege_dic
            st.dictionaries(st.text(), st.text()),  # http_dict
            st.dictionaries(st.text(), st.text()),  # secuContextDic
            st.dictionaries(st.text(), st.text()),  # nSpaceDict
            st.dictionaries(st.text(), st.text()),  # absentResoDict
            st.dictionaries(st.text(), st.text()),  # rollUpdateDic
            st.dictionaries(st.text(), st.text()),  # netPolicyDict
            st.dictionaries(st.text(), st.text()),  # pidfDict
            st.dictionaries(st.text(), st.text()),  # ipcDict
            st.dictionaries(st.text(), st.text()),  # dockersockDic
            st.dictionaries(st.text(), st.text()),  # hostNetDict
            st.dictionaries(st.text(), st.text()),  # cap_sys_dic
            st.dictionaries(st.text(), st.text()),  # host_alias_dic
            st.dictionaries(st.text(), st.text()),  # allow_priv_dic
            st.dictionaries(st.text(), st.text()),  # unconfined_dic
            st.dictionaries(st.text(), st.text()),  # cap_module_dic
            st.booleans(),  # k8s_flag
            st.booleans(),  # helm_flag
        )
    )
)
@settings(max_examples=20)
def test_getCountFromAnalysis(input_data):
    try:
        getCountFromAnalysis(input_data)
    except Exception as e:
        log_crash("getCountFromAnalysis", input_data, e)


# 2. Test scanner.runScanner with fake directory names
@given(st.text())
@settings(max_examples=10)
def test_runScanner(fake_path):
    try:
        scanner.runScanner(fake_path)
    except Exception as e:
        log_crash("runScanner", fake_path, e)



# 3. Test pd.read_csv with generated CSV strings
@given(st.text())
@settings(max_examples=10)
def test_dataframe_read(data):
    try:
        csv_like = StringIO(data)
        pd.read_csv(csv_like)
    except Exception as e:
        log_crash("pd.read_csv", data, e)


# 4. JSON parsing fuzz
@given(st.text())
@settings(max_examples=10)
def test_json_parsing(data):
    try:
        json.loads(data)
    except Exception as e:
        log_crash("json.loads", data, e)


# 5. to_csv with a DataFrame and known CSV_HEADER
@given(st.text())
@settings(max_examples=10)
def test_dataframe_to_csv(data):
    try:
        df = pd.DataFrame([[data]])
        df.to_csv(StringIO(), header=constants.CSV_HEADER, index=False, encoding=constants.CSV_ENCODING)
    except Exception as e:
        log_crash("df.to_csv", data, e)


# Entry point
if __name__ == '__main__':
    test_getCountFromAnalysis()
    test_runScanner()
    test_dataframe_read()
    test_json_parsing()
    test_dataframe_to_csv()
