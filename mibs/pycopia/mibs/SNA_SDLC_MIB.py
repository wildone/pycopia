# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Counter32, Integer32, TimeTicks
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from RFC1213_MIB import mib_2, ifIndex, ifAdminStatus, ifOperStatus
from SNMPv2_TC import DisplayString, RowStatus, TimeInterval

class SNA_SDLC_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNA-SDLC-MIB'
	conformance = 2
	name = 'SNA-SDLC-MIB'
	language = 2
	description = 'This is the MIB module for objects used to\nmanage SDLC devices.'

# nodes
class snaDLC(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41])
	name = 'snaDLC'

class sdlc(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1])
	name = 'sdlc'

class sdlcPortGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1])
	name = 'sdlcPortGroup'

class sdlcLSGroup(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2])
	name = 'sdlcLSGroup'

class sdlcTraps(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 3])
	name = 'sdlcTraps'

class sdlcConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4])
	name = 'sdlcConformance'

class sdlcCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 1])
	name = 'sdlcCompliances'

class sdlcGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2])
	name = 'sdlcGroups'

class sdlcCoreGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1])
	name = 'sdlcCoreGroups'

class sdlcPrimaryGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2])
	name = 'sdlcPrimaryGroups'


# macros
# types 
# scalars 
# columns
class sdlcPortAdminName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sdlcPortAdminRole(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primary'), Enum(2, 'secondary'), Enum(3, 'negotiable')]


class sdlcPortAdminType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'leased'), Enum(2, 'switched')]


class sdlcPortAdminTopology(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pointToPoint'), Enum(2, 'multipoint')]


class sdlcPortAdminISTATUS(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class sdlcPortAdminACTIVTO(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortAdminPAUSE(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortAdminSERVLIM(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcPortAdminSlowPollTimer(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortOperName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sdlcPortOperRole(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primary'), Enum(2, 'secondary'), Enum(3, 'undefined')]


class sdlcPortOperType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'leased'), Enum(2, 'switched')]


class sdlcPortOperTopology(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'pointToPoint'), Enum(2, 'multipoint')]


class sdlcPortOperISTATUS(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class sdlcPortOperACTIVTO(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortOperPAUSE(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortOperSlowPollMethod(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'servlim'), Enum(2, 'pollpause'), Enum(3, 'other')]


class sdlcPortOperSERVLIM(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcPortOperSlowPollTimer(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcPortOperLastModifyTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sdlcPortOperLastFailTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sdlcPortOperLastFailCause(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'undefined'), Enum(2, 'physical')]


class sdlcPortStatsPhysicalFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsInvalidAddresses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsDwarfFrames(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsPollsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsPollsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsPollRspsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsPollRspsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsLocalBusies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsRemoteBusies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsIFramesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsIFramesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsOctetsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsOctetsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsProtocolErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsActivityTOs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsRNRLIMITs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsRetriesExps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsRetransmitsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcPortStatsRetransmitsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSAddress(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sdlcLSAdminState(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class sdlcLSAdminISTATUS(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'inactive'), Enum(2, 'active')]


class sdlcLSAdminMAXDATASend(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminMAXDATARcv(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminREPLYTO(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSAdminMAXIN(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminMAXOUT(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminMODULO(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(8, 'eight'), Enum(128, 'onetwentyeight')]


class sdlcLSAdminRETRIESm(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminRETRIESt(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSAdminRETRIESn(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminRNRLIMIT(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSAdminDATMODE(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'half'), Enum(2, 'full')]


class sdlcLSAdminGPoll(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSAdminSimRim(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'no'), Enum(2, 'yes')]


class sdlcLSAdminXmitRcvCap(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'twa'), Enum(2, 'tws')]


class sdlcLSAdminRowStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class sdlcLSOperName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class sdlcLSOperRole(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'primary'), Enum(2, 'secondary'), Enum(3, 'undefined')]


class sdlcLSOperState(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'discontacted'), Enum(2, 'contactPending'), Enum(3, 'contacted'), Enum(4, 'discontactPending')]


class sdlcLSOperMAXDATASend(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperREPLYTO(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSOperMAXIN(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperMAXOUT(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperMODULO(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(8, 'eight'), Enum(128, 'onetwentyeight')]


class sdlcLSOperRETRIESm(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperRETRIESt(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSOperRETRIESn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperRNRLIMIT(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class sdlcLSOperDATMODE(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'half'), Enum(2, 'full')]


class sdlcLSOperLastModifyTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sdlcLSOperLastFailTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class sdlcLSOperLastFailCause(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'undefined'), Enum(2, 'rxFRMR'), Enum(3, 'txFRMR'), Enum(4, 'noResponse'), Enum(5, 'protocolErr'), Enum(6, 'noActivity'), Enum(7, 'rnrLimit'), Enum(8, 'retriesExpired')]


class sdlcLSOperLastFailCtrlIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sdlcLSOperLastFailCtrlOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sdlcLSOperLastFailFRMRInfo(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class sdlcLSOperLastFailREPLYTOs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSOperEcho(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'no'), Enum(2, 'yes')]


class sdlcLSOperGPoll(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sdlcLSOperSimRim(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'no'), Enum(2, 'yes')]


class sdlcLSOperXmitRcvCap(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'twa'), Enum(2, 'tws')]


class sdlcLSStatsBLUsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsBLUsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsOctetsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsOctetsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsPollsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsPollsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsPollRspsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsPollRspsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsLocalBusies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRemoteBusies(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsIFramesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsIFramesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsUIFramesIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsUIFramesOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsXIDsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsXIDsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsTESTsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsTESTsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsREJsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsREJsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsFRMRsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsFRMRsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsSIMsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 23])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsSIMsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 24])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRIMsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 25])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRIMsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 26])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsDISCIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 27])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsDISCOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 28])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsUAIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 29])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsUAOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 30])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsDMIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 31])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsDMOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 32])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsSNRMIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 33])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsSNRMOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 34])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsProtocolErrs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 35])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsActivityTOs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 36])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRNRLIMITs(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 37])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRetriesExps(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 38])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRetransmitsIn(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 39])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sdlcLSStatsRetransmitsOut(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1, 40])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


# rows 
class sdlcPortAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 1, 1])
	access = 2
	columns = {'sdlcPortAdminName': sdlcPortAdminName, 'sdlcPortAdminRole': sdlcPortAdminRole, 'sdlcPortAdminType': sdlcPortAdminType, 'sdlcPortAdminTopology': sdlcPortAdminTopology, 'sdlcPortAdminISTATUS': sdlcPortAdminISTATUS, 'sdlcPortAdminACTIVTO': sdlcPortAdminACTIVTO, 'sdlcPortAdminPAUSE': sdlcPortAdminPAUSE, 'sdlcPortAdminSERVLIM': sdlcPortAdminSERVLIM, 'sdlcPortAdminSlowPollTimer': sdlcPortAdminSlowPollTimer}


class sdlcPortOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 2, 1])
	access = 2
	columns = {'sdlcPortOperName': sdlcPortOperName, 'sdlcPortOperRole': sdlcPortOperRole, 'sdlcPortOperType': sdlcPortOperType, 'sdlcPortOperTopology': sdlcPortOperTopology, 'sdlcPortOperISTATUS': sdlcPortOperISTATUS, 'sdlcPortOperACTIVTO': sdlcPortOperACTIVTO, 'sdlcPortOperPAUSE': sdlcPortOperPAUSE, 'sdlcPortOperSlowPollMethod': sdlcPortOperSlowPollMethod, 'sdlcPortOperSERVLIM': sdlcPortOperSERVLIM, 'sdlcPortOperSlowPollTimer': sdlcPortOperSlowPollTimer, 'sdlcPortOperLastModifyTime': sdlcPortOperLastModifyTime, 'sdlcPortOperLastFailTime': sdlcPortOperLastFailTime, 'sdlcPortOperLastFailCause': sdlcPortOperLastFailCause}


class sdlcPortStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 1, 3, 1])
	access = 2
	columns = {'sdlcPortStatsPhysicalFailures': sdlcPortStatsPhysicalFailures, 'sdlcPortStatsInvalidAddresses': sdlcPortStatsInvalidAddresses, 'sdlcPortStatsDwarfFrames': sdlcPortStatsDwarfFrames, 'sdlcPortStatsPollsIn': sdlcPortStatsPollsIn, 'sdlcPortStatsPollsOut': sdlcPortStatsPollsOut, 'sdlcPortStatsPollRspsIn': sdlcPortStatsPollRspsIn, 'sdlcPortStatsPollRspsOut': sdlcPortStatsPollRspsOut, 'sdlcPortStatsLocalBusies': sdlcPortStatsLocalBusies, 'sdlcPortStatsRemoteBusies': sdlcPortStatsRemoteBusies, 'sdlcPortStatsIFramesIn': sdlcPortStatsIFramesIn, 'sdlcPortStatsIFramesOut': sdlcPortStatsIFramesOut, 'sdlcPortStatsOctetsIn': sdlcPortStatsOctetsIn, 'sdlcPortStatsOctetsOut': sdlcPortStatsOctetsOut, 'sdlcPortStatsProtocolErrs': sdlcPortStatsProtocolErrs, 'sdlcPortStatsActivityTOs': sdlcPortStatsActivityTOs, 'sdlcPortStatsRNRLIMITs': sdlcPortStatsRNRLIMITs, 'sdlcPortStatsRetriesExps': sdlcPortStatsRetriesExps, 'sdlcPortStatsRetransmitsIn': sdlcPortStatsRetransmitsIn, 'sdlcPortStatsRetransmitsOut': sdlcPortStatsRetransmitsOut}


class sdlcLSAdminEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, sdlcLSAddress], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 1, 1])
	access = 2
	rowstatus = sdlcLSAdminRowStatus
	columns = {'sdlcLSAddress': sdlcLSAddress, 'sdlcLSAdminName': sdlcLSAdminName, 'sdlcLSAdminState': sdlcLSAdminState, 'sdlcLSAdminISTATUS': sdlcLSAdminISTATUS, 'sdlcLSAdminMAXDATASend': sdlcLSAdminMAXDATASend, 'sdlcLSAdminMAXDATARcv': sdlcLSAdminMAXDATARcv, 'sdlcLSAdminREPLYTO': sdlcLSAdminREPLYTO, 'sdlcLSAdminMAXIN': sdlcLSAdminMAXIN, 'sdlcLSAdminMAXOUT': sdlcLSAdminMAXOUT, 'sdlcLSAdminMODULO': sdlcLSAdminMODULO, 'sdlcLSAdminRETRIESm': sdlcLSAdminRETRIESm, 'sdlcLSAdminRETRIESt': sdlcLSAdminRETRIESt, 'sdlcLSAdminRETRIESn': sdlcLSAdminRETRIESn, 'sdlcLSAdminRNRLIMIT': sdlcLSAdminRNRLIMIT, 'sdlcLSAdminDATMODE': sdlcLSAdminDATMODE, 'sdlcLSAdminGPoll': sdlcLSAdminGPoll, 'sdlcLSAdminSimRim': sdlcLSAdminSimRim, 'sdlcLSAdminXmitRcvCap': sdlcLSAdminXmitRcvCap, 'sdlcLSAdminRowStatus': sdlcLSAdminRowStatus}


class sdlcLSOperEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, sdlcLSAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 2, 1])
	access = 2
	columns = {'sdlcLSOperName': sdlcLSOperName, 'sdlcLSOperRole': sdlcLSOperRole, 'sdlcLSOperState': sdlcLSOperState, 'sdlcLSOperMAXDATASend': sdlcLSOperMAXDATASend, 'sdlcLSOperREPLYTO': sdlcLSOperREPLYTO, 'sdlcLSOperMAXIN': sdlcLSOperMAXIN, 'sdlcLSOperMAXOUT': sdlcLSOperMAXOUT, 'sdlcLSOperMODULO': sdlcLSOperMODULO, 'sdlcLSOperRETRIESm': sdlcLSOperRETRIESm, 'sdlcLSOperRETRIESt': sdlcLSOperRETRIESt, 'sdlcLSOperRETRIESn': sdlcLSOperRETRIESn, 'sdlcLSOperRNRLIMIT': sdlcLSOperRNRLIMIT, 'sdlcLSOperDATMODE': sdlcLSOperDATMODE, 'sdlcLSOperLastModifyTime': sdlcLSOperLastModifyTime, 'sdlcLSOperLastFailTime': sdlcLSOperLastFailTime, 'sdlcLSOperLastFailCause': sdlcLSOperLastFailCause, 'sdlcLSOperLastFailCtrlIn': sdlcLSOperLastFailCtrlIn, 'sdlcLSOperLastFailCtrlOut': sdlcLSOperLastFailCtrlOut, 'sdlcLSOperLastFailFRMRInfo': sdlcLSOperLastFailFRMRInfo, 'sdlcLSOperLastFailREPLYTOs': sdlcLSOperLastFailREPLYTOs, 'sdlcLSOperEcho': sdlcLSOperEcho, 'sdlcLSOperGPoll': sdlcLSOperGPoll, 'sdlcLSOperSimRim': sdlcLSOperSimRim, 'sdlcLSOperXmitRcvCap': sdlcLSOperXmitRcvCap}


class sdlcLSStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, sdlcLSAddress], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 2, 3, 1])
	access = 2
	columns = {'sdlcLSStatsBLUsIn': sdlcLSStatsBLUsIn, 'sdlcLSStatsBLUsOut': sdlcLSStatsBLUsOut, 'sdlcLSStatsOctetsIn': sdlcLSStatsOctetsIn, 'sdlcLSStatsOctetsOut': sdlcLSStatsOctetsOut, 'sdlcLSStatsPollsIn': sdlcLSStatsPollsIn, 'sdlcLSStatsPollsOut': sdlcLSStatsPollsOut, 'sdlcLSStatsPollRspsOut': sdlcLSStatsPollRspsOut, 'sdlcLSStatsPollRspsIn': sdlcLSStatsPollRspsIn, 'sdlcLSStatsLocalBusies': sdlcLSStatsLocalBusies, 'sdlcLSStatsRemoteBusies': sdlcLSStatsRemoteBusies, 'sdlcLSStatsIFramesIn': sdlcLSStatsIFramesIn, 'sdlcLSStatsIFramesOut': sdlcLSStatsIFramesOut, 'sdlcLSStatsUIFramesIn': sdlcLSStatsUIFramesIn, 'sdlcLSStatsUIFramesOut': sdlcLSStatsUIFramesOut, 'sdlcLSStatsXIDsIn': sdlcLSStatsXIDsIn, 'sdlcLSStatsXIDsOut': sdlcLSStatsXIDsOut, 'sdlcLSStatsTESTsIn': sdlcLSStatsTESTsIn, 'sdlcLSStatsTESTsOut': sdlcLSStatsTESTsOut, 'sdlcLSStatsREJsIn': sdlcLSStatsREJsIn, 'sdlcLSStatsREJsOut': sdlcLSStatsREJsOut, 'sdlcLSStatsFRMRsIn': sdlcLSStatsFRMRsIn, 'sdlcLSStatsFRMRsOut': sdlcLSStatsFRMRsOut, 'sdlcLSStatsSIMsIn': sdlcLSStatsSIMsIn, 'sdlcLSStatsSIMsOut': sdlcLSStatsSIMsOut, 'sdlcLSStatsRIMsIn': sdlcLSStatsRIMsIn, 'sdlcLSStatsRIMsOut': sdlcLSStatsRIMsOut, 'sdlcLSStatsDISCIn': sdlcLSStatsDISCIn, 'sdlcLSStatsDISCOut': sdlcLSStatsDISCOut, 'sdlcLSStatsUAIn': sdlcLSStatsUAIn, 'sdlcLSStatsUAOut': sdlcLSStatsUAOut, 'sdlcLSStatsDMIn': sdlcLSStatsDMIn, 'sdlcLSStatsDMOut': sdlcLSStatsDMOut, 'sdlcLSStatsSNRMIn': sdlcLSStatsSNRMIn, 'sdlcLSStatsSNRMOut': sdlcLSStatsSNRMOut, 'sdlcLSStatsProtocolErrs': sdlcLSStatsProtocolErrs, 'sdlcLSStatsActivityTOs': sdlcLSStatsActivityTOs, 'sdlcLSStatsRNRLIMITs': sdlcLSStatsRNRLIMITs, 'sdlcLSStatsRetriesExps': sdlcLSStatsRetriesExps, 'sdlcLSStatsRetransmitsIn': sdlcLSStatsRetransmitsIn, 'sdlcLSStatsRetransmitsOut': sdlcLSStatsRetransmitsOut}


# notifications (traps) 
class sdlcPortStatusChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 3, 1])

class sdlcLSStatusChange(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 3, 2])

# groups 
class sdlcCorePortAdminGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 1])
	group = [sdlcPortAdminName, sdlcPortAdminRole, sdlcPortAdminType, sdlcPortAdminTopology, sdlcPortAdminISTATUS]

class sdlcCorePortOperGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 2])
	group = [sdlcPortOperName, sdlcPortOperRole, sdlcPortOperType, sdlcPortOperTopology, sdlcPortOperISTATUS, sdlcPortOperACTIVTO, sdlcPortOperLastFailTime, sdlcPortOperLastFailCause]

class sdlcCorePortStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 3])
	group = [sdlcPortStatsPhysicalFailures, sdlcPortStatsInvalidAddresses, sdlcPortStatsDwarfFrames]

class sdlcCoreLSAdminGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 4])
	group = [sdlcLSAddress, sdlcLSAdminName, sdlcLSAdminState, sdlcLSAdminISTATUS, sdlcLSAdminMAXDATASend, sdlcLSAdminMAXDATARcv, sdlcLSAdminMAXIN, sdlcLSAdminMAXOUT, sdlcLSAdminMODULO, sdlcLSAdminRETRIESm, sdlcLSAdminRETRIESt, sdlcLSAdminRETRIESn, sdlcLSAdminRNRLIMIT, sdlcLSAdminDATMODE, sdlcLSAdminGPoll, sdlcLSAdminSimRim, sdlcLSAdminRowStatus]

class sdlcCoreLSOperGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 5])
	group = [sdlcLSOperRole, sdlcLSOperState, sdlcLSOperMAXDATASend, sdlcLSOperMAXIN, sdlcLSOperMAXOUT, sdlcLSOperMODULO, sdlcLSOperRETRIESm, sdlcLSOperRETRIESt, sdlcLSOperRETRIESn, sdlcLSOperRNRLIMIT, sdlcLSOperDATMODE, sdlcLSOperLastFailTime, sdlcLSOperLastFailCause, sdlcLSOperLastFailCtrlIn, sdlcLSOperLastFailCtrlOut, sdlcLSOperLastFailFRMRInfo, sdlcLSOperLastFailREPLYTOs, sdlcLSOperEcho, sdlcLSOperGPoll]

class sdlcCoreLSStatsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 1, 6])
	group = [sdlcLSStatsBLUsIn, sdlcLSStatsBLUsOut, sdlcLSStatsOctetsIn, sdlcLSStatsOctetsOut, sdlcLSStatsPollsIn, sdlcLSStatsPollsOut, sdlcLSStatsPollRspsIn, sdlcLSStatsPollRspsOut, sdlcLSStatsLocalBusies, sdlcLSStatsRemoteBusies, sdlcLSStatsIFramesIn, sdlcLSStatsIFramesOut, sdlcLSStatsRetransmitsIn, sdlcLSStatsRetransmitsOut, sdlcLSStatsUIFramesIn, sdlcLSStatsUIFramesOut, sdlcLSStatsXIDsIn, sdlcLSStatsXIDsOut, sdlcLSStatsTESTsIn, sdlcLSStatsTESTsOut, sdlcLSStatsREJsIn, sdlcLSStatsREJsOut, sdlcLSStatsFRMRsIn, sdlcLSStatsFRMRsOut, sdlcLSStatsSIMsIn, sdlcLSStatsSIMsOut, sdlcLSStatsRIMsIn, sdlcLSStatsRIMsOut, sdlcLSStatsProtocolErrs, sdlcLSStatsRNRLIMITs, sdlcLSStatsRetriesExps]

class sdlcPrimaryGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 1])
	group = [sdlcPortAdminPAUSE, sdlcPortOperPAUSE, sdlcLSAdminREPLYTO, sdlcLSOperREPLYTO]

class sdlcPrimaryMultipointGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 41, 1, 4, 2, 2, 2])
	group = [sdlcPortAdminSERVLIM, sdlcPortAdminSlowPollTimer, sdlcPortOperSlowPollMethod, sdlcPortOperSERVLIM, sdlcPortOperSlowPollTimer]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
