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
        if '__class__' in jsonDict:
            class_name = jsonDict.pop('__class__')
            module_name = jsonDict.pop('__module__')
            print("class_name:%s module_name:%s"%(class_name, module_name))
            #class_ = getattr(module_name, class_name)
            class_ = globals()[class_name]
            args = dict((str(key.encode('ascii')), value) for key, value in jsonDict.items())
            instance = class_(**args)
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
    MyJsonDecoder().decode(jsonStr)
