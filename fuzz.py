from hypothesis import given, settings, strategies as st
import json
import pandas as pd
from io import StringIO

from main import getCountFromAnalysis
import scanner  # Make sure scanner.runScanner() can accept string paths
import constants


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
        print(f"[getCountFromAnalysis] Crash: {e}")


# 2. Test scanner.runScanner with fake directory names
@given(st.text())
@settings(max_examples=10)
def test_runScanner(fake_path):
    try:
        scanner.runScanner(fake_path)
    except Exception as e:
        print(f"[runScanner] Crash: {e}")


# 3. Test pd.read_csv with generated CSV strings
@given(st.text())
@settings(max_examples=10)
def test_dataframe_read(data):
    try:
        csv_like = StringIO(data)
        pd.read_csv(csv_like)
    except Exception as e:
        print(f"[DataFrame Read] Crash: {e}")


# 4. JSON parsing fuzz
@given(st.text())
@settings(max_examples=10)
def test_json_parsing(data):
    try:
        json.loads(data)
    except Exception as e:
        print(f"[json.loads] Crash: {e}")


# 5. to_csv with a DataFrame and known CSV_HEADER
@given(st.text())
@settings(max_examples=10)
def test_dataframe_to_csv(data):
    try:
        df = pd.DataFrame([[data]])
        df.to_csv(StringIO(), header=constants.CSV_HEADER, index=False, encoding=constants.CSV_ENCODING)
    except Exception as e:
        print(f"[to_csv] Crash: {e}")


# Entry point
if __name__ == '__main__':
    test_getCountFromAnalysis()
    test_runScanner()
    test_dataframe_read()
    test_json_parsing()
    test_dataframe_to_csv()
