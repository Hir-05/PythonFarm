from pydantic import BaseModel,Field,validator
from bson import ObjectId
from  typing import Optional,Dict,Any

class Employee(BaseModel):
    firstName: str
    lastName: str
    age: int
    department_id: str

    @validator("department_id", pre=True, always=True)
    def validate_department_id(cls, v):
        if not isinstance(v, str) or len(v) != 24:
            raise ValueError("Invalid department_id format.")
        return v



class EmployeeOut(Employee):
    id:str = Field(alias="_id")
    department :Optional[Dict[str,Any]]= None
    
    #1st validote -->emplouee object str
    @validator("id",pre=True,always=True)
    def convert_objectId(cls,v):
        if isinstance(v,ObjectId):
            return str(v)
        return v
    
    #{empoyee:,,,,,dept:{"_id":}}
    @validator("department",pre=True,always=True)
    def convertDepartmentId_str(cls,v):
        if isinstance(v,dict) and "_id" in v:
            v[" _id"] = str(v["_id"])
        return v
