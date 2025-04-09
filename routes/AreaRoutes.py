from bson import ObjectId
from fastapi import APIRouter,HTTPException
from controllers import AreaController
from models.AreaModel import Area,AreaOut

router = APIRouter()
@router.post("/area")
async def post_area(area: Area):
    return await AreaController.addArea(area)

@router.get("/area")
async def get_area():
    return await AreaController.getArea()