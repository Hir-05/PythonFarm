from fastapi import APIRouter,HTTPException
from controllers import CityControllers #.....
from models.CityModel import City,CityOut
from bson import ObjectId

router = APIRouter()
@router.post("/city")
async def post_city(city:City):
    return await CityControllers.addCity(city)

@router.get("/city")
async def get_city():
    return await CityControllers.getCity()