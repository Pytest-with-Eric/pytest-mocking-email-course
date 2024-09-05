from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict
import uuid
import requests

API_URL = "https://api.cargo.example"


@dataclass
class OrderLine:
    sku: str
    qty: int


@dataclass
class Shipment:
    reference: str
    lines: List[OrderLine]
    eta: Optional[date]
    incoterm: str  # where the shipment changes ownership

    def save(self):
        pass


def create_shipment(
    quantities: Dict[str, int],
    incoterm: str,
):
    reference = uuid.uuid4().hex[:10]
    order_lines = [OrderLine(sku=sku, qty=qty) for sku, qty in quantities.items()]
    shipment = Shipment(
        reference=reference,
        lines=order_lines,
        eta=None,
        incoterm=incoterm,
    )
    shipment.save()
    sync_to_api(shipment)
    return shipment


def sync_to_api(shipment: Shipment):
    """
    Sync the shipment to the Cargo API - If the shipment already exists, update it
    """
    external_shipment_id = get_shipment_id(shipment.reference)
    if external_shipment_id is None:
        requests.post(
            f"{API_URL}/shipments",
            json={
                "client_reference": shipment.reference,
                "arrival_date": shipment.eta,
                "products": [
                    {"sku": ol.sku, "quantity": ol.qty} for ol in shipment.lines
                ],
            },
        )
    else:
        requests.put(
            f"{API_URL}/shipments/{external_shipment_id}",
            json={
                "client_reference": shipment.reference,
                "arrival_date": shipment.eta,
                "products": [
                    {"sku": ol.sku, "quantity": ol.qty} for ol in shipment.lines
                ],
            },
        )


def get_shipment_id(our_reference: str) -> Optional[str]:
    their_shipments = requests.get(f"{API_URL}/shipments").json()
    return next(
        (s["id"] for s in their_shipments if s["client_reference"] == our_reference),
        None,  # Return None if no matching shipment is found
    )
