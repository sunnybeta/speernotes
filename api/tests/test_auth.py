def test_signup(client):
    res = client.post("/api/auth/signup", json={
        'username':'test_username',
        'email':'test@mailman.com',
        'password':'Abc@123'
    })
    data = res.json()['data']
    assert data['id'].startswith("usr_")
    assert "id" in data
    assert "username" in data
    assert "email" in data
    assert "token" in data
    assert res.status_code == 201
    res = client.post("/api/auth/signup", json={
        'username':'test_username',
        'email':'test@mailman.com',
        'password':'Abc@123'
    })
    assert res.status_code == 400

def test_login_with_email(client):
    res = client.post("/api/auth/login", json={
        'user':'test@mailman.com',
        'password':'Abc@123'
    })
    assert res.status_code == 200

def test_login_with_username(client):
    res = client.post("/api/auth/login", json={
        'user':'test_username',
        'password':'Abc@123'
    })
    assert res.status_code == 200

def test_login_failed_invalid_password(client):
    res = client.post("/api/auth/login", json={
        'user':'test_username',
        'password':'Abc@124'
    })
    assert res.status_code == 400

def test_login_failed_invalid_username(client):
    res = client.post("/api/auth/login", json={
        'user':'test_usernamee',
        'password':'Abc@123'
    })
    assert res.status_code == 400
