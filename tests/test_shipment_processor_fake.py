from unittest.mock import patch
from src.shipment_processor_fake import create_shipment, FakeCargoAPI


@patch("src.shipment_processor_fake.RealCargoAPI")
def test_create_shipment_syncs_to_api(mock_RealCargoAPI):
    fake_api = FakeCargoAPI()
    mock_RealCargoAPI.return_value = fake_api
    shipment = create_shipment({"sku1": 10}, incoterm="EXW")
    assert shipment in fake_api
