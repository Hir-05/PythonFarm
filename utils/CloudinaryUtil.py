import cloudinary
from cloudinary.uploader import upload

cloudinary.config(
    cloud_name = "div qar hry",
    api_key="665664884198717",
    api_secret="i3um-DFO8N1H_M70elhHOoeimB0"
)

async def upload_image(image:bytes):
    result = upload(image)
    print("cloundianry response,",result)
    return result["secure_url"]