# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Counter64, Integer32, IpAddress
from CISCO_TC import SAPType
from CISCO_SMI import ciscoMgmt
from RFC1213_MIB import ifIndex
from SNMPv2_TC import DisplayString, TruthValue, RowStatus, TEXTUAL_CONVENTION, MacAddress

class CISCO_CIPTG_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-CIPTG-MIB'
	conformance = 2
	name = 'CISCO-CIPTG-MIB'
	language = 2
	description = 'This is the Management Information Base (MIB) \nmodule for objects used to manage Transmission Groups \n(TGs) in Cisco Mainframe Channel Connection (CMCC)\nenvironments.\n\n---------------------------------------------------\n| Acronym Definitions:                            |\n| CIP      =   Channel Interface Processor        |\n| CMCC     =   Cisco Mainframe Channel Connection |\n| Cmgr     =   Connection Manager                 |\n| HPDT     =   High Performance Data Transfer     |\n| HPR      =   High Performance Routing           |\n| HSAS     =   High Speed Access Services         |\n| LLC      =   Logical Link Control               |\n| MPC      =   Multi-Path Channel                 |\n| MPC+     =   HPDT MPC                           |\n| SNA      =   Systems Network Architecture       |\n| TG       =   Transmission Group                 |\n| VC       =   Virtual Circuit                    |\n---------------------------------------------------\n\n\nThis MIB consists of the following tables:\n1) TG LLC Connection Administration\n2) TG LLC Connection Operational\n3) TG LLC Connection Statistics\n4) TG IP Connection Administration\n5) TG IP Connection Operational\n6) TG IP Connection Statistics\n\t7) TG Connection Manager Operational\n\nRefer to the following MIBs for an understanding of Cisco \nCIP internal LAN and adapter terminology:\n  CISCO-CIPLAN-MIB'

# nodes
class ciscoCipTgMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73])
	name = 'ciscoCipTgMIB'

class cipTgObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1])
	name = 'cipTgObjects'

class cipTgLlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1])
	name = 'cipTgLlc'

class cipTgIp(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2])
	name = 'cipTgIp'

class cipTgCmgr(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3])
	name = 'cipTgCmgr'

class ciscoCipTgMibConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3])
	name = 'ciscoCipTgMibConformance'

class ciscoCipTgMibCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 1])
	name = 'ciscoCipTgMibCompliances'

class ciscoCipTgMibGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2])
	name = 'ciscoCipTgMibGroups'


# macros
# types 

class ChannelTgName(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(8, 8))


class ChannelTgToken(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(0, 24))

# scalars 
# columns
class cipTgLlcAdminName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 1])
	syntaxobject = ChannelTgName


class cipTgLlcAdminLanType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'iso88023csmacd'), Enum(2, 'iso88025tokenRing'), Enum(3, 'fddi')]


class cipTgLlcAdminAdaptNo(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipTgLlcAdminLSAP(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 4])
	syntaxobject = SAPType


class cipTgLlcAdminRMAC(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class cipTgLlcAdminRSAP(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 6])
	syntaxobject = SAPType


class cipTgLlcAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cipTgLlcOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'shutdown'), Enum(2, 'reset'), Enum(3, 'locatePeer'), Enum(4, 'peerLocated'), Enum(5, 'negotiation'), Enum(6, 'contactPending'), Enum(7, 'active')]


class cipTgLlcOperTGN(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipTgLlcOperLocalCP(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cipTgLlcOperRemoteCP(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cipTgLlcOperMaxIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipTgLlcOperMaxOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cipTgLlcOperHpr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cipTgLlcOperHprLSAP(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 8])
	syntaxobject = SAPType


class cipTgLlcOperHprRSAP(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 9])
	syntaxobject = SAPType


class cipTgLlcOperRIF(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cipTgLlcOperLocalVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 11])
	syntaxobject = ChannelTgToken


class cipTgLlcOperRemoteVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 12])
	syntaxobject = ChannelTgToken


class cipTgLlcOperLocalConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 13])
	syntaxobject = ChannelTgToken


class cipTgLlcOperRemoteConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 14])
	syntaxobject = ChannelTgToken


class cipTgLlcOperVcStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'active')]


class cipTgLlcOperConnStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'connRequestSent'), Enum(3, 'pendingActive'), Enum(4, 'active')]


class cipTgLlcStatsIFramesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsIFrameBytesIn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgLlcStatsHCIFrameBytesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipTgLlcStatsIFramesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsIFrameBytesOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgLlcStatsHCIFrameBytesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipTgLlcStatsUIFramesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsUIFrameBytesIn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgLlcStatsHCUIFrameBytesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipTgLlcStatsUIFramesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsUIFrameBytesOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgLlcStatsHCUIFrameBytesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cipTgLlcStatsTestCmdsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsTestRspsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsXidCmdsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsXidCmdsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsXidRspsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsXidRspsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsConnNumberRecv(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgLlcStatsConnNumberSent(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgIpAdminName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 1])
	syntaxobject = ChannelTgName


class cipTgIpAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'tcpIp'), Enum(2, 'hsas')]


class cipTgIpAdminRemoteIpAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cipTgIpAdminLocalIpAddr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cipTgIpAdminBroadcast(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cipTgIpAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cipTgIpOperLocalVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 1])
	syntaxobject = ChannelTgToken


class cipTgIpOperRemoteVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 2])
	syntaxobject = ChannelTgToken


class cipTgIpOperLocalConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 3])
	syntaxobject = ChannelTgToken


class cipTgIpOperRemoteConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 4])
	syntaxobject = ChannelTgToken


class cipTgIpOperVcStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'active')]


class cipTgIpOperConnStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'connRequestSent'), Enum(3, 'pendingActive'), Enum(4, 'active')]


class cipTgIpStatsPacketsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgIpStatsBytesIn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgIpStatsHCBytesIn(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class cipTgIpStatsPacketsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cipTgIpStatsBytesOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'octets'


class cipTgIpStatsHCBytesOut(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter64
	access = 4
	units = 'octets'


class cipTgCmgrOperName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 1])
	syntaxobject = ChannelTgName


class cipTgCmgrOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pointToPoint'), Enum(2, 'pointToMultiPoint')]


class cipTgCmgrOperLocalGrToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 3])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperRemoteGrToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 4])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperLocalVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 5])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperRemoteVcToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 6])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperLocalConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 7])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperRemoteConnToken(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 8])
	syntaxobject = ChannelTgToken


class cipTgCmgrOperVcStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'active')]


class cipTgCmgrOperConnStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'reset'), Enum(2, 'active')]


# rows 
class cipTgLlcAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgLlcAdminName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 1, 1])
	access = 2
	rowstatus = cipTgLlcAdminRowStatus
	columns = {'cipTgLlcAdminName': cipTgLlcAdminName, 'cipTgLlcAdminLanType': cipTgLlcAdminLanType, 'cipTgLlcAdminAdaptNo': cipTgLlcAdminAdaptNo, 'cipTgLlcAdminLSAP': cipTgLlcAdminLSAP, 'cipTgLlcAdminRMAC': cipTgLlcAdminRMAC, 'cipTgLlcAdminRSAP': cipTgLlcAdminRSAP, 'cipTgLlcAdminRowStatus': cipTgLlcAdminRowStatus}


from RFC1213_MIB import ifIndex
from CISCO_CIPTG_MIB import cipTgLlcAdminName
class cipTgLlcOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgLlcAdminName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 2, 1])
	access = 2
	columns = {'cipTgLlcOperState': cipTgLlcOperState, 'cipTgLlcOperTGN': cipTgLlcOperTGN, 'cipTgLlcOperLocalCP': cipTgLlcOperLocalCP, 'cipTgLlcOperRemoteCP': cipTgLlcOperRemoteCP, 'cipTgLlcOperMaxIn': cipTgLlcOperMaxIn, 'cipTgLlcOperMaxOut': cipTgLlcOperMaxOut, 'cipTgLlcOperHpr': cipTgLlcOperHpr, 'cipTgLlcOperHprLSAP': cipTgLlcOperHprLSAP, 'cipTgLlcOperHprRSAP': cipTgLlcOperHprRSAP, 'cipTgLlcOperRIF': cipTgLlcOperRIF, 'cipTgLlcOperLocalVcToken': cipTgLlcOperLocalVcToken, 'cipTgLlcOperRemoteVcToken': cipTgLlcOperRemoteVcToken, 'cipTgLlcOperLocalConnToken': cipTgLlcOperLocalConnToken, 'cipTgLlcOperRemoteConnToken': cipTgLlcOperRemoteConnToken, 'cipTgLlcOperVcStatus': cipTgLlcOperVcStatus, 'cipTgLlcOperConnStatus': cipTgLlcOperConnStatus}


from RFC1213_MIB import ifIndex
from CISCO_CIPTG_MIB import cipTgLlcAdminName
class cipTgLlcStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgLlcAdminName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 1, 3, 1])
	access = 2
	columns = {'cipTgLlcStatsIFramesIn': cipTgLlcStatsIFramesIn, 'cipTgLlcStatsIFrameBytesIn': cipTgLlcStatsIFrameBytesIn, 'cipTgLlcStatsHCIFrameBytesIn': cipTgLlcStatsHCIFrameBytesIn, 'cipTgLlcStatsIFramesOut': cipTgLlcStatsIFramesOut, 'cipTgLlcStatsIFrameBytesOut': cipTgLlcStatsIFrameBytesOut, 'cipTgLlcStatsHCIFrameBytesOut': cipTgLlcStatsHCIFrameBytesOut, 'cipTgLlcStatsUIFramesIn': cipTgLlcStatsUIFramesIn, 'cipTgLlcStatsUIFrameBytesIn': cipTgLlcStatsUIFrameBytesIn, 'cipTgLlcStatsHCUIFrameBytesIn': cipTgLlcStatsHCUIFrameBytesIn, 'cipTgLlcStatsUIFramesOut': cipTgLlcStatsUIFramesOut, 'cipTgLlcStatsUIFrameBytesOut': cipTgLlcStatsUIFrameBytesOut, 'cipTgLlcStatsHCUIFrameBytesOut': cipTgLlcStatsHCUIFrameBytesOut, 'cipTgLlcStatsTestCmdsOut': cipTgLlcStatsTestCmdsOut, 'cipTgLlcStatsTestRspsIn': cipTgLlcStatsTestRspsIn, 'cipTgLlcStatsXidCmdsIn': cipTgLlcStatsXidCmdsIn, 'cipTgLlcStatsXidCmdsOut': cipTgLlcStatsXidCmdsOut, 'cipTgLlcStatsXidRspsIn': cipTgLlcStatsXidRspsIn, 'cipTgLlcStatsXidRspsOut': cipTgLlcStatsXidRspsOut, 'cipTgLlcStatsConnNumberRecv': cipTgLlcStatsConnNumberRecv, 'cipTgLlcStatsConnNumberSent': cipTgLlcStatsConnNumberSent}


class cipTgIpAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgIpAdminName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 1, 1])
	access = 2
	rowstatus = cipTgIpAdminRowStatus
	columns = {'cipTgIpAdminName': cipTgIpAdminName, 'cipTgIpAdminType': cipTgIpAdminType, 'cipTgIpAdminRemoteIpAddr': cipTgIpAdminRemoteIpAddr, 'cipTgIpAdminLocalIpAddr': cipTgIpAdminLocalIpAddr, 'cipTgIpAdminBroadcast': cipTgIpAdminBroadcast, 'cipTgIpAdminRowStatus': cipTgIpAdminRowStatus}


from RFC1213_MIB import ifIndex
from CISCO_CIPTG_MIB import cipTgIpAdminName
class cipTgIpOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgIpAdminName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 2, 1])
	access = 2
	columns = {'cipTgIpOperLocalVcToken': cipTgIpOperLocalVcToken, 'cipTgIpOperRemoteVcToken': cipTgIpOperRemoteVcToken, 'cipTgIpOperLocalConnToken': cipTgIpOperLocalConnToken, 'cipTgIpOperRemoteConnToken': cipTgIpOperRemoteConnToken, 'cipTgIpOperVcStatus': cipTgIpOperVcStatus, 'cipTgIpOperConnStatus': cipTgIpOperConnStatus}


from RFC1213_MIB import ifIndex
from CISCO_CIPTG_MIB import cipTgIpAdminName
class cipTgIpStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgIpAdminName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 2, 3, 1])
	access = 2
	columns = {'cipTgIpStatsPacketsIn': cipTgIpStatsPacketsIn, 'cipTgIpStatsBytesIn': cipTgIpStatsBytesIn, 'cipTgIpStatsHCBytesIn': cipTgIpStatsHCBytesIn, 'cipTgIpStatsPacketsOut': cipTgIpStatsPacketsOut, 'cipTgIpStatsBytesOut': cipTgIpStatsBytesOut, 'cipTgIpStatsHCBytesOut': cipTgIpStatsHCBytesOut}


class cipTgCmgrOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cipTgCmgrOperName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 1, 3, 1, 1])
	access = 2
	columns = {'cipTgCmgrOperName': cipTgCmgrOperName, 'cipTgCmgrOperType': cipTgCmgrOperType, 'cipTgCmgrOperLocalGrToken': cipTgCmgrOperLocalGrToken, 'cipTgCmgrOperRemoteGrToken': cipTgCmgrOperRemoteGrToken, 'cipTgCmgrOperLocalVcToken': cipTgCmgrOperLocalVcToken, 'cipTgCmgrOperRemoteVcToken': cipTgCmgrOperRemoteVcToken, 'cipTgCmgrOperLocalConnToken': cipTgCmgrOperLocalConnToken, 'cipTgCmgrOperRemoteConnToken': cipTgCmgrOperRemoteConnToken, 'cipTgCmgrOperVcStatus': cipTgCmgrOperVcStatus, 'cipTgCmgrOperConnStatus': cipTgCmgrOperConnStatus}


# notifications (traps) 
# groups 
class ciscoCipTgLlcGroupRev1(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 3])
	group = [cipTgLlcAdminLanType, cipTgLlcAdminAdaptNo, cipTgLlcAdminLSAP, cipTgLlcAdminRMAC, cipTgLlcAdminRSAP, cipTgLlcAdminRowStatus, cipTgLlcOperState, cipTgLlcOperTGN, cipTgLlcOperLocalCP, cipTgLlcOperRemoteCP, cipTgLlcOperMaxIn, cipTgLlcOperMaxOut, cipTgLlcOperHpr, cipTgLlcOperHprLSAP, cipTgLlcOperHprRSAP, cipTgLlcOperRIF, cipTgLlcOperLocalVcToken, cipTgLlcOperRemoteVcToken, cipTgLlcOperLocalConnToken, cipTgLlcOperRemoteConnToken, cipTgLlcOperVcStatus, cipTgLlcOperConnStatus, cipTgLlcStatsIFramesIn, cipTgLlcStatsIFrameBytesIn, cipTgLlcStatsHCIFrameBytesIn, cipTgLlcStatsIFramesOut, cipTgLlcStatsIFrameBytesOut, cipTgLlcStatsHCIFrameBytesOut, cipTgLlcStatsUIFramesIn, cipTgLlcStatsUIFrameBytesIn, cipTgLlcStatsHCUIFrameBytesIn, cipTgLlcStatsUIFramesOut, cipTgLlcStatsUIFrameBytesOut, cipTgLlcStatsHCUIFrameBytesOut, cipTgLlcStatsTestCmdsOut, cipTgLlcStatsTestRspsIn, cipTgLlcStatsXidCmdsIn, cipTgLlcStatsXidCmdsOut, cipTgLlcStatsXidRspsIn, cipTgLlcStatsXidRspsOut, cipTgLlcStatsConnNumberRecv, cipTgLlcStatsConnNumberSent]

class ciscoCipTgIpGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 4])
	group = [cipTgIpAdminType, cipTgIpAdminRemoteIpAddr, cipTgIpAdminLocalIpAddr, cipTgIpAdminBroadcast, cipTgIpAdminRowStatus, cipTgIpOperLocalVcToken, cipTgIpOperRemoteVcToken, cipTgIpOperLocalConnToken, cipTgIpOperRemoteConnToken, cipTgIpOperVcStatus, cipTgIpOperConnStatus, cipTgIpStatsPacketsIn, cipTgIpStatsBytesIn, cipTgIpStatsHCBytesIn, cipTgIpStatsPacketsOut, cipTgIpStatsBytesOut, cipTgIpStatsHCBytesOut]

class ciscoCipTgCmgrGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 73, 3, 2, 5])
	group = [cipTgCmgrOperType, cipTgCmgrOperLocalGrToken, cipTgCmgrOperRemoteGrToken, cipTgCmgrOperLocalVcToken, cipTgCmgrOperRemoteVcToken, cipTgCmgrOperLocalConnToken, cipTgCmgrOperRemoteConnToken, cipTgCmgrOperVcStatus, cipTgCmgrOperConnStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
