import pytest
import json

@pytest.mark.django_db
class TestViewAccess:
    def test_authenticated_user_cannot_list_prompts(self, api_user_client):
        res = api_user_client.get("/api/prompts/")
        assert res.status_code == 403

    def test_anon_user_cannot_list_prompts(self, anon_user_client):
        res = anon_user_client.get("/api/prompts/")
        assert res.status_code == 401

    def test_admin_user_can_list_prompts(self, admin_user_client):
        res = admin_user_client.get("/api/prompts/")
        assert res.status_code == 200

    def test_anon_user_can_retrieve_prompt(self, anon_user_client, new_prompt):
        res = anon_user_client.get(
            f"/api/prompts/{new_prompt.id}/",
            headers={"Accept": "application/json", "Content-Type": "application/json"}
        )

        assert res.status_code == 200

@pytest.mark.django_db
class TestViewOperations:
    def test_anon_user_can_patch_new_prompt(self, anon_user_client, new_prompt, new_prompt_response):
        res = anon_user_client.patch(
            f"/api/prompts/{new_prompt.id}/",
            data=json.dumps(new_prompt_response),
            content_type="application/json",
            headers={"Accept": "application/json", "Content-Type": "application/json"}
        )

        assert res.status_code == 200

    def test_anon_user_can_patch_new_prompt_and_response_persists(self, anon_user_client, new_prompt, new_prompt_response):
        print(new_prompt_response)
        res = anon_user_client.patch(
            f"/api/prompts/{new_prompt.id}/",
            data=json.dumps(new_prompt_response),
            content_type="application/json",
            headers={"Accept": "application/json"}
        )

        assert "response" in res.json() and res.json()["response"]

    def test_anon_user_cannot_patch_new_prompt_badly(self, anon_user_client, new_prompt, new_prompt_response):
        res = anon_user_client.patch(
            f"/api/prompts/{new_prompt.id}/",
            data=json.dumps({"wrong format": new_prompt_response}),
            content_type="application/json",
            headers={"Accept": "application/json", "Content-Type": "application/json"}
        )

        assert res.status_code == 400

    def test_auth_user_can_create_new_prompt(self, api_user_client, new_prompt_schema):
            
            res = api_user_client.post(
                f"/api/prompts/",
                data=json.dumps({"schema": new_prompt_schema}),
                content_type="application/json",
                headers={"Accept": "application/json"}
            )

            assert res.status_code == 201

    def test_anon_user_cannot_patch_completed_prompt(self, anon_user_client, new_prompt, new_prompt_response):
        res_complete = anon_user_client.patch(
            f"/api/prompts/{new_prompt.id}/",
            data=json.dumps(new_prompt_response),
            content_type="application/json",
            headers={"Accept": "application/json", "Content-Type": "application/json"}
        )

        res_change = anon_user_client.patch(
            f"/api/prompts/{new_prompt.id}/",
            data=json.dumps(new_prompt_response),
            content_type="application/json",
            headers={"Accept": "application/json", "Content-Type": "application/json"}
        )

        assert res_change.status_code == 400