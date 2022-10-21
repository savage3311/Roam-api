from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import orderdata
import json
import requests
from sign_head import headers
from aut import url


blp = Blueprint("orderData", __name__, description="Operation on orderData")
@blp.route("/roam")
class Order(MethodView):
    def post(self):
        roam_data = request.get_json()
        roam_name = "dps"
        roam = {"orderData":{"customerName": roam_name,"items": [{"barcode" : roam_data["barcode"], "orderStatus": roam_data["orderStatus"], "timeStamp": roam_data["timeStamp"], "courierServiceName": roam_data["courierServiceName"], "trackingNumber": roam_data["trackingNumber"] }]} }
        orderdata[roam_name] = roam
        payload = json.dumps(roam, indent=4)
        response = requests.post(url, headers=headers, data=payload)
        return roam



