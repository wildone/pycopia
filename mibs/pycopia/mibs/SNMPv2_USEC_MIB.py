# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Unsigned32, snmpModules
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION

class SNMPv2_USEC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNMPv2-USEC-MIB'
	conformance = 3
	name = 'SNMPv2-USEC-MIB'
	language = 2
	description = 'The MIB module for SNMPv2 entities implementing the user-\nbased security model.'

# nodes
class usecMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6])
	name = 'usecMIB'

class usecMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1])
	name = 'usecMIBObjects'

class usecAgent(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 1])
	name = 'usecAgent'

class usecStats(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2])
	name = 'usecStats'

class usecMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 2])
	name = 'usecMIBConformance'

class usecMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 2, 1])
	name = 'usecMIBCompliances'

class usecMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 2, 2])
	name = 'usecMIBGroups'


# macros
# types 

class AgentID(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(12, 12))

# scalars 
class agentID(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 1, 1])
	syntaxobject = AgentID


class agentBoots(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentTime(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 4
	units = 'seconds'


class agentSize(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class usecStatsUnsupportedQoS(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsNotInWindows(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsUnknownUserNames(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsWrongDigestValues(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsUnknownContexts(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsBadParameters(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class usecStatsUnauthorizedOperations(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 1, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# columns
# rows 
# notifications (traps) 
# groups 
class usecBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 2, 2, 1])
	group = [agentID, agentBoots, agentTime, agentSize]

class usecStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 6, 2, 2, 2])
	group = [usecStatsUnsupportedQoS, usecStatsNotInWindows, usecStatsUnknownUserNames, usecStatsWrongDigestValues, usecStatsUnknownContexts, usecStatsBadParameters, usecStatsUnauthorizedOperations]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
