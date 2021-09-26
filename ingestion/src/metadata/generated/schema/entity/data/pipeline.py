# generated by datamodel-codegen:
#   filename:  schema/entity/data/pipeline.json
#   timestamp: 2021-09-25T21:02:32+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import AnyUrl, BaseModel, Field, constr

from ...type import basic, entityReference, tagLabel


class Pipeline(BaseModel):
    id: basic.Uuid = Field(
        ..., description='Unique identifier that identifies a pipeline instance.'
    )
    name: constr(min_length=1, max_length=64) = Field(
        ..., description='Name that identifies this pipeline instance uniquely.'
    )
    displayName: Optional[str] = Field(
        None,
        description='Display Name that identifies this Pipeline. It could be title or label from the source services.',
    )
    fullyQualifiedName: Optional[constr(min_length=1, max_length=64)] = Field(
        None,
        description="A unique name that identifies a pipeline in the format 'ServiceName.PipelineName'.",
    )
    description: Optional[str] = Field(
        None, description='Description of this Pipeline.'
    )
    pipelineUrl: Optional[AnyUrl] = Field(
        None,
        description='Pipeline  URL to visit/manage. This URL points to respective pipeline service UI',
    )
    tasks: Optional[List[entityReference.EntityReference]] = Field(
        None, description='All the tasks that are part of pipeline.'
    )
    followers: Optional[entityReference.EntityReferenceList] = Field(
        None, description='Followers of this Pipeline.'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Pipeline.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this pipeline.'
    )
    service: entityReference.EntityReference = Field(
        ..., description='Link to service where this pipeline is hosted in.'
    )
