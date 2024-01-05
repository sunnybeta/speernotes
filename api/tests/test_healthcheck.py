def test_healthcheck(client):
    res = client.get("/healthcheck")
    data = res.json()
    assert data['status'] == 'healthy'
