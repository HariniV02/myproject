import pytest
from faker import Faker
from main import perform_calculation  # Import the calculation function

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int)

@pytest.fixture
def generate_test_data(request):
    num_records = request.config.getoption("--num_records")
    records = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        expected_result = perform_calculation(a, b, operation)
        records.append((a, b, operation, expected_result))
    return records
