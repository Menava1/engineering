from tracker import get_version


def test_tracker_version():
    assert get_version() == "0.1.0"