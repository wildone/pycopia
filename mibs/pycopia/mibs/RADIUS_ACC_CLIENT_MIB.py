# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, OBJECT_IDENTITY, Counter32, Integer32, Gauge32, IpAddress, TimeTicks, mib_2
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from INET_ADDRESS_MIB import InetAddressType, InetAddress, InetPortNumber
from SNMP_FRAMEWORK_MIB import SnmpAdminString

class RADIUS_ACC_CLIENT_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/RADIUS-ACC-CLIENT-MIB'
	conformance = 4
	name = 'RADIUS-ACC-CLIENT-MIB'
	language = 2
	description = 'The MIB module for entities implementing the client\nside of the Remote Authentication Dial-In User Service\n(RADIUS) accounting protocol.  Copyright (C) The\nInternet Society (2006).  This version of this MIB\nmodule is part of RFC 4670; see the RFC itself for\nfull legal notices.'

# nodes
class radiusMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67])
	name = 'radiusMIB'

class radiusAccounting(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2])
	name = 'radiusAccounting'

class radiusAccClientMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2])
	name = 'radiusAccClientMIB'

class radiusAccClientMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1])
	name = 'radiusAccClientMIBObjects'

class radiusAccClient(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1])
	name = 'radiusAccClient'

class radiusAccClientMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 2])
	name = 'radiusAccClientMIBConformance'

class radiusAccClientMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 1])
	name = 'radiusAccClientMIBCompliances'

class radiusAccClientMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2])
	name = 'radiusAccClientMIBGroups'


# macros
# types 
# scalars 
class radiusAccClientInvalidServerAddresses(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientIdentifier(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 2])
	syntaxobject = SnmpAdminString


# columns
class radiusAccServerIndex(ColumnObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusAccServerAddress(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class radiusAccClientServerPortNumber(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusAccClientRoundTripTime(ColumnObject):
	access = 4
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class radiusAccClientRequests(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientRetransmissions(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientResponses(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientMalformedResponses(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientBadAuthenticators(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientPendingRequests(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'packets'


class radiusAccClientTimeouts(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'timeouts'


class radiusAccClientUnknownTypes(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientPacketsDropped(ColumnObject):
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccServerExtIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class radiusAccServerInetAddressType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 2])
	syntaxobject = InetAddressType


class radiusAccServerInetAddress(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 3])
	syntaxobject = InetAddress


class radiusAccClientServerInetPortNumber(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 4])
	syntaxobject = InetPortNumber


class radiusAccClientExtRoundTripTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks


class radiusAccClientExtRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtRetransmissions(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtResponses(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtMalformedResponses(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtBadAuthenticators(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtPendingRequests(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'packets'


class radiusAccClientExtTimeouts(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'timeouts'


class radiusAccClientExtUnknownTypes(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientExtPacketsDropped(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Counter32
	access = 4
	units = 'packets'


class radiusAccClientCounterDiscontinuity(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.TimeTicks
	access = 4
	units = 'centiseconds'


# rows 
class radiusAccServerEntry(RowObject):
	status = 2
	index = pycopia.SMI.Objects.IndexObjects([radiusAccServerIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 3, 1])
	access = 2
	columns = {'radiusAccServerIndex': radiusAccServerIndex, 'radiusAccServerAddress': radiusAccServerAddress, 'radiusAccClientServerPortNumber': radiusAccClientServerPortNumber, 'radiusAccClientRoundTripTime': radiusAccClientRoundTripTime, 'radiusAccClientRequests': radiusAccClientRequests, 'radiusAccClientRetransmissions': radiusAccClientRetransmissions, 'radiusAccClientResponses': radiusAccClientResponses, 'radiusAccClientMalformedResponses': radiusAccClientMalformedResponses, 'radiusAccClientBadAuthenticators': radiusAccClientBadAuthenticators, 'radiusAccClientPendingRequests': radiusAccClientPendingRequests, 'radiusAccClientTimeouts': radiusAccClientTimeouts, 'radiusAccClientUnknownTypes': radiusAccClientUnknownTypes, 'radiusAccClientPacketsDropped': radiusAccClientPacketsDropped}


class radiusAccServerExtEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([radiusAccServerExtIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 1, 1, 4, 1])
	access = 2
	columns = {'radiusAccServerExtIndex': radiusAccServerExtIndex, 'radiusAccServerInetAddressType': radiusAccServerInetAddressType, 'radiusAccServerInetAddress': radiusAccServerInetAddress, 'radiusAccClientServerInetPortNumber': radiusAccClientServerInetPortNumber, 'radiusAccClientExtRoundTripTime': radiusAccClientExtRoundTripTime, 'radiusAccClientExtRequests': radiusAccClientExtRequests, 'radiusAccClientExtRetransmissions': radiusAccClientExtRetransmissions, 'radiusAccClientExtResponses': radiusAccClientExtResponses, 'radiusAccClientExtMalformedResponses': radiusAccClientExtMalformedResponses, 'radiusAccClientExtBadAuthenticators': radiusAccClientExtBadAuthenticators, 'radiusAccClientExtPendingRequests': radiusAccClientExtPendingRequests, 'radiusAccClientExtTimeouts': radiusAccClientExtTimeouts, 'radiusAccClientExtUnknownTypes': radiusAccClientExtUnknownTypes, 'radiusAccClientExtPacketsDropped': radiusAccClientExtPacketsDropped, 'radiusAccClientCounterDiscontinuity': radiusAccClientCounterDiscontinuity}


# notifications (traps) 
# groups 
class radiusAccClientMIBGroup(GroupObject):
	access = 2
	status = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 1])
	group = [radiusAccClientIdentifier, radiusAccClientInvalidServerAddresses, radiusAccServerAddress, radiusAccClientServerPortNumber, radiusAccClientRoundTripTime, radiusAccClientRequests, radiusAccClientRetransmissions, radiusAccClientResponses, radiusAccClientMalformedResponses, radiusAccClientBadAuthenticators, radiusAccClientPendingRequests, radiusAccClientTimeouts, radiusAccClientUnknownTypes, radiusAccClientPacketsDropped]

class radiusAccClientExtMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 67, 2, 2, 2, 2, 2])
	group = [radiusAccClientIdentifier, radiusAccClientInvalidServerAddresses, radiusAccServerInetAddressType, radiusAccServerInetAddress, radiusAccClientServerInetPortNumber, radiusAccClientExtRoundTripTime, radiusAccClientExtRequests, radiusAccClientExtRetransmissions, radiusAccClientExtResponses, radiusAccClientExtMalformedResponses, radiusAccClientExtBadAuthenticators, radiusAccClientExtPendingRequests, radiusAccClientExtTimeouts, radiusAccClientExtUnknownTypes, radiusAccClientExtPacketsDropped, radiusAccClientCounterDiscontinuity]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
