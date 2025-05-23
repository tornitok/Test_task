```markdown
# Test Task Project

## Overview

This project is a test automation suite that includes:

- ✅ **API testing** using `pytest` and `requests`
- 🎯 **UI testing** using `Selenium WebDriver`
- 🔧 Modular architecture using page objects and API endpoint classes
- 📦 Easy configuration and session management using `pytest` fixtures

The tests target both UI elements of a web application (https://www.saucedemo.com/) and the endpoints of the Airport Gap API ([https://airportgap.com/docs](https://airportgap.com/docs)).

---

## Project Structure


Test\_task/
├── api/                    # API endpoint classes (e.g., airports, distance)
│   └── endpoints/
├── pages/                  # UI page object models (e.g., login, inventory)
├── tests/
├── config/                 # Base URL and configuration values
├── conftest.py             # Fixtures for drivers, sessions, and test setup
└── README.md


---

## Installation

1. **Clone the repository**:

   ```bash
   git clone <your-repo-url>
   cd Test_task
````

2. **Create a virtual environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

---

## Running Tests

### 🧪 Tests

```bash
pytest tests/
```

You can also run specific tests with:

```bash
pytest -k "test_login_page"
```

---

## Example Test Case

### API: Distance Between Airports

```python
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
    assert distance_km > 400, f"Expected > 400 km, got {distance_km} km"
```

---