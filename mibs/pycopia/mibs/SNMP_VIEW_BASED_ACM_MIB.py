# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_CONF import MODULE_COMPLIANCE, OBJECT_GROUP
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_TYPE, snmpModules
from SNMPv2_TC import TestAndIncr, RowStatus, StorageType
from SNMP_FRAMEWORK_MIB import SnmpAdminString, SnmpSecurityLevel, SnmpSecurityModel

class SNMP_VIEW_BASED_ACM_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/ietf/SNMP-VIEW-BASED-ACM-MIB'
	conformance = 3
	name = 'SNMP-VIEW-BASED-ACM-MIB'
	language = 2
	description = 'The management information definitions for the\nView-based Access Control Model for SNMP.\n\nCopyright (C) The Internet Society (2002). This\nversion of this MIB module is part of RFC 3415;\nsee the RFC itself for full legal notices.'

# nodes
class snmpVacmMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16])
	name = 'snmpVacmMIB'

class vacmMIBObjects(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1])
	name = 'vacmMIBObjects'

class vacmMIBViews(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5])
	name = 'vacmMIBViews'

class vacmMIBConformance(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 2])
	name = 'vacmMIBConformance'

class vacmMIBCompliances(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 2, 1])
	name = 'vacmMIBCompliances'

class vacmMIBGroups(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 2, 2])
	name = 'vacmMIBGroups'


# macros
# types 
# scalars 
class vacmViewSpinLock(ScalarObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 1])
	syntaxobject = pycopia.SMI.Basetypes.TestAndIncr


# columns
class vacmContextName(ColumnObject):
	access = 4
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1])
	syntaxobject = SnmpAdminString


class vacmSecurityModel(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 1])
	syntaxobject = SnmpSecurityModel


class vacmSecurityName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 2])
	syntaxobject = SnmpAdminString


class vacmGroupName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3])
	syntaxobject = SnmpAdminString


class vacmSecurityToGroupStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class vacmSecurityToGroupStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class vacmAccessContextPrefix(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 1])
	syntaxobject = SnmpAdminString


class vacmAccessSecurityModel(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 2])
	syntaxobject = SnmpSecurityModel


class vacmAccessSecurityLevel(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 3])
	syntaxobject = SnmpSecurityLevel


class vacmAccessContextMatch(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'exact'), Enum(2, 'prefix')]


class vacmAccessReadViewName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5])
	syntaxobject = SnmpAdminString


class vacmAccessWriteViewName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6])
	syntaxobject = SnmpAdminString


class vacmAccessNotifyViewName(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7])
	syntaxobject = SnmpAdminString


class vacmAccessStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class vacmAccessStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


class vacmViewTreeFamilyViewName(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 1])
	syntaxobject = SnmpAdminString


class vacmViewTreeFamilySubtree(ColumnObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 2])
	syntaxobject = pycopia.SMI.Basetypes.ObjectIdentifier


class vacmViewTreeFamilyMask(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3])
	syntaxobject = pycopia.SMI.Basetypes.OctetString


class vacmViewTreeFamilyType(ColumnObject):
	status = 1
	access = 5
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4])
	syntaxobject = pycopia.SMI.Basetypes.Enumeration
	enumerations = [Enum(1, 'included'), Enum(2, 'excluded')]


class vacmViewTreeFamilyStorageType(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5])
	syntaxobject = pycopia.SMI.Basetypes.StorageType


class vacmViewTreeFamilyStatus(ColumnObject):
	access = 5
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6])
	syntaxobject = pycopia.SMI.Basetypes.RowStatus


# rows 
class vacmContextEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vacmContextName], False)
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 1, 1])
	access = 2
	columns = {'vacmContextName': vacmContextName}


class vacmSecurityToGroupEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vacmSecurityModel, vacmSecurityName], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 2, 1])
	access = 2
	rowstatus = vacmSecurityToGroupStatus
	columns = {'vacmSecurityModel': vacmSecurityModel, 'vacmSecurityName': vacmSecurityName, 'vacmGroupName': vacmGroupName, 'vacmSecurityToGroupStorageType': vacmSecurityToGroupStorageType, 'vacmSecurityToGroupStatus': vacmSecurityToGroupStatus}


class vacmAccessEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vacmGroupName, vacmAccessContextPrefix, vacmAccessSecurityModel, vacmAccessSecurityLevel], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 4, 1])
	access = 2
	rowstatus = vacmAccessStatus
	columns = {'vacmAccessContextPrefix': vacmAccessContextPrefix, 'vacmAccessSecurityModel': vacmAccessSecurityModel, 'vacmAccessSecurityLevel': vacmAccessSecurityLevel, 'vacmAccessContextMatch': vacmAccessContextMatch, 'vacmAccessReadViewName': vacmAccessReadViewName, 'vacmAccessWriteViewName': vacmAccessWriteViewName, 'vacmAccessNotifyViewName': vacmAccessNotifyViewName, 'vacmAccessStorageType': vacmAccessStorageType, 'vacmAccessStatus': vacmAccessStatus}


class vacmViewTreeFamilyEntry(RowObject):
	status = 1
	index = pycopia.SMI.Objects.IndexObjects([vacmViewTreeFamilyViewName, vacmViewTreeFamilySubtree], False)
	create = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1])
	access = 2
	rowstatus = vacmViewTreeFamilyStatus
	columns = {'vacmViewTreeFamilyViewName': vacmViewTreeFamilyViewName, 'vacmViewTreeFamilySubtree': vacmViewTreeFamilySubtree, 'vacmViewTreeFamilyMask': vacmViewTreeFamilyMask, 'vacmViewTreeFamilyType': vacmViewTreeFamilyType, 'vacmViewTreeFamilyStorageType': vacmViewTreeFamilyStorageType, 'vacmViewTreeFamilyStatus': vacmViewTreeFamilyStatus}


# notifications (traps) 
# groups 
class vacmBasicGroup(GroupObject):
	access = 2
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 6, 3, 16, 2, 2, 1])
	group = [vacmContextName, vacmGroupName, vacmSecurityToGroupStorageType, vacmSecurityToGroupStatus, vacmAccessContextMatch, vacmAccessReadViewName, vacmAccessWriteViewName, vacmAccessNotifyViewName, vacmAccessStorageType, vacmAccessStatus, vacmViewSpinLock, vacmViewTreeFamilyMask, vacmViewTreeFamilyType, vacmViewTreeFamilyStorageType, vacmViewTreeFamilyStatus]

# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
