import os
from typing import Optional, List
from notion_client import Client
from unstructured_client import UNSET, OptionalNullable
from pydantic import BaseModel
from unstructured_client.types import Nullable, OptionalNullable, UNSET


class NotionSourceConnectorConfigInput(BaseModel):
    page_id: str
    recursive: Optional[bool] = False
    extensions: OptionalNullable[List[str]] = UNSET
    api_token: Optional[str] = None

    def serialize_model(self):
        """Serialize the model for API usage."""
        return {
            "page_id": self.page_id,
            "recursive": self.recursive,
            "extensions": self.extensions if self.extensions != UNSET else None,
            "api_token": self.api_token,
        }


def _prepare_notion_source_config(
    page_id: str,
    recursive: Optional[bool] = False,
    extensions: OptionalNullable[List[str]] = UNSET,
) -> NotionSourceConnectorConfigInput:
    """Prepare the Notion source connector configuration."""
    return NotionSourceConnectorConfigInput(
        page_id=page_id,
        recursive=recursive,
        extensions=extensions,
        api_token=os.getenv("NOTION_API_TOKEN"),
    )


def create_notion_source(page_id: str, recursive: bool = False, extensions: OptionalNullable[List[str]] = UNSET):
    """
    Create a Notion source connector.

    Args:
        page_id (str): ID of the Notion page to connect to.
        recursive (bool): Whether to include sub-pages.
        extensions (Optional[List[str]]): File extensions to filter data.

    Returns:
        dict: Connection details.
    """
    config = _prepare_notion_source_config(page_id, recursive, extensions)
    notion = Client(auth=config.api_token)
    page = notion.pages.retrieve(page_id=config.page_id)
    return {"status": "success", "page": page}


def update_notion_source(page_id: str, properties: dict, recursive: Optional[bool] = None, extensions: OptionalNullable[List[str]] = UNSET):
    """
    Update a Notion source connector.

    Args:
        page_id (str): ID of the Notion page to update.
        properties (dict): Properties to update on the Notion page.
        recursive (Optional[bool]): Whether to include sub-pages.
        extensions (Optional[List[str]]): File extensions to filter data.

    Returns:
        dict: Update status.
    """
    config = _prepare_notion_source_config(page_id, recursive, extensions)
    notion = Client(auth=config.api_token)
    updated_page = notion.pages.update(page_id=config.page_id, properties=properties)
    return {"status": "success", "updated_page": updated_page}


def delete_notion_source(page_id: str):
    """
    Delete a Notion source connector.

    Args:
        page_id (str): ID of the Notion page to delete.

    Returns:
        dict: Deletion status.
    """
    config = _prepare_notion_source_config(page_id)
    notion = Client(auth=config.api_token)
    # Notion API does not support deleting pages directly, so we archive it instead
    archived_page = notion.pages.update(page_id=config.page_id, archived=True)
    return {"status": "success", "archived_page": archived_page}