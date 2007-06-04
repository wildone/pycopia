# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, Counter32, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import mib_2
from SNMPv2_TC import DisplayString

class Modem_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/Modem-MIB'
	conformance = 2
	name = 'Modem-MIB'
	language = 2
	description = 'The MIB module for management of dial-up modems.'

# nodes
class mdmMib(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38])
	name = 'mdmMib'

class mdmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1])
	name = 'mdmMIB'

class mdmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1])
	name = 'mdmMIBObjects'

class mdmLineCapabilities(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5])
	name = 'mdmLineCapabilities'

class mdmLineCapabilitiesV21(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 1])
	name = 'mdmLineCapabilitiesV21'

class mdmLineCapabilitiesV22(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 2])
	name = 'mdmLineCapabilitiesV22'

class mdmLineCapabilitiesV22bis(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 3])
	name = 'mdmLineCapabilitiesV22bis'

class mdmLineCapabilitiesV23CC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 4])
	name = 'mdmLineCapabilitiesV23CC'

class mdmLineCapabilitiesV23SC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 5])
	name = 'mdmLineCapabilitiesV23SC'

class mdmLineCapabilitiesV25bis(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 6])
	name = 'mdmLineCapabilitiesV25bis'

class mdmLineCapabilitiesV26bis(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 7])
	name = 'mdmLineCapabilitiesV26bis'

class mdmLineCapabilitiesV26ter(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 8])
	name = 'mdmLineCapabilitiesV26ter'

class mdmLineCapabilitiesV27ter(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 9])
	name = 'mdmLineCapabilitiesV27ter'

class mdmLineCapabilitiesV32(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 10])
	name = 'mdmLineCapabilitiesV32'

class mdmLineCapabilitiesV32bis(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 11])
	name = 'mdmLineCapabilitiesV32bis'

class mdmLineCapabilitiesV32terbo(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 12])
	name = 'mdmLineCapabilitiesV32terbo'

class mdmLineCapabilitiesVFC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 13])
	name = 'mdmLineCapabilitiesVFC'

class mdmLineCapabilitiesV34(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 14])
	name = 'mdmLineCapabilitiesV34'

class mdmLineCapabilitiesV42(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 15])
	name = 'mdmLineCapabilitiesV42'

class mdmLineCapabilitiesV42bis(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 16])
	name = 'mdmLineCapabilitiesV42bis'

class mdmLineCapabilitiesMNP1(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 17])
	name = 'mdmLineCapabilitiesMNP1'

class mdmLineCapabilitiesMNP2(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 18])
	name = 'mdmLineCapabilitiesMNP2'

class mdmLineCapabilitiesMNP3(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 19])
	name = 'mdmLineCapabilitiesMNP3'

class mdmLineCapabilitiesMNP4(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 20])
	name = 'mdmLineCapabilitiesMNP4'

class mdmLineCapabilitiesMNP5(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 21])
	name = 'mdmLineCapabilitiesMNP5'

class mdmLineCapabilitiesMNP6(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 22])
	name = 'mdmLineCapabilitiesMNP6'

class mdmLineCapabilitiesMNP7(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 23])
	name = 'mdmLineCapabilitiesMNP7'

class mdmLineCapabilitiesMNP8(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 24])
	name = 'mdmLineCapabilitiesMNP8'

class mdmLineCapabilitiesMNP9(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 25])
	name = 'mdmLineCapabilitiesMNP9'

class mdmLineCapabilitiesMNP10(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 26])
	name = 'mdmLineCapabilitiesMNP10'

class mdmLineCapabilitiesV29(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 27])
	name = 'mdmLineCapabilitiesV29'

class mdmLineCapabilitiesV33(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 28])
	name = 'mdmLineCapabilitiesV33'

class mdmLineCapabilitiesBell208(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 5, 29])
	name = 'mdmLineCapabilitiesBell208'

class mdmConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2])
	name = 'mdmConformance'

class mdmCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 1])
	name = 'mdmCompliances'

class mdmGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2])
	name = 'mdmGroups'


# macros
# types 
# scalars 
class mdmNumber(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


# columns
class mdmIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmIDManufacturerOID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mdmIDProductDetails(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class mdmLineCarrierLossTime(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmLineState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'onHook'), Enum(3, 'offHook'), Enum(4, 'connected'), Enum(5, 'busiedOut'), Enum(6, 'reset')]


class mdmLineCapabilitiesIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmLineCapabilitiesID(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mdmLineCapabilitiesEnableRequested(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disabled'), Enum(2, 'optional'), Enum(3, 'preferred')]


class mdmLineCapabilitiesEnableGranted(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disabled'), Enum(2, 'optional'), Enum(3, 'preferred')]


class mdmDTEActionDTROnToOff(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ignore'), Enum(2, 'escapeToCommandMode'), Enum(3, 'disconnectCall'), Enum(4, 'resetModem')]


class mdmDTEActionDTROffToOn(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ignore'), Enum(2, 'enableDial'), Enum(3, 'autoAnswerEnable'), Enum(4, 'establishConnection')]


class mdmDTESyncTimingSource(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'internal'), Enum(2, 'external'), Enum(3, 'loopback'), Enum(4, 'network')]


class mdmDTESyncAsyncMode(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'async'), Enum(2, 'sync'), Enum(3, 'syncAfterDial')]


class mdmDTEInactivityTimeout(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmCCRingsBeforeAnswer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmCCCallSetUpFailTimer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmCCResultCodeEnable(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'disabled'), Enum(2, 'numericEnabled'), Enum(3, 'verboseEnabled')]


class mdmCCEscapeAction(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ignoreEscape'), Enum(2, 'hangUp'), Enum(3, 'enterCommandMode')]


class mdmCCCallDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmCCConnectionFailReason(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'unknown'), Enum(2, 'other'), Enum(3, 'managementCommand'), Enum(4, 'inactivityTimeout'), Enum(5, 'mnpIncompatibility'), Enum(6, 'protocolError'), Enum(10, 'powerLoss'), Enum(11, 'equipmentFailure'), Enum(20, 'dtrDrop'), Enum(30, 'noDialTone'), Enum(31, 'lineBusy'), Enum(32, 'noAnswer'), Enum(33, 'voiceDetected'), Enum(40, 'carrierLost'), Enum(41, 'trainingFailed'), Enum(42, 'faxDetected')]


class mdmCCStoredDialStringIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmCCStoredDialString(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class mdmECErrorControlUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mdmDCCompressionTypeUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mdmSCCurrentLineTransmitRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmSCCurrentLineReceiveRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmSCInitialLineTransmitRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmSCInitialLineReceiveRate(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmSCModulationSchemeUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class mdmStatsRingNoAnswers(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsIncomingConnectionFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsIncomingConnectionCompletions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsFailedDialAttempts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsOutgoingConnectionFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsOutgoingConnectionCompletions(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsRetrains(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStats2400OrLessConnections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStats2400To14400Connections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsGreaterThan14400Connections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsErrorControlledConnections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsCompressedConnections(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsCompressionEfficiency(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class mdmStatsSentOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsReceivedOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsSentDataFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsReceivedDataFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsResentFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class mdmStatsErrorFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class mdmIDEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 2, 1])
	access = 2
	columns = {'mdmIndex': mdmIndex, 'mdmIDManufacturerOID': mdmIDManufacturerOID, 'mdmIDProductDetails': mdmIDProductDetails}


from Modem_MIB import mdmIndex
class mdmLineEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 3, 1])
	access = 2
	columns = {'mdmLineCarrierLossTime': mdmLineCarrierLossTime, 'mdmLineState': mdmLineState}


class mdmLineCapabilitiesEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex, mdmLineCapabilitiesIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 4, 1])
	access = 2
	columns = {'mdmLineCapabilitiesIndex': mdmLineCapabilitiesIndex, 'mdmLineCapabilitiesID': mdmLineCapabilitiesID, 'mdmLineCapabilitiesEnableRequested': mdmLineCapabilitiesEnableRequested, 'mdmLineCapabilitiesEnableGranted': mdmLineCapabilitiesEnableGranted}


from Modem_MIB import mdmIndex
class mdmDTEInterfaceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 6, 1])
	access = 2
	columns = {'mdmDTEActionDTROnToOff': mdmDTEActionDTROnToOff, 'mdmDTEActionDTROffToOn': mdmDTEActionDTROffToOn, 'mdmDTESyncTimingSource': mdmDTESyncTimingSource, 'mdmDTESyncAsyncMode': mdmDTESyncAsyncMode, 'mdmDTEInactivityTimeout': mdmDTEInactivityTimeout}


from Modem_MIB import mdmIndex
class mdmCallControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 7, 1])
	access = 2
	columns = {'mdmCCRingsBeforeAnswer': mdmCCRingsBeforeAnswer, 'mdmCCCallSetUpFailTimer': mdmCCCallSetUpFailTimer, 'mdmCCResultCodeEnable': mdmCCResultCodeEnable, 'mdmCCEscapeAction': mdmCCEscapeAction, 'mdmCCCallDuration': mdmCCCallDuration, 'mdmCCConnectionFailReason': mdmCCConnectionFailReason}


class mdmCCStoredDialStringEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex, mdmCCStoredDialStringIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 8, 1])
	access = 2
	columns = {'mdmCCStoredDialStringIndex': mdmCCStoredDialStringIndex, 'mdmCCStoredDialString': mdmCCStoredDialString}


from Modem_MIB import mdmIndex
class mdmECEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 9, 1])
	access = 2
	columns = {'mdmECErrorControlUsed': mdmECErrorControlUsed}


from Modem_MIB import mdmIndex
class mdmDCEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 10, 1])
	access = 2
	columns = {'mdmDCCompressionTypeUsed': mdmDCCompressionTypeUsed}


from Modem_MIB import mdmIndex
class mdmSCEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 11, 1])
	access = 2
	columns = {'mdmSCCurrentLineTransmitRate': mdmSCCurrentLineTransmitRate, 'mdmSCCurrentLineReceiveRate': mdmSCCurrentLineReceiveRate, 'mdmSCInitialLineTransmitRate': mdmSCInitialLineTransmitRate, 'mdmSCInitialLineReceiveRate': mdmSCInitialLineReceiveRate, 'mdmSCModulationSchemeUsed': mdmSCModulationSchemeUsed}


from Modem_MIB import mdmIndex
class mdmStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([mdmIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 1, 12, 1])
	access = 2
	columns = {'mdmStatsRingNoAnswers': mdmStatsRingNoAnswers, 'mdmStatsIncomingConnectionFailures': mdmStatsIncomingConnectionFailures, 'mdmStatsIncomingConnectionCompletions': mdmStatsIncomingConnectionCompletions, 'mdmStatsFailedDialAttempts': mdmStatsFailedDialAttempts, 'mdmStatsOutgoingConnectionFailures': mdmStatsOutgoingConnectionFailures, 'mdmStatsOutgoingConnectionCompletions': mdmStatsOutgoingConnectionCompletions, 'mdmStatsRetrains': mdmStatsRetrains, 'mdmStats2400OrLessConnections': mdmStats2400OrLessConnections, 'mdmStats2400To14400Connections': mdmStats2400To14400Connections, 'mdmStatsGreaterThan14400Connections': mdmStatsGreaterThan14400Connections, 'mdmStatsErrorControlledConnections': mdmStatsErrorControlledConnections, 'mdmStatsCompressedConnections': mdmStatsCompressedConnections, 'mdmStatsCompressionEfficiency': mdmStatsCompressionEfficiency, 'mdmStatsSentOctets': mdmStatsSentOctets, 'mdmStatsReceivedOctets': mdmStatsReceivedOctets, 'mdmStatsSentDataFrames': mdmStatsSentDataFrames, 'mdmStatsReceivedDataFrames': mdmStatsReceivedDataFrames, 'mdmStatsResentFrames': mdmStatsResentFrames, 'mdmStatsErrorFrames': mdmStatsErrorFrames}


# notifications (traps) 
# groups 
class mdmIDGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 1])
	group = [mdmIDManufacturerOID, mdmIDProductDetails]

class mdmLineInterfaceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 2])
	group = [mdmLineCarrierLossTime, mdmLineState, mdmLineCapabilitiesID, mdmLineCapabilitiesEnableRequested, mdmLineCapabilitiesEnableGranted]

class mdmDTEInterfaceGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 3])
	group = [mdmDTEActionDTROnToOff, mdmDTEActionDTROffToOn, mdmDTESyncTimingSource, mdmDTESyncAsyncMode, mdmDTEInactivityTimeout]

class mdmCallControlGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 4])
	group = [mdmCCRingsBeforeAnswer, mdmCCCallSetUpFailTimer, mdmCCResultCodeEnable, mdmCCEscapeAction, mdmCCCallDuration, mdmCCConnectionFailReason, mdmCCStoredDialString]

class mdmErrorControlGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 5])
	group = [mdmECErrorControlUsed]

class mdmDataCompressionGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 6])
	group = [mdmDCCompressionTypeUsed]

class mdmSignalConvertorGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 7])
	group = [mdmSCCurrentLineReceiveRate, mdmSCCurrentLineTransmitRate, mdmSCInitialLineReceiveRate, mdmSCInitialLineTransmitRate, mdmSCModulationSchemeUsed]

class mdmStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 38, 1, 2, 2, 8])
	group = [mdmStatsRingNoAnswers, mdmStatsIncomingConnectionFailures, mdmStatsIncomingConnectionCompletions, mdmStatsFailedDialAttempts, mdmStatsOutgoingConnectionFailures, mdmStatsOutgoingConnectionCompletions, mdmStatsRetrains, mdmStats2400OrLessConnections, mdmStats2400To14400Connections, mdmStatsGreaterThan14400Connections, mdmStatsErrorControlledConnections, mdmStatsCompressedConnections, mdmStatsCompressionEfficiency, mdmStatsSentOctets, mdmStatsReceivedOctets, mdmStatsSentDataFrames, mdmStatsReceivedDataFrames, mdmStatsResentFrames, mdmStatsErrorFrames]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
