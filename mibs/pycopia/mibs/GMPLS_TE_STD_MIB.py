# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP, NOTIFICATION_GROUP
from SNMP_FRAMEWORK_MIB import SnmpAdminString
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Unsigned32, Counter32, Counter64, zeroDotZero, Gauge32
from MPLS_TC_STD_MIB import mplsStdMIB
from IANA_GMPLS_TC_MIB import IANAGmplsLSPEncodingTypeTC, IANAGmplsSwitchingTypeTC, IANAGmplsGeneralizedPidTC, IANAGmplsAdminStatusInformationTC
from MPLS_TE_STD_MIB import mplsTunnelIndex, mplsTunnelInstance, mplsTunnelIngressLSRId, mplsTunnelEgressLSRId, mplsTunnelHopListIndex, mplsTunnelHopPathOptionIndex, mplsTunnelHopIndex, mplsTunnelARHopListIndex, mplsTunnelARHopIndex, mplsTunnelCHopListIndex, mplsTunnelCHopIndex, mplsTunnelEntry, mplsTunnelAdminStatus, mplsTunnelOperStatus, mplsTunnelGroup, mplsTunnelScalarGroup
from INET_ADDRESS_MIB import InetAddress, InetAddressType
from SNMPv2_TC import TruthValue, TimeStamp, RowPointer

class GMPLS_TE_STD_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/GMPLS-TE-STD-MIB'
	conformance = 4
	name = 'GMPLS-TE-STD-MIB'
	language = 2
	description = 'Copyright (C) The IETF Trust (2007).  This version of\nthis MIB module is part of RFC 4802; see the RFC itself for\nfull legal notices.\n\nThis MIB module contains managed object definitions\nfor GMPLS Traffic Engineering (TE) as defined in:\n1. Generalized Multi-Protocol Label Switching (GMPLS)\n   Signaling Functional Description, Berger, L. (Editor),\n   RFC 3471, January 2003.\n2. Generalized MPLS Signaling - RSVP-TE Extensions, Berger,\n   L. (Editor), RFC 3473, January 2003.'

# nodes
class gmplsTeStdMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13])
	name = 'gmplsTeStdMIB'

class gmplsTeNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 0])
	name = 'gmplsTeNotifications'

class gmplsTeScalars(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 1])
	name = 'gmplsTeScalars'

class gmplsTeObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2])
	name = 'gmplsTeObjects'

class gmplsTeConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3])
	name = 'gmplsTeConformance'

class gmplsTeGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1])
	name = 'gmplsTeGroups'

class gmplsTeCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 2])
	name = 'gmplsTeCompliances'


# macros
# types 
# scalars 
class gmplsTunnelsConfigured(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class gmplsTunnelsActive(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


# columns
class gmplsTunnelUnnumIf(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class gmplsTunnelAttributes(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelLSPEncoding(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 3])
	syntaxobject = IANAGmplsLSPEncodingTypeTC


class gmplsTunnelSwitchingType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 4])
	syntaxobject = IANAGmplsSwitchingTypeTC


class gmplsTunnelLinkProtection(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelGPid(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 6])
	syntaxobject = IANAGmplsGeneralizedPidTC


class gmplsTunnelSecondary(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class gmplsTunnelDirection(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'forward'), Enum(1, 'bidirectional')]


class gmplsTunnelPathComp(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dynamicFull'), Enum(2, 'explicit'), Enum(3, 'dynamicPartial')]


class gmplsTunnelUpstreamNotifyRecipientType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 10])
	syntaxobject = InetAddressType


class gmplsTunnelUpstreamNotifyRecipient(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 11])
	syntaxobject = InetAddress


class gmplsTunnelSendResvNotifyRecipientType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 12])
	syntaxobject = InetAddressType


class gmplsTunnelSendResvNotifyRecipient(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 13])
	syntaxobject = InetAddress


class gmplsTunnelDownstreamNotifyRecipientType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 14])
	syntaxobject = InetAddressType


class gmplsTunnelDownstreamNotifyRecipient(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 15])
	syntaxobject = InetAddress


class gmplsTunnelSendPathNotifyRecipientType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 16])
	syntaxobject = InetAddressType


class gmplsTunnelSendPathNotifyRecipient(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 17])
	syntaxobject = InetAddress


class gmplsTunnelAdminStatusFlags(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 18])
	syntaxobject = IANAGmplsAdminStatusInformationTC


class gmplsTunnelExtraParamsPtr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelHopLabelStatuses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelHopExplicitForwardLabel(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelHopExplicitForwardLabelPtr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelHopExplicitReverseLabel(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelHopExplicitReverseLabelPtr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelARHopLabelStatuses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelARHopExplicitForwardLabel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelARHopExplicitForwardLabelPtr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelARHopExplicitReverseLabel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelARHopExplicitReverseLabelPtr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelARHopProtection(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelCHopLabelStatuses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.BITS


class gmplsTunnelCHopExplicitForwardLabel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelCHopExplicitForwardLabelPtr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelCHopExplicitReverseLabel(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelCHopExplicitReverseLabelPtr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowPointer


class gmplsTunnelReversePerfPackets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class gmplsTunnelReversePerfHCPackets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class gmplsTunnelReversePerfErrors(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class gmplsTunnelReversePerfBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class gmplsTunnelReversePerfHCBytes(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class gmplsTunnelErrorLastErrorType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(0, 'noError'), Enum(1, 'unknown'), Enum(2, 'protocol'), Enum(3, 'pathComputation'), Enum(4, 'localConfiguration'), Enum(5, 'localResources'), Enum(6, 'localOther')]


class gmplsTunnelErrorLastTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class gmplsTunnelErrorReporterType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 3])
	syntaxobject = InetAddressType


class gmplsTunnelErrorReporter(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 4])
	syntaxobject = InetAddress


class gmplsTunnelErrorCode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelErrorSubcode(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class gmplsTunnelErrorTLVs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class gmplsTunnelErrorHelpString(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1, 8])
	syntaxobject = SnmpAdminString


# rows 
class gmplsTunnelEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelIndex, mplsTunnelInstance, mplsTunnelIngressLSRId, mplsTunnelEgressLSRId], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 1, 1])
	access = 2
	columns = {'gmplsTunnelUnnumIf': gmplsTunnelUnnumIf, 'gmplsTunnelAttributes': gmplsTunnelAttributes, 'gmplsTunnelLSPEncoding': gmplsTunnelLSPEncoding, 'gmplsTunnelSwitchingType': gmplsTunnelSwitchingType, 'gmplsTunnelLinkProtection': gmplsTunnelLinkProtection, 'gmplsTunnelGPid': gmplsTunnelGPid, 'gmplsTunnelSecondary': gmplsTunnelSecondary, 'gmplsTunnelDirection': gmplsTunnelDirection, 'gmplsTunnelPathComp': gmplsTunnelPathComp, 'gmplsTunnelUpstreamNotifyRecipientType': gmplsTunnelUpstreamNotifyRecipientType, 'gmplsTunnelUpstreamNotifyRecipient': gmplsTunnelUpstreamNotifyRecipient, 'gmplsTunnelSendResvNotifyRecipientType': gmplsTunnelSendResvNotifyRecipientType, 'gmplsTunnelSendResvNotifyRecipient': gmplsTunnelSendResvNotifyRecipient, 'gmplsTunnelDownstreamNotifyRecipientType': gmplsTunnelDownstreamNotifyRecipientType, 'gmplsTunnelDownstreamNotifyRecipient': gmplsTunnelDownstreamNotifyRecipient, 'gmplsTunnelSendPathNotifyRecipientType': gmplsTunnelSendPathNotifyRecipientType, 'gmplsTunnelSendPathNotifyRecipient': gmplsTunnelSendPathNotifyRecipient, 'gmplsTunnelAdminStatusFlags': gmplsTunnelAdminStatusFlags, 'gmplsTunnelExtraParamsPtr': gmplsTunnelExtraParamsPtr}


class gmplsTunnelHopEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelHopListIndex, mplsTunnelHopPathOptionIndex, mplsTunnelHopIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 2, 1])
	access = 2
	columns = {'gmplsTunnelHopLabelStatuses': gmplsTunnelHopLabelStatuses, 'gmplsTunnelHopExplicitForwardLabel': gmplsTunnelHopExplicitForwardLabel, 'gmplsTunnelHopExplicitForwardLabelPtr': gmplsTunnelHopExplicitForwardLabelPtr, 'gmplsTunnelHopExplicitReverseLabel': gmplsTunnelHopExplicitReverseLabel, 'gmplsTunnelHopExplicitReverseLabelPtr': gmplsTunnelHopExplicitReverseLabelPtr}


class gmplsTunnelARHopEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelARHopListIndex, mplsTunnelARHopIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 3, 1])
	access = 2
	columns = {'gmplsTunnelARHopLabelStatuses': gmplsTunnelARHopLabelStatuses, 'gmplsTunnelARHopExplicitForwardLabel': gmplsTunnelARHopExplicitForwardLabel, 'gmplsTunnelARHopExplicitForwardLabelPtr': gmplsTunnelARHopExplicitForwardLabelPtr, 'gmplsTunnelARHopExplicitReverseLabel': gmplsTunnelARHopExplicitReverseLabel, 'gmplsTunnelARHopExplicitReverseLabelPtr': gmplsTunnelARHopExplicitReverseLabelPtr, 'gmplsTunnelARHopProtection': gmplsTunnelARHopProtection}


class gmplsTunnelCHopEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelCHopListIndex, mplsTunnelCHopIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 4, 1])
	access = 2
	columns = {'gmplsTunnelCHopLabelStatuses': gmplsTunnelCHopLabelStatuses, 'gmplsTunnelCHopExplicitForwardLabel': gmplsTunnelCHopExplicitForwardLabel, 'gmplsTunnelCHopExplicitForwardLabelPtr': gmplsTunnelCHopExplicitForwardLabelPtr, 'gmplsTunnelCHopExplicitReverseLabel': gmplsTunnelCHopExplicitReverseLabel, 'gmplsTunnelCHopExplicitReverseLabelPtr': gmplsTunnelCHopExplicitReverseLabelPtr}


from MPLS_TE_STD_MIB import mplsTunnelIndex
from MPLS_TE_STD_MIB import mplsTunnelInstance
from MPLS_TE_STD_MIB import mplsTunnelIngressLSRId
from MPLS_TE_STD_MIB import mplsTunnelEgressLSRId
class gmplsTunnelReversePerfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelIndex, mplsTunnelInstance, mplsTunnelIngressLSRId, mplsTunnelEgressLSRId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 5, 1])
	access = 2
	columns = {'gmplsTunnelReversePerfPackets': gmplsTunnelReversePerfPackets, 'gmplsTunnelReversePerfHCPackets': gmplsTunnelReversePerfHCPackets, 'gmplsTunnelReversePerfErrors': gmplsTunnelReversePerfErrors, 'gmplsTunnelReversePerfBytes': gmplsTunnelReversePerfBytes, 'gmplsTunnelReversePerfHCBytes': gmplsTunnelReversePerfHCBytes}


from MPLS_TE_STD_MIB import mplsTunnelIndex
from MPLS_TE_STD_MIB import mplsTunnelInstance
from MPLS_TE_STD_MIB import mplsTunnelIngressLSRId
from MPLS_TE_STD_MIB import mplsTunnelEgressLSRId
class gmplsTunnelErrorEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mplsTunnelIndex, mplsTunnelInstance, mplsTunnelIngressLSRId, mplsTunnelEgressLSRId], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 2, 6, 1])
	access = 2
	columns = {'gmplsTunnelErrorLastErrorType': gmplsTunnelErrorLastErrorType, 'gmplsTunnelErrorLastTime': gmplsTunnelErrorLastTime, 'gmplsTunnelErrorReporterType': gmplsTunnelErrorReporterType, 'gmplsTunnelErrorReporter': gmplsTunnelErrorReporter, 'gmplsTunnelErrorCode': gmplsTunnelErrorCode, 'gmplsTunnelErrorSubcode': gmplsTunnelErrorSubcode, 'gmplsTunnelErrorTLVs': gmplsTunnelErrorTLVs, 'gmplsTunnelErrorHelpString': gmplsTunnelErrorHelpString}


# notifications (traps) 
class gmplsTunnelDown(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 0, 1])

# groups 
class gmplsTunnelGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 1])
	group = [gmplsTunnelDirection, gmplsTunnelReversePerfPackets, gmplsTunnelReversePerfHCPackets, gmplsTunnelReversePerfErrors, gmplsTunnelReversePerfBytes, gmplsTunnelReversePerfHCBytes, gmplsTunnelErrorLastErrorType, gmplsTunnelErrorLastTime, gmplsTunnelErrorReporterType, gmplsTunnelErrorReporter, gmplsTunnelErrorCode, gmplsTunnelErrorSubcode, gmplsTunnelErrorTLVs, gmplsTunnelErrorHelpString, gmplsTunnelUnnumIf]

class gmplsTunnelSignaledGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 2])
	group = [gmplsTunnelAttributes, gmplsTunnelLSPEncoding, gmplsTunnelSwitchingType, gmplsTunnelLinkProtection, gmplsTunnelGPid, gmplsTunnelSecondary, gmplsTunnelPathComp, gmplsTunnelUpstreamNotifyRecipientType, gmplsTunnelUpstreamNotifyRecipient, gmplsTunnelSendResvNotifyRecipientType, gmplsTunnelSendResvNotifyRecipient, gmplsTunnelDownstreamNotifyRecipientType, gmplsTunnelDownstreamNotifyRecipient, gmplsTunnelSendPathNotifyRecipientType, gmplsTunnelSendPathNotifyRecipient, gmplsTunnelAdminStatusFlags, gmplsTunnelHopLabelStatuses, gmplsTunnelHopExplicitForwardLabel, gmplsTunnelHopExplicitForwardLabelPtr, gmplsTunnelHopExplicitReverseLabel, gmplsTunnelHopExplicitReverseLabelPtr]

class gmplsTunnelScalarGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 3])
	group = [gmplsTunnelsConfigured, gmplsTunnelsActive]

class gmplsTunnelOptionalGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 4])
	group = [gmplsTunnelExtraParamsPtr, gmplsTunnelARHopLabelStatuses, gmplsTunnelARHopExplicitForwardLabel, gmplsTunnelARHopExplicitForwardLabelPtr, gmplsTunnelARHopExplicitReverseLabel, gmplsTunnelARHopExplicitReverseLabelPtr, gmplsTunnelARHopProtection, gmplsTunnelCHopLabelStatuses, gmplsTunnelCHopExplicitForwardLabel, gmplsTunnelCHopExplicitForwardLabelPtr, gmplsTunnelCHopExplicitReverseLabel, gmplsTunnelCHopExplicitReverseLabelPtr]

class gmplsTeNotificationGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 10, 166, 13, 3, 1, 5])
	group = [gmplsTunnelDown]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
