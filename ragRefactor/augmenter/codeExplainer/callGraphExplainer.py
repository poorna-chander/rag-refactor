import numpy as np
from ragRefactor.dataService.code_ql.codeQuery import getCallerCalleeDetails, getPkgClassCallableDetails 

def explainCallGraph(mode = "query"):
    if mode == "query":
        callerCaleeDF = getCallerCalleeDetails()
        # pkgClassMethodDF = getPkgClassCallableDetails()

    callerCaleeDF["caller_class"] = callerCaleeDF["call_encapsule_location"].apply(lambda x: genPackageClass(x))
    callerCaleeDF["callee_class"] = callerCaleeDF["callee_location"].apply(lambda x: genPackageClass(x))
    callerCaleeDF["callee"] = np.where(callerCaleeDF["callee_feat_type"].str.strip() == "Constructor", "Constructor", callerCaleeDF["callee"].str.strip())
    callerCaleeDF["call_encapsule"] = np.where(callerCaleeDF["call_encapsule_feat_type"].str.strip() == "Constructor", "Constructor", callerCaleeDF["call_encapsule"].str.strip())
    callerCaleeDF = callerCaleeDF[["call_encapsule","caller_class","callee","callee_class"]]
    callerCaleeDF.columns = ["caller_method","caller_class","callee_method","callee_class"]
    callerCaleeDF = callerCaleeDF[callerCaleeDF["callee_method"].str.strip() != "<obinit>"]
    formatted_output = formatCallGraphYAML(callerCaleeDF)
    print("here")
def formatCallGraphYAML(callGraphDF):
    formatted_output = ""

    grouped_df = callGraphDF.groupby(['caller_class', 'caller_method'])

    for (caller_class, caller_method), group in grouped_df:
        formatted_output += f"Class {caller_class}:\n"
        formatted_output += f"    - Method {caller_method}\n"
        
        called_methods = group.apply(lambda row: f"{row['callee_method']} in {row['callee_class']}", axis=1).tolist()
        
        if called_methods:
            formatted_output += f"        Calls to: {called_methods}\n\n"
        else:
            formatted_output += f"        Calls to: []\n\n"
    
    return formatted_output
    
def genPackageClass(x):
    pkgLoc= x.split("/")[-2:]
    return ".".join([pkgLoc[0], pkgLoc[-1].split(":")[0].split(".")[0]])
    
if __name__=="__main__":
    explainCallGraph()