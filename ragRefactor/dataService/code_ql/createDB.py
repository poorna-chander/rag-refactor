import subprocess
import os

# print("Current working directory:", os.getcwd())
import ragRefactor.commonUtils as common

def createCodeQLDB():
    dbDirectory = common.globalConfig['codeql']['db_directory']
    repoDirectory = common.globalConfig['codeql']['repo_directory']
    for codebase, codebaseName in common.globalConfig['codeql']['sample_codebase'].items():
        databasePath = os.path.join(dbDirectory, common.globalConfig['codeql']['sample_db'][codebase])
        codebasePath = os.path.join(repoDirectory, codebaseName)
        os.chdir(codebasePath)
        subprocess.run(['codeql', 'database', 'create', '--language=java-kotlin', databasePath], check=True)

if __name__ == "__main__": 
    print(os.getcwd())   
    createCodeQLDB()
    print(os.getcwd())  

