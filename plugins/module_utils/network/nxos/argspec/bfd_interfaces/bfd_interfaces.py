#
# -*- coding: utf-8 -*-
# Copyright 2019 Cisco and/or its affiliates.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The arg spec for the nxos_bfd_interfaces module
"""


class Bfd_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_bfd_interfaces module"""

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "elements": "dict",
            "options": {
                "name": {"type": "str"},
                "bfd": {"choices": ["enable", "disable"], "type": "str"},
                "echo": {"choices": ["enable", "disable"], "type": "str"},
            },
            "type": "list",
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
