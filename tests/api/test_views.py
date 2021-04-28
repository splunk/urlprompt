from tests.conftest import api_user_client
import pytest

@pytest.mark.django_db
class TestViews:
    def test_authenticated_user_cannot_list_prompts(self, api_user_client):
        res = api_user_client.get("/api/prompts/")
        assert res.status_code == 403 

    def test_anon_user_cannot_list_prompts(self, anon_user_client):
        res = anon_user_client.get("/api/prompts/")
        assert res.status_code == 401 
    
    def test_admin_user_can_list_prompts(self, admin_user_client):
        res = admin_user_client.get("/api/prompts/")
        assert res.status_code == 200
