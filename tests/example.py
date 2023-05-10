#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
  Author:  Jacek Kotlarski --<szumak@viertost.pl>
  Created: 10.05.2023

  Purpose:
"""

import inspect
from raisetool.formatter import Raise


class Example:
    def __init__(self):
        print(f"1: {Raise.message('example message 1')}")
        print(
            f"2: {Raise.message('example message 2', self.__class__.__name__)}"
        )
        print(
            f"3: {Raise.message('example message 3', self.__class__.__name__, inspect.currentframe(), )}"
        )
        try:
            raise Raise.value_error(
                "example message 4",
                self.__class__.__name__,
                inspect.currentframe(),
            )
        except ValueError as ex:
            print(f"4: {ex.__class__.__name__}: {ex}")


if __name__ == "__main__":
    obj = Example()


# #[EOF]#######################################################################
