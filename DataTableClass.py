import json

class MyJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        jsonDict={}
        jsonDict['__class__'] = obj.__class__.__name__
        jsonDict['__module__'] = obj.__module__
        jsonDict.update(obj.__dict__)
        return jsonDict

class MyJsonDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2Obj)

    def dict2Obj(self, jsonDict ):
        print("jsonDict:%s  type: %s"%(jsonDict, type(jsonDict)))
        if '__class__' in jsonDict:
            class_name = jsonDict.pop('__class__')
            module_name = jsonDict.pop('__module__')
            module_ = __import__(module_name)
            print("class_name:%s module_name:%s"%(class_name, module_name))
            class_ = getattr(module_, class_name)
            instance = class_()
            for key, value in jsonDict.items():
                instance.__dict__[key] = value
        else:
            instance = jsonDict
        return instance

class DataTable:
    #attributes
    appName=None
    apkName=None
    owner=None
    depart=None
    businessDes=None
    businessRegion=None
    serverRegion=None
    
    #constructor
    def __init__(self,_appName =None,     _apkName =None,     _owner =None,     _depart =None,     _businessDes =None,     _businessRegion =None,     _serverRegion =None): 
        self.appName         =_appName        
        self.apkName         =_apkName 
        self.owner           =_owner 
        self.depart          =_depart 
        self.businessDes     =_businessDes 
        self.businessRegion  =_businessRegion
        self.serverRegion    =_serverRegion 
    

if __name__ == '__main__':
    dt = DataTable('AA','BB', 'CC')
    jsonStr=json.dumps(dt, cls=MyJsonEncoder)
    obj=MyJsonDecoder().decode(jsonStr)
    print("obj %s type %s"%(obj, type(obj)))
