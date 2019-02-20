from model.index import IndexModel

dataModel = IndexModel()

def getList(request):
    return dataModel.getList()
