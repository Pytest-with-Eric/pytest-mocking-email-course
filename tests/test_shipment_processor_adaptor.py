from unittest.mock import patch
from src.shipment_processor_adaptor import RealCargoAPI, create_shipment


@patch("src.shipment_processor_adaptor.RealCargoAPI")
def test_create_shipment_syncs_to_api(mock_RealCargoAPI):
    # Mock RealCargoAPI instance
    mock_cargo_api = mock_RealCargoAPI.return_value

    # Create a shipment and ensure sync is called with the correct Shipment object
    shipment = create_shipment(
        {"sku1": 10}, incoterm="EXW", real_cargo_api=mock_cargo_api
    )

    # Assert that the sync method was called with the correct shipment
    mock_cargo_api.sync.assert_called_with(shipment)
