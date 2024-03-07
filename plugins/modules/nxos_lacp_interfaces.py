#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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

"""
The module file for nxos_lacp_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: nxos_lacp_interfaces
short_description: LACP interfaces resource module
description: This module manages Link Aggregation Control Protocol (LACP) attributes
  of NX-OS Interfaces.
version_added: 1.0.0
author: Trishna Guha (@trishnaguha)
notes:
- Tested against NXOS 7.3.(0)D1(1) on VIRL
- Unsupported for Cisco MDS
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the NX-OS device
      by executing the command B(show running-config | section ^interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A dictionary of LACP interfaces options.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the interface.
        required: true
        type: str
      port_priority:
        description:
        - LACP port priority for the interface. Range 1-65535. Applicable only for
          Ethernet.
        type: int
      rate:
        description:
        - Rate at which PDUs are sent by LACP. Applicable only for Ethernet. At fast
          rate LACP is transmitted once every 1 second. At normal rate LACP is transmitted
          every 30 seconds after the link is bundled.
        type: str
        choices:
        - fast
        - normal
      links:
        description:
        - This dict contains configurable options related to max and min port-channel
          links. Applicable only for Port-channel.
        type: dict
        suboptions:
          max:
            description:
            - Port-channel max bundle.
            type: int
          min:
            description:
            - Port-channel min links.
            type: int
      mode:
        description:
        - LACP mode. Applicable only for Port-channel.
        type: str
        choices:
        - delay
      suspend_individual:
        description:
        - port-channel lacp state. Disabling this will cause lacp to put the port
          to individual state and not suspend the port in case it does not get LACP
          BPDU from the peer ports in the port-channel.
        type: bool
      convergence:
        description:
        - This dict contains configurable options related to convergence. Applicable
          only for Port-channel.
        type: dict
        suboptions:
          graceful:
            description:
            - port-channel lacp graceful convergence. Disable this only with lacp
              ports connected to Non-Nexus peer. Disabling this with Nexus peer can
              lead to port suspension.
            type: bool
          vpc:
            description:
            - Enable lacp convergence for vPC port channels.
            type: bool
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged

"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
      - name: Ethernet1/3
        port_priority: 5
        rate: fast
    state: merged

# After state:
# ------------
#
# interface Ethernet1/3
# lacp port-priority 5
# lacp rate fast


# Using replaced

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Replace device lacp interfaces configuration with the given configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
      - name: port-channel11
        links:
          min: 4
    state: replaced

# After state:
# ------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp min-links 4


# Using overridden

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Override device configuration of all LACP interfaces attributes of given interfaces
    on device with provided configuration.
  cisco.nxos.nxos_lacp_interfaces:
    config:
      - name: port-channel11
        links:
          min: 4
    state: overridden

# After state:
# ------------
#
# interface port-channel11
# lacp min-links 4


# Using deleted

# Before state:
# -------------
#
# interface Ethernet1/3
#   lacp port-priority 5
# interface port-channel11
#   lacp mode delay

- name: Delete LACP interfaces configurations.
  cisco.nxos.nxos_lacp_interfaces:
    state: deleted

# After state:
# ------------
#

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_lacp_interfaces:
    config:
      - name: Ethernet1/800
        rate: fast
      - name: Ethernet1/801
        rate: fast
        port_priority: 32
      - name: port-channel10
        links:
          max: 15
          min: 2
        convergence:
          graceful: true
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#  - "interface Ethernet1/800"
#  - "lacp rate fast"
#  - "interface Ethernet1/801"
#  - "lacp port-priority 32"
#  - "lacp rate fast"
#  - "interface port-channel10"
#  - "lacp min-links 2"
#  - "lacp max-bundle 15"
#  - "lacp graceful-convergence"

# Using parsed

# parsed.cfg
# ------------

# interface port-channel10
#   lacp min-links 10
#   lacp max-bundle 15
# interface Ethernet1/800
#   lacp port-priority 100
#   lacp rate fast

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_lacp_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#   - name: port-channel10
#     links:
#       max: 15
#       min: 10
#   - name: Ethernet1/800
#     port_priority: 100
#     rate: fast

# Using gathered

# Existing device config state
# -------------------------------
# interface Ethernet1/1
#   lacp port-priority 5
#   lacp rate fast
# interface port-channel10
#   lacp mode delay
# interface port-channel11
#   lacp max-bundle 10
#   lacp min-links 5

- name: Gather lacp_interfaces facts from the device using nxos_lacp_interfaces
  cisco.nxos.nxos_lacp_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  - name: Ethernet1/1
#    port_priority: 5
#    rate: fast
#  - name: port-channel10
#    mode: delay
#  - name: port-channel11
#    links:
#      max: 10
#      min: 5
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['interface port-channel10', 'lacp min-links 5', 'lacp mode delay']
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.lacp_interfaces.lacp_interfaces import (
    Lacp_interfacesArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.lacp_interfaces.lacp_interfaces import (
    Lacp_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Lacp_interfacesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Lacp_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
