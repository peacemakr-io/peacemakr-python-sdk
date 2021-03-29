# coding: utf-8

"""
    Peacemakr

    This API describes the Peacemakr services, which enable seamless application layer encryption and verification.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PricingPlan(object):
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
        'stripe_product_id': 'str',
        'stripe_plan_id': 'str',
        'number_of_keys_included': 'int',
        'price': 'int',
        'billing_interval_seconds': 'int'
    }

    attribute_map = {
        'stripe_product_id': 'stripeProductID',
        'stripe_plan_id': 'stripePlanID',
        'number_of_keys_included': 'numberOfKeysIncluded',
        'price': 'price',
        'billing_interval_seconds': 'billingIntervalSeconds'
    }

    def __init__(self, stripe_product_id=None, stripe_plan_id=None, number_of_keys_included=None, price=None, billing_interval_seconds=None):  # noqa: E501
        """PricingPlan - a model defined in Swagger"""  # noqa: E501

        self._stripe_product_id = None
        self._stripe_plan_id = None
        self._number_of_keys_included = None
        self._price = None
        self._billing_interval_seconds = None
        self.discriminator = None

        self.stripe_product_id = stripe_product_id
        self.stripe_plan_id = stripe_plan_id
        self.number_of_keys_included = number_of_keys_included
        self.price = price
        self.billing_interval_seconds = billing_interval_seconds

    @property
    def stripe_product_id(self):
        """Gets the stripe_product_id of this PricingPlan.  # noqa: E501


        :return: The stripe_product_id of this PricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._stripe_product_id

    @stripe_product_id.setter
    def stripe_product_id(self, stripe_product_id):
        """Sets the stripe_product_id of this PricingPlan.


        :param stripe_product_id: The stripe_product_id of this PricingPlan.  # noqa: E501
        :type: str
        """
        if stripe_product_id is None:
            raise ValueError("Invalid value for `stripe_product_id`, must not be `None`")  # noqa: E501

        self._stripe_product_id = stripe_product_id

    @property
    def stripe_plan_id(self):
        """Gets the stripe_plan_id of this PricingPlan.  # noqa: E501


        :return: The stripe_plan_id of this PricingPlan.  # noqa: E501
        :rtype: str
        """
        return self._stripe_plan_id

    @stripe_plan_id.setter
    def stripe_plan_id(self, stripe_plan_id):
        """Sets the stripe_plan_id of this PricingPlan.


        :param stripe_plan_id: The stripe_plan_id of this PricingPlan.  # noqa: E501
        :type: str
        """
        if stripe_plan_id is None:
            raise ValueError("Invalid value for `stripe_plan_id`, must not be `None`")  # noqa: E501

        self._stripe_plan_id = stripe_plan_id

    @property
    def number_of_keys_included(self):
        """Gets the number_of_keys_included of this PricingPlan.  # noqa: E501


        :return: The number_of_keys_included of this PricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._number_of_keys_included

    @number_of_keys_included.setter
    def number_of_keys_included(self, number_of_keys_included):
        """Sets the number_of_keys_included of this PricingPlan.


        :param number_of_keys_included: The number_of_keys_included of this PricingPlan.  # noqa: E501
        :type: int
        """
        if number_of_keys_included is None:
            raise ValueError("Invalid value for `number_of_keys_included`, must not be `None`")  # noqa: E501

        self._number_of_keys_included = number_of_keys_included

    @property
    def price(self):
        """Gets the price of this PricingPlan.  # noqa: E501


        :return: The price of this PricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this PricingPlan.


        :param price: The price of this PricingPlan.  # noqa: E501
        :type: int
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")  # noqa: E501

        self._price = price

    @property
    def billing_interval_seconds(self):
        """Gets the billing_interval_seconds of this PricingPlan.  # noqa: E501


        :return: The billing_interval_seconds of this PricingPlan.  # noqa: E501
        :rtype: int
        """
        return self._billing_interval_seconds

    @billing_interval_seconds.setter
    def billing_interval_seconds(self, billing_interval_seconds):
        """Sets the billing_interval_seconds of this PricingPlan.


        :param billing_interval_seconds: The billing_interval_seconds of this PricingPlan.  # noqa: E501
        :type: int
        """
        if billing_interval_seconds is None:
            raise ValueError("Invalid value for `billing_interval_seconds`, must not be `None`")  # noqa: E501

        self._billing_interval_seconds = billing_interval_seconds

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
        if issubclass(PricingPlan, dict):
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
        if not isinstance(other, PricingPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
