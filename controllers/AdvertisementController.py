from fastapi import UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from models.AdvertisementModel import Advertisement, AdvertisementOut
from config.database import advertisement_collection
import cloudinary
import cloudinary.uploader


cloudinary.config(
    cloud_name="div qar hry",
    api_key="665664884198717",
    api_secret="i3um-DFO8N1H_M70elhHOoeimB0t"
)

async def create_ad(ad: Advertisement, image: UploadFile = File(...)):
    try:
        upload_result = cloudinary.uploader.upload(image.file, folder="ads/")
        image_url = upload_result.get("secure_url")

        ad_data = ad.dict()
        ad_data["image_url"] = image_url

        await advertisement_collection.insert_one(ad_data)

        return JSONResponse(status_code=201, content={"message": "Advertisement created", "data": ad_data})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_all_ads():
    ads_cursor = advertisement_collection.find()
    ads = await ads_cursor.to_list(length=None)

    return [AdvertisementOut(**ad) for ad in ads]
