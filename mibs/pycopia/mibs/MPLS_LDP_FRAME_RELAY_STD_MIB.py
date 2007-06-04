# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from IF_MIB import InterfaceIndexOrZero
from FRAME_RELAY_DTE_MIB import DLCI
from SNMPv2_SMI import OBJECT_TYPE, MODULE_IDENTITY, Unsigned32
from MPLS_TC_STD_MIB import mplsStdMIB
from MPLS_LDP_STD_MIB import mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId
from SNMPv2_TC import RowStatus, StorageType

class MPLS_LDP_FRAME_RELAY_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/MPLS-LDP-FRAME-RELAY-STD-MIB'
	conformance = 4
	name = 'MPLS-LDP-FRAME-RELAY-STD-MIB'
	language = 2
	description = 'Copyright (C) The Internet Society (year). The\ninitial version of this MIB module was published\nin RFC 3815. For full legal notices see the RFC\nitself or see:\nhttp://www.ietf.org/copyrights/ianamib.html\n\nThis MIB contains managed object definitions for\nconfiguring and monitoring the Multiprotocol Label\nSwitching (MPLS), Label Distribution Protocol (LDP),\nutilizing Frame Relay as the Layer 2 media.'

# nodes
class mplsLdpFrameRelayStdMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6])
	name = 'mplsLdpFrameRelayStdMIB'

class mplsLdpFrameRelayObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1])
	name = 'mplsLdpFrameRelayObjects'

class mplsLdpEntityFrameRelayObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1])
	name = 'mplsLdpEntityFrameRelayObjects'

class mplsLdpFrameRelaySessionObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2])
	name = 'mplsLdpFrameRelaySessionObjects'

class mplsLdpFrameRelayConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 2])
	name = 'mplsLdpFrameRelayConformance'

class mplsLdpFrameRelayGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1])
	name = 'mplsLdpFrameRelayGroups'

class mplsLdpFrameRelayCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 2])
	name = 'mplsLdpFrameRelayCompliances'


# macros
# types 
# scalars 
# columns
class mplsLdpEntityFrameRelayIfIndexOrZero(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 1])
	syntaxobject = InterfaceIndexOrZero


class mplsLdpEntityFrameRelayMergeCap(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'notSupported'), Enum(1, 'supported')]


class mplsLdpEntityFrameRelayLRComponents(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class mplsLdpEntityFrameRelayVcDirectionality(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'bidirectional'), Enum(1, 'unidirection')]


class mplsLdpEntityFrameRelayStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class mplsLdpEntityFrameRelayRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsLdpEntityFrameRelayLRMinDlci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 1])
	syntaxobject = DLCI


class mplsLdpEntityFrameRelayLRMaxDlci(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 2])
	syntaxobject = DLCI


class mplsLdpEntityFrameRelayLRLen(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'tenDlciBits'), Enum(2, 'twentyThreeDlciBits')]


class mplsLdpEntityFrameRelayLRStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class mplsLdpEntityFrameRelayLRRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class mplsLdpFrameRelaySessionMinDlci(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 1])
	syntaxobject = DLCI


class mplsLdpFrameRelaySessionMaxDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 2])
	syntaxobject = DLCI


class mplsLdpFrameRelaySessionLen(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'tenDlciBits'), Enum(2, 'twentyThreeDlciBits')]


# rows 
class mplsLdpEntityFrameRelayEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsLdpEntityLdpId, mplsLdpEntityIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 1, 1])
	access = 2
	rowstatus = mplsLdpEntityFrameRelayRowStatus
	columns = {'mplsLdpEntityFrameRelayIfIndexOrZero': mplsLdpEntityFrameRelayIfIndexOrZero, 'mplsLdpEntityFrameRelayMergeCap': mplsLdpEntityFrameRelayMergeCap, 'mplsLdpEntityFrameRelayLRComponents': mplsLdpEntityFrameRelayLRComponents, 'mplsLdpEntityFrameRelayVcDirectionality': mplsLdpEntityFrameRelayVcDirectionality, 'mplsLdpEntityFrameRelayStorageType': mplsLdpEntityFrameRelayStorageType, 'mplsLdpEntityFrameRelayRowStatus': mplsLdpEntityFrameRelayRowStatus}


class mplsLdpEntityFrameRelayLREntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpEntityFrameRelayLRMinDlci], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 1, 2, 1])
	access = 2
	rowstatus = mplsLdpEntityFrameRelayLRRowStatus
	columns = {'mplsLdpEntityFrameRelayLRMinDlci': mplsLdpEntityFrameRelayLRMinDlci, 'mplsLdpEntityFrameRelayLRMaxDlci': mplsLdpEntityFrameRelayLRMaxDlci, 'mplsLdpEntityFrameRelayLRLen': mplsLdpEntityFrameRelayLRLen, 'mplsLdpEntityFrameRelayLRStorageType': mplsLdpEntityFrameRelayLRStorageType, 'mplsLdpEntityFrameRelayLRRowStatus': mplsLdpEntityFrameRelayLRRowStatus}


class mplsLdpFrameRelaySessionEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId, mplsLdpFrameRelaySessionMinDlci], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 1, 2, 1, 1])
	access = 2
	columns = {'mplsLdpFrameRelaySessionMinDlci': mplsLdpFrameRelaySessionMinDlci, 'mplsLdpFrameRelaySessionMaxDlci': mplsLdpFrameRelaySessionMaxDlci, 'mplsLdpFrameRelaySessionLen': mplsLdpFrameRelaySessionLen}


# notifications (traps) 
# groups 
class mplsLdpFrameRelayGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 6, 2, 1, 1])
	group = [mplsLdpEntityFrameRelayIfIndexOrZero, mplsLdpEntityFrameRelayMergeCap, mplsLdpEntityFrameRelayLRComponents, mplsLdpEntityFrameRelayVcDirectionality, mplsLdpEntityFrameRelayStorageType, mplsLdpEntityFrameRelayRowStatus, mplsLdpEntityFrameRelayLRMaxDlci, mplsLdpEntityFrameRelayLRLen, mplsLdpEntityFrameRelayLRStorageType, mplsLdpEntityFrameRelayLRRowStatus, mplsLdpFrameRelaySessionMaxDlci, mplsLdpFrameRelaySessionLen]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
