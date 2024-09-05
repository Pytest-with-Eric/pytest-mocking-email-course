from unittest.mock import patch
from src.shipment_processor_v2 import create_shipment

API_URL = "https://api.cargo.example"


@patch("src.shipment_processor_v2.uuid")
@patch("src.shipment_processor_v2.requests")
def test_does_PUT_if_shipment_already_exists(mock_requests, mock_uuid):
    mock_uuid.uuid4.return_value.hex = "our-id"
    mock_requests.get.return_value.json.return_value = [
        {"id": "their-id", "client_reference": "our-id"}
    ]

    shipment = create_shipment({"sku": 10}, incoterm="EXW")
    assert mock_requests.post.called is False
    expected_data = {
        "client_reference": "our-id",
        "arrival_date": None,
        "products": [{"sku": "sku", "quantity": 10}],
    }
    assert mock_requests.put.call_args == (
        (f"{API_URL}/shipments/their-id",),
        {"json": expected_data},
    )
