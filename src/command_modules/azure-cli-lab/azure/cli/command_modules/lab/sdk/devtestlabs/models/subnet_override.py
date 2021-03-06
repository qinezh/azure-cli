# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class SubnetOverride(Model):
    """Property overrides on a subnet of a virtual network.

    :param resource_id: The resource ID of the subnet.
    :type resource_id: str
    :param lab_subnet_name: The name given to the subnet within the lab.
    :type lab_subnet_name: str
    :param use_in_vm_creation_permission: Indicates whether this subnet can be
     used during virtual machine creation (i.e. Allow, Deny). Possible values
     include: 'Default', 'Deny', 'Allow'
    :type use_in_vm_creation_permission: str or :class:`UsagePermissionType
     <azure.mgmt.devtestlabs.models.UsagePermissionType>`
    :param use_public_ip_address_permission: Indicates whether public IP
     addresses can be assigned to virtual machines on this subnet (i.e. Allow,
     Deny). Possible values include: 'Default', 'Deny', 'Allow'
    :type use_public_ip_address_permission: str or :class:`UsagePermissionType
     <azure.mgmt.devtestlabs.models.UsagePermissionType>`
    :param shared_public_ip_address_configuration: Properties that virtual
     machines on this subnet will share.
    :type shared_public_ip_address_configuration:
     :class:`SubnetSharedPublicIpAddressConfiguration
     <azure.mgmt.devtestlabs.models.SubnetSharedPublicIpAddressConfiguration>`
    :param virtual_network_pool_name: The virtual network pool associated with
     this subnet.
    :type virtual_network_pool_name: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'lab_subnet_name': {'key': 'labSubnetName', 'type': 'str'},
        'use_in_vm_creation_permission': {'key': 'useInVmCreationPermission', 'type': 'str'},
        'use_public_ip_address_permission': {'key': 'usePublicIpAddressPermission', 'type': 'str'},
        'shared_public_ip_address_configuration': {'key': 'sharedPublicIpAddressConfiguration', 'type': 'SubnetSharedPublicIpAddressConfiguration'},
        'virtual_network_pool_name': {'key': 'virtualNetworkPoolName', 'type': 'str'},
    }

    def __init__(self, resource_id=None, lab_subnet_name=None, use_in_vm_creation_permission=None, use_public_ip_address_permission=None, shared_public_ip_address_configuration=None, virtual_network_pool_name=None):
        self.resource_id = resource_id
        self.lab_subnet_name = lab_subnet_name
        self.use_in_vm_creation_permission = use_in_vm_creation_permission
        self.use_public_ip_address_permission = use_public_ip_address_permission
        self.shared_public_ip_address_configuration = shared_public_ip_address_configuration
        self.virtual_network_pool_name = virtual_network_pool_name
