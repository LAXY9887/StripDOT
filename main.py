# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 15:06:51 2022

@author: Cryptomero‧Zero
"""

from stripDOT import strip
import option

parameters = option.parameter_validate(option.prepare_parameters())

inputFile = parameters.in_file
targetCol = parameters.num
symbol = parameters.symbol
sep = parameters.sep
output = parameters.out_file

strip(
      fileDir = inputFile,
      targetCol = targetCol,
      stripSymbol = symbol,
      sep = sep,
      outFile = output
)

print(
      """
      {} was process. \n
      Gene accession ID without {} was recorded to {}
      """.format(inputFile,symbol,output)
)