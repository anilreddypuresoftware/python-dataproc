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
import proto  # type: ignore

from google.cloud.dataproc_v1.types import clusters
from google.cloud.dataproc_v1.types import jobs as gcd_jobs
from google.protobuf import duration_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dataproc.v1",
    manifest={
        "WorkflowTemplate",
        "WorkflowTemplatePlacement",
        "ManagedCluster",
        "ClusterSelector",
        "OrderedJob",
        "TemplateParameter",
        "ParameterValidation",
        "RegexValidation",
        "ValueValidation",
        "WorkflowMetadata",
        "ClusterOperation",
        "WorkflowGraph",
        "WorkflowNode",
        "CreateWorkflowTemplateRequest",
        "GetWorkflowTemplateRequest",
        "InstantiateWorkflowTemplateRequest",
        "InstantiateInlineWorkflowTemplateRequest",
        "UpdateWorkflowTemplateRequest",
        "ListWorkflowTemplatesRequest",
        "ListWorkflowTemplatesResponse",
        "DeleteWorkflowTemplateRequest",
    },
)


class WorkflowTemplate(proto.Message):
    r"""A Dataproc workflow template resource.

    Attributes:
        id (str):

        name (str):
            Output only. The resource name of the workflow template, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates``, the resource
               name of the template has the following format:
               ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``

            -  For ``projects.locations.workflowTemplates``, the
               resource name of the template has the following format:
               ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``
        version (int):
            Optional. Used to perform a consistent read-modify-write.

            This field should be left blank for a
            ``CreateWorkflowTemplate`` request. It is required for an
            ``UpdateWorkflowTemplate`` request, and must match the
            current server version. A typical update template flow would
            fetch the current template with a ``GetWorkflowTemplate``
            request, which will return the current template with the
            ``version`` field filled in with the current server version.
            The user updates other fields in the template, then returns
            it as part of the ``UpdateWorkflowTemplate`` request.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time template was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time template was last
            updated.
        labels (Sequence[google.cloud.dataproc_v1.types.WorkflowTemplate.LabelsEntry]):
            Optional. The labels to associate with this template. These
            labels will be propagated to all jobs and clusters created
            by the workflow instance.

            Label **keys** must contain 1 to 63 characters, and must
            conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.

            Label **values** may be empty, but, if present, must contain
            1 to 63 characters, and must conform to `RFC
            1035 <https://www.ietf.org/rfc/rfc1035.txt>`__.

            No more than 32 labels can be associated with a template.
        placement (google.cloud.dataproc_v1.types.WorkflowTemplatePlacement):
            Required. WorkflowTemplate scheduling
            information.
        jobs (Sequence[google.cloud.dataproc_v1.types.OrderedJob]):
            Required. The Directed Acyclic Graph of Jobs
            to submit.
        parameters (Sequence[google.cloud.dataproc_v1.types.TemplateParameter]):
            Optional. Template parameters whose values
            are substituted into the template. Values for
            parameters must be provided when the template is
            instantiated.
        dag_timeout (google.protobuf.duration_pb2.Duration):
            Optional. Timeout duration for the DAG of jobs, expressed in
            seconds (see `JSON representation of
            duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
            The timeout duration must be from 10 minutes ("600s") to 24
            hours ("86400s"). The timer begins when the first job is
            submitted. If the workflow is running at the end of the
            timeout period, any remaining jobs are cancelled, the
            workflow is ended, and if the workflow was running on a
            `managed
            cluster </dataproc/docs/concepts/workflows/using-workflows#configuring_or_selecting_a_cluster>`__,
            the cluster is deleted.
    """

    id = proto.Field(proto.STRING, number=2,)
    name = proto.Field(proto.STRING, number=1,)
    version = proto.Field(proto.INT32, number=3,)
    create_time = proto.Field(proto.MESSAGE, number=4, message=timestamp_pb2.Timestamp,)
    update_time = proto.Field(proto.MESSAGE, number=5, message=timestamp_pb2.Timestamp,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=6,)
    placement = proto.Field(
        proto.MESSAGE, number=7, message="WorkflowTemplatePlacement",
    )
    jobs = proto.RepeatedField(proto.MESSAGE, number=8, message="OrderedJob",)
    parameters = proto.RepeatedField(
        proto.MESSAGE, number=9, message="TemplateParameter",
    )
    dag_timeout = proto.Field(proto.MESSAGE, number=10, message=duration_pb2.Duration,)


class WorkflowTemplatePlacement(proto.Message):
    r"""Specifies workflow execution target.

    Either ``managed_cluster`` or ``cluster_selector`` is required.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        managed_cluster (google.cloud.dataproc_v1.types.ManagedCluster):
            A cluster that is managed by the workflow.

            This field is a member of `oneof`_ ``placement``.
        cluster_selector (google.cloud.dataproc_v1.types.ClusterSelector):
            Optional. A selector that chooses target
            cluster for jobs based on metadata.

            The selector is evaluated at the time each job
            is submitted.

            This field is a member of `oneof`_ ``placement``.
    """

    managed_cluster = proto.Field(
        proto.MESSAGE, number=1, oneof="placement", message="ManagedCluster",
    )
    cluster_selector = proto.Field(
        proto.MESSAGE, number=2, oneof="placement", message="ClusterSelector",
    )


class ManagedCluster(proto.Message):
    r"""Cluster that is managed by the workflow.

    Attributes:
        cluster_name (str):
            Required. The cluster name prefix. A unique
            cluster name will be formed by appending a
            random suffix.
            The name must contain only lower-case letters
            (a-z), numbers (0-9), and hyphens (-). Must
            begin with a letter. Cannot begin or end with
            hyphen. Must consist of between 2 and 35
            characters.
        config (google.cloud.dataproc_v1.types.ClusterConfig):
            Required. The cluster configuration.
        labels (Sequence[google.cloud.dataproc_v1.types.ManagedCluster.LabelsEntry]):
            Optional. The labels to associate with this cluster.

            Label keys must be between 1 and 63 characters long, and
            must conform to the following PCRE regular expression:
            [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}

            Label values must be between 1 and 63 characters long, and
            must conform to the following PCRE regular expression:
            [\p{Ll}\p{Lo}\p{N}_-]{0,63}

            No more than 32 labels can be associated with a given
            cluster.
    """

    cluster_name = proto.Field(proto.STRING, number=2,)
    config = proto.Field(proto.MESSAGE, number=3, message=clusters.ClusterConfig,)
    labels = proto.MapField(proto.STRING, proto.STRING, number=4,)


class ClusterSelector(proto.Message):
    r"""A selector that chooses target cluster for jobs based on
    metadata.

    Attributes:
        zone (str):
            Optional. The zone where workflow process
            executes. This parameter does not affect the
            selection of the cluster.
            If unspecified, the zone of the first cluster
            matching the selector is used.
        cluster_labels (Sequence[google.cloud.dataproc_v1.types.ClusterSelector.ClusterLabelsEntry]):
            Required. The cluster labels. Cluster must
            have all labels to match.
    """

    zone = proto.Field(proto.STRING, number=1,)
    cluster_labels = proto.MapField(proto.STRING, proto.STRING, number=2,)


class OrderedJob(proto.Message):
    r"""A job executed by the workflow.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        step_id (str):
            Required. The step id. The id must be unique among all jobs
            within the template.

            The step id is used as prefix for job id, as job
            ``goog-dataproc-workflow-step-id`` label, and in
            [prerequisiteStepIds][google.cloud.dataproc.v1.OrderedJob.prerequisite_step_ids]
            field from other steps.

            The id must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). Cannot begin or end with
            underscore or hyphen. Must consist of between 3 and 50
            characters.
        hadoop_job (google.cloud.dataproc_v1.types.HadoopJob):
            Optional. Job is a Hadoop job.

            This field is a member of `oneof`_ ``job_type``.
        spark_job (google.cloud.dataproc_v1.types.SparkJob):
            Optional. Job is a Spark job.

            This field is a member of `oneof`_ ``job_type``.
        pyspark_job (google.cloud.dataproc_v1.types.PySparkJob):
            Optional. Job is a PySpark job.

            This field is a member of `oneof`_ ``job_type``.
        hive_job (google.cloud.dataproc_v1.types.HiveJob):
            Optional. Job is a Hive job.

            This field is a member of `oneof`_ ``job_type``.
        pig_job (google.cloud.dataproc_v1.types.PigJob):
            Optional. Job is a Pig job.

            This field is a member of `oneof`_ ``job_type``.
        spark_r_job (google.cloud.dataproc_v1.types.SparkRJob):
            Optional. Job is a SparkR job.

            This field is a member of `oneof`_ ``job_type``.
        spark_sql_job (google.cloud.dataproc_v1.types.SparkSqlJob):
            Optional. Job is a SparkSql job.

            This field is a member of `oneof`_ ``job_type``.
        presto_job (google.cloud.dataproc_v1.types.PrestoJob):
            Optional. Job is a Presto job.

            This field is a member of `oneof`_ ``job_type``.
        labels (Sequence[google.cloud.dataproc_v1.types.OrderedJob.LabelsEntry]):
            Optional. The labels to associate with this job.

            Label keys must be between 1 and 63 characters long, and
            must conform to the following regular expression:
            [\p{Ll}\p{Lo}][\p{Ll}\p{Lo}\p{N}_-]{0,62}

            Label values must be between 1 and 63 characters long, and
            must conform to the following regular expression:
            [\p{Ll}\p{Lo}\p{N}_-]{0,63}

            No more than 32 labels can be associated with a given job.
        scheduling (google.cloud.dataproc_v1.types.JobScheduling):
            Optional. Job scheduling configuration.
        prerequisite_step_ids (Sequence[str]):
            Optional. The optional list of prerequisite job step_ids. If
            not specified, the job will start at the beginning of
            workflow.
    """

    step_id = proto.Field(proto.STRING, number=1,)
    hadoop_job = proto.Field(
        proto.MESSAGE, number=2, oneof="job_type", message=gcd_jobs.HadoopJob,
    )
    spark_job = proto.Field(
        proto.MESSAGE, number=3, oneof="job_type", message=gcd_jobs.SparkJob,
    )
    pyspark_job = proto.Field(
        proto.MESSAGE, number=4, oneof="job_type", message=gcd_jobs.PySparkJob,
    )
    hive_job = proto.Field(
        proto.MESSAGE, number=5, oneof="job_type", message=gcd_jobs.HiveJob,
    )
    pig_job = proto.Field(
        proto.MESSAGE, number=6, oneof="job_type", message=gcd_jobs.PigJob,
    )
    spark_r_job = proto.Field(
        proto.MESSAGE, number=11, oneof="job_type", message=gcd_jobs.SparkRJob,
    )
    spark_sql_job = proto.Field(
        proto.MESSAGE, number=7, oneof="job_type", message=gcd_jobs.SparkSqlJob,
    )
    presto_job = proto.Field(
        proto.MESSAGE, number=12, oneof="job_type", message=gcd_jobs.PrestoJob,
    )
    labels = proto.MapField(proto.STRING, proto.STRING, number=8,)
    scheduling = proto.Field(proto.MESSAGE, number=9, message=gcd_jobs.JobScheduling,)
    prerequisite_step_ids = proto.RepeatedField(proto.STRING, number=10,)


class TemplateParameter(proto.Message):
    r"""A configurable parameter that replaces one or more fields in
    the template. Parameterizable fields:
    - Labels
    - File uris
    - Job properties
    - Job arguments
    - Script variables
    - Main class (in HadoopJob and SparkJob)
    - Zone (in ClusterSelector)

    Attributes:
        name (str):
            Required. Parameter name. The parameter name is used as the
            key, and paired with the parameter value, which are passed
            to the template when the template is instantiated. The name
            must contain only capital letters (A-Z), numbers (0-9), and
            underscores (_), and must not start with a number. The
            maximum length is 40 characters.
        fields (Sequence[str]):
            Required. Paths to all fields that the parameter replaces. A
            field is allowed to appear in at most one parameter's list
            of field paths.

            A field path is similar in syntax to a
            [google.protobuf.FieldMask][google.protobuf.FieldMask]. For
            example, a field path that references the zone field of a
            workflow template's cluster selector would be specified as
            ``placement.clusterSelector.zone``.

            Also, field paths can reference fields using the following
            syntax:

            -  Values in maps can be referenced by key:

               -  labels['key']
               -  placement.clusterSelector.clusterLabels['key']
               -  placement.managedCluster.labels['key']
               -  placement.clusterSelector.clusterLabels['key']
               -  jobs['step-id'].labels['key']

            -  Jobs in the jobs list can be referenced by step-id:

               -  jobs['step-id'].hadoopJob.mainJarFileUri
               -  jobs['step-id'].hiveJob.queryFileUri
               -  jobs['step-id'].pySparkJob.mainPythonFileUri
               -  jobs['step-id'].hadoopJob.jarFileUris[0]
               -  jobs['step-id'].hadoopJob.archiveUris[0]
               -  jobs['step-id'].hadoopJob.fileUris[0]
               -  jobs['step-id'].pySparkJob.pythonFileUris[0]

            -  Items in repeated fields can be referenced by a
               zero-based index:

               -  jobs['step-id'].sparkJob.args[0]

            -  Other examples:

               -  jobs['step-id'].hadoopJob.properties['key']
               -  jobs['step-id'].hadoopJob.args[0]
               -  jobs['step-id'].hiveJob.scriptVariables['key']
               -  jobs['step-id'].hadoopJob.mainJarFileUri
               -  placement.clusterSelector.zone

            It may not be possible to parameterize maps and repeated
            fields in their entirety since only individual map values
            and individual items in repeated fields can be referenced.
            For example, the following field paths are invalid:

            -  placement.clusterSelector.clusterLabels
            -  jobs['step-id'].sparkJob.args
        description (str):
            Optional. Brief description of the parameter.
            Must not exceed 1024 characters.
        validation (google.cloud.dataproc_v1.types.ParameterValidation):
            Optional. Validation rules to be applied to
            this parameter's value.
    """

    name = proto.Field(proto.STRING, number=1,)
    fields = proto.RepeatedField(proto.STRING, number=2,)
    description = proto.Field(proto.STRING, number=3,)
    validation = proto.Field(proto.MESSAGE, number=4, message="ParameterValidation",)


class ParameterValidation(proto.Message):
    r"""Configuration for parameter validation.

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        regex (google.cloud.dataproc_v1.types.RegexValidation):
            Validation based on regular expressions.

            This field is a member of `oneof`_ ``validation_type``.
        values (google.cloud.dataproc_v1.types.ValueValidation):
            Validation based on a list of allowed values.

            This field is a member of `oneof`_ ``validation_type``.
    """

    regex = proto.Field(
        proto.MESSAGE, number=1, oneof="validation_type", message="RegexValidation",
    )
    values = proto.Field(
        proto.MESSAGE, number=2, oneof="validation_type", message="ValueValidation",
    )


class RegexValidation(proto.Message):
    r"""Validation based on regular expressions.

    Attributes:
        regexes (Sequence[str]):
            Required. RE2 regular expressions used to
            validate the parameter's value. The value must
            match the regex in its entirety (substring
            matches are not sufficient).
    """

    regexes = proto.RepeatedField(proto.STRING, number=1,)


class ValueValidation(proto.Message):
    r"""Validation based on a list of allowed values.

    Attributes:
        values (Sequence[str]):
            Required. List of allowed values for the
            parameter.
    """

    values = proto.RepeatedField(proto.STRING, number=1,)


class WorkflowMetadata(proto.Message):
    r"""A Dataproc workflow template resource.

    Attributes:
        template (str):
            Output only. The resource name of the workflow template as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates``, the resource
               name of the template has the following format:
               ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``

            -  For ``projects.locations.workflowTemplates``, the
               resource name of the template has the following format:
               ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``
        version (int):
            Output only. The version of template at the
            time of workflow instantiation.
        create_cluster (google.cloud.dataproc_v1.types.ClusterOperation):
            Output only. The create cluster operation
            metadata.
        graph (google.cloud.dataproc_v1.types.WorkflowGraph):
            Output only. The workflow graph.
        delete_cluster (google.cloud.dataproc_v1.types.ClusterOperation):
            Output only. The delete cluster operation
            metadata.
        state (google.cloud.dataproc_v1.types.WorkflowMetadata.State):
            Output only. The workflow state.
        cluster_name (str):
            Output only. The name of the target cluster.
        parameters (Sequence[google.cloud.dataproc_v1.types.WorkflowMetadata.ParametersEntry]):
            Map from parameter names to values that were
            used for those parameters.
        start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Workflow start time.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. Workflow end time.
        cluster_uuid (str):
            Output only. The UUID of target cluster.
        dag_timeout (google.protobuf.duration_pb2.Duration):
            Output only. The timeout duration for the DAG of jobs,
            expressed in seconds (see `JSON representation of
            duration <https://developers.google.com/protocol-buffers/docs/proto3#json>`__).
        dag_start_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. DAG start time, only set for workflows with
            [dag_timeout][google.cloud.dataproc.v1.WorkflowMetadata.dag_timeout]
            when DAG begins.
        dag_end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. DAG end time, only set for workflows with
            [dag_timeout][google.cloud.dataproc.v1.WorkflowMetadata.dag_timeout]
            when DAG ends.
    """

    class State(proto.Enum):
        r"""The operation state."""
        UNKNOWN = 0
        PENDING = 1
        RUNNING = 2
        DONE = 3

    template = proto.Field(proto.STRING, number=1,)
    version = proto.Field(proto.INT32, number=2,)
    create_cluster = proto.Field(proto.MESSAGE, number=3, message="ClusterOperation",)
    graph = proto.Field(proto.MESSAGE, number=4, message="WorkflowGraph",)
    delete_cluster = proto.Field(proto.MESSAGE, number=5, message="ClusterOperation",)
    state = proto.Field(proto.ENUM, number=6, enum=State,)
    cluster_name = proto.Field(proto.STRING, number=7,)
    parameters = proto.MapField(proto.STRING, proto.STRING, number=8,)
    start_time = proto.Field(proto.MESSAGE, number=9, message=timestamp_pb2.Timestamp,)
    end_time = proto.Field(proto.MESSAGE, number=10, message=timestamp_pb2.Timestamp,)
    cluster_uuid = proto.Field(proto.STRING, number=11,)
    dag_timeout = proto.Field(proto.MESSAGE, number=12, message=duration_pb2.Duration,)
    dag_start_time = proto.Field(
        proto.MESSAGE, number=13, message=timestamp_pb2.Timestamp,
    )
    dag_end_time = proto.Field(
        proto.MESSAGE, number=14, message=timestamp_pb2.Timestamp,
    )


class ClusterOperation(proto.Message):
    r"""The cluster operation triggered by a workflow.

    Attributes:
        operation_id (str):
            Output only. The id of the cluster operation.
        error (str):
            Output only. Error, if operation failed.
        done (bool):
            Output only. Indicates the operation is done.
    """

    operation_id = proto.Field(proto.STRING, number=1,)
    error = proto.Field(proto.STRING, number=2,)
    done = proto.Field(proto.BOOL, number=3,)


class WorkflowGraph(proto.Message):
    r"""The workflow graph.

    Attributes:
        nodes (Sequence[google.cloud.dataproc_v1.types.WorkflowNode]):
            Output only. The workflow nodes.
    """

    nodes = proto.RepeatedField(proto.MESSAGE, number=1, message="WorkflowNode",)


class WorkflowNode(proto.Message):
    r"""The workflow node.

    Attributes:
        step_id (str):
            Output only. The name of the node.
        prerequisite_step_ids (Sequence[str]):
            Output only. Node's prerequisite nodes.
        job_id (str):
            Output only. The job id; populated after the
            node enters RUNNING state.
        state (google.cloud.dataproc_v1.types.WorkflowNode.NodeState):
            Output only. The node state.
        error (str):
            Output only. The error detail.
    """

    class NodeState(proto.Enum):
        r"""The workflow node state."""
        NODE_STATE_UNSPECIFIED = 0
        BLOCKED = 1
        RUNNABLE = 2
        RUNNING = 3
        COMPLETED = 4
        FAILED = 5

    step_id = proto.Field(proto.STRING, number=1,)
    prerequisite_step_ids = proto.RepeatedField(proto.STRING, number=2,)
    job_id = proto.Field(proto.STRING, number=3,)
    state = proto.Field(proto.ENUM, number=5, enum=NodeState,)
    error = proto.Field(proto.STRING, number=6,)


class CreateWorkflowTemplateRequest(proto.Message):
    r"""A request to create a workflow template.

    Attributes:
        parent (str):
            Required. The resource name of the region or location, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates.create``, the
               resource name of the region has the following format:
               ``projects/{project_id}/regions/{region}``

            -  For ``projects.locations.workflowTemplates.create``, the
               resource name of the location has the following format:
               ``projects/{project_id}/locations/{location}``
        template (google.cloud.dataproc_v1.types.WorkflowTemplate):
            Required. The Dataproc workflow template to
            create.
    """

    parent = proto.Field(proto.STRING, number=1,)
    template = proto.Field(proto.MESSAGE, number=2, message="WorkflowTemplate",)


class GetWorkflowTemplateRequest(proto.Message):
    r"""A request to fetch a workflow template.

    Attributes:
        name (str):
            Required. The resource name of the workflow template, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates.get``, the
               resource name of the template has the following format:
               ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``

            -  For ``projects.locations.workflowTemplates.get``, the
               resource name of the template has the following format:
               ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``
        version (int):
            Optional. The version of workflow template to
            retrieve. Only previously instantiated versions
            can be retrieved.
            If unspecified, retrieves the current version.
    """

    name = proto.Field(proto.STRING, number=1,)
    version = proto.Field(proto.INT32, number=2,)


class InstantiateWorkflowTemplateRequest(proto.Message):
    r"""A request to instantiate a workflow template.

    Attributes:
        name (str):
            Required. The resource name of the workflow template, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates.instantiate``,
               the resource name of the template has the following
               format:
               ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``

            -  For ``projects.locations.workflowTemplates.instantiate``,
               the resource name of the template has the following
               format:
               ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``
        version (int):
            Optional. The version of workflow template to
            instantiate. If specified, the workflow will be
            instantiated only if the current version of the
            workflow template has the supplied version.
            This option cannot be used to instantiate a
            previous version of workflow template.
        request_id (str):
            Optional. A tag that prevents multiple concurrent workflow
            instances with the same tag from running. This mitigates
            risk of concurrent instances started due to retries.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The tag must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
        parameters (Sequence[google.cloud.dataproc_v1.types.InstantiateWorkflowTemplateRequest.ParametersEntry]):
            Optional. Map from parameter names to values
            that should be used for those parameters. Values
            may not exceed 1000 characters.
    """

    name = proto.Field(proto.STRING, number=1,)
    version = proto.Field(proto.INT32, number=2,)
    request_id = proto.Field(proto.STRING, number=5,)
    parameters = proto.MapField(proto.STRING, proto.STRING, number=6,)


class InstantiateInlineWorkflowTemplateRequest(proto.Message):
    r"""A request to instantiate an inline workflow template.

    Attributes:
        parent (str):
            Required. The resource name of the region or location, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For
               ``projects.regions.workflowTemplates,instantiateinline``,
               the resource name of the region has the following format:
               ``projects/{project_id}/regions/{region}``

            -  For
               ``projects.locations.workflowTemplates.instantiateinline``,
               the resource name of the location has the following
               format: ``projects/{project_id}/locations/{location}``
        template (google.cloud.dataproc_v1.types.WorkflowTemplate):
            Required. The workflow template to
            instantiate.
        request_id (str):
            Optional. A tag that prevents multiple concurrent workflow
            instances with the same tag from running. This mitigates
            risk of concurrent instances started due to retries.

            It is recommended to always set this value to a
            `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`__.

            The tag must contain only letters (a-z, A-Z), numbers (0-9),
            underscores (_), and hyphens (-). The maximum length is 40
            characters.
    """

    parent = proto.Field(proto.STRING, number=1,)
    template = proto.Field(proto.MESSAGE, number=2, message="WorkflowTemplate",)
    request_id = proto.Field(proto.STRING, number=3,)


class UpdateWorkflowTemplateRequest(proto.Message):
    r"""A request to update a workflow template.

    Attributes:
        template (google.cloud.dataproc_v1.types.WorkflowTemplate):
            Required. The updated workflow template.

            The ``template.version`` field must match the current
            version.
    """

    template = proto.Field(proto.MESSAGE, number=1, message="WorkflowTemplate",)


class ListWorkflowTemplatesRequest(proto.Message):
    r"""A request to list workflow templates in a project.

    Attributes:
        parent (str):
            Required. The resource name of the region or location, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates,list``, the
               resource name of the region has the following format:
               ``projects/{project_id}/regions/{region}``

            -  For ``projects.locations.workflowTemplates.list``, the
               resource name of the location has the following format:
               ``projects/{project_id}/locations/{location}``
        page_size (int):
            Optional. The maximum number of results to
            return in each response.
        page_token (str):
            Optional. The page token, returned by a
            previous call, to request the next page of
            results.
    """

    parent = proto.Field(proto.STRING, number=1,)
    page_size = proto.Field(proto.INT32, number=2,)
    page_token = proto.Field(proto.STRING, number=3,)


class ListWorkflowTemplatesResponse(proto.Message):
    r"""A response to a request to list workflow templates in a
    project.

    Attributes:
        templates (Sequence[google.cloud.dataproc_v1.types.WorkflowTemplate]):
            Output only. WorkflowTemplates list.
        next_page_token (str):
            Output only. This token is included in the response if there
            are more results to fetch. To fetch additional results,
            provide this value as the page_token in a subsequent
            ListWorkflowTemplatesRequest.
    """

    @property
    def raw_page(self):
        return self

    templates = proto.RepeatedField(
        proto.MESSAGE, number=1, message="WorkflowTemplate",
    )
    next_page_token = proto.Field(proto.STRING, number=2,)


class DeleteWorkflowTemplateRequest(proto.Message):
    r"""A request to delete a workflow template.
    Currently started workflows will remain running.

    Attributes:
        name (str):
            Required. The resource name of the workflow template, as
            described in
            https://cloud.google.com/apis/design/resource_names.

            -  For ``projects.regions.workflowTemplates.delete``, the
               resource name of the template has the following format:
               ``projects/{project_id}/regions/{region}/workflowTemplates/{template_id}``

            -  For ``projects.locations.workflowTemplates.instantiate``,
               the resource name of the template has the following
               format:
               ``projects/{project_id}/locations/{location}/workflowTemplates/{template_id}``
        version (int):
            Optional. The version of workflow template to
            delete. If specified, will only delete the
            template if the current server version matches
            specified version.
    """

    name = proto.Field(proto.STRING, number=1,)
    version = proto.Field(proto.INT32, number=2,)


__all__ = tuple(sorted(__protobuf__.manifest))
