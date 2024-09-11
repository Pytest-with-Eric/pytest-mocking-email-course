from src.shipment_processor_fake_dep_injection import create_shipment, FakeCargoAPI


def test_create_shipment_syncs_to_api():
    fake_api = FakeCargoAPI()
    shipment = create_shipment({"sku1": 10}, incoterm="EXW", cargo_api=fake_api)
    assert shipment in fake_api
