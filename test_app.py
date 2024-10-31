 # testapp.py

from app import app  # Import the Flask app from app.py

def test_home():
    # Use the Flask test client to simulate requests
    with app.test_client() as client:
        response = client.get('/')  # Send a GET request to the home route

        # Check that the response status code is 200 (OK)
        assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"

        # Check that the response data matches the expected JSON structure
        expected_response = {"message": "Hello level 400 FET, Quality Assurance!"}
        assert response.get_json() == expected_response, \
            f"Expected JSON response {expected_response} but got {response.get_json()}"
