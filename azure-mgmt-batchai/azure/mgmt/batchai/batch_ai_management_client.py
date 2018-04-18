# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.usage_operations import UsageOperations
from .operations.clusters_operations import ClustersOperations
from .operations.file_servers_operations import FileServersOperations
from .operations.workspaces_operations import WorkspacesOperations
from .operations.experiments_operations import ExperimentsOperations
from .operations.jobs_operations import JobsOperations
from . import models


class BatchAIManagementClientConfiguration(AzureConfiguration):
    """Configuration for BatchAIManagementClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscriptionID for the Azure user.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(BatchAIManagementClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-batchai/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class BatchAIManagementClient(object):
    """The Azure BatchAI Management API.

    :ivar config: Configuration for client.
    :vartype config: BatchAIManagementClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.batchai.operations.Operations
    :ivar usage: Usage operations
    :vartype usage: azure.mgmt.batchai.operations.UsageOperations
    :ivar clusters: Clusters operations
    :vartype clusters: azure.mgmt.batchai.operations.ClustersOperations
    :ivar file_servers: FileServers operations
    :vartype file_servers: azure.mgmt.batchai.operations.FileServersOperations
    :ivar workspaces: Workspaces operations
    :vartype workspaces: azure.mgmt.batchai.operations.WorkspacesOperations
    :ivar experiments: Experiments operations
    :vartype experiments: azure.mgmt.batchai.operations.ExperimentsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.batchai.operations.JobsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscriptionID for the Azure user.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = BatchAIManagementClientConfiguration(credentials, subscription_id, base_url)
        self._client = ServiceClient(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-05-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.usage = UsageOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.clusters = ClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.file_servers = FileServersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.workspaces = WorkspacesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.experiments = ExperimentsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
