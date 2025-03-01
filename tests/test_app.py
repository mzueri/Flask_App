
def test_request_example(client):
    response = client.get("/hello/")
    assert b"Hello, world!" in response.data

def test_homepage(client):
    """Test the homepage route."""
    response = client.get('/')
    assert response.status_code == 200  # Check if it loads successfully

def test_404_page(client):
    """Test a non-existent route."""
    response = client.get('/nonexistent')
    assert response.status_code == 404  # Should return a 404 error