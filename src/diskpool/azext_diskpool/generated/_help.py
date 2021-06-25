# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['disk-pool'] = """
    type: group
    short-summary: Manage disk pool with diskpool
"""

helps['disk-pool list'] = """
    type: command
    short-summary: "Gets a list of DiskPools in a resource group. And Gets a list of Disk Pools in a subscription."
    examples:
      - name: List Disk Pools
        text: |-
               az disk-pool list --resource-group "myResourceGroup"
      - name: List Disk Pools by subscription
        text: |-
               az disk-pool list
"""

helps['disk-pool show'] = """
    type: command
    short-summary: "Get a Disk pool."
    examples:
      - name: Get Disk pool
        text: |-
               az disk-pool show --name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool create'] = """
    type: command
    short-summary: "Create Disk pool."
    parameters:
      - name: --sku
        short-summary: "Determines the SKU of the Disk Pool"
        long-summary: |
            Usage: --sku name=XX tier=XX

            name: Required. Sku name
            tier: Sku tier
      - name: --disks
        short-summary: "List of Azure Managed Disks to attach to a Disk Pool."
        long-summary: |
            The order of this parameter is specific customized. Usage:  --disks id-value

            id: Required. Unique Azure Resource ID of the Managed Disk.

            Multiple actions can be specified by using more than one --disks argument.
    examples:
      - name: Create or Update Disk pool
        text: |-
               az disk-pool create --location "westus" --availability-zones "1" --disks "/subscriptions/11111111-1111-1\
111-1111-111111111111/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/vm-name_DataDisk_0" --disks \
"/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/v\
m-name_DataDisk_1" --subnet-id "/subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/myResourceGroup/prov\
iders/Microsoft.Network/virtualNetworks/myvnet/subnets/mysubnet" --sku name="Basic_V0" tier="Basic" --tags key="value" \
--name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool update'] = """
    type: command
    short-summary: "Update a Disk pool."
    parameters:
      - name: --disks
        short-summary: "List of Azure Managed Disks to attach to a Disk Pool."
        long-summary: |
            The order of this parameter is specific customized. Usage:  --disks id-value

            id: Required. Unique Azure Resource ID of the Managed Disk.

            Multiple actions can be specified by using more than one --disks argument.
    examples:
      - name: Update Disk pool
        text: |-
               az disk-pool update --name "myDiskPool" --disks "/subscriptions/11111111-1111-1111-1111-111111111111/res\
ourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/vm-name_DataDisk_0" --disks \
"/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/myResourceGroup/providers/Microsoft.Compute/disks/v\
m-name_DataDisk_1" --tags key="value" --resource-group "myResourceGroup"
"""

helps['disk-pool delete'] = """
    type: command
    short-summary: "Delete a Disk pool."
    examples:
      - name: Delete Disk pool
        text: |-
               az disk-pool delete --name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool list-outbound-network-dependency-endpoint'] = """
    type: command
    short-summary: "Gets the network endpoints of all outbound dependencies of a Disk Pool."
    examples:
      - name: Get Disk Pool outbound network dependencies
        text: |-
               az disk-pool list-outbound-network-dependency-endpoint --name "SampleAse" --resource-group \
"Sample-WestUSResourceGroup"
"""

helps['disk-pool list-skus'] = """
    type: command
    short-summary: "Lists available Disk Pool Skus in an Azure location."
    examples:
      - name: List Disk Pool Skus
        text: |-
               az disk-pool list-skus --location "eastus"
"""

helps['disk-pool start'] = """
    type: command
    short-summary: "The operation to start a Disk Pool."
    examples:
      - name: Start Disk Pool
        text: |-
               az disk-pool start --name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool stop'] = """
    type: command
    short-summary: "Shuts down the Disk Pool and releases the compute resources. You are not billed for the compute \
resources that this Disk Pool uses."
    examples:
      - name: Deallocate Disk Pool
        text: |-
               az disk-pool stop --name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the disk-pool is met.
    examples:
      - name: Pause executing next line of CLI script until the disk-pool is successfully created.
        text: |-
               az disk-pool wait --name "myDiskPool" --resource-group "myResourceGroup" --created
      - name: Pause executing next line of CLI script until the disk-pool is successfully updated.
        text: |-
               az disk-pool wait --name "myDiskPool" --resource-group "myResourceGroup" --updated
      - name: Pause executing next line of CLI script until the disk-pool is successfully deleted.
        text: |-
               az disk-pool wait --name "myDiskPool" --resource-group "myResourceGroup" --deleted
"""

helps['disk-pool iscsi-target'] = """
    type: group
    short-summary: Manage iscsi target with diskpool
"""

helps['disk-pool iscsi-target list'] = """
    type: command
    short-summary: "Get iSCSI Targets in a Disk pool."
    examples:
      - name: List Disk Pools by Resource Group
        text: |-
               az disk-pool iscsi-target list --disk-pool-name "myDiskPool" --resource-group "myResourceGroup"
"""

helps['disk-pool iscsi-target show'] = """
    type: command
    short-summary: "Get an iSCSI Target."
    examples:
      - name: Get iSCSI Target
        text: |-
               az disk-pool iscsi-target show --disk-pool-name "myDiskPool" --name "myIscsiTarget" --resource-group \
"myResourceGroup"
"""

helps['disk-pool iscsi-target create'] = """
    type: command
    short-summary: "Create an iSCSI Target."
    parameters:
      - name: --static-acls
        short-summary: "Access Control List (ACL) for an iSCSI Target; defines LUN masking policy"
        long-summary: |
            Usage: --static-acls initiator-iqn=XX mapped-luns=XX

            initiator-iqn: Required. iSCSI initiator IQN (iSCSI Qualified Name); example: \
"iqn.2005-03.org.iscsi:client".
            mapped-luns: Required. List of LUN names mapped to the ACL.

            Multiple actions can be specified by using more than one --static-acls argument.
      - name: --luns
        short-summary: "List of LUNs to be exposed through iSCSI Target."
        long-summary: |
            Usage: --luns name=XX managed-disk-azure-resource-id=XX

            name: Required. User defined name for iSCSI LUN; example: "lun0"
            managed-disk-azure-resource-id: Required. Azure Resource ID of the Managed Disk.

            Multiple actions can be specified by using more than one --luns argument.
    examples:
      - name: Create or Update iSCSI Target
        text: |-
               az disk-pool iscsi-target create --disk-pool-name "myDiskPool" --acl-mode "Dynamic" --luns name="lun0" \
managed-disk-azure-resource-id="/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/myResourceGroup/prov\
iders/Microsoft.Compute/disks/vm-name_DataDisk_1" --target-iqn "iqn.2005-03.org.iscsi:server1" --name "myIscsiTarget" \
--resource-group "myResourceGroup"
"""

helps['disk-pool iscsi-target update'] = """
    type: command
    short-summary: "Update an iSCSI Target."
    parameters:
      - name: --static-acls
        short-summary: "Access Control List (ACL) for an iSCSI Target; defines LUN masking policy"
        long-summary: |
            Usage: --static-acls initiator-iqn=XX mapped-luns=XX

            initiator-iqn: Required. iSCSI initiator IQN (iSCSI Qualified Name); example: \
"iqn.2005-03.org.iscsi:client".
            mapped-luns: Required. List of LUN names mapped to the ACL.

            Multiple actions can be specified by using more than one --static-acls argument.
      - name: --luns
        short-summary: "List of LUNs to be exposed through iSCSI Target."
        long-summary: |
            Usage: --luns name=XX managed-disk-azure-resource-id=XX

            name: Required. User defined name for iSCSI LUN; example: "lun0"
            managed-disk-azure-resource-id: Required. Azure Resource ID of the Managed Disk.

            Multiple actions can be specified by using more than one --luns argument.
    examples:
      - name: Update iSCSI Target
        text: |-
               az disk-pool iscsi-target update --disk-pool-name "myDiskPool" --name "myIscsiTarget" --luns \
name="lun0" managed-disk-azure-resource-id="/subscriptions/11111111-1111-1111-1111-111111111111/resourceGroups/myResour\
ceGroup/providers/Microsoft.Compute/disks/vm-name_DataDisk_1" --static-acls initiator-iqn="iqn.2005-03.org.iscsi:client\
" mapped-luns="lun0" --resource-group "myResourceGroup"
"""

helps['disk-pool iscsi-target delete'] = """
    type: command
    short-summary: "Delete an iSCSI Target."
    examples:
      - name: Delete iSCSI Target
        text: |-
               az disk-pool iscsi-target delete --disk-pool-name "myDiskPool" --name "myIscsiTarget" --resource-group \
"myResourceGroup"
"""

helps['disk-pool iscsi-target wait'] = """
    type: command
    short-summary: Place the CLI in a waiting state until a condition of the disk-pool iscsi-target is met.
    examples:
      - name: Pause executing next line of CLI script until the disk-pool iscsi-target is successfully created.
        text: |-
               az disk-pool iscsi-target wait --disk-pool-name "myDiskPool" --name "myIscsiTarget" --resource-group \
"myResourceGroup" --created
      - name: Pause executing next line of CLI script until the disk-pool iscsi-target is successfully updated.
        text: |-
               az disk-pool iscsi-target wait --disk-pool-name "myDiskPool" --name "myIscsiTarget" --resource-group \
"myResourceGroup" --updated
      - name: Pause executing next line of CLI script until the disk-pool iscsi-target is successfully deleted.
        text: |-
               az disk-pool iscsi-target wait --disk-pool-name "myDiskPool" --name "myIscsiTarget" --resource-group \
"myResourceGroup" --deleted
"""
