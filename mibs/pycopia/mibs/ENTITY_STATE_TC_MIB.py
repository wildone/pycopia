# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class ENTITY_STATE_TC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ENTITY-STATE-TC-MIB'
	conformance = 5
	name = 'ENTITY-STATE-TC-MIB'
	language = 2
	description = 'This MIB defines state textual conventions.\n\nCopyright (C) The Internet Society 2005.  This version\nof this MIB module is part of RFC 4268;  see the RFC\nitself for full legal notices.'

# nodes
class entityStateTc(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 130])
	name = 'entityStateTc'


# macros
# types 

class EntityAdminState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'locked'), Enum(3, 'shuttingDown'), Enum(4, 'unlocked')]


class EntityOperState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'disabled'), Enum(3, 'enabled'), Enum(4, 'testing')]


class EntityUsageState(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'idle'), Enum(3, 'active'), Enum(4, 'busy')]


class EntityAlarmStatus(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'unknown'), Enum(1, 'underRepair'), Enum(2, 'critical'), Enum(3, 'major'), Enum(4, 'minor'), Enum(5, 'warning'), Enum(6, 'indeterminate')]


class EntityStandbyStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'unknown'), Enum(2, 'hotStandby'), Enum(3, 'coldStandby'), Enum(4, 'providingService')]

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
