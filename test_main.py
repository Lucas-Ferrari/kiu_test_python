from main import create_sample_data, insert_data, generate_report_by_day
from models import Packages


def test_create_sample_data_not_return_empty():
    test_tb_clients, test_tb_travels, test_tb_packages = [], [], []

    assert len(test_tb_clients) == 0
    assert len(test_tb_travels) == 0
    assert len(test_tb_packages) == 0

    create_sample_data(test_tb_clients, test_tb_travels, test_tb_packages)

    assert len(test_tb_clients) == 4
    assert len(test_tb_travels) == 4
    assert len(test_tb_packages) == 12
    print("test_create_sample_data_not_return_empty: OK")


def test_insert_data():
    test_tb_clients = []
    test_client_3 = (3, "Client 3", "Lucas AAA", "112341431", "Rua 3")

    assert len(test_tb_clients) == 0

    insert_data(test_tb_clients, test_client_3)

    assert len(test_tb_clients) == 1
    print("test_insert_data: OK")


def test_generate_report_by_day_no_packages():
    test_tb_travels, test_tb_packages = [], []
    test_day = "2021-01-01"

    try:
        generate_report_by_day(test_tb_packages, test_tb_travels, test_day)
    except AssertionError as e:
        assert str(e) == "No packages"
    print("test_generate_report_by_day_no_packages: OK")


def test_generate_report_by_day_no_travels():
    test_tb_travels, test_tb_packages = [], []
    test_day = "2021-01-01"
    test_package = Packages(1, 1, 1, "Fragile")
    insert_data(test_tb_packages, test_package)

    try:
        generate_report_by_day(test_tb_packages, test_tb_travels, test_day)
    except AssertionError as e:
        assert str(e) == "No travels"
    print("test_generate_report_by_day_no_travels: OK")


def test_generate_report_by_day_no_day():
    test_tb_travels, test_tb_packages, test_tb_clients = [], [], []
    test_day = None
    create_sample_data(test_tb_clients, test_tb_travels, test_tb_packages)

    try:
        generate_report_by_day(test_tb_packages, test_tb_travels, test_day)
    except AssertionError as e:
        assert str(e) == "Day is required"
    print("test_generate_report_by_day_no_day: OK")


def test_generate_report_by_day_ok():
    test_tb_travels, test_tb_packages, test_tb_clients = [], [], []
    test_day = "2023-12-01"
    create_sample_data(test_tb_clients, test_tb_travels, test_tb_packages)

    report = generate_report_by_day(test_tb_packages, test_tb_travels, test_day)

    assert report["date"] == test_day
    assert report["total_packages"] == 3
    assert report["total_earnings"] == 3 * 10
    print("test_generate_report_by_day_ok: OK")


test_create_sample_data_not_return_empty()
test_insert_data()
test_generate_report_by_day_no_packages()
test_generate_report_by_day_no_travels()
test_generate_report_by_day_no_day()
test_generate_report_by_day_ok()
