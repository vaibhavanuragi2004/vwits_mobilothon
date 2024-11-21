from accident_response.src.severity_analyzer import assess_severity

def test_assess_severity():
    sensor_data = {"accelerometer": (5, 5, 5)}
    assert 0 <= assess_severity(sensor_data) <= 1
