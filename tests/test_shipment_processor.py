from unittest.mock import patch
from src.shipment_processor import create_shipment


@patch("src.shipment_processor.requests")
def test_create_shipment_does_post_to_external_api(mock_requests):
    shipment = create_shipment(quantities={"sku1": 10}, incoterm="EXW")
    expected_data = {
        "client_reference": shipment.reference,
        "arrival_date": None,
        "products": [{"sku": "sku1", "quantity": 10}],
    }
    assert mock_requests.post.call_args == (
        ("f{API_URL}/shipments",),
        {"json": expected_data},
    )
