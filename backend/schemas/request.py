from pydantic import BaseModel

class ProjectRequest(BaseModel):
    idea:str
    experience:str
    time_weeks:int
    team:int
    tech:str

    print("schema-request-2")