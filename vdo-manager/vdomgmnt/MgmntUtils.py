#
# Copyright (c) 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA. 
#

"""
  MgmntUtils - miscellaneous utilities for the VDO manager

  $Id: //eng/vdo-releases/magnesium/src/python/vdo/vdomgmnt/MgmntUtils.py#1 $

"""
from .Utils import Utils
from utils import CommandError, runCommand

class MgmntUtils(Utils):

  ######################################################################
  # Public methods
  ######################################################################
  @classmethod
  def statusHelper(cls, commandList, tag):
    """Helper function for returning status summaries."""
    try:
      s = runCommand(commandList,
                     environment={ 'UDS_LOG_LEVEL' : 'WARNING' },
                     strip=True)
      return [tag + s.translate(None, "\"")]
    except CommandError:
      return [tag + _("not available")]
