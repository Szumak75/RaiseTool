# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@virthost.pl>
  Created: 08.05.2023

  Purpose:
"""

from types import FrameType
from typing import Optional
from attribtool.ndattrib import NoDynamicAttributes


class Raise(NoDynamicAttributes):
    """Raise class for formatting thrown exception messages."""

    @classmethod
    def message(
        cls,
        message: str,
        class_name: str = "",
        currentframe: Optional[FrameType] = None,
    ) -> str:
        """Message formatter method.

        message: str    - message to format
        class_name: str - caller class name (self.__class__.__name__)
        currentframe: FrameType - object from inspect.currentframe()

        Return: formatted message string
        """
        template = f"{message}"
        if currentframe and isinstance(currentframe, FrameType):
            template = f"{currentframe.f_code.co_name} [line:{currentframe.f_lineno}]: {template}"
        elif isinstance(class_name, str) and class_name != "":
            template = f"{class_name}: {template}"
            return template
        else:
            return template
        template = f"{class_name}.{template}"
        return template


# #[EOF]#######################################################################
