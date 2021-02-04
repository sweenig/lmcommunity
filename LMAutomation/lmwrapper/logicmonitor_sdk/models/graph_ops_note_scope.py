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


class GraphOpsNoteScope(object):
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
        'service_group_ids': 'list[int]',
        'service_id': 'int',
        'type': 'str',
        'device_group_ids': 'list[int]',
        'device_id': 'int'
    }

    attribute_map = {
        'service_group_ids': 'serviceGroupIds',
        'service_id': 'serviceId',
        'type': 'type',
        'device_group_ids': 'deviceGroupIds',
        'device_id': 'deviceId'
    }

    def __init__(self, service_group_ids=None, service_id=None, type=None, device_group_ids=None, device_id=None):  # noqa: E501
        """GraphOpsNoteScope - a model defined in Swagger"""  # noqa: E501

        self._service_group_ids = None
        self._service_id = None
        self._type = None
        self._device_group_ids = None
        self._device_id = None
        self.discriminator = None

        if service_group_ids is not None:
            self.service_group_ids = service_group_ids
        if service_id is not None:
            self.service_id = service_id
        if type is not None:
            self.type = type
        if device_group_ids is not None:
            self.device_group_ids = device_group_ids
        if device_id is not None:
            self.device_id = device_id

    @property
    def service_group_ids(self):
        """Gets the service_group_ids of this GraphOpsNoteScope.  # noqa: E501


        :return: The service_group_ids of this GraphOpsNoteScope.  # noqa: E501
        :rtype: list[int]
        """
        return self._service_group_ids

    @service_group_ids.setter
    def service_group_ids(self, service_group_ids):
        """Sets the service_group_ids of this GraphOpsNoteScope.


        :param service_group_ids: The service_group_ids of this GraphOpsNoteScope.  # noqa: E501
        :type: list[int]
        """

        self._service_group_ids = service_group_ids

    @property
    def service_id(self):
        """Gets the service_id of this GraphOpsNoteScope.  # noqa: E501


        :return: The service_id of this GraphOpsNoteScope.  # noqa: E501
        :rtype: int
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this GraphOpsNoteScope.


        :param service_id: The service_id of this GraphOpsNoteScope.  # noqa: E501
        :type: int
        """

        self._service_id = service_id

    @property
    def type(self):
        """Gets the type of this GraphOpsNoteScope.  # noqa: E501


        :return: The type of this GraphOpsNoteScope.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GraphOpsNoteScope.


        :param type: The type of this GraphOpsNoteScope.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def device_group_ids(self):
        """Gets the device_group_ids of this GraphOpsNoteScope.  # noqa: E501


        :return: The device_group_ids of this GraphOpsNoteScope.  # noqa: E501
        :rtype: list[int]
        """
        return self._device_group_ids

    @device_group_ids.setter
    def device_group_ids(self, device_group_ids):
        """Sets the device_group_ids of this GraphOpsNoteScope.


        :param device_group_ids: The device_group_ids of this GraphOpsNoteScope.  # noqa: E501
        :type: list[int]
        """

        self._device_group_ids = device_group_ids

    @property
    def device_id(self):
        """Gets the device_id of this GraphOpsNoteScope.  # noqa: E501


        :return: The device_id of this GraphOpsNoteScope.  # noqa: E501
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this GraphOpsNoteScope.


        :param device_id: The device_id of this GraphOpsNoteScope.  # noqa: E501
        :type: int
        """

        self._device_id = device_id

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
        if issubclass(GraphOpsNoteScope, dict):
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
        if not isinstance(other, GraphOpsNoteScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
