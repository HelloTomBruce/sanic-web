from model.index import IndexModel

dataModel = IndexModel()

def getList(request):
    return dataModel.getList()

def getNotice(url, encodeType, urlType):
    return dataModel.getNotice(url, encodeType, urlType)
