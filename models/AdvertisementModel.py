from pydantic import BaseModel
from typing import Optional

class Advertisement(BaseModel):
    adtype: str
    adtitle: str
    addescription: str

class AdvertisementOut(Advertisement):
    image_url: Optional[str]
