from motor.motor_asyncio import AsyncIOMotorClient

#db url
MONGO_URL = "mongodb://localhost:27017/"
DATABASE_NAME ="Advertisement"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
role_collection = db["roles"]
user_collection = db["users"]
department_collection = db["departments"]
employee_collection = db["employees"]
state_collection = db["states"]
city_collection = db["cities"]
area_collection = db["area"]
product_collection = db["products"]
advertisement_collection = db["advertisement"]