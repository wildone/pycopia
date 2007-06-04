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
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Integer32
from CISCO_SMI import ciscoMgmt
from RFC1213_MIB import ifIndex
from SNMPv2_TC import MacAddress, TEXTUAL_CONVENTION

class CISCO_DLC_SWITCH_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-DLCSW-MIB'
	conformance = 2
	name = 'CISCO-DLC-SWITCH-MIB'
	language = 2
	description = 'This is the MIB module for objects used to\nmanage FRAS sessions to the endstation. \n\tThese objects are specific to downstream or \n\tenduster sessions only. It does not contain \n\tobjects supported by the FRAS-HOST MIB which \n\tare specific to upstream or host-end sessions.'

# nodes
class ciscoDlcSwitchMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76])
	name = 'ciscoDlcSwitchMIB'

class ciscoDlcSwitchMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1])
	name = 'ciscoDlcSwitchMIBObjects'

class frasBnnSdlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1])
	name = 'frasBnnSdlc'

class frasBnnLlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2])
	name = 'frasBnnLlc'

class frasBanSdlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3])
	name = 'frasBanSdlc'

class frasBanLlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4])
	name = 'frasBanLlc'

class ciscoDlcSwitchConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2])
	name = 'ciscoDlcSwitchConformance'

class ciscoDlcSwitchCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 1])
	name = 'ciscoDlcSwitchCompliances'

class ciscoDlcSwitchGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2])
	name = 'ciscoDlcSwitchGroups'


# macros
# types 

class SAP(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 1))


class SdlcAddress(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(1, 1))

# scalars 
# columns
class bnnSdlcConAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 1])
	syntaxobject = SdlcAddress


class bnnSdlcConState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'testSent'), Enum(3, 'xidexchg'), Enum(4, 'connrqsent'), Enum(5, 'sigstnwait'), Enum(6, 'connrspwait'), Enum(7, 'connrspsent'), Enum(8, 'contacted'), Enum(9, 'discwait')]


class bnnSdlcConDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bnnSdlcConFRInterface(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 4])
	syntaxobject = InterfaceIndexOrZero


class bnnSdlcConLocalSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 5])
	syntaxobject = SAP


class bnnSdlcConRemoteSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1, 6])
	syntaxobject = SAP


class bnnLlcConDeviceMacAddress(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class bnnLlcConLanLocalSap(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 2])
	syntaxobject = SAP


class bnnLlcConLanRemoteSap(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 3])
	syntaxobject = SAP


class bnnLlcConLanInterface(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 4])
	syntaxobject = InterfaceIndexOrZero


class bnnLlcConDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class bnnLlcConState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'testSent'), Enum(3, 'xidexchg'), Enum(4, 'connrqsent'), Enum(5, 'sigstnwait'), Enum(6, 'connrspwait'), Enum(7, 'connrspsent'), Enum(8, 'contacted'), Enum(9, 'discwait')]


class bnnLlcConLocalMacAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class bnnLlcConFrLocalSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 8])
	syntaxobject = SAP


class bnnLlcConFrRemoteSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1, 9])
	syntaxobject = SAP


class banSdlcConLocalInterface(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 1])
	syntaxobject = InterfaceIndexOrZero


class banSdlcConAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 2])
	syntaxobject = SdlcAddress


class banSdlcConBanDlciMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banSdlcConDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class banSdlcConState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'testSent'), Enum(3, 'xidexchg'), Enum(4, 'connrqsent'), Enum(5, 'sigstnwait'), Enum(6, 'connrspwait'), Enum(7, 'connrspsent'), Enum(8, 'contacted'), Enum(9, 'discwait')]


class banSdlcConVmac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banSdlcConBniAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banSdlcConFrLocalSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 8])
	syntaxobject = SAP


class banSdlcConFrRemoteSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1, 9])
	syntaxobject = SAP


class banLlcEndstnLocalMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banLlcBanDlciMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banLlcConLocalSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 3])
	syntaxobject = SAP


class banLlcConRemoteSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 4])
	syntaxobject = SAP


class banLlcConDlci(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class banLlcConState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'testSent'), Enum(3, 'xidexchg'), Enum(4, 'connrqsent'), Enum(5, 'sigstnwait'), Enum(6, 'connrspwait'), Enum(7, 'connrspsent'), Enum(8, 'contacted'), Enum(9, 'discwait')]


class banLlcConFrInterface(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 7])
	syntaxobject = InterfaceIndexOrZero


class banLlcBniAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class banLlcConFrLocalSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 9])
	syntaxobject = SAP


class banLlcConFrRemoteSap(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1, 10])
	syntaxobject = SAP


# rows 
class frasBnnSdlcConEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, bnnSdlcConAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 1, 1, 1])
	access = 2
	columns = {'bnnSdlcConAddress': bnnSdlcConAddress, 'bnnSdlcConState': bnnSdlcConState, 'bnnSdlcConDlci': bnnSdlcConDlci, 'bnnSdlcConFRInterface': bnnSdlcConFRInterface, 'bnnSdlcConLocalSap': bnnSdlcConLocalSap, 'bnnSdlcConRemoteSap': bnnSdlcConRemoteSap}


class frasBnnLlcConEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, bnnLlcConDeviceMacAddress, bnnLlcConLanLocalSap, bnnLlcConLanRemoteSap], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 2, 1, 1])
	access = 2
	columns = {'bnnLlcConDeviceMacAddress': bnnLlcConDeviceMacAddress, 'bnnLlcConLanLocalSap': bnnLlcConLanLocalSap, 'bnnLlcConLanRemoteSap': bnnLlcConLanRemoteSap, 'bnnLlcConLanInterface': bnnLlcConLanInterface, 'bnnLlcConDlci': bnnLlcConDlci, 'bnnLlcConState': bnnLlcConState, 'bnnLlcConLocalMacAddress': bnnLlcConLocalMacAddress, 'bnnLlcConFrLocalSap': bnnLlcConFrLocalSap, 'bnnLlcConFrRemoteSap': bnnLlcConFrRemoteSap}


class frasBanSdlcConEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, banSdlcConAddress, banSdlcConBanDlciMac], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 3, 1, 1])
	access = 2
	columns = {'banSdlcConLocalInterface': banSdlcConLocalInterface, 'banSdlcConAddress': banSdlcConAddress, 'banSdlcConBanDlciMac': banSdlcConBanDlciMac, 'banSdlcConDlci': banSdlcConDlci, 'banSdlcConState': banSdlcConState, 'banSdlcConVmac': banSdlcConVmac, 'banSdlcConBniAddress': banSdlcConBniAddress, 'banSdlcConFrLocalSap': banSdlcConFrLocalSap, 'banSdlcConFrRemoteSap': banSdlcConFrRemoteSap}


class frasBanLlcConEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([banLlcEndstnLocalMac, banLlcConLocalSap, banLlcConRemoteSap, banLlcBanDlciMac], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 1, 4, 1, 1])
	access = 2
	columns = {'banLlcEndstnLocalMac': banLlcEndstnLocalMac, 'banLlcBanDlciMac': banLlcBanDlciMac, 'banLlcConLocalSap': banLlcConLocalSap, 'banLlcConRemoteSap': banLlcConRemoteSap, 'banLlcConDlci': banLlcConDlci, 'banLlcConState': banLlcConState, 'banLlcConFrInterface': banLlcConFrInterface, 'banLlcBniAddress': banLlcBniAddress, 'banLlcConFrLocalSap': banLlcConFrLocalSap, 'banLlcConFrRemoteSap': banLlcConFrRemoteSap}


# notifications (traps) 
# groups 
class frasBnnSdlcGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 1])
	group = [bnnSdlcConState, bnnSdlcConDlci, bnnSdlcConFRInterface, bnnSdlcConLocalSap, bnnSdlcConRemoteSap]

class frasBnnLlcGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 2])
	group = [bnnLlcConLanInterface, bnnLlcConDlci, bnnLlcConState, bnnLlcConLocalMacAddress, bnnLlcConFrLocalSap, bnnLlcConFrRemoteSap]

class frasBanSdlcGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 3])
	group = [banSdlcConLocalInterface, banSdlcConAddress, banSdlcConBanDlciMac, banSdlcConDlci, banSdlcConState, banSdlcConVmac, banSdlcConBniAddress, banSdlcConFrLocalSap, banSdlcConFrRemoteSap]

class frasBanLlcGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 76, 2, 2, 4])
	group = [banLlcEndstnLocalMac, banLlcBanDlciMac, banLlcConDlci, banLlcConLocalSap, banLlcConRemoteSap, banLlcConState, banLlcConFrInterface, banLlcBniAddress, banLlcConFrLocalSap, banLlcConFrRemoteSap]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
