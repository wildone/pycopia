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
from IF_MIB import InterfaceIndexOrZero
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Integer32, Unsigned32
from INET_ADDRESS_MIB import InetAddressType, InetAddress
from RMON_MIB import OwnerString, rmon
from SNMPv2_TC import TEXTUAL_CONVENTION, StorageType, TruthValue, RowStatus
from APM_MIB import AppLocalIndex

class SSPM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SSPM-MIB'
	conformance = 4
	name = 'SSPM-MIB'
	language = 2
	description = 'This SSPM MIB module is applicable to probes\nimplementing Synthetic Source for Performance\nMonitoring functions.\n\nCopyright (C) The Internet Society (2005).  This version\nof this MIB module is part of RFC 4149; see the RFC\nitself for full legal notices.'

# nodes
class sspmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28])
	name = 'sspmMIB'

class sspmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1])
	name = 'sspmMIBObjects'

class sspmGeneral(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1])
	name = 'sspmGeneral'

class sspmSource(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2])
	name = 'sspmSource'

class sspmSink(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5])
	name = 'sspmSink'

class sspmMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 2])
	name = 'sspmMIBNotifications'

class sspmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3])
	name = 'sspmMIBConformance'

class sspmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 1])
	name = 'sspmCompliances'

class sspmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 2])
	name = 'sspmGroups'


# macros
# types 

class SspmMicroSeconds(pycopia.SMI.Basetypes.Unsigned32):
	status = 1
	format = 'd'


class SspmClockSource(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 255))
	format = 'd'


class SspmClockMaxSkew(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(1, 65535))
	format = 'd'

# scalars 
class sspmGeneralClockResolution(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 1])
	syntaxobject = SspmMicroSeconds


class sspmGeneralClockMaxSkew(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 2])
	syntaxobject = SspmClockMaxSkew


class sspmGeneralClockSource(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 3])
	syntaxobject = SspmClockSource


class sspmGeneralMinFrequency(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 4])
	syntaxobject = SspmMicroSeconds


# columns
class sspmCapabilitiesInstance(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1, 1])
	syntaxobject = AppLocalIndex


class sspmSourceProfileInstance(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSourceProfileType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 2])
	syntaxobject = AppLocalIndex


class sspmSourceProfilePacketSize(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSourceProfilePacketFillType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'random'), Enum(2, 'pattern'), Enum(3, 'url')]


class sspmSourceProfilePacketFillValue(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sspmSourceProfileTOS(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceProfileFlowLabel(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceProfileLooseSrcRteFill(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sspmSourceProfileLooseSrcRteLen(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceProfileTTL(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceProfileNoFrag(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class sspmSourceProfile8021Tagging(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceProfileUsername(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 13])
	syntaxobject = Utf8String


class sspmSourceProfilePassword(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 14])
	syntaxobject = Utf8String


class sspmSourceProfileParameter(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sspmSourceProfileOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 16])
	syntaxobject = OwnerString


class sspmSourceProfileStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class sspmSourceProfileStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class sspmSourceControlInstance(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSourceControlProfile(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sspmSourceControlSrc(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 3])
	syntaxobject = InterfaceIndexOrZero


class sspmSourceControlDestAddrType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 4])
	syntaxobject = InetAddressType


class sspmSourceControlDestAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 5])
	syntaxobject = InetAddress


class sspmSourceControlEnabled(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class sspmSourceControlTimeOut(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 7])
	syntaxobject = SspmMicroSeconds


class sspmSourceControlSamplingDist(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'deterministic'), Enum(2, 'poisson')]


class sspmSourceControlFrequency(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 9])
	syntaxobject = SspmMicroSeconds


class sspmSourceControlFirstSeqNum(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSourceControlLastSeqNum(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSourceControlOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 12])
	syntaxobject = OwnerString


class sspmSourceControlStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class sspmSourceControlStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class sspmSinkInstance(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSinkType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 2])
	syntaxobject = AppLocalIndex


class sspmSinkSourceAddressType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 3])
	syntaxobject = InetAddressType


class sspmSinkSourceAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 4])
	syntaxobject = InetAddress


class sspmSinkExpectedRate(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 5])
	syntaxobject = SspmMicroSeconds


class sspmSinkEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class sspmSinkExpectedFirstSequenceNum(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSinkLastSequenceNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class sspmSinkLastSequenceInvalid(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sspmSinkStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class sspmSinkStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class sspmCapabilitiesEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sspmCapabilitiesInstance], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 1, 5, 1])
	access = 2
	columns = {'sspmCapabilitiesInstance': sspmCapabilitiesInstance}


class sspmSourceProfileEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sspmSourceProfileInstance], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 1, 1])
	access = 2
	rowstatus = sspmSourceProfileStatus
	columns = {'sspmSourceProfileInstance': sspmSourceProfileInstance, 'sspmSourceProfileType': sspmSourceProfileType, 'sspmSourceProfilePacketSize': sspmSourceProfilePacketSize, 'sspmSourceProfilePacketFillType': sspmSourceProfilePacketFillType, 'sspmSourceProfilePacketFillValue': sspmSourceProfilePacketFillValue, 'sspmSourceProfileTOS': sspmSourceProfileTOS, 'sspmSourceProfileFlowLabel': sspmSourceProfileFlowLabel, 'sspmSourceProfileLooseSrcRteFill': sspmSourceProfileLooseSrcRteFill, 'sspmSourceProfileLooseSrcRteLen': sspmSourceProfileLooseSrcRteLen, 'sspmSourceProfileTTL': sspmSourceProfileTTL, 'sspmSourceProfileNoFrag': sspmSourceProfileNoFrag, 'sspmSourceProfile8021Tagging': sspmSourceProfile8021Tagging, 'sspmSourceProfileUsername': sspmSourceProfileUsername, 'sspmSourceProfilePassword': sspmSourceProfilePassword, 'sspmSourceProfileParameter': sspmSourceProfileParameter, 'sspmSourceProfileOwner': sspmSourceProfileOwner, 'sspmSourceProfileStorageType': sspmSourceProfileStorageType, 'sspmSourceProfileStatus': sspmSourceProfileStatus}


class sspmSourceControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sspmSourceControlInstance], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 2, 2, 1])
	access = 2
	rowstatus = sspmSourceControlStatus
	columns = {'sspmSourceControlInstance': sspmSourceControlInstance, 'sspmSourceControlProfile': sspmSourceControlProfile, 'sspmSourceControlSrc': sspmSourceControlSrc, 'sspmSourceControlDestAddrType': sspmSourceControlDestAddrType, 'sspmSourceControlDestAddr': sspmSourceControlDestAddr, 'sspmSourceControlEnabled': sspmSourceControlEnabled, 'sspmSourceControlTimeOut': sspmSourceControlTimeOut, 'sspmSourceControlSamplingDist': sspmSourceControlSamplingDist, 'sspmSourceControlFrequency': sspmSourceControlFrequency, 'sspmSourceControlFirstSeqNum': sspmSourceControlFirstSeqNum, 'sspmSourceControlLastSeqNum': sspmSourceControlLastSeqNum, 'sspmSourceControlOwner': sspmSourceControlOwner, 'sspmSourceControlStorageType': sspmSourceControlStorageType, 'sspmSourceControlStatus': sspmSourceControlStatus}


class sspmSinkEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sspmSinkInstance], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 1, 5, 1, 1])
	access = 2
	rowstatus = sspmSinkStatus
	columns = {'sspmSinkInstance': sspmSinkInstance, 'sspmSinkType': sspmSinkType, 'sspmSinkSourceAddressType': sspmSinkSourceAddressType, 'sspmSinkSourceAddress': sspmSinkSourceAddress, 'sspmSinkExpectedRate': sspmSinkExpectedRate, 'sspmSinkEnable': sspmSinkEnable, 'sspmSinkExpectedFirstSequenceNum': sspmSinkExpectedFirstSequenceNum, 'sspmSinkLastSequenceNumber': sspmSinkLastSequenceNumber, 'sspmSinkLastSequenceInvalid': sspmSinkLastSequenceInvalid, 'sspmSinkStorageType': sspmSinkStorageType, 'sspmSinkStatus': sspmSinkStatus}


# notifications (traps) 
# groups 
class sspmGeneralGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 1])
	group = [sspmGeneralClockResolution, sspmGeneralClockMaxSkew, sspmGeneralClockSource, sspmGeneralMinFrequency, sspmCapabilitiesInstance]

class sspmSourceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 2])
	group = [sspmSourceProfileType, sspmSourceProfilePacketSize, sspmSourceProfilePacketFillType, sspmSourceProfilePacketFillValue, sspmSourceProfileTOS, sspmSourceProfileFlowLabel, sspmSourceProfileLooseSrcRteFill, sspmSourceProfileLooseSrcRteLen, sspmSourceProfileTTL, sspmSourceProfileNoFrag, sspmSourceProfile8021Tagging, sspmSourceProfileUsername, sspmSourceProfilePassword, sspmSourceProfileParameter, sspmSourceProfileOwner, sspmSourceProfileStorageType, sspmSourceProfileStatus, sspmSourceControlProfile, sspmSourceControlSrc, sspmSourceControlDestAddrType, sspmSourceControlDestAddr, sspmSourceControlEnabled, sspmSourceControlTimeOut, sspmSourceControlSamplingDist, sspmSourceControlFrequency, sspmSourceControlFirstSeqNum, sspmSourceControlLastSeqNum, sspmSourceControlOwner, sspmSourceControlStorageType, sspmSourceControlStatus]

class sspmUserPassGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 3])
	group = [sspmSourceProfileUsername, sspmSourceProfilePassword]

class sspmSinkGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 16, 28, 3, 2, 4])
	group = [sspmSinkType, sspmSinkSourceAddressType, sspmSinkSourceAddress, sspmSinkExpectedRate, sspmSinkEnable, sspmSinkExpectedFirstSequenceNum, sspmSinkLastSequenceNumber, sspmSinkLastSequenceInvalid, sspmSinkStorageType, sspmSinkStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
