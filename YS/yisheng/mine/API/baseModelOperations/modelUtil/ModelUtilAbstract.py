from django.apps import apps


class ModelUtilAbstract:

    # 不输出的字段
    modelFieldExclude = []
    # 不显示的字段
    modelShowFieldExclude = []
    # 不显示的字段类型
    modelFieldTypeExclude = []

    def __init__(self,modelName):
        self.appName,self.modelName = modelName.split('_',1)
        self.modelobj = apps.get_model(self.appName, self.modelName)

    def getModel(self):
        return self.modelobj

    def getChoicesFieldDict(self):
        pass

    def getDatas(self,search_field,current_page,page_size):
        pass

    def getModelField(self):
        pass

    def getModelFieldType(self):
        pass

    def getModelShowField(self):
        pass

    def downloadModelExcel(self):
        pass

    def addObj(self,data):
        pass

    def delObj(self,IdList):
        pass

    def updateObj(self,updateData):
        pass