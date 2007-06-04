# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, Counter32, Gauge32
from CISCO_TC import Unsigned32
from CISCO_SMI import ciscoExperiment
from RFC1213_MIB import ifIndex
from SNMPv2_TC import TEXTUAL_CONVENTION, DisplayString

class CISCO_ATM_RM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ATM-RM-MIB'
	conformance = 2
	name = 'CISCO-ATM-RM-MIB'
	language = 2
	description = 'The MIB module which complements standard ATM MIBs for\nCisco devices, for Resource Management.'

# nodes
class ciscoAtmRmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10])
	name = 'ciscoAtmRmMIB'

class ciscoAtmRmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1])
	name = 'ciscoAtmRmMIBObjects'

class ciscoAtmRmSwitchCfg(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1])
	name = 'ciscoAtmRmSwitchCfg'

class ciscoAtmRmSwitchSharedMem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2])
	name = 'ciscoAtmRmSwitchSharedMem'

class ciscoAtmRmIfCfg(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3])
	name = 'ciscoAtmRmIfCfg'

class ciscoAtmRmIfState(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4])
	name = 'ciscoAtmRmIfState'

class ciscoAtmRmIfStatistics(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5])
	name = 'ciscoAtmRmIfStatistics'

class ciscoAtmRmIfSharedMem(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6])
	name = 'ciscoAtmRmIfSharedMem'

class ciscoLsPerVcqAtmRmSwitch(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7])
	name = 'ciscoLsPerVcqAtmRmSwitch'

class ciscoLsPerVcqAtmRmIf(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8])
	name = 'ciscoLsPerVcqAtmRmIf'

class ciscoAtmRmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3])
	name = 'ciscoAtmRmMIBConformance'

class ciscoAtmRmMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 1])
	name = 'ciscoAtmRmMIBCompliances'

class ciscoAtmRmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2])
	name = 'ciscoAtmRmMIBGroups'


# macros
# types 

class ForceValue(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'forceChange'), Enum(2, 'noForceChange')]


class FineQueueThreshold(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'percent12'), Enum(2, 'percent25'), Enum(3, 'percent37'), Enum(4, 'percent50'), Enum(5, 'percent62'), Enum(6, 'percent75'), Enum(7, 'percent87'), Enum(8, 'percent100')]


class LsPerVcqServiceClass(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'c1'), Enum(2, 'c2'), Enum(3, 'c3'), Enum(4, 'c4'), Enum(5, 'c5'), Enum(6, 'c6'), Enum(7, 'c7'), Enum(8, 'c8')]


class LsPerVcqServiceClassNoC1(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(2, 'c2'), Enum(3, 'c3'), Enum(4, 'c4'), Enum(5, 'c5'), Enum(6, 'c6'), Enum(7, 'c7'), Enum(8, 'c8')]


class LsPerVcqThresholdGroup(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'tg1'), Enum(2, 'tg2'), Enum(3, 'tg3'), Enum(4, 'tg4'), Enum(5, 'tg5'), Enum(6, 'tg6'), Enum(7, 'tg7'), Enum(8, 'tg8'), Enum(9, 'tg9'), Enum(10, 'tg10'), Enum(11, 'tg11'), Enum(12, 'tg12'), Enum(13, 'tg13'), Enum(14, 'tg14'), Enum(15, 'tg15'), Enum(16, 'tg16')]


class LsPerVcqThresholdGroupService(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'cbr'), Enum(2, 'vbrRt'), Enum(3, 'vbrNrt'), Enum(4, 'abr'), Enum(5, 'ubr')]

# scalars 
class rmSwitchOverSubFactor(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmSwitchScrMarginFactor(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmSwitchAbrCongNotify(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'relativeRate'), Enum(2, 'efci'), Enum(3, 'efciAndRelativeRate')]


class lsPerVcqRmHierarchicalSchedulingMode(ScalarObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 3])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'enabled'), Enum(2, 'disabled')]


# columns
class rmDefaultQosServiceCategory(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'cbr'), Enum(2, 'vbrRt'), Enum(3, 'vbrNrt')]


class rmScDefaultQosMaxCtd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'microseconds'


class rmScDefaultQosPeakToPeakCdv(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'microseconds'


class rmScDefaultQosClr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmScDefaultQosClrClp01(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sharedMemRmCellPriority(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'p1'), Enum(2, 'p2'), Enum(3, 'p3'), Enum(4, 'p4')]


class sharedMemRmSwitchQueuedCellLimit(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'cells'


class sharedMemRmSwitchQueuedCellCount(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells'


class rmIfOutPacingRateRequested(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'kilobits-per-second'


class rmIfOutPacingRateInstalled(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 4
	units = 'kilobits-per-second'


class rmIfOutPacingForce(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 3])
	syntaxobject = ForceValue


class rmIfLinkDistance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'kilometers'


class rmIfBestEffortLimit(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32


class rmIfCbrDefaultRxUpcTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfVbrRtDefaultRxUpcTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfVbrNrtDefaultRxUpcTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfAbrDefaultRxUpcTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfUbrDefaultRxUpcTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfVbrRtDefaultRxUpcCdvt(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfVbrNrtDefaultRxUpcCdvt(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfServCategorySupport(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirection(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'receive'), Enum(2, 'transmit')]


class rmIfDirControlLinkShareMaxAgg(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMinCbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMaxCbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMinVbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMaxVbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirMaxCbrPcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxCbrTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfDirMaxVbrPcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxVbrScr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxVbrTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfDirMaxAbrPcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 12])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxAbrTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 13])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfDirMaxUbrPcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 14])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxUbrTolerance(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 15])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfDirMaxAbrMcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 16])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxUbrMcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 17])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cells-per-second'


class rmIfDirMaxVbrCdvt(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 18])
	syntaxobject = pycopia.SMI.Basetypes.Unsigned32
	access = 5
	units = 'cell-times'


class rmIfDirControlLinkShareMinAbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 19])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMaxAbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 20])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMinUbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 21])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfDirControlLinkShareMaxUbr(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1, 22])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class rmIfSc(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'cbr'), Enum(2, 'vbrRt'), Enum(3, 'vbrNrt'), Enum(4, 'abr'), Enum(5, 'ubr')]


class rmIfScRxAcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells-per-second'


class rmIfScTxAcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells-per-second'


class rmIfScRxAlcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells-per-second'


class rmIfScTxAlcr(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells-per-second'


class rmIfScNumSvxConns(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'number of connections'


class rmIfScNumPvxConns(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'number of connections'


class rmIfScTxMaxCtd(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'microseconds'


class rmIfScTxP2PeakCdv(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'microseconds'


class rmIfScTxClr(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class rmIfScTxClrClp01(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1, 11])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32


class rmIfScRcacResultNumAdmit(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumTotalRequests(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailTraffComb(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailBw(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailLoss(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailDelay(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailCdv(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailBeLimit(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailParmLimit(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class rmIfScRcacResultNumFailOther(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1, 10])
	syntaxobject = pycopia.SMI.Basetypes.Counter32


class sharedMemRmIfOutputQ(ColumnObject):
	status = 1
	access = 2
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'q1'), Enum(2, 'q2'), Enum(3, 'q3'), Enum(4, 'q4')]


class sharedMemRmIfOutputQServCategory(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class sharedMemRmIfOutputQRequestedMaxSize(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'cells'


class sharedMemRmIfOutputQInstalledMaxSize(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 4
	units = 'cells'


class sharedMemRmIfOutputQMaxSizeForce(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 5])
	syntaxobject = ForceValue


class sharedMemRmIfOutputQCellCount(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells'


class sharedMemRmIfDiscardThreshold(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 1])
	syntaxobject = FineQueueThreshold


class sharedMemRmIfEfciThreshold(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'percent12'), Enum(2, 'percent25'), Enum(3, 'percent50'), Enum(4, 'percent100')]


class sharedMemRmIfAbrRelativeRateThreshold(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1, 3])
	syntaxobject = FineQueueThreshold


class lsPerVcqRmThreshGrp(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 1])
	syntaxobject = LsPerVcqThresholdGroup


class lsPerVcqRmThreshGrpMaxSize(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'cells'


class lsPerVcqRmThreshGrpQMaxSize(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'cells'


class lsPerVcqRmThreshGrpQMinSize(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'cells'


class lsPerVcqRmThreshGrpDiscThreshold(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'percentage'


class lsPerVcqRmThreshGrpMarkThreshold(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'percentage'


class lsPerVcqRmThreshGrpName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 7])
	syntaxobject = pycopia.SMI.Basetypes.DisplayString


class lsPerVcqRmThreshGrpCellCount(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.Gauge32
	access = 4
	units = 'cells'


class lsPerVcqRmThreshGrpService(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1, 1])
	syntaxobject = LsPerVcqThresholdGroupService


class lsPerVcqRmThreshGrpServGroup(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1, 2])
	syntaxobject = LsPerVcqThresholdGroup


class lsPerVcqRmIfMinWrrServiceClass(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 1, 1, 1])
	syntaxobject = LsPerVcqServiceClassNoC1
	access = 5
	units = 'service class'


class lsPerVcqRmIfServiceClass(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 1])
	syntaxobject = LsPerVcqServiceClass


class lsPerVcqRmIfServClassConnType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class lsPerVcqRmIfServClassWrrWeight(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.Integer32
	access = 5
	units = 'weight'


# rows 
class rmDefaultQosObjectiveEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([rmDefaultQosServiceCategory], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 1, 4, 1])
	access = 2
	columns = {'rmDefaultQosServiceCategory': rmDefaultQosServiceCategory, 'rmScDefaultQosMaxCtd': rmScDefaultQosMaxCtd, 'rmScDefaultQosPeakToPeakCdv': rmScDefaultQosPeakToPeakCdv, 'rmScDefaultQosClr': rmScDefaultQosClr, 'rmScDefaultQosClrClp01': rmScDefaultQosClrClp01}


class sharedMemRmSwitchQueuedCellEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([sharedMemRmCellPriority], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 2, 1, 1])
	access = 2
	columns = {'sharedMemRmCellPriority': sharedMemRmCellPriority, 'sharedMemRmSwitchQueuedCellLimit': sharedMemRmSwitchQueuedCellLimit, 'sharedMemRmSwitchQueuedCellCount': sharedMemRmSwitchQueuedCellCount}


class rmIfCfgEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 3, 1])
	access = 2
	columns = {'rmIfOutPacingRateRequested': rmIfOutPacingRateRequested, 'rmIfOutPacingRateInstalled': rmIfOutPacingRateInstalled, 'rmIfOutPacingForce': rmIfOutPacingForce, 'rmIfLinkDistance': rmIfLinkDistance, 'rmIfBestEffortLimit': rmIfBestEffortLimit, 'rmIfCbrDefaultRxUpcTolerance': rmIfCbrDefaultRxUpcTolerance, 'rmIfVbrRtDefaultRxUpcTolerance': rmIfVbrRtDefaultRxUpcTolerance, 'rmIfVbrNrtDefaultRxUpcTolerance': rmIfVbrNrtDefaultRxUpcTolerance, 'rmIfAbrDefaultRxUpcTolerance': rmIfAbrDefaultRxUpcTolerance, 'rmIfUbrDefaultRxUpcTolerance': rmIfUbrDefaultRxUpcTolerance, 'rmIfVbrRtDefaultRxUpcCdvt': rmIfVbrRtDefaultRxUpcCdvt, 'rmIfVbrNrtDefaultRxUpcCdvt': rmIfVbrNrtDefaultRxUpcCdvt, 'rmIfServCategorySupport': rmIfServCategorySupport}


class rmIfDirectionCfgEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, rmIfDirection], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 3, 4, 1])
	access = 2
	columns = {'rmIfDirection': rmIfDirection, 'rmIfDirControlLinkShareMaxAgg': rmIfDirControlLinkShareMaxAgg, 'rmIfDirControlLinkShareMinCbr': rmIfDirControlLinkShareMinCbr, 'rmIfDirControlLinkShareMaxCbr': rmIfDirControlLinkShareMaxCbr, 'rmIfDirControlLinkShareMinVbr': rmIfDirControlLinkShareMinVbr, 'rmIfDirControlLinkShareMaxVbr': rmIfDirControlLinkShareMaxVbr, 'rmIfDirMaxCbrPcr': rmIfDirMaxCbrPcr, 'rmIfDirMaxCbrTolerance': rmIfDirMaxCbrTolerance, 'rmIfDirMaxVbrPcr': rmIfDirMaxVbrPcr, 'rmIfDirMaxVbrScr': rmIfDirMaxVbrScr, 'rmIfDirMaxVbrTolerance': rmIfDirMaxVbrTolerance, 'rmIfDirMaxAbrPcr': rmIfDirMaxAbrPcr, 'rmIfDirMaxAbrTolerance': rmIfDirMaxAbrTolerance, 'rmIfDirMaxUbrPcr': rmIfDirMaxUbrPcr, 'rmIfDirMaxUbrTolerance': rmIfDirMaxUbrTolerance, 'rmIfDirMaxAbrMcr': rmIfDirMaxAbrMcr, 'rmIfDirMaxUbrMcr': rmIfDirMaxUbrMcr, 'rmIfDirMaxVbrCdvt': rmIfDirMaxVbrCdvt, 'rmIfDirControlLinkShareMinAbr': rmIfDirControlLinkShareMinAbr, 'rmIfDirControlLinkShareMaxAbr': rmIfDirControlLinkShareMaxAbr, 'rmIfDirControlLinkShareMinUbr': rmIfDirControlLinkShareMinUbr, 'rmIfDirControlLinkShareMaxUbr': rmIfDirControlLinkShareMaxUbr}


class rmIfServiceCategoryStateEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, rmIfSc], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 4, 1, 1])
	access = 2
	columns = {'rmIfSc': rmIfSc, 'rmIfScRxAcr': rmIfScRxAcr, 'rmIfScTxAcr': rmIfScTxAcr, 'rmIfScRxAlcr': rmIfScRxAlcr, 'rmIfScTxAlcr': rmIfScTxAlcr, 'rmIfScNumSvxConns': rmIfScNumSvxConns, 'rmIfScNumPvxConns': rmIfScNumPvxConns, 'rmIfScTxMaxCtd': rmIfScTxMaxCtd, 'rmIfScTxP2PeakCdv': rmIfScTxP2PeakCdv, 'rmIfScTxClr': rmIfScTxClr, 'rmIfScTxClrClp01': rmIfScTxClrClp01}


class rmIfServiceCategoryStatisticsEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, rmIfSc], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 5, 1, 1])
	access = 2
	columns = {'rmIfScRcacResultNumAdmit': rmIfScRcacResultNumAdmit, 'rmIfScRcacResultNumTotalRequests': rmIfScRcacResultNumTotalRequests, 'rmIfScRcacResultNumFailTraffComb': rmIfScRcacResultNumFailTraffComb, 'rmIfScRcacResultNumFailBw': rmIfScRcacResultNumFailBw, 'rmIfScRcacResultNumFailLoss': rmIfScRcacResultNumFailLoss, 'rmIfScRcacResultNumFailDelay': rmIfScRcacResultNumFailDelay, 'rmIfScRcacResultNumFailCdv': rmIfScRcacResultNumFailCdv, 'rmIfScRcacResultNumFailBeLimit': rmIfScRcacResultNumFailBeLimit, 'rmIfScRcacResultNumFailParmLimit': rmIfScRcacResultNumFailParmLimit, 'rmIfScRcacResultNumFailOther': rmIfScRcacResultNumFailOther}


class sharedMemRmIfOutputQCfgEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, sharedMemRmIfOutputQ], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 1, 1])
	access = 2
	columns = {'sharedMemRmIfOutputQ': sharedMemRmIfOutputQ, 'sharedMemRmIfOutputQServCategory': sharedMemRmIfOutputQServCategory, 'sharedMemRmIfOutputQRequestedMaxSize': sharedMemRmIfOutputQRequestedMaxSize, 'sharedMemRmIfOutputQInstalledMaxSize': sharedMemRmIfOutputQInstalledMaxSize, 'sharedMemRmIfOutputQMaxSizeForce': sharedMemRmIfOutputQMaxSizeForce, 'sharedMemRmIfOutputQCellCount': sharedMemRmIfOutputQCellCount}


class sharedMemRmIfThresholdCfgEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, rmIfSc], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 6, 2, 1])
	access = 2
	columns = {'sharedMemRmIfDiscardThreshold': sharedMemRmIfDiscardThreshold, 'sharedMemRmIfEfciThreshold': sharedMemRmIfEfciThreshold, 'sharedMemRmIfAbrRelativeRateThreshold': sharedMemRmIfAbrRelativeRateThreshold}


class lsPerVcqRmThreshGrpEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lsPerVcqRmThreshGrp], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 1, 1])
	access = 2
	columns = {'lsPerVcqRmThreshGrp': lsPerVcqRmThreshGrp, 'lsPerVcqRmThreshGrpMaxSize': lsPerVcqRmThreshGrpMaxSize, 'lsPerVcqRmThreshGrpQMaxSize': lsPerVcqRmThreshGrpQMaxSize, 'lsPerVcqRmThreshGrpQMinSize': lsPerVcqRmThreshGrpQMinSize, 'lsPerVcqRmThreshGrpDiscThreshold': lsPerVcqRmThreshGrpDiscThreshold, 'lsPerVcqRmThreshGrpMarkThreshold': lsPerVcqRmThreshGrpMarkThreshold, 'lsPerVcqRmThreshGrpName': lsPerVcqRmThreshGrpName, 'lsPerVcqRmThreshGrpCellCount': lsPerVcqRmThreshGrpCellCount}


class lsPerVcqRmThreshGrpServiceEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([lsPerVcqRmThreshGrpService], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 7, 2, 1])
	access = 2
	columns = {'lsPerVcqRmThreshGrpService': lsPerVcqRmThreshGrpService, 'lsPerVcqRmThreshGrpServGroup': lsPerVcqRmThreshGrpServGroup}


class lsPerVcqRmIfEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 1, 1])
	access = 2
	columns = {'lsPerVcqRmIfMinWrrServiceClass': lsPerVcqRmIfMinWrrServiceClass}


class lsPerVcqRmIfServiceClassEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([ifIndex, lsPerVcqRmIfServiceClass], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 1, 8, 2, 1])
	access = 2
	columns = {'lsPerVcqRmIfServiceClass': lsPerVcqRmIfServiceClass, 'lsPerVcqRmIfServClassConnType': lsPerVcqRmIfServClassConnType, 'lsPerVcqRmIfServClassWrrWeight': lsPerVcqRmIfServClassWrrWeight}


# notifications (traps) 
# groups 
class sharedMemAtmRmSwitchMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 2])
	group = [sharedMemRmSwitchQueuedCellLimit, sharedMemRmSwitchQueuedCellCount]

class atmRmIfStatsMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 6])
	group = [rmIfScRcacResultNumAdmit, rmIfScRcacResultNumTotalRequests, rmIfScRcacResultNumFailTraffComb, rmIfScRcacResultNumFailBw, rmIfScRcacResultNumFailLoss, rmIfScRcacResultNumFailDelay, rmIfScRcacResultNumFailCdv, rmIfScRcacResultNumFailBeLimit, rmIfScRcacResultNumFailParmLimit, rmIfScRcacResultNumFailOther]

class sharedMemAtmRmPhyIfMIBGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 7])
	group = [sharedMemRmIfOutputQServCategory, sharedMemRmIfOutputQRequestedMaxSize, sharedMemRmIfOutputQInstalledMaxSize, sharedMemRmIfOutputQMaxSizeForce, sharedMemRmIfOutputQCellCount, sharedMemRmIfDiscardThreshold, sharedMemRmIfEfciThreshold, sharedMemRmIfAbrRelativeRateThreshold]

class atmRmSwitchCfgMIBGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 8])
	group = [rmSwitchOverSubFactor, rmSwitchScrMarginFactor, rmSwitchAbrCongNotify, rmScDefaultQosMaxCtd, rmScDefaultQosPeakToPeakCdv, rmScDefaultQosClr, rmScDefaultQosClrClp01]

class atmRmIfAllStateMIBGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 10])
	group = [rmIfScRxAcr, rmIfScTxAcr, rmIfScRxAlcr, rmIfScTxAlcr, rmIfScNumSvxConns, rmIfScNumPvxConns, rmIfScTxMaxCtd, rmIfScTxP2PeakCdv, rmIfScTxClr, rmIfScTxClrClp01]

class atmRmPhyIfCfgMIBGroup3(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 12])
	group = [rmIfOutPacingRateRequested, rmIfOutPacingRateInstalled, rmIfOutPacingForce, rmIfDirControlLinkShareMaxAgg, rmIfDirControlLinkShareMinCbr, rmIfDirControlLinkShareMaxCbr, rmIfDirControlLinkShareMinVbr, rmIfDirControlLinkShareMaxVbr, rmIfCbrDefaultRxUpcTolerance, rmIfVbrRtDefaultRxUpcTolerance, rmIfVbrNrtDefaultRxUpcTolerance, rmIfAbrDefaultRxUpcTolerance, rmIfUbrDefaultRxUpcTolerance, rmIfVbrRtDefaultRxUpcCdvt, rmIfVbrNrtDefaultRxUpcCdvt, rmIfDirControlLinkShareMinAbr, rmIfDirControlLinkShareMaxAbr, rmIfDirControlLinkShareMinUbr, rmIfDirControlLinkShareMaxUbr]

class atmRmAllIfCfgMIBGroup3(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 14])
	group = [rmIfLinkDistance, rmIfBestEffortLimit, rmIfDirMaxCbrPcr, rmIfDirMaxCbrTolerance, rmIfDirMaxVbrPcr, rmIfDirMaxVbrScr, rmIfDirMaxVbrTolerance, rmIfDirMaxAbrPcr, rmIfDirMaxAbrTolerance, rmIfDirMaxUbrPcr, rmIfDirMaxUbrTolerance, rmIfDirMaxAbrMcr, rmIfDirMaxUbrMcr, rmIfDirMaxVbrCdvt, rmIfServCategorySupport]

class lsPerVcqAtmRmGroup2(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 10, 10, 3, 2, 15])
	group = [lsPerVcqRmIfMinWrrServiceClass, lsPerVcqRmIfServClassConnType, lsPerVcqRmIfServClassWrrWeight, lsPerVcqRmThreshGrpMaxSize, lsPerVcqRmThreshGrpQMaxSize, lsPerVcqRmThreshGrpQMinSize, lsPerVcqRmThreshGrpDiscThreshold, lsPerVcqRmThreshGrpMarkThreshold, lsPerVcqRmThreshGrpName, lsPerVcqRmThreshGrpCellCount, lsPerVcqRmThreshGrpServGroup, lsPerVcqRmHierarchicalSchedulingMode]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
