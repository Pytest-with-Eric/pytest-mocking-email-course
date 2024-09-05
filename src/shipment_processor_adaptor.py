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


class RealCargoAPI:
    API_URL = "https://cargo-api.com"

    def sync(self, shipment: Shipment) -> None:
        external_shipment_id = self._get_shipment_id(shipment.reference)
        if external_shipment_id is None:
            requests.post(
                f"{self.API_URL}/shipments",
                json={},
            )
        else:
            requests.put(
                f"{self.API_URL}/shipments/{external_shipment_id}",
                json={},
            )

    def get_latest_eta(self, reference: str) -> Optional[date]:
        pass

    def _get_shipment_id(self, our_reference: str) -> Optional[str]:
        pass


def create_shipment(
    quantities: Dict[str, int],
    incoterm: str,
    real_cargo_api: RealCargoAPI,
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
    real_cargo_api.sync(shipment)
    return shipment
