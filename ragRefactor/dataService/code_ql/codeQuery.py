import subprocess
import os
import pandas as pd
import ragRefactor.commonUtils as common


def getCallerCalleeDetails():
    caller_callee_df = runQueryTable("caller_callee_details.ql")
    caller_callee_df.columns = ["call","call_location","call_feat_type","call_encapsule","call_encapsule_location","call_encapsule_feat_type","call_encapsule_file_class","callee","callee_location","callee_file_class","callee_feat_type"]
    return caller_callee_df

def getPkgClassCallableDetails():
    pkg_class_mthd_df = runQueryTable("pkg_class_method.ql")
    pkg_class_mthd_df.columns = ["package","cllable_file_class","callable","param_types","return_type","callable_location"]
    return pkg_class_mthd_df

def runQueryTable(queryFile):
    dbDirectory = common.globalConfig['codeql']['db_directory']
    dbPath = os.path.join(dbDirectory, common.globalConfig['codeql']['currect_db'])
    queriesDirectory = common.globalConfig['codeql']['queries_path']
    queryPath = os.path.join(queriesDirectory, queryFile)
    output = subprocess.run(['codeql', 'query', 'run',  f'--database={dbPath}', queryPath], capture_output=True, text=True, check=True)
    df = parseStandardOutputTable(output)
    return df

def parseStandardOutputTable(outputString):
    result_lines = outputString.stdout.strip().split('\n')
    headers = [header.strip() for header in result_lines[0].split('|') if header.strip()]
    data_lines = [line.strip().split('|')[1:-1] for line in result_lines[2:]]
    caller_callee_df = pd.DataFrame(data_lines, columns=headers)
    return caller_callee_df
    
if __name__=="__main__":
    caller_callee_df = getCallerCalleeDetails()
    pkg_class_mthd_df = getPkgClassCallableDetails()
    print(pkg_class_mthd_df)