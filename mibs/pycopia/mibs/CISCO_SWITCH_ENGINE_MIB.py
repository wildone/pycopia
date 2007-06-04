# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from ENTITY_MIB import entPhysicalIndex
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Gauge32, Counter32, Counter64, Integer32, IpAddress
from CISCO_TC import CiscoNetworkProtocol, Unsigned32
from CISCO_SMI import ciscoMgmt
from IF_MIB import ifIndex, OwnerString
from CISCO_VTP_MIB import VlanIndex
from SNMPv2_TC import TEXTUAL_CONVENTION, DisplayString, RowStatus, TimeInterval, MacAddress, TruthValue, TimeStamp

class CISCO_SWITCH_ENGINE_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-SWITCH-ENGINE-MIB'
	conformance = 3
	name = 'CISCO-SWITCH-ENGINE-MIB'
	language = 2
	description = "This MIB module defines management objects for Cisco Layer 2/3 switches. \nThese devices may either have a single (central) switching engine\nentity or may consist of multiple (distributed) switching engine \nentities which are inter-connected via a common 'switching fabric'. \nIn the central switching engine model, all the physical ports in the \nsystem are handled by the only switching engine in the system.  In \nthe distributed switching model, each switching engine will handle a \nset of 'local' physical ports and when necessary, packets are also \nswitched between switching engines over the switching fabric.\n\nCisco L2/L3 switching devices use regular routers to assist them\nin learning packet 'flows' by observing how a router routes a\ncandidate flow.  A flow is some combination of source network address,\ndestination network address and the transport port numbers, as\napplicable.  Once a flow is established (learned), all traffic\nbelonging to that flow will be switched at Layer 3 by the switch\nengine, effectively bypassing the router, until the flow has been\n'aged' out. Most Cisco L2/L3 switching devices employ built-in\n(internal) router module(s) for integrating Layer 3 switching with\nLayer 2 forwarding. However, they can also learn 'flows' through\nother physically-sepapate (external) Cisco routers that are\nconnected to the switch-engine through the network."

# nodes
class ciscoSwitchEngineMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97])
	name = 'ciscoSwitchEngineMIB'

class cseMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1])
	name = 'cseMIBObjects'

class cseL2Objects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1])
	name = 'cseL2Objects'

class cseFlow(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2])
	name = 'cseFlow'

class cseNetflowLS(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3])
	name = 'cseNetflowLS'

class cseL3Objects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4])
	name = 'cseL3Objects'

class cseProtocolFilter(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5])
	name = 'cseProtocolFilter'

class cseMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 2])
	name = 'cseMIBNotifications'

class cseMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3])
	name = 'cseMIBConformance'

class cseMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 1])
	name = 'cseMIBCompliances'

class cseMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2])
	name = 'cseMIBGroups'


# macros
# types 

class CiscoGauge64(pycopia.SMI.Basetypes.Counter64):
	status = 1


class ControlStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


class FlowAddressComponent(pycopia.SMI.Basetypes.OctetString):
	status = 1
	ranges = Ranges(Range(6, 6), Range(10, 10))
	format = '1x:'

# scalars 
class cseFlowEstablishedAgingTime(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class cseFlowFastAgingTime(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'seconds'


class cseFlowFastAgePktThreshold(ScalarObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'packets'


class cseFlowMaxQueries(ScalarObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 7])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cseNetflowLSExportStatus(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 1])
	syntaxobject = ControlStatus


class cseNetflowLSExportHost(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 2])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cseNetflowLSExportTransportNumber(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cseNetflowLSExportDataSource(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 4])
	syntaxobject = FlowAddressComponent


class cseNetflowLSExportDataSourceMask(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 5])
	syntaxobject = FlowAddressComponent


class cseNetflowLSExportDataDest(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 6])
	syntaxobject = FlowAddressComponent


class cseNetflowLSExportDataDestMask(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 3, 7])
	syntaxobject = FlowAddressComponent


# columns
class cseL2ForwardedLocalPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2ForwardedLocalOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseL2ForwardedTotalPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2NewAddressLearns(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2AddrLearnFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2DstAddrLookupMisses(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2IpPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2IpxPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2AssignedProtoPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL2OtherProtoPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseRouterIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cseRouterFlowMask(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dstOnly'), Enum(2, 'srcDst'), Enum(3, 'fullFlow')]


class cseRouterName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cseRouterStatic(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cseStaticRouterName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class cseStaticRouterOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 2])
	syntaxobject = OwnerString


class cseStaticRouterStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cseRouterMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class cseRouterVlan(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 2])
	syntaxobject = VlanIndex


class cseRouterProtocol(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cseFlowQueryIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cseFlowQueryMask(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'dstOnly'), Enum(2, 'srcOrDst'), Enum(3, 'srcAndDst'), Enum(4, 'fullFlow'), Enum(5, 'ipxDstOnly'), Enum(6, 'ipxSrcAndDst'), Enum(7, 'any')]


class cseFlowQueryTransport(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class cseFlowQuerySource(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 4])
	syntaxobject = FlowAddressComponent


class cseFlowQuerySourceMask(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 5])
	syntaxobject = FlowAddressComponent


class cseFlowQueryDestination(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 6])
	syntaxobject = FlowAddressComponent


class cseFlowQueryDestinationMask(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 7])
	syntaxobject = FlowAddressComponent


class cseFlowQueryRouterIndex(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.IpAddress


class cseFlowQueryOwner(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 9])
	syntaxobject = OwnerString


class cseFlowQueryResultingRows(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cseFlowQueryResultTotalPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 11])
	syntaxobject = CiscoGauge64


class cseFlowQueryResultTotalOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 12])
	syntaxobject = CiscoGauge64


class cseFlowQueryResultAvgDuration(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class cseFlowQueryResultAvgIdle(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.TimeInterval


class cseFlowQueryStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class cseFlowQueryCreateTime(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cseFlowDataIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class cseFlowDataSrcMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class cseFlowDataDstMac(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.MacAddress


class cseFlowDataStaticFlow(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class cseFlowDataEncapType(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ipArpa'), Enum(2, 'ipxEthernet'), Enum(3, 'ipx802raw'), Enum(4, 'ipx802sap'), Enum(5, 'ipx802snap'), Enum(6, 'other')]


class cseFlowDataSource(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 6])
	syntaxobject = FlowAddressComponent


class cseFlowDataDestination(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 7])
	syntaxobject = FlowAddressComponent


class cseFlowDataDestVlan(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 8])
	syntaxobject = VlanIndex


class cseFlowDataIpQOS(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cseFlowDataIpQOSPolicy(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class cseFlowDataWhenCreated(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cseFlowDataLastUsed(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class cseFlowDataPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cseFlowDataOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1, 14])
	syntaxobject = CiscoGauge64


class cseFlowSwitchProtocol(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1, 1])
	syntaxobject = CiscoNetworkProtocol


class cseFlowSwitchStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1, 2])
	syntaxobject = ControlStatus


class cseL3SwitchedTotalPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3SwitchedTotalOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseL3CandidateFlowHits(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3EstablishedFlowHits(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3ActiveFlows(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class cseL3FlowLearnFailures(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3IntFlowInvalids(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3ExtFlowInvalids(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class cseL3VlanIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 1])
	syntaxobject = VlanIndex


class cseL3VlanInPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseL3VlanInOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseL3VlanOutPkts(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseL3VlanOutOctets(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter64


class cseProtocolFilterPortProtocol(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'ip'), Enum(2, 'ipx'), Enum(3, 'grpProtocols')]


class cseProtocolFilterPortAdminStatus(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'on'), Enum(2, 'off'), Enum(3, 'auto')]


class cseProtocolFilterPortOperStatus(ColumnObject):
	status = 1
	access = 4
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'on'), Enum(2, 'off'), Enum(3, 'notSupported')]


# rows 
class cseL2StatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 1, 1, 1])
	access = 2
	columns = {'cseL2ForwardedLocalPkts': cseL2ForwardedLocalPkts, 'cseL2ForwardedLocalOctets': cseL2ForwardedLocalOctets, 'cseL2ForwardedTotalPkts': cseL2ForwardedTotalPkts, 'cseL2NewAddressLearns': cseL2NewAddressLearns, 'cseL2AddrLearnFailures': cseL2AddrLearnFailures, 'cseL2DstAddrLookupMisses': cseL2DstAddrLookupMisses, 'cseL2IpPkts': cseL2IpPkts, 'cseL2IpxPkts': cseL2IpxPkts, 'cseL2AssignedProtoPkts': cseL2AssignedProtoPkts, 'cseL2OtherProtoPkts': cseL2OtherProtoPkts}


class cseRouterEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cseRouterIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 4, 1])
	access = 2
	columns = {'cseRouterIndex': cseRouterIndex, 'cseRouterFlowMask': cseRouterFlowMask, 'cseRouterName': cseRouterName, 'cseRouterStatic': cseRouterStatic}


class cseStaticExtRouterEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cseRouterIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 5, 1])
	access = 2
	rowstatus = cseStaticRouterStatus
	columns = {'cseStaticRouterName': cseStaticRouterName, 'cseStaticRouterOwner': cseStaticRouterOwner, 'cseStaticRouterStatus': cseStaticRouterStatus}


class cseRouterVlanEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cseRouterIndex, cseRouterMac, cseRouterVlan], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 6, 1])
	access = 2
	columns = {'cseRouterMac': cseRouterMac, 'cseRouterVlan': cseRouterVlan, 'cseRouterProtocol': cseRouterProtocol}


class cseFlowQueryEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex, cseFlowQueryIndex], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 8, 1])
	access = 2
	rowstatus = cseFlowQueryStatus
	columns = {'cseFlowQueryIndex': cseFlowQueryIndex, 'cseFlowQueryMask': cseFlowQueryMask, 'cseFlowQueryTransport': cseFlowQueryTransport, 'cseFlowQuerySource': cseFlowQuerySource, 'cseFlowQuerySourceMask': cseFlowQuerySourceMask, 'cseFlowQueryDestination': cseFlowQueryDestination, 'cseFlowQueryDestinationMask': cseFlowQueryDestinationMask, 'cseFlowQueryRouterIndex': cseFlowQueryRouterIndex, 'cseFlowQueryOwner': cseFlowQueryOwner, 'cseFlowQueryResultingRows': cseFlowQueryResultingRows, 'cseFlowQueryResultTotalPkts': cseFlowQueryResultTotalPkts, 'cseFlowQueryResultTotalOctets': cseFlowQueryResultTotalOctets, 'cseFlowQueryResultAvgDuration': cseFlowQueryResultAvgDuration, 'cseFlowQueryResultAvgIdle': cseFlowQueryResultAvgIdle, 'cseFlowQueryStatus': cseFlowQueryStatus, 'cseFlowQueryCreateTime': cseFlowQueryCreateTime}


class cseFlowDataEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex, cseFlowQueryIndex, cseFlowDataIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 9, 1])
	access = 2
	columns = {'cseFlowDataIndex': cseFlowDataIndex, 'cseFlowDataSrcMac': cseFlowDataSrcMac, 'cseFlowDataDstMac': cseFlowDataDstMac, 'cseFlowDataStaticFlow': cseFlowDataStaticFlow, 'cseFlowDataEncapType': cseFlowDataEncapType, 'cseFlowDataSource': cseFlowDataSource, 'cseFlowDataDestination': cseFlowDataDestination, 'cseFlowDataDestVlan': cseFlowDataDestVlan, 'cseFlowDataIpQOS': cseFlowDataIpQOS, 'cseFlowDataIpQOSPolicy': cseFlowDataIpQOSPolicy, 'cseFlowDataWhenCreated': cseFlowDataWhenCreated, 'cseFlowDataLastUsed': cseFlowDataLastUsed, 'cseFlowDataPkts': cseFlowDataPkts, 'cseFlowDataOctets': cseFlowDataOctets}


class cseFlowSwitchControlEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([cseFlowSwitchProtocol], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 2, 10, 1])
	access = 2
	columns = {'cseFlowSwitchProtocol': cseFlowSwitchProtocol, 'cseFlowSwitchStatus': cseFlowSwitchStatus}


class cseL3StatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 1, 1])
	access = 2
	columns = {'cseL3SwitchedTotalPkts': cseL3SwitchedTotalPkts, 'cseL3SwitchedTotalOctets': cseL3SwitchedTotalOctets, 'cseL3CandidateFlowHits': cseL3CandidateFlowHits, 'cseL3EstablishedFlowHits': cseL3EstablishedFlowHits, 'cseL3ActiveFlows': cseL3ActiveFlows, 'cseL3FlowLearnFailures': cseL3FlowLearnFailures, 'cseL3IntFlowInvalids': cseL3IntFlowInvalids, 'cseL3ExtFlowInvalids': cseL3ExtFlowInvalids}


class cseL3VlanStatsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex, cseL3VlanIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 4, 2, 1])
	access = 2
	columns = {'cseL3VlanIndex': cseL3VlanIndex, 'cseL3VlanInPkts': cseL3VlanInPkts, 'cseL3VlanInOctets': cseL3VlanInOctets, 'cseL3VlanOutPkts': cseL3VlanOutPkts, 'cseL3VlanOutOctets': cseL3VlanOutOctets}


class cseProtocolFilterPortEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, cseProtocolFilterPortProtocol], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 1, 5, 2, 1])
	access = 2
	columns = {'cseProtocolFilterPortProtocol': cseProtocolFilterPortProtocol, 'cseProtocolFilterPortAdminStatus': cseProtocolFilterPortAdminStatus, 'cseProtocolFilterPortOperStatus': cseProtocolFilterPortOperStatus}


# notifications (traps) 
# groups 
class cseStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 1])
	group = [cseL2ForwardedLocalPkts, cseL2ForwardedLocalOctets, cseL2ForwardedTotalPkts, cseL2NewAddressLearns, cseL2AddrLearnFailures, cseL2DstAddrLookupMisses, cseL3SwitchedTotalPkts, cseL3SwitchedTotalOctets, cseL3CandidateFlowHits, cseL3EstablishedFlowHits, cseL3ActiveFlows, cseL3FlowLearnFailures, cseL3IntFlowInvalids, cseL3ExtFlowInvalids]

class cseVlanStatisticsGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 2])
	group = [cseL3VlanInPkts, cseL3VlanInOctets, cseL3VlanOutPkts, cseL3VlanOutOctets]

class cseRouterGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 3])
	group = [cseRouterFlowMask, cseRouterName, cseRouterStatic, cseStaticRouterOwner, cseStaticRouterName, cseStaticRouterStatus, cseRouterMac, cseRouterProtocol]

class cseFlowMgmtGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 4])
	group = [cseFlowEstablishedAgingTime, cseFlowFastAgingTime, cseFlowFastAgePktThreshold, cseFlowMaxQueries, cseFlowQueryMask, cseFlowQueryTransport, cseFlowQuerySource, cseFlowQuerySourceMask, cseFlowQueryDestination, cseFlowQueryDestinationMask, cseFlowQueryRouterIndex, cseFlowQueryOwner, cseFlowQueryResultingRows, cseFlowQueryResultTotalPkts, cseFlowQueryResultTotalOctets, cseFlowQueryResultAvgDuration, cseFlowQueryResultAvgIdle, cseFlowQueryStatus, cseFlowQueryCreateTime, cseFlowDataSrcMac, cseFlowDataDstMac, cseFlowDataEncapType, cseFlowDataSource, cseFlowDataStaticFlow, cseFlowDataDestination, cseFlowDataDestVlan, cseFlowDataIpQOS, cseFlowDataIpQOSPolicy, cseFlowDataWhenCreated, cseFlowDataLastUsed, cseFlowDataPkts, cseFlowDataOctets, cseFlowSwitchStatus]

class cseNetflowLSGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 5])
	group = [cseNetflowLSExportHost, cseNetflowLSExportTransportNumber, cseNetflowLSExportStatus, cseNetflowLSExportDataSource, cseNetflowLSExportDataSourceMask, cseNetflowLSExportDataDest, cseNetflowLSExportDataDestMask]

class cseProtocolFilterGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 97, 3, 2, 6])
	group = [cseProtocolFilterPortAdminStatus, cseProtocolFilterPortOperStatus, cseL2IpPkts, cseL2IpxPkts, cseL2AssignedProtoPkts, cseL2OtherProtoPkts]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
