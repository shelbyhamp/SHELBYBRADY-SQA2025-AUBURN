'''
Prof Akond Rahman 
Sep 21, 2022
Source Code to Run Tool on All Kubernetes Manifests  
'''
import scanner 
import pandas as pd 
import constants
import typer 
from pathlib import Path

import logging

# Configure the logger
logging.basicConfig(
    filename='integration-test-results/forensics_log.csv',
    level=logging.INFO,
    format='%(asctime)s,INFO,%(message)s'
)


def getCountFromAnalysis(ls_):
    logging.info("Starting analysis of list")
    list2ret = []

    try:
        # Iterate through each tuple in the input list
        for tup_ in ls_:
            logging.debug(f"Processing tuple: {tup_}")
            
            # Extracting data from the tuple
            dir_name = tup_[0]
            script_name = tup_[1]
            within_secret = tup_[2]  # A list of dicts: [unameDict, passwordDict, tokenDict]
            
            # Counting the secrets in the list
            within_sec_cnt = len(within_secret[0]) + len(within_secret[1]) + len(within_secret[2])
            logging.debug(f"Secret count: {within_sec_cnt}")

            # Extracting other elements from the tuple (these can be adjusted for your use case)
            templa_secret = tup_[3]
            taint_secret = tup_[4]
            privilege_dic = tup_[5]
            http_dict = tup_[6]
            secuContextDic = tup_[7]
            nSpaceDict = tup_[8]
            absentResoDict = tup_[9]
            rollUpdateDic = tup_[10]
            netPolicyDict = tup_[11]
            pidfDict = tup_[12]
            ipcDict = tup_[13]
            dockersockDic = tup_[14]
            hostNetDict = tup_[15]
            cap_sys_dic = tup_[16]
            host_alias_dic = tup_[17]
            allow_priv_dic = tup_[18]
            unconfined_dic = tup_[19]
            cap_module_dic = tup_[20]
            k8s_flag = tup_[21]
            helm_flag = tup_[22]

            # Logging the extraction of values
            logging.debug(f"Extracted values: {dir_name}, {script_name}, {within_sec_cnt}, {len(taint_secret)}, "
                          f"{len(privilege_dic)}, {len(http_dict)}, {len(secuContextDic)}, {len(nSpaceDict)}, "
                          f"{len(absentResoDict)}, {len(rollUpdateDic)}, {len(netPolicyDict)}, {len(pidfDict)}, "
                          f"{len(ipcDict)}, {len(dockersockDic)}, {len(hostNetDict)}, {len(cap_sys_dic)}, "
                          f"{len(host_alias_dic)}, {len(allow_priv_dic)}, {len(unconfined_dic)}, {len(cap_module_dic)}, "
                          f"{k8s_flag}, {helm_flag}")

            # Append the result as a tuple to the list
            list2ret.append((dir_name, script_name, within_sec_cnt, len(taint_secret), len(privilege_dic),
                             len(http_dict), len(secuContextDic), len(nSpaceDict), len(absentResoDict),
                             len(rollUpdateDic), len(netPolicyDict), len(pidfDict), len(ipcDict), len(dockersockDic),
                             len(hostNetDict), len(cap_sys_dic), len(host_alias_dic), len(allow_priv_dic),
                             len(unconfined_dic), len(cap_module_dic), k8s_flag, helm_flag))
        
        logging.info(f"Analysis completed with {len(list2ret)} results.")
    
    except Exception as e:
        logging.error(f"Error in getCountFromAnalysis: {e}")
    
    return list2ret



def main(directory: Path = typer.Argument(..., exists=True, help="Absolute path to the folder that contains Kubernetes manifests")):
    """
    Run KubeSec in a Kubernetes directory and get results in a CSV file.
    """
    logging.info(f"Started analysis for directory: {directory}")
    
    try:
        # Run the scanner to get the results
        content_as_ls, sarif_json = scanner.runScanner(directory)
        logging.info("Scanner run completed successfully.")
        
        # Write SARIF output to file
        with open("SLIKUBE.sarif", "w") as f:
            f.write(sarif_json)
            logging.debug("SARIF JSON written to SLIKUBE.sarif")

        # Process the analysis results
        df_all = pd.DataFrame(getCountFromAnalysis(content_as_ls))
        logging.info("Analysis data frame created successfully.")
        
        # Output the results to a CSV file
        outfile = Path(directory, "slikube_results.csv")
        df_all.to_csv(outfile, header=constants.CSV_HEADER, index=False, encoding=constants.CSV_ENCODING)
        logging.info(f"Results saved to {outfile}")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == '__main__':

    '''
    DO NOT DELETE ALL IN K8S_REPOS AS TAINT TRACKING RELIES ON BASH SCRIPTS, ONE OF THE STRENGTHS OF THE TOOL 
    '''
    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITHUB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_GITHUB_OUTPUT.csv'

    # ORG_DIR         = '/Users/arahman/K8S_REPOS/GITLAB_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_GITLAB_OUTPUT.csv'


    # ORG_DIR         = '/Users/arahman/K8S_REPOS/BRINTO_REPOS/'
    # OUTPUT_FILE_CSV = '/Users/arahman/Documents/OneDriveWingUp/OneDrive-TennesseeTechUniversity/Research/Kubernetes/StaticTaint/data/V16_BRINTO_OUTPUT.csv'

    # take sarif_json from scanner
    main()




