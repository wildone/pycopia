# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import OBJECT_TYPE, MODULE_IDENTITY, zeroDotZero, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import RowStatus, StorageType, RowPointer, DateAndTime
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class DIFFSERV_CONFIG_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/DIFFSERV-CONFIG-MIB'
	name = 'DIFFSERV-CONFIG-MIB'
	language = 2
	description = "This MIB module contains differentiated services\nspecific managed objects to perform higher-level\nconfiguration management.  This MIB allows policies\nto use 'templates' to instantiate Differentiated\nServices functional datapath configurations to\nbe assigned (associated with an interface and\ndirection) when a policy is activated.\n\nCopyright (C) The Internet Society (2004).  This version\nof this MIB module is part of RFC 3747;  see the RFC\nitself for full legal notices."

# nodes
class diffServConfigMib(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108])
	name = 'diffServConfigMib'

class diffServConfigMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1])
	name = 'diffServConfigMIBObjects'

class diffServConfigMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 2])
	name = 'diffServConfigMIBConformance'

class diffServConfigMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 2, 1])
	name = 'diffServConfigMIBCompliances'

class diffServConfigMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 2, 2])
	name = 'diffServConfigMIBGroups'


# macros
# types 
# scalars 
# columns
class diffServConfigId(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 1])
	syntaxobject = SnmpAdminString


class diffServConfigDescr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 2])
	syntaxobject = SnmpAdminString


class diffServConfigOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 3])
	syntaxobject = SnmpAdminString


class diffServConfigLastChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class diffServConfigStart(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class diffServConfigStorage(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class diffServConfigStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class diffServConfigEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([diffServConfigId], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 1, 2, 1])
	access = 2
	rowstatus = diffServConfigStatus
	columns = {'diffServConfigId': diffServConfigId, 'diffServConfigDescr': diffServConfigDescr, 'diffServConfigOwner': diffServConfigOwner, 'diffServConfigLastChange': diffServConfigLastChange, 'diffServConfigStart': diffServConfigStart, 'diffServConfigStorage': diffServConfigStorage, 'diffServConfigStatus': diffServConfigStatus}


# notifications (traps) 
# groups 
class diffServConfigMIBConfigGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 108, 2, 2, 1])
	group = [diffServConfigDescr, diffServConfigOwner, diffServConfigLastChange, diffServConfigStart, diffServConfigStorage, diffServConfigStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
