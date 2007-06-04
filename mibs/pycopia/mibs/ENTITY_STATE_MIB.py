# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMPv2_TC import DateAndTime
from ENTITY_MIB import entPhysicalIndex
from ENTITY_STATE_TC_MIB import EntityAdminState, EntityOperState, EntityUsageState, EntityAlarmStatus, EntityStandbyStatus

class ENTITY_STATE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/ENTITY-STATE-MIB'
	name = 'ENTITY-STATE-MIB'
	language = 2
	description = 'This MIB defines a state extension to the Entity MIB.\n\nCopyright (C) The Internet Society 2005.  This version\nof this MIB module is part of RFC 4268; see the RFC\nitself for full legal notices.'

# nodes
class entityStateMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131])
	name = 'entityStateMIB'

class entStateNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 0])
	name = 'entStateNotifications'

class entStateObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1])
	name = 'entStateObjects'

class entStateConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 2])
	name = 'entStateConformance'

class entStateCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 2, 1])
	name = 'entStateCompliances'

class entStateGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 2, 2])
	name = 'entStateGroups'


# macros
# types 
# scalars 
# columns
class entStateLastChanged(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class entStateAdmin(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 2])
	syntaxobject = EntityAdminState


class entStateOper(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 3])
	syntaxobject = EntityOperState


class entStateUsage(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 4])
	syntaxobject = EntityUsageState


class entStateAlarm(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 5])
	syntaxobject = EntityAlarmStatus


class entStateStandby(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1, 6])
	syntaxobject = EntityStandbyStatus


# rows 
class entStateEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 1, 1, 1])
	access = 2
	columns = {'entStateLastChanged': entStateLastChanged, 'entStateAdmin': entStateAdmin, 'entStateOper': entStateOper, 'entStateUsage': entStateUsage, 'entStateAlarm': entStateAlarm, 'entStateStandby': entStateStandby}


# notifications (traps) 
class entStateOperEnabled(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 0, 1])

class entStateOperDisabled(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 0, 2])

# groups 
class entStateGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 2, 2, 1])
	group = [entStateLastChanged, entStateAdmin, entStateOper, entStateUsage, entStateAlarm, entStateStandby]

class entStateNotificationsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 131, 2, 2, 2])
	group = [entStateOperEnabled, entStateOperDisabled]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
