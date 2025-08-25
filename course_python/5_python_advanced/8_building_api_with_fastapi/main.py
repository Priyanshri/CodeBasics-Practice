# uninstall previous version of fastapi if any by : pip uninstall fastapi or, pip uninstall uvicorn
# install fastapi by : pip install "fastapi[standard]" 

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

food_items = {
    'indian' : [ "Samosa", "Dosa" ],
    'american' : [ "Hot Dog", "Apple Pie"],
    'italian' : [ "Ravioli", "Pizza"]
}

class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

@app.get("/get_items/{cuisine}")
def get_items(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int):
    return { 'discount_amount': coupon_code.get(code) }


# to run this code got to the previous folder by : cd C:\Code\course_python\5_python_advanced\8_building_api_with_fastapi
#  then run : fastapi dev .\main.py or, python -m uvicorn main:app
# then open the browser by clicking the link which appears like :  http://127.0.0.1:8000
# we can see documentation by going to :  http://127.0.0.1:8000/docs

# You can see all the details of fastapi in : https://fastapi.tiangolo.com/