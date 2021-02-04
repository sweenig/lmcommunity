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

from logicmonitor_sdk.models.stats_d_metric_definition import StatsDMetricDefinition  # noqa: F401,E501


class StatsDGraph(object):
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
        'min_value': 'float',
        'max_value': 'float',
        'namespace': 'str',
        'vertical_label': 'str',
        'metrics': 'list[StatsDMetricDefinition]',
        'scale_unit': 'int'
    }

    attribute_map = {
        'min_value': 'minValue',
        'max_value': 'maxValue',
        'namespace': 'namespace',
        'vertical_label': 'verticalLabel',
        'metrics': 'metrics',
        'scale_unit': 'scaleUnit'
    }

    def __init__(self, min_value=None, max_value=None, namespace=None, vertical_label=None, metrics=None, scale_unit=None):  # noqa: E501
        """StatsDGraph - a model defined in Swagger"""  # noqa: E501

        self._min_value = None
        self._max_value = None
        self._namespace = None
        self._vertical_label = None
        self._metrics = None
        self._scale_unit = None
        self.discriminator = None

        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if namespace is not None:
            self.namespace = namespace
        if vertical_label is not None:
            self.vertical_label = vertical_label
        if metrics is not None:
            self.metrics = metrics
        if scale_unit is not None:
            self.scale_unit = scale_unit

    @property
    def min_value(self):
        """Gets the min_value of this StatsDGraph.  # noqa: E501


        :return: The min_value of this StatsDGraph.  # noqa: E501
        :rtype: float
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        """Sets the min_value of this StatsDGraph.


        :param min_value: The min_value of this StatsDGraph.  # noqa: E501
        :type: float
        """

        self._min_value = min_value

    @property
    def max_value(self):
        """Gets the max_value of this StatsDGraph.  # noqa: E501


        :return: The max_value of this StatsDGraph.  # noqa: E501
        :rtype: float
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        """Sets the max_value of this StatsDGraph.


        :param max_value: The max_value of this StatsDGraph.  # noqa: E501
        :type: float
        """

        self._max_value = max_value

    @property
    def namespace(self):
        """Gets the namespace of this StatsDGraph.  # noqa: E501


        :return: The namespace of this StatsDGraph.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this StatsDGraph.


        :param namespace: The namespace of this StatsDGraph.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def vertical_label(self):
        """Gets the vertical_label of this StatsDGraph.  # noqa: E501


        :return: The vertical_label of this StatsDGraph.  # noqa: E501
        :rtype: str
        """
        return self._vertical_label

    @vertical_label.setter
    def vertical_label(self, vertical_label):
        """Sets the vertical_label of this StatsDGraph.


        :param vertical_label: The vertical_label of this StatsDGraph.  # noqa: E501
        :type: str
        """

        self._vertical_label = vertical_label

    @property
    def metrics(self):
        """Gets the metrics of this StatsDGraph.  # noqa: E501


        :return: The metrics of this StatsDGraph.  # noqa: E501
        :rtype: list[StatsDMetricDefinition]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this StatsDGraph.


        :param metrics: The metrics of this StatsDGraph.  # noqa: E501
        :type: list[StatsDMetricDefinition]
        """

        self._metrics = metrics

    @property
    def scale_unit(self):
        """Gets the scale_unit of this StatsDGraph.  # noqa: E501


        :return: The scale_unit of this StatsDGraph.  # noqa: E501
        :rtype: int
        """
        return self._scale_unit

    @scale_unit.setter
    def scale_unit(self, scale_unit):
        """Sets the scale_unit of this StatsDGraph.


        :param scale_unit: The scale_unit of this StatsDGraph.  # noqa: E501
        :type: int
        """

        self._scale_unit = scale_unit

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
        if issubclass(StatsDGraph, dict):
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
        if not isinstance(other, StatsDGraph):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
