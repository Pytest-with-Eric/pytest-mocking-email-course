import uuid
import requests
from src.shipment_processor_adaptor import OrderLine, RealCargoAPI, Shipment


def test_can_create_new_shipment():
    api = RealCargoAPI("https://sandbox.cargo-api.com")
    line = OrderLine(sku="sku1", qty=10)
    ref = uuid.uuid4().hex[:10]
    shipment = Shipment(reference=ref, lines=[line], eta=None, incoterm="EXW")

    api.sync(shipment)

    shipments = requests.get(f"{api.API_URL}/shipments").json()["items"]
    new_shipment = next(s for s in shipments if s["reference"] == ref)
    assert new_shipment["arrival_date"] is None
    assert new_shipment["products"] == [{"sku": "sku1", "quantity": 10}]


def test_can_update_a_shipment():
    api = RealCargoAPI("https://sandbox.cargo-api.com")
    line = OrderLine(sku="sku1", qty=10)
    ref = uuid.uuid4().hex[:10]
    shipment = Shipment(reference=ref, lines=[line], eta=None, incoterm="EXW")

    api.sync(shipment)

    shipment.lines[0].qty = 20

    api.sync(shipment)

    shipments = requests.get(f"{api.API_URL}/shipments").json()["items"]
    new_shipment = next(s for s in shipments if s["reference"] == ref)
    assert new_shipment["products"] == [{"sku": "sku1", "quantity": 20}]
