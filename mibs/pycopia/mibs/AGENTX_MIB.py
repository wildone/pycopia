# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Unsigned32, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp, TruthValue, TDomain
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class AGENTX_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/AGENTX-MIB'
	conformance = 5
	name = 'AGENTX-MIB'
	language = 2
	description = 'This is the MIB module for the SNMP Agent Extensibility\nProtocol (AgentX).  This MIB module will be implemented by\nthe master agent.'

# nodes
class agentxMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74])
	name = 'agentxMIB'

class agentxObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1])
	name = 'agentxObjects'

class agentxGeneral(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 1])
	name = 'agentxGeneral'

class agentxConnection(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2])
	name = 'agentxConnection'

class agentxSession(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3])
	name = 'agentxSession'

class agentxRegistration(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4])
	name = 'agentxRegistration'

class agentxConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 2])
	name = 'agentxConformance'

class agentxMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 2, 1])
	name = 'agentxMIBGroups'

class agentxMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 2, 2])
	name = 'agentxMIBCompliances'


# macros
# types 

class AgentxTAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 255))

# scalars 
class agentxDefaultTimeout(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class agentxMasterAgentXVer(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class agentxConnTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class agentxSessionTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class agentxRegistrationTableLastChange(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# columns
class agentxConnIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxConnOpenTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class agentxConnTransportDomain(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.TDomain


class agentxConnTransportAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1, 4])
	syntaxobject = AgentxTAddress


class agentxSessionIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxSessionObjectID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class agentxSessionDescr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 3])
	syntaxobject = SnmpAdminString


class agentxSessionAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down')]


class agentxSessionOpenTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class agentxSessionAgentXVer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class agentxSessionTimeout(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class agentxRegIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxRegContext(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class agentxRegStart(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class agentxRegRangeSubId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxRegUpperBound(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxRegPriority(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class agentxRegTimeout(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'seconds'


class agentxRegInstance(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# rows 
class agentxConnectionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([agentxConnIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 2, 2, 1])
	access = 2
	columns = {'agentxConnIndex': agentxConnIndex, 'agentxConnOpenTime': agentxConnOpenTime, 'agentxConnTransportDomain': agentxConnTransportDomain, 'agentxConnTransportAddress': agentxConnTransportAddress}


class agentxSessionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([agentxConnIndex, agentxSessionIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 3, 2, 1])
	access = 2
	columns = {'agentxSessionIndex': agentxSessionIndex, 'agentxSessionObjectID': agentxSessionObjectID, 'agentxSessionDescr': agentxSessionDescr, 'agentxSessionAdminStatus': agentxSessionAdminStatus, 'agentxSessionOpenTime': agentxSessionOpenTime, 'agentxSessionAgentXVer': agentxSessionAgentXVer, 'agentxSessionTimeout': agentxSessionTimeout}


class agentxRegistrationEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([agentxConnIndex, agentxSessionIndex, agentxRegIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 1, 4, 2, 1])
	access = 2
	columns = {'agentxRegIndex': agentxRegIndex, 'agentxRegContext': agentxRegContext, 'agentxRegStart': agentxRegStart, 'agentxRegRangeSubId': agentxRegRangeSubId, 'agentxRegUpperBound': agentxRegUpperBound, 'agentxRegPriority': agentxRegPriority, 'agentxRegTimeout': agentxRegTimeout, 'agentxRegInstance': agentxRegInstance}


# notifications (traps) 
# groups 
class agentxMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 74, 2, 1, 1])
	group = [agentxDefaultTimeout, agentxMasterAgentXVer, agentxConnTableLastChange, agentxConnOpenTime, agentxConnTransportDomain, agentxConnTransportAddress, agentxSessionTableLastChange, agentxSessionTimeout, agentxSessionObjectID, agentxSessionDescr, agentxSessionAdminStatus, agentxSessionOpenTime, agentxSessionAgentXVer, agentxRegistrationTableLastChange, agentxRegContext, agentxRegStart, agentxRegRangeSubId, agentxRegUpperBound, agentxRegPriority, agentxRegTimeout, agentxRegInstance]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
