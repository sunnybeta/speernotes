def test_create_note_and_get_note(client):
    res = client.post("/api/notes", json={"title":"test_title","content":"test_content"})
    data = res.json()
    note_id = data['data']['id']
    assert res.status_code == 201
    assert note_id.startswith("not")
    res = client.get(f"/api/notes/{note_id}")
    assert res.status_code == 200
    res = client.post("/api/notes", json={"title":"test_title_2","content":"test_content_1"})
    res = client.post("/api/notes", json={"title":"test_title_3","content":"test_content_2"})
    res = client.get("/api/notes")
    data = res.json()
    assert len(data['data']) == 3
    assert res.status_code == 200


def test_update_notes_by_id(client):
    res = client.post("/api/notes", json={"title":"test_title","content":"test_content"})
    data = res.json()
    note_id = data['data']['id']
    res = client.put(f"/api/notes/{note_id}", json={"title":"updated_title_0","content":"updated_content_0"})
    assert res.status_code == 202
    res = client.get(f"/api/notes/{note_id}")
    data = res.json()
    assert data['data']['title']  == "updated_title_0"
    assert data['data']['content'] == "updated_content_0"


def test_delete_note_by_id(client):
    res = client.post("/api/notes", json={"title":"test_title_4","content":"test_content_4"})
    data = res.json()
    note_id = data['data']['id']
    res = client.delete(f"/api/notes/{note_id}")
    assert res.status_code == 204
    res = client.get(f"/api/notes/{note_id}")
    assert res.status_code == 404
