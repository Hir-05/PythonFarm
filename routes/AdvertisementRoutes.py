from fastapi import APIRouter, UploadFile, File, Depends
from models.AdvertisementModel import Advertisement
from controllers.AdvertisementController import create_ad, get_all_ads

router = APIRouter()

@router.post("/ads")
async def add_ad(ad: Advertisement = Depends(), image: UploadFile = File(...)):
    return await create_ad(ad, image)

@router.get("/ads")
async def fetch_ads():
    return await get_all_ads()
