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


class CargoAPI:
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


class FakeCargoAPI:
    def __init__(self):
        self._shipments = {}

    def get_latest_eta(self, reference: str) -> Optional[date]:
        return self._shipments[reference].eta

    def sync(self, shipment: Shipment) -> None:
        self._shipments[shipment.reference] = shipment

    def __contains__(self, shipment: Shipment) -> bool:
        return shipment in self._shipments.values()


def create_shipment(
    quantities: Dict[str, int],
    incoterm: str,
    cargo_api: CargoAPI,
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
    cargo_api.sync(shipment)
    return shipment
