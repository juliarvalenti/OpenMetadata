#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import requests

from metadata.ingestion.models.json_serializable import JsonSerializable
from metadata.config.common import ConfigModel
from metadata.ingestion.api.common import WorkflowContext, Record
from metadata.ingestion.api.sink import Sink, SinkStatus
from metadata.ingestion.models.user import MetadataUser
from metadata.ingestion.ometa.auth_provider import MetadataServerConfig

logger = logging.getLogger(__name__)


class LDAPSourceConfig(ConfigModel):
    api_end_point: str


class LdapUserRestSink(Sink, JsonSerializable):
    config: LDAPSourceConfig
    status: SinkStatus

    def __init__(self, ctx: WorkflowContext, config: LDAPSourceConfig, metadata_config: MetadataServerConfig):
        super().__init__(ctx)
        self.config = config
        self.metadata_config = metadata_config
        self.status = SinkStatus()
        self.api_users = self.metadata_config.api_endpoint + "/v1/users"
        self.headers = {'Content-type': 'application/json'}

    @classmethod
    def create(cls, config_dict: dict, metadata_config_dict: dict, ctx: WorkflowContext):
        config = LDAPSourceConfig.parse_obj(config_dict)
        metadata_config = MetadataServerConfig.parse_obj(metadata_config_dict)
        return cls(ctx, config, metadata_config)

    def write_record(self, record: Record) -> None:
        self._create_user(record)

    def _create_user(self, record: MetadataUser) -> None:
        metadata_user = MetadataUser(name=record.github_username[0],
                                     display_name=record.name[0],
                                     email=record.email[0])
        r = requests.post(self.api_users, data=metadata_user.to_json(), headers=self.headers)
        if r.status_code == 200 or r.status_code == 201:
            self.status.records_written(record.name[0])
        else:
            logging.error(r.status_code)
            logging.error(r.text)

    def get_status(self):
        return self.status

    def close(self):
        pass