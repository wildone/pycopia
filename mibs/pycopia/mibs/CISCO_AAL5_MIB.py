# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from ATM_MIB import aal5VccEntry

class CISCO_AAL5_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-AAL5-MIB'
	name = 'CISCO-AAL5-MIB'
	language = 2
	description = 'Cisco Enterprise AAL5 MIB file that provide AAL5\nspecific information that are either excluded by \nRFC 1695 or specific to Cisco product'

# nodes
class ciscoAal5MIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66])
	name = 'ciscoAal5MIB'

class ciscoAal5MIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1])
	name = 'ciscoAal5MIBObjects'

class cAal5Connections(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1])
	name = 'cAal5Connections'

class ciscoAal5MIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 3])
	name = 'ciscoAal5MIBConformance'

class ciscoAal5MIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 1])
	name = 'ciscoAal5MIBCompliances'

class ciscoAal5MIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2])
	name = 'ciscoAal5MIBGroups'


# macros
# types 
# scalars 
# columns
class cAal5VccInPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cAal5VccOutPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cAal5VccInOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cAal5VccOutOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
from IF_MIB import ifIndex
from ATM_MIB import aal5VccVpi
from ATM_MIB import aal5VccVci
class cAal5VccEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, aal5VccVpi, aal5VccVci], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 1, 1, 1, 1])
	access = 2
	columns = {'cAal5VccInPkts': cAal5VccInPkts, 'cAal5VccOutPkts': cAal5VccOutPkts, 'cAal5VccInOctets': cAal5VccInOctets, 'cAal5VccOutOctets': cAal5VccOutOctets}


# notifications (traps) 
# groups 
class ciscoAal5MIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 66, 3, 2, 1])
	group = [cAal5VccInPkts, cAal5VccOutPkts, cAal5VccInOctets, cAal5VccOutOctets]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
