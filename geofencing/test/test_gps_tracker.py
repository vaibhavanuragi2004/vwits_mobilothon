from geofencing.src.gps_tracker import is_within_boundary

def test_is_within_boundary():
    assert is_within_boundary((28.7, 77.1), [(28.6, 77.0), (28.8, 77.2)]) == True
    assert is_within_boundary((28.9, 77.3), [(28.6, 77.0), (28.8, 77.2)]) == False
