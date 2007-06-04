# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SYSAPPL_MIB import Utf8String
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TestAndIncr, DateAndTime, TimeStamp
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Unsigned32, TimeTicks, IpAddress, Counter32, Gauge32, Counter64
from IANATn3270eTC_MIB import IANATn3270eAddrType, IANATn3270eAddress, IANATn3270eClientType, IANATn3270Functions, IANATn3270ResourceType, IANATn3270DeviceType, IANATn3270eLogData
from SNA_NAU_MIB import snanauMIB

class TN3270E_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/TN3270E-MIB'
	conformance = 4
	name = 'TN3270E-MIB'
	language = 2
	description = 'This module defines a portion of the management\ninformation base (MIB) for managing TN3270E servers.'

# nodes
class tn3270eMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8])
	name = 'tn3270eMIB'

class tn3270eNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 0])
	name = 'tn3270eNotifications'

class tn3270eObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1])
	name = 'tn3270eObjects'

class tn3270eConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3])
	name = 'tn3270eConformance'

class tn3270eGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 1])
	name = 'tn3270eGroups'

class tn3270eCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 2])
	name = 'tn3270eCompliances'


# macros
# types 

class SnaResourceName(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 17))


class Tn3270eTraceData(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 0), Range(3, 4096))

# scalars 
class tn3270eConfSpinLock(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TestAndIncr


# columns
class tn3270eSrvrConfIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eSrvrConfInactivityTimeout(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class tn3270eSrvrConfConnectivityChk(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'timingMark'), Enum(2, 'nop'), Enum(3, 'noCheck')]


class tn3270eSrvrConfTmNopInactTime(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class tn3270eSrvrConfTmNopInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class tn3270eSrvrFunctionsSupported(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 6])
	syntaxobject = IANATn3270Functions


class tn3270eSrvrConfAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'stopImmediate')]


class tn3270eSrvrConfOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'up'), Enum(2, 'down'), Enum(3, 'busy'), Enum(4, 'shuttingDown')]


class tn3270eSrvrConfSessionTermState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'terminate'), Enum(2, 'luSessionPend'), Enum(3, 'queueSession')]


class tn3270eSrvrConfSrvrType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'host'), Enum(2, 'gateway')]


class tn3270eSrvrConfContact(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 11])
	syntaxobject = SnmpAdminString


class tn3270eSrvrConfRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class tn3270eSrvrConfLastActTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.DateAndTime


class tn3270eSrvrConfTmTimeout(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'seconds'


class tn3270eSrvrPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eSrvrPortAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 2])
	syntaxobject = IANATn3270eAddrType


class tn3270eSrvrPortAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 3])
	syntaxobject = IANATn3270eAddress


class tn3270eSrvrPortRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class tn3270eSrvrStatsUpTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class tn3270eSrvrStatsMaxTerms(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 4
	units = 'LUs'


class tn3270eSrvrStatsInUseTerms(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'LUs'


class tn3270eSrvrStatsSpareTerms(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'LUs'


class tn3270eSrvrStatsMaxPtrs(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 4
	units = 'Printer Resources'


class tn3270eSrvrStatsInUsePtrs(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'Printer Resources'


class tn3270eSrvrStatsSparePtrs(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'Spare Printer Resources'


class tn3270eSrvrStatsInConnects(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'connections'


class tn3270eSrvrStatsConnResrceRejs(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'connection attempts'


class tn3270eSrvrStatsDisconnects(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'disconnections'


class tn3270eSrvrStatsHCInOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class tn3270eSrvrStatsInOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class tn3270eSrvrStatsHCOutOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class tn3270eSrvrStatsOutOctets(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class tn3270eSrvrStatsConnErrorRejs(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'connection attempts'


class tn3270eClientGroupName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 1])
	syntaxobject = Utf8String


class tn3270eClientGroupAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 2])
	syntaxobject = IANATn3270eAddrType


class tn3270eClientGroupAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 3])
	syntaxobject = IANATn3270eAddress


class tn3270eClientGroupSubnetMask(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class tn3270eClientGroupPfxLength(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'bits'


class tn3270eClientGroupRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class tn3270eResPoolName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 1])
	syntaxobject = Utf8String


class tn3270eResPoolElementName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 2])
	syntaxobject = SnaResourceName


class tn3270eResPoolElementType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 3])
	syntaxobject = IANATn3270ResourceType


class tn3270eResPoolRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class tn3270eSnaMapSscpSuppliedName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 1])
	syntaxobject = SnaResourceName


class tn3270eSnaMapLocalName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 2])
	syntaxobject = SnaResourceName


class tn3270eSnaMapPrimaryLuName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1, 3])
	syntaxobject = SnaResourceName


class tn3270eClientResMapPoolName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 1])
	syntaxobject = Utf8String


class tn3270eClientResMapClientGroupName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 2])
	syntaxobject = Utf8String


class tn3270eClientResMapClientPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eClientResMapRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class tn3270eResMapElementName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 1])
	syntaxobject = SnaResourceName


class tn3270eResMapAddrType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 2])
	syntaxobject = IANATn3270eAddrType


class tn3270eResMapAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 3])
	syntaxobject = IANATn3270eAddress


class tn3270eResMapPort(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eResMapElementType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 5])
	syntaxobject = IANATn3270ResourceType


class tn3270eResMapSscpSuppliedName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1, 6])
	syntaxobject = SnaResourceName


class tn3270eTcpConnRemAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 1])
	syntaxobject = IANATn3270eAddrType


class tn3270eTcpConnRemAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 2])
	syntaxobject = IANATn3270eAddress


class tn3270eTcpConnRemPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eTcpConnLocalAddrType(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 4])
	syntaxobject = IANATn3270eAddrType


class tn3270eTcpConnLocalAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 5])
	syntaxobject = IANATn3270eAddress


class tn3270eTcpConnLocalPort(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eTcpConnLastActivity(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class tn3270eTcpConnBytesIn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class tn3270eTcpConnBytesOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class tn3270eTcpConnResourceElement(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 10])
	syntaxobject = SnaResourceName


class tn3270eTcpConnResourceType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 11])
	syntaxobject = IANATn3270ResourceType


class tn3270eTcpConnDeviceType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 12])
	syntaxobject = IANATn3270DeviceType


class tn3270eTcpConnFunctions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 13])
	syntaxobject = IANATn3270Functions


class tn3270eTcpConnId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eTcpConnClientIdFormat(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 15])
	syntaxobject = IANATn3270eClientType


class tn3270eTcpConnClientId(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class tn3270eTcpConnTraceData(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 17])
	syntaxobject = Tn3270eTraceData


class tn3270eTcpConnLogInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 18])
	syntaxobject = IANATn3270eLogData


class tn3270eTcpConnLuLuBindImage(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class tn3270eTcpConnSnaState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'noSluSession'), Enum(3, 'sscpLuSession'), Enum(4, 'luLuSession'), Enum(5, 'sscpLuSessionAndLuLuSession')]


class tn3270eTcpConnStateLastDiscReason(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'hostSendsUnbind'), Enum(3, 'hostDontAcceptConnection'), Enum(4, 'outOfResource'), Enum(5, 'clientProtocolError'), Enum(6, 'invalidDeviceName'), Enum(7, 'deviceInUse'), Enum(8, 'inactivityTimeout'), Enum(9, 'hostNotResponding'), Enum(10, 'clientNotResponding'), Enum(11, 'serverClose'), Enum(12, 'sysreqLogoff'), Enum(13, 'serverSpecificHexCode')]


class tn3270eTcpConnSrvrConfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class tn3270eTcpConnActivationTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# rows 
class tn3270eSrvrConfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 1, 1])
	access = 2
	rowstatus = tn3270eSrvrConfRowStatus
	columns = {'tn3270eSrvrConfIndex': tn3270eSrvrConfIndex, 'tn3270eSrvrConfInactivityTimeout': tn3270eSrvrConfInactivityTimeout, 'tn3270eSrvrConfConnectivityChk': tn3270eSrvrConfConnectivityChk, 'tn3270eSrvrConfTmNopInactTime': tn3270eSrvrConfTmNopInactTime, 'tn3270eSrvrConfTmNopInterval': tn3270eSrvrConfTmNopInterval, 'tn3270eSrvrFunctionsSupported': tn3270eSrvrFunctionsSupported, 'tn3270eSrvrConfAdminStatus': tn3270eSrvrConfAdminStatus, 'tn3270eSrvrConfOperStatus': tn3270eSrvrConfOperStatus, 'tn3270eSrvrConfSessionTermState': tn3270eSrvrConfSessionTermState, 'tn3270eSrvrConfSrvrType': tn3270eSrvrConfSrvrType, 'tn3270eSrvrConfContact': tn3270eSrvrConfContact, 'tn3270eSrvrConfRowStatus': tn3270eSrvrConfRowStatus, 'tn3270eSrvrConfLastActTime': tn3270eSrvrConfLastActTime, 'tn3270eSrvrConfTmTimeout': tn3270eSrvrConfTmTimeout}


class tn3270eSrvrPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eSrvrPort, tn3270eSrvrPortAddrType, tn3270eSrvrPortAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 2, 1])
	access = 2
	rowstatus = tn3270eSrvrPortRowStatus
	columns = {'tn3270eSrvrPort': tn3270eSrvrPort, 'tn3270eSrvrPortAddrType': tn3270eSrvrPortAddrType, 'tn3270eSrvrPortAddress': tn3270eSrvrPortAddress, 'tn3270eSrvrPortRowStatus': tn3270eSrvrPortRowStatus}


class tn3270eSrvrStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eSrvrPort, tn3270eSrvrPortAddrType, tn3270eSrvrPortAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 3, 1])
	access = 2
	columns = {'tn3270eSrvrStatsUpTime': tn3270eSrvrStatsUpTime, 'tn3270eSrvrStatsMaxTerms': tn3270eSrvrStatsMaxTerms, 'tn3270eSrvrStatsInUseTerms': tn3270eSrvrStatsInUseTerms, 'tn3270eSrvrStatsSpareTerms': tn3270eSrvrStatsSpareTerms, 'tn3270eSrvrStatsMaxPtrs': tn3270eSrvrStatsMaxPtrs, 'tn3270eSrvrStatsInUsePtrs': tn3270eSrvrStatsInUsePtrs, 'tn3270eSrvrStatsSparePtrs': tn3270eSrvrStatsSparePtrs, 'tn3270eSrvrStatsInConnects': tn3270eSrvrStatsInConnects, 'tn3270eSrvrStatsConnResrceRejs': tn3270eSrvrStatsConnResrceRejs, 'tn3270eSrvrStatsDisconnects': tn3270eSrvrStatsDisconnects, 'tn3270eSrvrStatsHCInOctets': tn3270eSrvrStatsHCInOctets, 'tn3270eSrvrStatsInOctets': tn3270eSrvrStatsInOctets, 'tn3270eSrvrStatsHCOutOctets': tn3270eSrvrStatsHCOutOctets, 'tn3270eSrvrStatsOutOctets': tn3270eSrvrStatsOutOctets, 'tn3270eSrvrStatsConnErrorRejs': tn3270eSrvrStatsConnErrorRejs}


class tn3270eClientGroupEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eClientGroupName, tn3270eClientGroupAddrType, tn3270eClientGroupAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 4, 1])
	access = 2
	rowstatus = tn3270eClientGroupRowStatus
	columns = {'tn3270eClientGroupName': tn3270eClientGroupName, 'tn3270eClientGroupAddrType': tn3270eClientGroupAddrType, 'tn3270eClientGroupAddress': tn3270eClientGroupAddress, 'tn3270eClientGroupSubnetMask': tn3270eClientGroupSubnetMask, 'tn3270eClientGroupPfxLength': tn3270eClientGroupPfxLength, 'tn3270eClientGroupRowStatus': tn3270eClientGroupRowStatus}


class tn3270eResPoolEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eResPoolName, tn3270eResPoolElementName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 5, 1])
	access = 2
	rowstatus = tn3270eResPoolRowStatus
	columns = {'tn3270eResPoolName': tn3270eResPoolName, 'tn3270eResPoolElementName': tn3270eResPoolElementName, 'tn3270eResPoolElementType': tn3270eResPoolElementType, 'tn3270eResPoolRowStatus': tn3270eResPoolRowStatus}


class tn3270eSnaMapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eSnaMapSscpSuppliedName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 6, 1])
	access = 2
	columns = {'tn3270eSnaMapSscpSuppliedName': tn3270eSnaMapSscpSuppliedName, 'tn3270eSnaMapLocalName': tn3270eSnaMapLocalName, 'tn3270eSnaMapPrimaryLuName': tn3270eSnaMapPrimaryLuName}


class tn3270eClientResMapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eClientResMapPoolName, tn3270eClientResMapClientGroupName, tn3270eClientResMapClientPort], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 7, 1])
	access = 2
	rowstatus = tn3270eClientResMapRowStatus
	columns = {'tn3270eClientResMapPoolName': tn3270eClientResMapPoolName, 'tn3270eClientResMapClientGroupName': tn3270eClientResMapClientGroupName, 'tn3270eClientResMapClientPort': tn3270eClientResMapClientPort, 'tn3270eClientResMapRowStatus': tn3270eClientResMapRowStatus}


class tn3270eResMapEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eSrvrConfIndex, tn3270eResMapElementName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 8, 1])
	access = 2
	columns = {'tn3270eResMapElementName': tn3270eResMapElementName, 'tn3270eResMapAddrType': tn3270eResMapAddrType, 'tn3270eResMapAddress': tn3270eResMapAddress, 'tn3270eResMapPort': tn3270eResMapPort, 'tn3270eResMapElementType': tn3270eResMapElementType, 'tn3270eResMapSscpSuppliedName': tn3270eResMapSscpSuppliedName}


class tn3270eTcpConnEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([tn3270eTcpConnRemAddrType, tn3270eTcpConnRemAddress, tn3270eTcpConnRemPort, tn3270eTcpConnLocalAddrType, tn3270eTcpConnLocalAddress, tn3270eTcpConnLocalPort], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 1, 9, 1])
	access = 2
	columns = {'tn3270eTcpConnRemAddrType': tn3270eTcpConnRemAddrType, 'tn3270eTcpConnRemAddress': tn3270eTcpConnRemAddress, 'tn3270eTcpConnRemPort': tn3270eTcpConnRemPort, 'tn3270eTcpConnLocalAddrType': tn3270eTcpConnLocalAddrType, 'tn3270eTcpConnLocalAddress': tn3270eTcpConnLocalAddress, 'tn3270eTcpConnLocalPort': tn3270eTcpConnLocalPort, 'tn3270eTcpConnLastActivity': tn3270eTcpConnLastActivity, 'tn3270eTcpConnBytesIn': tn3270eTcpConnBytesIn, 'tn3270eTcpConnBytesOut': tn3270eTcpConnBytesOut, 'tn3270eTcpConnResourceElement': tn3270eTcpConnResourceElement, 'tn3270eTcpConnResourceType': tn3270eTcpConnResourceType, 'tn3270eTcpConnDeviceType': tn3270eTcpConnDeviceType, 'tn3270eTcpConnFunctions': tn3270eTcpConnFunctions, 'tn3270eTcpConnId': tn3270eTcpConnId, 'tn3270eTcpConnClientIdFormat': tn3270eTcpConnClientIdFormat, 'tn3270eTcpConnClientId': tn3270eTcpConnClientId, 'tn3270eTcpConnTraceData': tn3270eTcpConnTraceData, 'tn3270eTcpConnLogInfo': tn3270eTcpConnLogInfo, 'tn3270eTcpConnLuLuBindImage': tn3270eTcpConnLuLuBindImage, 'tn3270eTcpConnSnaState': tn3270eTcpConnSnaState, 'tn3270eTcpConnStateLastDiscReason': tn3270eTcpConnStateLastDiscReason, 'tn3270eTcpConnSrvrConfIndex': tn3270eTcpConnSrvrConfIndex, 'tn3270eTcpConnActivationTime': tn3270eTcpConnActivationTime}


# notifications (traps) 
# groups 
class tn3270eBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 1])
	group = [tn3270eSrvrConfInactivityTimeout, tn3270eSrvrConfConnectivityChk, tn3270eSrvrConfTmNopInactTime, tn3270eSrvrConfTmNopInterval, tn3270eSrvrFunctionsSupported, tn3270eSrvrConfAdminStatus, tn3270eSrvrConfOperStatus, tn3270eSrvrConfSessionTermState, tn3270eSrvrConfSrvrType, tn3270eSrvrConfContact, tn3270eSrvrConfRowStatus, tn3270eSrvrConfLastActTime, tn3270eSrvrConfTmTimeout, tn3270eSrvrPortRowStatus, tn3270eSrvrStatsUpTime, tn3270eSrvrStatsMaxTerms, tn3270eSrvrStatsInUseTerms, tn3270eSrvrStatsSpareTerms, tn3270eSrvrStatsMaxPtrs, tn3270eSrvrStatsInUsePtrs, tn3270eSrvrStatsSparePtrs, tn3270eSrvrStatsInConnects, tn3270eSrvrStatsConnResrceRejs, tn3270eSrvrStatsDisconnects, tn3270eSrvrStatsInOctets, tn3270eSrvrStatsOutOctets, tn3270eSrvrStatsConnErrorRejs, tn3270eClientGroupSubnetMask, tn3270eClientGroupPfxLength, tn3270eClientGroupRowStatus, tn3270eSnaMapLocalName, tn3270eSnaMapPrimaryLuName, tn3270eConfSpinLock]

class tn3270eSessionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 2])
	group = [tn3270eResMapAddrType, tn3270eResMapAddress, tn3270eResMapPort, tn3270eResMapElementType, tn3270eResMapSscpSuppliedName, tn3270eTcpConnLastActivity, tn3270eTcpConnBytesIn, tn3270eTcpConnBytesOut, tn3270eTcpConnResourceElement, tn3270eTcpConnResourceType, tn3270eTcpConnDeviceType, tn3270eTcpConnFunctions, tn3270eTcpConnSrvrConfIndex, tn3270eTcpConnActivationTime]

class tn3270eResMapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 3])
	group = [tn3270eResPoolElementType, tn3270eResPoolRowStatus, tn3270eClientResMapRowStatus, tn3270eTcpConnId, tn3270eTcpConnClientIdFormat, tn3270eTcpConnClientId, tn3270eTcpConnTraceData, tn3270eTcpConnLogInfo, tn3270eTcpConnLuLuBindImage, tn3270eTcpConnSnaState, tn3270eTcpConnStateLastDiscReason]

class tn3270eHiCapacityGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 34, 8, 3, 1, 4])
	group = [tn3270eSrvrStatsHCInOctets, tn3270eSrvrStatsHCOutOctets]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
