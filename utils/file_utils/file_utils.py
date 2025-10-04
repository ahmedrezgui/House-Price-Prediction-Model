def getUnprocessedDataSetFilePath(fileName, repositoryPath):
    return f"{repositoryPath}\\data\\raw\\{fileName}"


def getProcessedDataSetFilePath(fileName, repositoryPath):
    return f"{repositoryPath}\\data\\processed\\{fileName}"


def getSaveUtilsFilePath(repositoryPath, fileName):
    return f"{repositoryPath}\\utils\\{fileName}"
