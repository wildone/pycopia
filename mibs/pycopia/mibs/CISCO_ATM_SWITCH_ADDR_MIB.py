# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus

class CISCO_ATM_SWITCH_ADDR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-SWITCH-ADDR-MIB'
	conformance = 5
	name = 'CISCO-ATM-SWITCH-ADDR-MIB'
	language = 2
	description = 'ATM Switch address MIB'

# nodes
class ciscoAtmSwAddrMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51])
	name = 'ciscoAtmSwAddrMIB'

class ciscoAtmSwAddrMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 1])
	name = 'ciscoAtmSwAddrMIBObjects'

class ciscoAtmSwAddrMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 3])
	name = 'ciscoAtmSwAddrMIBConformance'

class ciscoAtmSwAddrMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 1])
	name = 'ciscoAtmSwAddrMIBCompliances'

class ciscoAtmSwAddrMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2])
	name = 'ciscoAtmSwAddrMIBGroups'


# macros
# types 

class AtmAddr(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(13, 13), Range(20, 20))

# scalars 
# columns
class ciscoAtmSwAddrIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class ciscoAtmSwAddrAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 2])
	syntaxobject = AtmAddr


class ciscoAtmSwAddrRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class ciscoAtmSwAddrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ciscoAtmSwAddrIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 1, 1, 1])
	access = 2
	rowstatus = ciscoAtmSwAddrRowStatus
	columns = {'ciscoAtmSwAddrIndex': ciscoAtmSwAddrIndex, 'ciscoAtmSwAddrAddress': ciscoAtmSwAddrAddress, 'ciscoAtmSwAddrRowStatus': ciscoAtmSwAddrRowStatus}


# notifications (traps) 
# groups 
class ciscoAtmSwAddrMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 51, 3, 2, 1])
	group = [ciscoAtmSwAddrAddress, ciscoAtmSwAddrRowStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
