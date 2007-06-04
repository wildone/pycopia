# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, NOTIFICATION_TYPE, Integer32
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from CISCO_SMI import ciscoMgmt
from SNMPv2_TC import TEXTUAL_CONVENTION, TimeStamp, TruthValue
from ENTITY_MIB import entPhysicalIndex

class CISCO_ENTITY_SENSOR_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/site/CISCO-ENTITY-SENSOR-MIB'
	conformance = 3
	name = 'CISCO-ENTITY-SENSOR-MIB'
	language = 2
	description = 'The CISCO-ENTITY-SENSOR-MIB is used to monitor \nthe values of sensors in the Entity-MIB (RFC 2037) \nentPhysicalTable.'

# nodes
class entitySensorMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91])
	name = 'entitySensorMIB'

class entitySensorMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1])
	name = 'entitySensorMIBObjects'

class entSensorValues(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1])
	name = 'entSensorValues'

class entSensorThresholds(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2])
	name = 'entSensorThresholds'

class entitySensorMIBNotificationPrefix(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 2])
	name = 'entitySensorMIBNotificationPrefix'

class entitySensorMIBNotifications(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0])
	name = 'entitySensorMIBNotifications'

class entitySensorMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 3])
	name = 'entitySensorMIBConformance'

class entitySensorMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 1])
	name = 'entitySensorMIBCompliances'

class entitySensorMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2])
	name = 'entitySensorMIBGroups'


# macros
# types 

class SensorDataType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'voltsAC'), Enum(4, 'voltsDC'), Enum(5, 'amperes'), Enum(6, 'watts'), Enum(7, 'hertz'), Enum(8, 'celsius'), Enum(9, 'percentRH'), Enum(10, 'rpm'), Enum(11, 'cmm'), Enum(12, 'truthvalue'), Enum(13, 'specialEnum')]


class SensorDataScale(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'yocto'), Enum(2, 'zepto'), Enum(3, 'atto'), Enum(4, 'femto'), Enum(5, 'pico'), Enum(6, 'nano'), Enum(7, 'micro'), Enum(8, 'milli'), Enum(9, 'units'), Enum(10, 'kilo'), Enum(11, 'mega'), Enum(12, 'giga'), Enum(13, 'tera'), Enum(14, 'exa'), Enum(15, 'peta'), Enum(16, 'zetta'), Enum(17, 'yotta')]


class SensorPrecision(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(-8, 9))


class SensorValue(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(-1000000000, 1000000000))


class SensorStatus(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'ok'), Enum(2, 'unavailable'), Enum(3, 'nonoperational')]


class SensorValueUpdateRate(pycopia.SMI.Basetypes.Integer32):
	status = 1
	ranges = Ranges(Range(0, 999999999))


class SensorThresholdSeverity(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(10, 'minor'), Enum(20, 'major')]


class SensorThresholdRelation(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'lessThan'), Enum(2, 'lessOrEqual'), Enum(3, 'greaterThan'), Enum(4, 'greaterOrEqual'), Enum(5, 'equalTo'), Enum(6, 'notEqualTo')]

# scalars 
# columns
class entSensorType(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 1])
	syntaxobject = SensorDataType


class entSensorScale(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 2])
	syntaxobject = SensorDataScale


class entSensorPrecision(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 3])
	syntaxobject = SensorPrecision


class entSensorValue(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 4])
	syntaxobject = SensorValue


class entSensorStatus(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 5])
	syntaxobject = SensorStatus


class entSensorValueTimeStamp(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TimeStamp


class entSensorValueUpdateRate(ColumnObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1, 7])
	syntaxobject = SensorValueUpdateRate
	access = 4
	units = 'seconds'


class entSensorThresholdIndex(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 1])
	syntaxobject = pycopia.SMI.Basetypes.Integer32


class entSensorThresholdSeverity(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 2])
	syntaxobject = SensorThresholdSeverity


class entSensorThresholdRelation(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 3])
	syntaxobject = SensorThresholdRelation


class entSensorThresholdValue(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 4])
	syntaxobject = SensorValue


class entSensorThresholdEvaluation(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


class entSensorThresholdNotificationEnable(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.TruthValue


# rows 
class entSensorValueEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 1, 1, 1])
	access = 2
	columns = {'entSensorType': entSensorType, 'entSensorScale': entSensorScale, 'entSensorPrecision': entSensorPrecision, 'entSensorValue': entSensorValue, 'entSensorStatus': entSensorStatus, 'entSensorValueTimeStamp': entSensorValueTimeStamp, 'entSensorValueUpdateRate': entSensorValueUpdateRate}


class entSensorThresholdEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([entPhysicalIndex, entSensorThresholdIndex], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 1, 2, 1, 1])
	access = 2
	columns = {'entSensorThresholdIndex': entSensorThresholdIndex, 'entSensorThresholdSeverity': entSensorThresholdSeverity, 'entSensorThresholdRelation': entSensorThresholdRelation, 'entSensorThresholdValue': entSensorThresholdValue, 'entSensorThresholdEvaluation': entSensorThresholdEvaluation, 'entSensorThresholdNotificationEnable': entSensorThresholdNotificationEnable}


# notifications (traps) 
class entSensorThresholdNotification(NotificationObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 2, 0, 1])

# groups 
class entitySensorValueGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 1])
	group = [entSensorType, entSensorScale, entSensorPrecision, entSensorValue, entSensorStatus, entSensorValueTimeStamp, entSensorValueUpdateRate]

class entitySensorThresholdGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 4, 1, 9, 9, 91, 3, 2, 2])
	group = [entSensorThresholdSeverity, entSensorThresholdRelation, entSensorThresholdValue, entSensorThresholdEvaluation, entSensorThresholdNotificationEnable]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
