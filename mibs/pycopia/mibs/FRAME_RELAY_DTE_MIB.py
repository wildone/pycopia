# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, NOTIFICATION_TYPE
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from RFC1213_MIB import transmission
from SNMPv2_TC import TEXTUAL_CONVENTION, RowStatus, TimeStamp
from IF_MIB import InterfaceIndex

class FRAME_RELAY_DTE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/FRAME-RELAY-DTE-MIB'
	conformance = 5
	name = 'FRAME-RELAY-DTE-MIB'
	language = 2
	description = 'The MIB module to describe the use of a Frame Relay\ninterface by a DTE.'

# nodes
class frameRelayDTE(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32])
	name = 'frameRelayDTE'

class frameRelayTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 0])
	name = 'frameRelayTraps'

class frameRelayTrapControl(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 4])
	name = 'frameRelayTrapControl'

class frConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6])
	name = 'frConformance'

class frGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1])
	name = 'frGroups'

class frCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 2])
	name = 'frCompliances'


# macros
# types 

class DLCI(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 8388607))

# scalars 
class frTrapState(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 4, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class frTrapMaxRate(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 4, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class frDlcmiIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 1])
	syntaxobject = InterfaceIndex


class frDlcmiState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'noLmiConfigured'), Enum(2, 'lmiRev1'), Enum(3, 'ansiT1617D'), Enum(4, 'ansiT1617B'), Enum(5, 'itut933A'), Enum(6, 'ansiT1617D1994')]


class frDlcmiAddress(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'q921'), Enum(2, 'q922March90'), Enum(3, 'q922November90'), Enum(4, 'q922')]


class frDlcmiAddressLen(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(2, 'twoOctets'), Enum(3, 'threeOctets'), Enum(4, 'fourOctets')]


class frDlcmiPollingInterval(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class frDlcmiFullEnquiryInterval(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frDlcmiErrorThreshold(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frDlcmiMonitoredEvents(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frDlcmiMaxSupportedVCs(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 9])
	syntaxobject = DLCI


class frDlcmiMulticast(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'nonBroadcast'), Enum(2, 'broadcast')]


class frDlcmiStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'running'), Enum(2, 'fault'), Enum(3, 'initializing')]


class frDlcmiRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class frCircuitIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 1])
	syntaxobject = InterfaceIndex


class frCircuitDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 2])
	syntaxobject = DLCI


class frCircuitState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'invalid'), Enum(2, 'active'), Enum(3, 'inactive')]


class frCircuitReceivedFECNs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitReceivedBECNs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitSentFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitSentOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitReceivedFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitReceivedOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitCreationTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class frCircuitLastTimeChange(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class frCircuitCommittedBurst(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frCircuitExcessBurst(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frCircuitThroughput(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class frCircuitMulticast(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unicast'), Enum(2, 'oneWay'), Enum(3, 'twoWay'), Enum(4, 'nWay')]


class frCircuitType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'static'), Enum(2, 'dynamic')]


class frCircuitDiscards(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitReceivedDEs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitSentDEs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frCircuitLogicalIfIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 20])
	syntaxobject = InterfaceIndex


class frCircuitRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class frErrIfIndex(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 1])
	syntaxobject = InterfaceIndex


class frErrType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknownError'), Enum(2, 'receiveShort'), Enum(3, 'receiveLong'), Enum(4, 'illegalAddress'), Enum(5, 'unknownAddress'), Enum(6, 'dlcmiProtoErr'), Enum(7, 'dlcmiUnknownIE'), Enum(8, 'dlcmiSequenceErr'), Enum(9, 'dlcmiUnknownRpt'), Enum(10, 'noErrorSinceReset')]


class frErrData(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class frErrTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class frErrFaults(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class frErrFaultTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


# rows 
class frDlcmiEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([frDlcmiIfIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 1, 1])
	access = 2
	rowstatus = frDlcmiRowStatus
	columns = {'frDlcmiIfIndex': frDlcmiIfIndex, 'frDlcmiState': frDlcmiState, 'frDlcmiAddress': frDlcmiAddress, 'frDlcmiAddressLen': frDlcmiAddressLen, 'frDlcmiPollingInterval': frDlcmiPollingInterval, 'frDlcmiFullEnquiryInterval': frDlcmiFullEnquiryInterval, 'frDlcmiErrorThreshold': frDlcmiErrorThreshold, 'frDlcmiMonitoredEvents': frDlcmiMonitoredEvents, 'frDlcmiMaxSupportedVCs': frDlcmiMaxSupportedVCs, 'frDlcmiMulticast': frDlcmiMulticast, 'frDlcmiStatus': frDlcmiStatus, 'frDlcmiRowStatus': frDlcmiRowStatus}


class frCircuitEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([frCircuitIfIndex, frCircuitDlci], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 2, 1])
	access = 2
	rowstatus = frCircuitRowStatus
	columns = {'frCircuitIfIndex': frCircuitIfIndex, 'frCircuitDlci': frCircuitDlci, 'frCircuitState': frCircuitState, 'frCircuitReceivedFECNs': frCircuitReceivedFECNs, 'frCircuitReceivedBECNs': frCircuitReceivedBECNs, 'frCircuitSentFrames': frCircuitSentFrames, 'frCircuitSentOctets': frCircuitSentOctets, 'frCircuitReceivedFrames': frCircuitReceivedFrames, 'frCircuitReceivedOctets': frCircuitReceivedOctets, 'frCircuitCreationTime': frCircuitCreationTime, 'frCircuitLastTimeChange': frCircuitLastTimeChange, 'frCircuitCommittedBurst': frCircuitCommittedBurst, 'frCircuitExcessBurst': frCircuitExcessBurst, 'frCircuitThroughput': frCircuitThroughput, 'frCircuitMulticast': frCircuitMulticast, 'frCircuitType': frCircuitType, 'frCircuitDiscards': frCircuitDiscards, 'frCircuitReceivedDEs': frCircuitReceivedDEs, 'frCircuitSentDEs': frCircuitSentDEs, 'frCircuitLogicalIfIndex': frCircuitLogicalIfIndex, 'frCircuitRowStatus': frCircuitRowStatus}


class frErrEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([frErrIfIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 3, 1])
	access = 2
	columns = {'frErrIfIndex': frErrIfIndex, 'frErrType': frErrType, 'frErrData': frErrData, 'frErrTime': frErrTime, 'frErrFaults': frErrFaults, 'frErrFaultTime': frErrFaultTime}


# notifications (traps) 
class frDLCIStatusChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 0, 1])

# groups 
class frPortGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 1])
	group = [frDlcmiIfIndex, frDlcmiState, frDlcmiAddress, frDlcmiAddressLen, frDlcmiPollingInterval, frDlcmiFullEnquiryInterval, frDlcmiErrorThreshold, frDlcmiMonitoredEvents, frDlcmiMaxSupportedVCs, frDlcmiMulticast, frDlcmiStatus, frDlcmiRowStatus]

class frCircuitGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 2])
	group = [frCircuitIfIndex, frCircuitDlci, frCircuitState, frCircuitReceivedFECNs, frCircuitReceivedBECNs, frCircuitSentFrames, frCircuitSentOctets, frCircuitReceivedFrames, frCircuitReceivedOctets, frCircuitCreationTime, frCircuitLastTimeChange, frCircuitCommittedBurst, frCircuitExcessBurst, frCircuitThroughput, frCircuitMulticast, frCircuitType, frCircuitDiscards, frCircuitReceivedDEs, frCircuitSentDEs, frCircuitLogicalIfIndex, frCircuitRowStatus]

class frTrapGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 3])
	group = [frTrapState, frTrapMaxRate]

class frErrGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 4])
	group = [frErrIfIndex, frErrType, frErrData, frErrTime, frErrFaults, frErrFaultTime]

class frNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 5])
	group = [frDLCIStatusChange]

class frPortGroup0(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 6])
	group = [frDlcmiIfIndex, frDlcmiState, frDlcmiAddress, frDlcmiAddressLen, frDlcmiPollingInterval, frDlcmiFullEnquiryInterval, frDlcmiErrorThreshold, frDlcmiMonitoredEvents, frDlcmiMaxSupportedVCs, frDlcmiMulticast]

class frCircuitGroup0(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 7])
	group = [frCircuitIfIndex, frCircuitDlci, frCircuitState, frCircuitReceivedFECNs, frCircuitReceivedBECNs, frCircuitSentFrames, frCircuitSentOctets, frCircuitReceivedFrames, frCircuitReceivedOctets, frCircuitCreationTime, frCircuitLastTimeChange, frCircuitCommittedBurst, frCircuitExcessBurst, frCircuitThroughput]

class frErrGroup0(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 8])
	group = [frErrIfIndex, frErrType, frErrData, frErrTime]

class frTrapGroup0(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 9])
	group = [frTrapState]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
