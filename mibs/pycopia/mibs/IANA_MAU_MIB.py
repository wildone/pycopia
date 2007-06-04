# python
# This file is generated by a program (mib2py). Any edits will be lost.

from pycopia.aid import Enum
import pycopia.SMI.Basetypes
Range = pycopia.SMI.Basetypes.Range
Ranges = pycopia.SMI.Basetypes.Ranges

from pycopia.SMI.Objects import ColumnObject, MacroObject, NotificationObject, RowObject, ScalarObject, NodeObject, ModuleObject, GroupObject

# imports 
from SNMPv2_SMI import MODULE_IDENTITY, OBJECT_IDENTITY, mib_2
from SNMPv2_TC import TEXTUAL_CONVENTION

class IANA_MAU_MIB(ModuleObject):
	path = '/usr/share/snmp/mibs/iana/IANA-MAU-MIB'
	conformance = 5
	name = 'IANA-MAU-MIB'
	language = 2
	description = "This MIB module defines dot3MauType OBJECT-IDENTITIES and\nIANAifMauListBits, IANAifMauMediaAvailable,\nIANAifMauAutoNegCapBits and IANAifJackType Textual Conventions,\nspecifying enumerated values of the ifMauTypeListBits,\nifMauMediaAvailable / rpMauMediaAvailable,\nifMauAutoNegCapabilityBits / ifMauAutoNegCapAdvertisedBits /\nifMauAutoNegCapReceivedBits and ifJackType / rpJackType objects\nrespectively, defined in the MAU-MIB.\n\nIt is intended that each new MAU type, Media Availability\nstate, Auto Negotiation capability and/or Jack type defined by\nthe IEEE 802.3 working group and approved for publication in a\nrevision of IEEE Std 802.3 will be added to this MIB module,\nprovided that it is suitable for being managed by the base\nobjects in the MAU-MIB. An Expert Review, as defined in\nRFC 2434 [RFC2434], is REQUIRED for such additions.\n\nThe following reference is used throughout this MIB module:\n\n[IEEE 802.3 Std] refers to:\n   IEEE Std 802.3, 2005 Edition: 'IEEE Standard for\n   Information technology - Telecommunications and information\n   exchange between systems - Local and metropolitan area\n   networks - Specific requirements -\n   Part 3: Carrier sense multiple access with collision\n   detection (CSMA/CD) access method and physical layer\n   specifications'.\n\nThis reference should be updated as appropriate when new\nMAU types, Media Availability states, Auto Negotiation\ncapabilities and/or Jack types are added to this MIB module.\n\n\tCopyright (C) The IETF Trust (2007). \n\tThe initial version of this MIB module was published in \n\tdraft-ietf-hubmib-rfc3636bis-05; \n\tfor full legal notices see the RFC itself. \n\tSupplementary information may be available at: \n\thttp://www.ietf.org/copyrights/ianamib.html"

# nodes
class dot3MauType(NodeObject):
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4])
	name = 'dot3MauType'

class dot3MauTypeAUI(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 1])
	name = 'dot3MauTypeAUI'

class dot3MauType10Base5(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 2])
	name = 'dot3MauType10Base5'

class dot3MauTypeFoirl(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 3])
	name = 'dot3MauTypeFoirl'

class dot3MauType10Base2(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 4])
	name = 'dot3MauType10Base2'

class dot3MauType10BaseT(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 5])
	name = 'dot3MauType10BaseT'

class dot3MauType10BaseFP(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 6])
	name = 'dot3MauType10BaseFP'

class dot3MauType10BaseFB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 7])
	name = 'dot3MauType10BaseFB'

class dot3MauType10BaseFL(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 8])
	name = 'dot3MauType10BaseFL'

class dot3MauType10Broad36(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 9])
	name = 'dot3MauType10Broad36'

class dot3MauType10BaseTHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 10])
	name = 'dot3MauType10BaseTHD'

class dot3MauType10BaseTFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 11])
	name = 'dot3MauType10BaseTFD'

class dot3MauType10BaseFLHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 12])
	name = 'dot3MauType10BaseFLHD'

class dot3MauType10BaseFLFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 13])
	name = 'dot3MauType10BaseFLFD'

class dot3MauType100BaseT4(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 14])
	name = 'dot3MauType100BaseT4'

class dot3MauType100BaseTXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 15])
	name = 'dot3MauType100BaseTXHD'

class dot3MauType100BaseTXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 16])
	name = 'dot3MauType100BaseTXFD'

class dot3MauType100BaseFXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 17])
	name = 'dot3MauType100BaseFXHD'

class dot3MauType100BaseFXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 18])
	name = 'dot3MauType100BaseFXFD'

class dot3MauType100BaseT2HD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 19])
	name = 'dot3MauType100BaseT2HD'

class dot3MauType100BaseT2FD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 20])
	name = 'dot3MauType100BaseT2FD'

class dot3MauType1000BaseXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 21])
	name = 'dot3MauType1000BaseXHD'

class dot3MauType1000BaseXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 22])
	name = 'dot3MauType1000BaseXFD'

class dot3MauType1000BaseLXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 23])
	name = 'dot3MauType1000BaseLXHD'

class dot3MauType1000BaseLXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 24])
	name = 'dot3MauType1000BaseLXFD'

class dot3MauType1000BaseSXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 25])
	name = 'dot3MauType1000BaseSXHD'

class dot3MauType1000BaseSXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 26])
	name = 'dot3MauType1000BaseSXFD'

class dot3MauType1000BaseCXHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 27])
	name = 'dot3MauType1000BaseCXHD'

class dot3MauType1000BaseCXFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 28])
	name = 'dot3MauType1000BaseCXFD'

class dot3MauType1000BaseTHD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 29])
	name = 'dot3MauType1000BaseTHD'

class dot3MauType1000BaseTFD(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 30])
	name = 'dot3MauType1000BaseTFD'

class dot3MauType10GigBaseX(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 31])
	name = 'dot3MauType10GigBaseX'

class dot3MauType10GigBaseLX4(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 32])
	name = 'dot3MauType10GigBaseLX4'

class dot3MauType10GigBaseR(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 33])
	name = 'dot3MauType10GigBaseR'

class dot3MauType10GigBaseER(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 34])
	name = 'dot3MauType10GigBaseER'

class dot3MauType10GigBaseLR(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 35])
	name = 'dot3MauType10GigBaseLR'

class dot3MauType10GigBaseSR(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 36])
	name = 'dot3MauType10GigBaseSR'

class dot3MauType10GigBaseW(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 37])
	name = 'dot3MauType10GigBaseW'

class dot3MauType10GigBaseEW(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 38])
	name = 'dot3MauType10GigBaseEW'

class dot3MauType10GigBaseLW(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 39])
	name = 'dot3MauType10GigBaseLW'

class dot3MauType10GigBaseSW(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 40])
	name = 'dot3MauType10GigBaseSW'

class dot3MauType10GigBaseCX4(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 41])
	name = 'dot3MauType10GigBaseCX4'

class dot3MauType2BaseTL(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 42])
	name = 'dot3MauType2BaseTL'

class dot3MauType10PassTS(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 43])
	name = 'dot3MauType10PassTS'

class dot3MauType100BaseBX10D(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 44])
	name = 'dot3MauType100BaseBX10D'

class dot3MauType100BaseBX10U(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 45])
	name = 'dot3MauType100BaseBX10U'

class dot3MauType100BaseLX10(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 46])
	name = 'dot3MauType100BaseLX10'

class dot3MauType1000BaseBX10D(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 47])
	name = 'dot3MauType1000BaseBX10D'

class dot3MauType1000BaseBX10U(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 48])
	name = 'dot3MauType1000BaseBX10U'

class dot3MauType1000BaseLX10(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 49])
	name = 'dot3MauType1000BaseLX10'

class dot3MauType1000BasePX10D(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 50])
	name = 'dot3MauType1000BasePX10D'

class dot3MauType1000BasePX10U(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 51])
	name = 'dot3MauType1000BasePX10U'

class dot3MauType1000BasePX20D(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 52])
	name = 'dot3MauType1000BasePX20D'

class dot3MauType1000BasePX20U(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 26, 4, 53])
	name = 'dot3MauType1000BasePX20U'

class ianaMauMIB(NodeObject):
	status = 1
	OID = pycopia.SMI.Basetypes.ObjectIdentifier([1, 3, 6, 1, 2, 1, 154])
	name = 'ianaMauMIB'


# macros
# types 

class IANAifMauTypeListBits(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'bOther'), Enum(1, 'bAUI'), Enum(2, 'b10base5'), Enum(3, 'bFoirl'), Enum(4, 'b10base2'), Enum(5, 'b10baseT'), Enum(6, 'b10baseFP'), Enum(7, 'b10baseFB'), Enum(8, 'b10baseFL'), Enum(9, 'b10broad36'), Enum(10, 'b10baseTHD'), Enum(11, 'b10baseTFD'), Enum(12, 'b10baseFLHD'), Enum(13, 'b10baseFLFD'), Enum(14, 'b100baseT4'), Enum(15, 'b100baseTXHD'), Enum(16, 'b100baseTXFD'), Enum(17, 'b100baseFXHD'), Enum(18, 'b100baseFXFD'), Enum(19, 'b100baseT2HD'), Enum(20, 'b100baseT2FD'), Enum(21, 'b1000baseXHD'), Enum(22, 'b1000baseXFD'), Enum(23, 'b1000baseLXHD'), Enum(24, 'b1000baseLXFD'), Enum(25, 'b1000baseSXHD'), Enum(26, 'b1000baseSXFD'), Enum(27, 'b1000baseCXHD'), Enum(28, 'b1000baseCXFD'), Enum(29, 'b1000baseTHD'), Enum(30, 'b1000baseTFD'), Enum(31, 'b10GbaseX'), Enum(32, 'b10GbaseLX4'), Enum(33, 'b10GbaseR'), Enum(34, 'b10GbaseER'), Enum(35, 'b10GbaseLR'), Enum(36, 'b10GbaseSR'), Enum(37, 'b10GbaseW'), Enum(38, 'b10GbaseEW'), Enum(39, 'b10GbaseLW'), Enum(40, 'b10GbaseSW'), Enum(41, 'b10GbaseCX4'), Enum(42, 'b2BaseTL'), Enum(43, 'b10PassTS'), Enum(44, 'b100BaseBX10D'), Enum(45, 'b100BaseBX10U'), Enum(46, 'b100BaseLX10'), Enum(47, 'b1000BaseBX10D'), Enum(48, 'b1000BaseBX10U'), Enum(49, 'b1000BaseLX10'), Enum(50, 'b1000BasePX10D'), Enum(51, 'b1000BasePX10U'), Enum(52, 'b1000BasePX20D'), Enum(53, 'b1000BasePX20U')]


class IANAifMauMediaAvailable(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'unknown'), Enum(3, 'available'), Enum(4, 'notAvailable'), Enum(5, 'remoteFault'), Enum(6, 'invalidSignal'), Enum(7, 'remoteJabber'), Enum(8, 'remoteLinkLoss'), Enum(9, 'remoteTest'), Enum(10, 'offline'), Enum(11, 'autoNegError'), Enum(12, 'pmdLinkFault'), Enum(13, 'wisFrameLoss'), Enum(14, 'wisSignalLoss'), Enum(15, 'pcsLinkFault'), Enum(16, 'excessiveBER'), Enum(17, 'dxsLinkFault'), Enum(18, 'pxsLinkFault'), Enum(19, 'availableReduced'), Enum(20, 'ready')]


class IANAifMauAutoNegCapBits(pycopia.SMI.Basetypes.BITS):
	status = 1
	enumerations = [Enum(0, 'bOther'), Enum(1, 'b10baseT'), Enum(2, 'b10baseTFD'), Enum(3, 'b100baseT4'), Enum(4, 'b100baseTX'), Enum(5, 'b100baseTXFD'), Enum(6, 'b100baseT2'), Enum(7, 'b100baseT2FD'), Enum(8, 'bFdxPause'), Enum(9, 'bFdxAPause'), Enum(10, 'bFdxSPause'), Enum(11, 'bFdxBPause'), Enum(12, 'b1000baseX'), Enum(13, 'b1000baseXFD'), Enum(14, 'b1000baseT'), Enum(15, 'b1000baseTFD')]


class IANAifJackType(pycopia.SMI.Basetypes.Enumeration):
	status = 1
	enumerations = [Enum(1, 'other'), Enum(2, 'rj45'), Enum(3, 'rj45S'), Enum(4, 'db9'), Enum(5, 'bnc'), Enum(6, 'fAUI'), Enum(7, 'mAUI'), Enum(8, 'fiberSC'), Enum(9, 'fiberMIC'), Enum(10, 'fiberST'), Enum(11, 'telco'), Enum(12, 'mtrj'), Enum(13, 'hssdc'), Enum(14, 'fiberLC'), Enum(15, 'cx4')]

# scalars 
# columns
# rows 
# notifications (traps) 
# groups 
# capabilities 

# special additions

# Add to master OIDMAP.
from pycopia import SMI
SMI.update_oidmap(__name__)
