def test_airport_count(airports):
    response = airports.get_airports()
    assert response.status_code == 200, "Request failed"

    data = response.json()
    airports = data.get("data", [])

    assert len(airports) == 30, f"Expected 30 airports, got {len(airports)}"


def test_specific_airports_exist(airports):
    response = airports.get_airports()
    assert response.status_code == 200, "Request failed"

    data = response.json()
    airport_names = [airport["attributes"]["name"] for airport in data.get("data", [])]

    required_airports = {
        "Akureyri Airport",
        "St. Anthony Airport",
        "CFB Bagotville"
    }

    missing = required_airports - set(airport_names)
    assert not missing, f"Missing airports in response: {missing}"


def test_distance_between_kix_and_nrt(distance):
    payload = {
        "from": "KIX",
        "to": "NRT"
    }
    distance_api = distance(payload)
    response = distance_api.post_distance()

    assert response.status_code == 200, "Request failed"

    data = response.json()
    distance_km = data.get("data", {}).get("attributes", {}).get("kilometers")

    assert distance_km is not None, "Distance not found"
    assert distance_km > 32, f"Expected > 400 km, got {distance_km} km"