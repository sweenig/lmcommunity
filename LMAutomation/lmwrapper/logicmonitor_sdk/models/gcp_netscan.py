# coding: utf-8

"""
    LogicMonitor REST API

    LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering granular performance monitoring and actionable data and insights. logicmonitor_sdk enables you to manage your LogicMonitor account programmatically.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from logicmonitor_sdk.models.exclude_duplicate_ips import ExcludeDuplicateIps  # noqa: F401,E501
from logicmonitor_sdk.models.netscan import Netscan  # noqa: F401,E501
from logicmonitor_sdk.models.rest_schedule import RestSchedule  # noqa: F401,E501


class GCPNetscan(Netscan):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'creator': 'str',
        'collector_group_name': 'str',
        'method': 'str',
        'collector_group': 'int',
        'description': 'str',
        'next_start': 'str',
        'duplicate': 'ExcludeDuplicateIps',
        'version': 'int',
        'collector': 'int',
        'schedule': 'RestSchedule',
        'collector_description': 'str',
        'name': 'str',
        'next_start_epoch': 'int',
        'id': 'int',
        'nsg_id': 'int',
        'group': 'str',
        'service_account_key': 'str',
        'gcp_service': 'str',
        'root_name': 'str',
        'group_id': 'int',
        'gcp_region': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'creator': 'creator',
        'collector_group_name': 'collectorGroupName',
        'method': 'method',
        'collector_group': 'collectorGroup',
        'description': 'description',
        'next_start': 'nextStart',
        'duplicate': 'duplicate',
        'version': 'version',
        'collector': 'collector',
        'schedule': 'schedule',
        'collector_description': 'collectorDescription',
        'name': 'name',
        'next_start_epoch': 'nextStartEpoch',
        'id': 'id',
        'nsg_id': 'nsgId',
        'group': 'group',
        'service_account_key': 'serviceAccountKey',
        'gcp_service': 'gcpService',
        'root_name': 'rootName',
        'group_id': 'groupId',
        'gcp_region': 'gcpRegion',
        'project_id': 'projectId'
    }

    def __init__(self, creator=None, collector_group_name=None, method=None, collector_group=None, description=None, next_start=None, duplicate=None, version=None, collector=None, schedule=None, collector_description=None, name=None, next_start_epoch=None, id=None, nsg_id=None, group=None, service_account_key=None, gcp_service=None, root_name=None, group_id=None, gcp_region=None, project_id=None):  # noqa: E501
        """GCPNetscan - a model defined in Swagger"""  # noqa: E501

        self._creator = None
        self._collector_group_name = None
        self._method = None
        self._collector_group = None
        self._description = None
        self._next_start = None
        self._duplicate = None
        self._version = None
        self._collector = None
        self._schedule = None
        self._collector_description = None
        self._name = None
        self._next_start_epoch = None
        self._id = None
        self._nsg_id = None
        self._group = None
        self._service_account_key = None
        self._gcp_service = None
        self._root_name = None
        self._group_id = None
        self._gcp_region = None
        self._project_id = None
        self.discriminator = None

        if creator is not None:
            self.creator = creator
        if collector_group_name is not None:
            self.collector_group_name = collector_group_name
        self.method = method
        if collector_group is not None:
            self.collector_group = collector_group
        if description is not None:
            self.description = description
        if next_start is not None:
            self.next_start = next_start
        self.duplicate = duplicate
        if version is not None:
            self.version = version
        self.collector = collector
        if schedule is not None:
            self.schedule = schedule
        if collector_description is not None:
            self.collector_description = collector_description
        self.name = name
        if next_start_epoch is not None:
            self.next_start_epoch = next_start_epoch
        if id is not None:
            self.id = id
        if nsg_id is not None:
            self.nsg_id = nsg_id
        if group is not None:
            self.group = group
        if service_account_key is not None:
            self.service_account_key = service_account_key
        if gcp_service is not None:
            self.gcp_service = gcp_service
        if root_name is not None:
            self.root_name = root_name
        if group_id is not None:
            self.group_id = group_id
        if gcp_region is not None:
            self.gcp_region = gcp_region
        if project_id is not None:
            self.project_id = project_id

    @property
    def creator(self):
        """Gets the creator of this GCPNetscan.  # noqa: E501

        The user that created the policy  # noqa: E501

        :return: The creator of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this GCPNetscan.

        The user that created the policy  # noqa: E501

        :param creator: The creator of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def collector_group_name(self):
        """Gets the collector_group_name of this GCPNetscan.  # noqa: E501

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group_name of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_group_name

    @collector_group_name.setter
    def collector_group_name(self, collector_group_name):
        """Sets the collector_group_name of this GCPNetscan.

        The name of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group_name: The collector_group_name of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._collector_group_name = collector_group_name

    @property
    def method(self):
        """Gets the method of this GCPNetscan.  # noqa: E501

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :return: The method of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this GCPNetscan.

        The method that should be used to discover devices. Options are nmap (ICMP Ping), nec2 (EC2), and script  # noqa: E501

        :param method: The method of this GCPNetscan.  # noqa: E501
        :type: str
        """
        if method is None:
            raise ValueError("Invalid value for `method`, must not be `None`")  # noqa: E501

        self._method = method

    @property
    def collector_group(self):
        """Gets the collector_group of this GCPNetscan.  # noqa: E501

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_group of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector_group

    @collector_group.setter
    def collector_group(self, collector_group):
        """Sets the collector_group of this GCPNetscan.

        The ID of the group of the Collector associated with this Netscan  # noqa: E501

        :param collector_group: The collector_group of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._collector_group = collector_group

    @property
    def description(self):
        """Gets the description of this GCPNetscan.  # noqa: E501

        The description of the Netscan Policy  # noqa: E501

        :return: The description of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GCPNetscan.

        The description of the Netscan Policy  # noqa: E501

        :param description: The description of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def next_start(self):
        """Gets the next_start of this GCPNetscan.  # noqa: E501

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :return: The next_start of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._next_start

    @next_start.setter
    def next_start(self, next_start):
        """Sets the next_start of this GCPNetscan.

        The date and time of the next start time of the scan - displayed as manual if the scan does not run on a schedule  # noqa: E501

        :param next_start: The next_start of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._next_start = next_start

    @property
    def duplicate(self):
        """Gets the duplicate of this GCPNetscan.  # noqa: E501

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :return: The duplicate of this GCPNetscan.  # noqa: E501
        :rtype: ExcludeDuplicateIps
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this GCPNetscan.

        Information that determines how duplicate discovered devices should be handled  # noqa: E501

        :param duplicate: The duplicate of this GCPNetscan.  # noqa: E501
        :type: ExcludeDuplicateIps
        """
        if duplicate is None:
            raise ValueError("Invalid value for `duplicate`, must not be `None`")  # noqa: E501

        self._duplicate = duplicate

    @property
    def version(self):
        """Gets the version of this GCPNetscan.  # noqa: E501

        The Id of the device  # noqa: E501

        :return: The version of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this GCPNetscan.

        The Id of the device  # noqa: E501

        :param version: The version of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def collector(self):
        """Gets the collector of this GCPNetscan.  # noqa: E501

        The ID of the Collector associated with this Netscan  # noqa: E501

        :return: The collector of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this GCPNetscan.

        The ID of the Collector associated with this Netscan  # noqa: E501

        :param collector: The collector of this GCPNetscan.  # noqa: E501
        :type: int
        """
        if collector is None:
            raise ValueError("Invalid value for `collector`, must not be `None`")  # noqa: E501

        self._collector = collector

    @property
    def schedule(self):
        """Gets the schedule of this GCPNetscan.  # noqa: E501

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :return: The schedule of this GCPNetscan.  # noqa: E501
        :rtype: RestSchedule
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this GCPNetscan.

        Information related to the recurring execution schedule for the Netscan Policy  # noqa: E501

        :param schedule: The schedule of this GCPNetscan.  # noqa: E501
        :type: RestSchedule
        """

        self._schedule = schedule

    @property
    def collector_description(self):
        """Gets the collector_description of this GCPNetscan.  # noqa: E501

        The description of the Collector associated with this Netscan  # noqa: E501

        :return: The collector_description of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._collector_description

    @collector_description.setter
    def collector_description(self, collector_description):
        """Sets the collector_description of this GCPNetscan.

        The description of the Collector associated with this Netscan  # noqa: E501

        :param collector_description: The collector_description of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._collector_description = collector_description

    @property
    def name(self):
        """Gets the name of this GCPNetscan.  # noqa: E501

        The name of the Netscan Policy  # noqa: E501

        :return: The name of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GCPNetscan.

        The name of the Netscan Policy  # noqa: E501

        :param name: The name of this GCPNetscan.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def next_start_epoch(self):
        """Gets the next_start_epoch of this GCPNetscan.  # noqa: E501

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :return: The next_start_epoch of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._next_start_epoch

    @next_start_epoch.setter
    def next_start_epoch(self, next_start_epoch):
        """Sets the next_start_epoch of this GCPNetscan.

        The epoch of the next start time of the scan - displayed as 0 if the scan does not run on a schedule  # noqa: E501

        :param next_start_epoch: The next_start_epoch of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._next_start_epoch = next_start_epoch

    @property
    def id(self):
        """Gets the id of this GCPNetscan.  # noqa: E501

        The ID of the Netscan Policy  # noqa: E501

        :return: The id of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GCPNetscan.

        The ID of the Netscan Policy  # noqa: E501

        :param id: The id of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def nsg_id(self):
        """Gets the nsg_id of this GCPNetscan.  # noqa: E501

        The ID of the group the policy belongs to  # noqa: E501

        :return: The nsg_id of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._nsg_id

    @nsg_id.setter
    def nsg_id(self, nsg_id):
        """Sets the nsg_id of this GCPNetscan.

        The ID of the group the policy belongs to  # noqa: E501

        :param nsg_id: The nsg_id of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._nsg_id = nsg_id

    @property
    def group(self):
        """Gets the group of this GCPNetscan.  # noqa: E501

        The group the Netscan policy should belong to  # noqa: E501

        :return: The group of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this GCPNetscan.

        The group the Netscan policy should belong to  # noqa: E501

        :param group: The group of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def service_account_key(self):
        """Gets the service_account_key of this GCPNetscan.  # noqa: E501


        :return: The service_account_key of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._service_account_key

    @service_account_key.setter
    def service_account_key(self, service_account_key):
        """Sets the service_account_key of this GCPNetscan.


        :param service_account_key: The service_account_key of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._service_account_key = service_account_key

    @property
    def gcp_service(self):
        """Gets the gcp_service of this GCPNetscan.  # noqa: E501


        :return: The gcp_service of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._gcp_service

    @gcp_service.setter
    def gcp_service(self, gcp_service):
        """Sets the gcp_service of this GCPNetscan.


        :param gcp_service: The gcp_service of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._gcp_service = gcp_service

    @property
    def root_name(self):
        """Gets the root_name of this GCPNetscan.  # noqa: E501


        :return: The root_name of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._root_name

    @root_name.setter
    def root_name(self, root_name):
        """Sets the root_name of this GCPNetscan.


        :param root_name: The root_name of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._root_name = root_name

    @property
    def group_id(self):
        """Gets the group_id of this GCPNetscan.  # noqa: E501


        :return: The group_id of this GCPNetscan.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this GCPNetscan.


        :param group_id: The group_id of this GCPNetscan.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def gcp_region(self):
        """Gets the gcp_region of this GCPNetscan.  # noqa: E501


        :return: The gcp_region of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._gcp_region

    @gcp_region.setter
    def gcp_region(self, gcp_region):
        """Sets the gcp_region of this GCPNetscan.


        :param gcp_region: The gcp_region of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._gcp_region = gcp_region

    @property
    def project_id(self):
        """Gets the project_id of this GCPNetscan.  # noqa: E501


        :return: The project_id of this GCPNetscan.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this GCPNetscan.


        :param project_id: The project_id of this GCPNetscan.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GCPNetscan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GCPNetscan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
