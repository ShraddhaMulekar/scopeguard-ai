from pydantic import BaseModel

class ProjectRequest(BaseModel):
    idea:str
    experience:str
    time:str
    team:int
    tech:str