from main import create_sample_data


def test_create_sample_data_not_return_empty():
    test_tb_clients, test_tb_travels, test_tb_packages = [], [], []

    assert len(test_tb_clients) == 0
    assert len(test_tb_travels) == 0
    assert len(test_tb_packages) == 0

    create_sample_data(test_tb_clients, test_tb_travels, test_tb_packages)

    assert len(test_tb_clients) == 4
    assert len(test_tb_travels) == 4
    assert len(test_tb_packages) == 12


test_create_sample_data_not_return_empty()
