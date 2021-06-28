# --- Resources --- #
# Pixela website: https://pixe.la/
# Pixela API Documentation: https://docs.pixe.la/
# API Request Module Documentation: https://docs.python-requests.org/en/latest/api/

# --- Check out the Peloton Chart Here --- #
# https://pixe.la/v1/users/andrewjash/graphs/peloton1.html

# --- Modules --- #
import requests
from p_data import *
from datetime import datetime as dt


# --------------- Creating a user on Pixela --------------- #
# --- User Params for Pixela --- #
pixela_user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_user_endpoint, json=pixela_user_params)
# print(response.text)



# --------------- Creating a graph on Pixela --------------- #
pixela_graph_config = {
    "id": PELOTON_GRAPH,
    "name": "Peloton Cycling Graph",
    "unit": "Mi",
    "type": "float",
    "color": PIXELA_RED,
}
# response = requests.post(url=pixela_graph_endpoint, json=pixela_graph_config, headers=HEADERS_PIXELA)
# print(response.text)


# --------------- Post a pixel on the graph --------------- #
# /v1/users/<username>/graphs/<graphID>

# --- Import today's date and stringify it --- #
# so that YYYY / MM / DD  becomes YYYYMMDD as needed by pixela

# TODAY = dt(year=2021, month=6, day=27).strftime('%Y%m%d')
TODAY = dt.now().strftime('%Y%m%d')
# print(TODAY)
DIST_QUANTITY = "5"

pixela_pixel_config = {
    "date": TODAY,
    # "quantity": DIST_QUANTITY,
    "quantity": input("How many miles did you cycle today? ")
}

response = requests.post(url=pixela_pixel_endpoint, json=pixela_pixel_config, headers=HEADERS_PIXELA)
print(response.text)


# --------------- Update a pixel/day on the graph --------------- #
# --- YYYYMMDD as needed by pixela
UPDATE_DATE = "20210627"
new_pixel_data ={
    "quantity": "1"
}

# response = requests.put(url=f"{pixela_pixel_endpoint}/{UPDATE_DATE}", json=new_pixel_data, headers=HEADERS_PIXELA)
# print(response.text)


# --------------- DELETE a pixel/day on the graph --------------- #
#/v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
# --- YYYYMMDD as needed by pixela
DELETE_DATE = "20210628"

# response = requests.delete(url=f"{pixela_pixel_endpoint}/{DELETE_DATE}", headers=HEADERS_PIXELA)
# print(response.text)