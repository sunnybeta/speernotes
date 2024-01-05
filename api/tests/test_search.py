from app.services.search import SearchService

def test_search(client):
    res = client.get("/api/search", params={"q":"content|4"})
    data = res.json()
    assert res.status_code == 200
    assert isinstance(data['data'], list)


def test_sanitize():
    q = 'this           is some   spaced content'
    assert SearchService._sanitize_query(q) == "this|is|some|spaced|content"
