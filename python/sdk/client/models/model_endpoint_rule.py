# Copyright 2020 The Merlin Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model deployment functionalities  # noqa: E501

    OpenAPI spec version: 0.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelEndpointRule(object):
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
        'destinations': 'list[ModelEndpointRuleDestination]',
        'mirror': 'VersionEndpoint'
    }

    attribute_map = {
        'destinations': 'destinations',
        'mirror': 'mirror'
    }

    def __init__(self, destinations=None, mirror=None):  # noqa: E501
        """ModelEndpointRule - a model defined in Swagger"""  # noqa: E501

        self._destinations = None
        self._mirror = None
        self.discriminator = None

        if destinations is not None:
            self.destinations = destinations
        if mirror is not None:
            self.mirror = mirror

    @property
    def destinations(self):
        """Gets the destinations of this ModelEndpointRule.  # noqa: E501


        :return: The destinations of this ModelEndpointRule.  # noqa: E501
        :rtype: list[ModelEndpointRuleDestination]
        """
        return self._destinations

    @destinations.setter
    def destinations(self, destinations):
        """Sets the destinations of this ModelEndpointRule.


        :param destinations: The destinations of this ModelEndpointRule.  # noqa: E501
        :type: list[ModelEndpointRuleDestination]
        """

        self._destinations = destinations

    @property
    def mirror(self):
        """Gets the mirror of this ModelEndpointRule.  # noqa: E501


        :return: The mirror of this ModelEndpointRule.  # noqa: E501
        :rtype: VersionEndpoint
        """
        return self._mirror

    @mirror.setter
    def mirror(self, mirror):
        """Sets the mirror of this ModelEndpointRule.


        :param mirror: The mirror of this ModelEndpointRule.  # noqa: E501
        :type: VersionEndpoint
        """

        self._mirror = mirror

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
        if issubclass(ModelEndpointRule, dict):
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
        if not isinstance(other, ModelEndpointRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other