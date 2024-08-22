from dover_nylas import Client
from dover_nylas.resources.applications import Applications
from dover_nylas.resources.attachments import Attachments
from dover_nylas.resources.auth import Auth
from dover_nylas.resources.calendars import Calendars
from dover_nylas.resources.connectors import Connectors
from dover_nylas.resources.contacts import Contacts
from dover_nylas.resources.drafts import Drafts
from dover_nylas.resources.events import Events
from dover_nylas.resources.folders import Folders
from dover_nylas.resources.grants import Grants
from dover_nylas.resources.messages import Messages
from dover_nylas.resources.threads import Threads
from dover_nylas.resources.webhooks import Webhooks


class TestClient:
    def test_client_init(self):
        client = Client(
            api_key="test-key",
            api_uri="https://test.nylas.com",
            timeout=60,
        )

        assert client.api_key == "test-key"
        assert client.api_uri == "https://test.nylas.com"
        assert client.http_client.timeout == 60

    def test_client_init_defaults(self):
        client = Client(
            api_key="test-key",
        )

        assert client.api_key == "test-key"
        assert client.api_uri == "https://api.us.nylas.com"
        assert client.http_client.timeout == 90

    def test_client_auth_property(self, client):
        assert client.auth is not None
        assert type(client.auth) is Auth

    def test_client_applications_property(self, client):
        assert client.applications is not None
        assert type(client.applications) is Applications

    def test_client_attachments_property(self, client):
        assert client.attachments is not None
        assert type(client.attachments) is Attachments

    def test_client_calendars_property(self, client):
        assert client.calendars is not None
        assert type(client.calendars) is Calendars

    def test_client_contacts_property(self, client):
        assert client.contacts is not None
        assert type(client.contacts) is Contacts

    def test_client_connectors_property(self, client):
        assert client.connectors is not None
        assert type(client.connectors) is Connectors

    def test_client_drafts_property(self, client):
        assert client.drafts is not None
        assert type(client.drafts) is Drafts

    def test_client_events_property(self, client):
        assert client.events is not None
        assert type(client.events) is Events

    def test_client_folders_property(self, client):
        assert client.folders is not None
        assert type(client.folders) is Folders

    def test_client_grants_property(self, client):
        assert client.grants is not None
        assert type(client.grants) is Grants

    def test_client_messages_property(self, client):
        assert client.messages is not None
        assert type(client.messages) is Messages

    def test_client_threads_property(self, client):
        assert client.threads is not None
        assert type(client.threads) is Threads

    def test_client_webhooks_property(self, client):
        assert client.webhooks is not None
        assert type(client.webhooks) is Webhooks
