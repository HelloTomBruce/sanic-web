from model.index import IndexModel

dataModel = IndexModel()

def getList(request):
    return dataModel.getList()

def getNotice(url, encodeType):
    return dataModel.getNotice(url, encodeType)
