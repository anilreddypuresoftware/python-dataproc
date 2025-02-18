# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.cloud.dataproc_v1.services.autoscaling_policy_service import pagers
from google.cloud.dataproc_v1.types import autoscaling_policies
from .transports.base import AutoscalingPolicyServiceTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import AutoscalingPolicyServiceGrpcAsyncIOTransport
from .client import AutoscalingPolicyServiceClient


class AutoscalingPolicyServiceAsyncClient:
    """The API interface for managing autoscaling policies in the
    Dataproc API.
    """

    _client: AutoscalingPolicyServiceClient

    DEFAULT_ENDPOINT = AutoscalingPolicyServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = AutoscalingPolicyServiceClient.DEFAULT_MTLS_ENDPOINT

    autoscaling_policy_path = staticmethod(
        AutoscalingPolicyServiceClient.autoscaling_policy_path
    )
    parse_autoscaling_policy_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_autoscaling_policy_path
    )
    common_billing_account_path = staticmethod(
        AutoscalingPolicyServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(AutoscalingPolicyServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        AutoscalingPolicyServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(
        AutoscalingPolicyServiceClient.common_project_path
    )
    parse_common_project_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        AutoscalingPolicyServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        AutoscalingPolicyServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AutoscalingPolicyServiceAsyncClient: The constructed client.
        """
        return AutoscalingPolicyServiceClient.from_service_account_info.__func__(AutoscalingPolicyServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            AutoscalingPolicyServiceAsyncClient: The constructed client.
        """
        return AutoscalingPolicyServiceClient.from_service_account_file.__func__(AutoscalingPolicyServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return AutoscalingPolicyServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> AutoscalingPolicyServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            AutoscalingPolicyServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(AutoscalingPolicyServiceClient).get_transport_class,
        type(AutoscalingPolicyServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, AutoscalingPolicyServiceTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the autoscaling policy service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.AutoscalingPolicyServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = AutoscalingPolicyServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_autoscaling_policy(
        self,
        request: Union[
            autoscaling_policies.CreateAutoscalingPolicyRequest, dict
        ] = None,
        *,
        parent: str = None,
        policy: autoscaling_policies.AutoscalingPolicy = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> autoscaling_policies.AutoscalingPolicy:
        r"""Creates new autoscaling policy.

        .. code-block:: python

            from google.cloud import dataproc_v1

            def sample_create_autoscaling_policy():
                # Create a client
                client = dataproc_v1.AutoscalingPolicyServiceClient()

                # Initialize request argument(s)
                policy = dataproc_v1.AutoscalingPolicy()
                policy.basic_algorithm.yarn_config.scale_up_factor = 0.1578
                policy.basic_algorithm.yarn_config.scale_down_factor = 0.1789
                policy.worker_config.max_instances = 1389

                request = dataproc_v1.CreateAutoscalingPolicyRequest(
                    parent="parent_value",
                    policy=policy,
                )

                # Make the request
                response = client.create_autoscaling_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dataproc_v1.types.CreateAutoscalingPolicyRequest, dict]):
                The request object. A request to create an autoscaling
                policy.
            parent (:class:`str`):
                Required. The "resource name" of the region or location,
                as described in
                https://cloud.google.com/apis/design/resource_names.

                -  For ``projects.regions.autoscalingPolicies.create``,
                   the resource name of the region has the following
                   format: ``projects/{project_id}/regions/{region}``

                -  For
                   ``projects.locations.autoscalingPolicies.create``,
                   the resource name of the location has the following
                   format:
                   ``projects/{project_id}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            policy (:class:`google.cloud.dataproc_v1.types.AutoscalingPolicy`):
                Required. The autoscaling policy to
                create.

                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.types.AutoscalingPolicy:
                Describes an autoscaling policy for
                Dataproc cluster autoscaler.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, policy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = autoscaling_policies.CreateAutoscalingPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if policy is not None:
            request.policy = policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_autoscaling_policy,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def update_autoscaling_policy(
        self,
        request: Union[
            autoscaling_policies.UpdateAutoscalingPolicyRequest, dict
        ] = None,
        *,
        policy: autoscaling_policies.AutoscalingPolicy = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> autoscaling_policies.AutoscalingPolicy:
        r"""Updates (replaces) autoscaling policy.

        Disabled check for update_mask, because all updates will be full
        replacements.


        .. code-block:: python

            from google.cloud import dataproc_v1

            def sample_update_autoscaling_policy():
                # Create a client
                client = dataproc_v1.AutoscalingPolicyServiceClient()

                # Initialize request argument(s)
                policy = dataproc_v1.AutoscalingPolicy()
                policy.basic_algorithm.yarn_config.scale_up_factor = 0.1578
                policy.basic_algorithm.yarn_config.scale_down_factor = 0.1789
                policy.worker_config.max_instances = 1389

                request = dataproc_v1.UpdateAutoscalingPolicyRequest(
                    policy=policy,
                )

                # Make the request
                response = client.update_autoscaling_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dataproc_v1.types.UpdateAutoscalingPolicyRequest, dict]):
                The request object. A request to update an autoscaling
                policy.
            policy (:class:`google.cloud.dataproc_v1.types.AutoscalingPolicy`):
                Required. The updated autoscaling
                policy.

                This corresponds to the ``policy`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.types.AutoscalingPolicy:
                Describes an autoscaling policy for
                Dataproc cluster autoscaler.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([policy])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = autoscaling_policies.UpdateAutoscalingPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if policy is not None:
            request.policy = policy

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_autoscaling_policy,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("policy.name", request.policy.name),)
            ),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def get_autoscaling_policy(
        self,
        request: Union[autoscaling_policies.GetAutoscalingPolicyRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> autoscaling_policies.AutoscalingPolicy:
        r"""Retrieves autoscaling policy.

        .. code-block:: python

            from google.cloud import dataproc_v1

            def sample_get_autoscaling_policy():
                # Create a client
                client = dataproc_v1.AutoscalingPolicyServiceClient()

                # Initialize request argument(s)
                request = dataproc_v1.GetAutoscalingPolicyRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_autoscaling_policy(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dataproc_v1.types.GetAutoscalingPolicyRequest, dict]):
                The request object. A request to fetch an autoscaling
                policy.
            name (:class:`str`):
                Required. The "resource name" of the autoscaling policy,
                as described in
                https://cloud.google.com/apis/design/resource_names.

                -  For ``projects.regions.autoscalingPolicies.get``, the
                   resource name of the policy has the following format:
                   ``projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}``

                -  For ``projects.locations.autoscalingPolicies.get``,
                   the resource name of the policy has the following
                   format:
                   ``projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.types.AutoscalingPolicy:
                Describes an autoscaling policy for
                Dataproc cluster autoscaler.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = autoscaling_policies.GetAutoscalingPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_autoscaling_policy,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # Done; return the response.
        return response

    async def list_autoscaling_policies(
        self,
        request: Union[
            autoscaling_policies.ListAutoscalingPoliciesRequest, dict
        ] = None,
        *,
        parent: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListAutoscalingPoliciesAsyncPager:
        r"""Lists autoscaling policies in the project.

        .. code-block:: python

            from google.cloud import dataproc_v1

            def sample_list_autoscaling_policies():
                # Create a client
                client = dataproc_v1.AutoscalingPolicyServiceClient()

                # Initialize request argument(s)
                request = dataproc_v1.ListAutoscalingPoliciesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_autoscaling_policies(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dataproc_v1.types.ListAutoscalingPoliciesRequest, dict]):
                The request object. A request to list autoscaling
                policies in a project.
            parent (:class:`str`):
                Required. The "resource name" of the region or location,
                as described in
                https://cloud.google.com/apis/design/resource_names.

                -  For ``projects.regions.autoscalingPolicies.list``,
                   the resource name of the region has the following
                   format: ``projects/{project_id}/regions/{region}``

                -  For ``projects.locations.autoscalingPolicies.list``,
                   the resource name of the location has the following
                   format:
                   ``projects/{project_id}/locations/{location}``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dataproc_v1.services.autoscaling_policy_service.pagers.ListAutoscalingPoliciesAsyncPager:
                A response to a request to list
                autoscaling policies in a project.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = autoscaling_policies.ListAutoscalingPoliciesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_autoscaling_policies,
            default_retry=retries.Retry(
                initial=0.1,
                maximum=60.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.DeadlineExceeded,
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=600.0,
            ),
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(request, retry=retry, timeout=timeout, metadata=metadata,)

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListAutoscalingPoliciesAsyncPager(
            method=rpc, request=request, response=response, metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_autoscaling_policy(
        self,
        request: Union[
            autoscaling_policies.DeleteAutoscalingPolicyRequest, dict
        ] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes an autoscaling policy. It is an error to
        delete an autoscaling policy that is in use by one or
        more clusters.


        .. code-block:: python

            from google.cloud import dataproc_v1

            def sample_delete_autoscaling_policy():
                # Create a client
                client = dataproc_v1.AutoscalingPolicyServiceClient()

                # Initialize request argument(s)
                request = dataproc_v1.DeleteAutoscalingPolicyRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_autoscaling_policy(request=request)

        Args:
            request (Union[google.cloud.dataproc_v1.types.DeleteAutoscalingPolicyRequest, dict]):
                The request object. A request to delete an autoscaling
                policy.
                Autoscaling policies in use by one or more clusters will
                not be deleted.
            name (:class:`str`):
                Required. The "resource name" of the autoscaling policy,
                as described in
                https://cloud.google.com/apis/design/resource_names.

                -  For ``projects.regions.autoscalingPolicies.delete``,
                   the resource name of the policy has the following
                   format:
                   ``projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}``

                -  For
                   ``projects.locations.autoscalingPolicies.delete``,
                   the resource name of the policy has the following
                   format:
                   ``projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = autoscaling_policies.DeleteAutoscalingPolicyRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_autoscaling_policy,
            default_timeout=600.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request, retry=retry, timeout=timeout, metadata=metadata,
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution("google-cloud-dataproc",).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("AutoscalingPolicyServiceAsyncClient",)
