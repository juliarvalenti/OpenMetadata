# generated by datamodel-codegen:
#   filename:  schema/type/collectionDescriptor.json
#   timestamp: 2021-09-27T20:43:46+00:00

from __future__ import annotations

from typing import Optional

from pydantic import AnyUrl, BaseModel, Field

from . import profile


class CollectionInfo(BaseModel):
    name: Optional[str] = Field(
        None, description='Unique name that identifies a collection.'
    )
    documentation: Optional[str] = Field(None, description='Description of collection.')
    href: Optional[AnyUrl] = Field(
        None,
        description='URL of the API endpoint where given collections are available.',
    )
    images: Optional[profile.ImageList] = None


class SchemaForCollectionDescriptor(BaseModel):
    collection: Optional[CollectionInfo] = None
