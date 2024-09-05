from dataclasses import dataclass
from datetime import date
from typing import List, Optional, Dict
import uuid
import requests


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
    Sync the shipment to the cargo API - Basic implementation
    """
    products = [{"sku": ol.sku, "quantity": ol.qty} for ol in shipment.lines]
    data = {
        "client_reference": shipment.reference,
        "arrival_date": shipment.eta.isoformat() if shipment.eta else None,
        "products": products,
    }
    requests.post("f{API_URL}/shipments", json=data)
