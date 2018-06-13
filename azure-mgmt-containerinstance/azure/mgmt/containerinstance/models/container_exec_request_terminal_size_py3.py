# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ContainerExecRequestTerminalSize(Model):
    """The size of the terminal.

    :param row: The row size of the terminal
    :type row: int
    :param column: The column size of the terminal
    :type column: int
    """

    _attribute_map = {
        'row': {'key': 'row', 'type': 'int'},
        'column': {'key': 'column', 'type': 'int'},
    }

    def __init__(self, *, row: int=None, column: int=None, **kwargs) -> None:
        super(ContainerExecRequestTerminalSize, self).__init__(**kwargs)
        self.row = row
        self.column = column