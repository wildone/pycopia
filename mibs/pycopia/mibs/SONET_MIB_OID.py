# python
# This file is generated by a program (mib2py). 

import SONET_MIB

OIDMAP = {
'1.3.6.1.2.1.10.39': SONET_MIB.sonetMIB,
'1.3.6.1.2.1.10.39.1': SONET_MIB.sonetObjects,
'1.3.6.1.2.1.10.39.1.1': SONET_MIB.sonetMedium,
'1.3.6.1.2.1.10.39.1.2': SONET_MIB.sonetSection,
'1.3.6.1.2.1.10.39.1.3': SONET_MIB.sonetLine,
'1.3.6.1.2.1.10.39.1.4': SONET_MIB.sonetFarEndLine,
'1.3.6.1.2.1.10.39.2': SONET_MIB.sonetObjectsPath,
'1.3.6.1.2.1.10.39.2.1': SONET_MIB.sonetPath,
'1.3.6.1.2.1.10.39.2.2': SONET_MIB.sonetFarEndPath,
'1.3.6.1.2.1.10.39.3': SONET_MIB.sonetObjectsVT,
'1.3.6.1.2.1.10.39.3.1': SONET_MIB.sonetVT,
'1.3.6.1.2.1.10.39.3.2': SONET_MIB.sonetFarEndVT,
'1.3.6.1.2.1.10.39.4': SONET_MIB.sonetConformance,
'1.3.6.1.2.1.10.39.4.1': SONET_MIB.sonetGroups,
'1.3.6.1.2.1.10.39.4.2': SONET_MIB.sonetCompliances,
'1.3.6.1.2.1.10.39.1.1.2': SONET_MIB.sonetSESthresholdSet,
'1.3.6.1.2.1.10.39.1.1.1.1.1': SONET_MIB.sonetMediumType,
'1.3.6.1.2.1.10.39.1.1.1.1.2': SONET_MIB.sonetMediumTimeElapsed,
'1.3.6.1.2.1.10.39.1.1.1.1.3': SONET_MIB.sonetMediumValidIntervals,
'1.3.6.1.2.1.10.39.1.1.1.1.4': SONET_MIB.sonetMediumLineCoding,
'1.3.6.1.2.1.10.39.1.1.1.1.5': SONET_MIB.sonetMediumLineType,
'1.3.6.1.2.1.10.39.1.1.1.1.6': SONET_MIB.sonetMediumCircuitIdentifier,
'1.3.6.1.2.1.10.39.1.1.1.1.7': SONET_MIB.sonetMediumInvalidIntervals,
'1.3.6.1.2.1.10.39.1.1.1.1.8': SONET_MIB.sonetMediumLoopbackConfig,
'1.3.6.1.2.1.10.39.1.2.1.1.1': SONET_MIB.sonetSectionCurrentStatus,
'1.3.6.1.2.1.10.39.1.2.1.1.2': SONET_MIB.sonetSectionCurrentESs,
'1.3.6.1.2.1.10.39.1.2.1.1.3': SONET_MIB.sonetSectionCurrentSESs,
'1.3.6.1.2.1.10.39.1.2.1.1.4': SONET_MIB.sonetSectionCurrentSEFSs,
'1.3.6.1.2.1.10.39.1.2.1.1.5': SONET_MIB.sonetSectionCurrentCVs,
'1.3.6.1.2.1.10.39.1.2.2.1.1': SONET_MIB.sonetSectionIntervalNumber,
'1.3.6.1.2.1.10.39.1.2.2.1.2': SONET_MIB.sonetSectionIntervalESs,
'1.3.6.1.2.1.10.39.1.2.2.1.3': SONET_MIB.sonetSectionIntervalSESs,
'1.3.6.1.2.1.10.39.1.2.2.1.4': SONET_MIB.sonetSectionIntervalSEFSs,
'1.3.6.1.2.1.10.39.1.2.2.1.5': SONET_MIB.sonetSectionIntervalCVs,
'1.3.6.1.2.1.10.39.1.2.2.1.6': SONET_MIB.sonetSectionIntervalValidData,
'1.3.6.1.2.1.10.39.1.3.1.1.1': SONET_MIB.sonetLineCurrentStatus,
'1.3.6.1.2.1.10.39.1.3.1.1.2': SONET_MIB.sonetLineCurrentESs,
'1.3.6.1.2.1.10.39.1.3.1.1.3': SONET_MIB.sonetLineCurrentSESs,
'1.3.6.1.2.1.10.39.1.3.1.1.4': SONET_MIB.sonetLineCurrentCVs,
'1.3.6.1.2.1.10.39.1.3.1.1.5': SONET_MIB.sonetLineCurrentUASs,
'1.3.6.1.2.1.10.39.1.3.2.1.1': SONET_MIB.sonetLineIntervalNumber,
'1.3.6.1.2.1.10.39.1.3.2.1.2': SONET_MIB.sonetLineIntervalESs,
'1.3.6.1.2.1.10.39.1.3.2.1.3': SONET_MIB.sonetLineIntervalSESs,
'1.3.6.1.2.1.10.39.1.3.2.1.4': SONET_MIB.sonetLineIntervalCVs,
'1.3.6.1.2.1.10.39.1.3.2.1.5': SONET_MIB.sonetLineIntervalUASs,
'1.3.6.1.2.1.10.39.1.3.2.1.6': SONET_MIB.sonetLineIntervalValidData,
'1.3.6.1.2.1.10.39.1.4.1.1.1': SONET_MIB.sonetFarEndLineCurrentESs,
'1.3.6.1.2.1.10.39.1.4.1.1.2': SONET_MIB.sonetFarEndLineCurrentSESs,
'1.3.6.1.2.1.10.39.1.4.1.1.3': SONET_MIB.sonetFarEndLineCurrentCVs,
'1.3.6.1.2.1.10.39.1.4.1.1.4': SONET_MIB.sonetFarEndLineCurrentUASs,
'1.3.6.1.2.1.10.39.1.4.2.1.1': SONET_MIB.sonetFarEndLineIntervalNumber,
'1.3.6.1.2.1.10.39.1.4.2.1.2': SONET_MIB.sonetFarEndLineIntervalESs,
'1.3.6.1.2.1.10.39.1.4.2.1.3': SONET_MIB.sonetFarEndLineIntervalSESs,
'1.3.6.1.2.1.10.39.1.4.2.1.4': SONET_MIB.sonetFarEndLineIntervalCVs,
'1.3.6.1.2.1.10.39.1.4.2.1.5': SONET_MIB.sonetFarEndLineIntervalUASs,
'1.3.6.1.2.1.10.39.1.4.2.1.6': SONET_MIB.sonetFarEndLineIntervalValidData,
'1.3.6.1.2.1.10.39.2.1.1.1.1': SONET_MIB.sonetPathCurrentWidth,
'1.3.6.1.2.1.10.39.2.1.1.1.2': SONET_MIB.sonetPathCurrentStatus,
'1.3.6.1.2.1.10.39.2.1.1.1.3': SONET_MIB.sonetPathCurrentESs,
'1.3.6.1.2.1.10.39.2.1.1.1.4': SONET_MIB.sonetPathCurrentSESs,
'1.3.6.1.2.1.10.39.2.1.1.1.5': SONET_MIB.sonetPathCurrentCVs,
'1.3.6.1.2.1.10.39.2.1.1.1.6': SONET_MIB.sonetPathCurrentUASs,
'1.3.6.1.2.1.10.39.2.1.2.1.1': SONET_MIB.sonetPathIntervalNumber,
'1.3.6.1.2.1.10.39.2.1.2.1.2': SONET_MIB.sonetPathIntervalESs,
'1.3.6.1.2.1.10.39.2.1.2.1.3': SONET_MIB.sonetPathIntervalSESs,
'1.3.6.1.2.1.10.39.2.1.2.1.4': SONET_MIB.sonetPathIntervalCVs,
'1.3.6.1.2.1.10.39.2.1.2.1.5': SONET_MIB.sonetPathIntervalUASs,
'1.3.6.1.2.1.10.39.2.1.2.1.6': SONET_MIB.sonetPathIntervalValidData,
'1.3.6.1.2.1.10.39.2.2.1.1.1': SONET_MIB.sonetFarEndPathCurrentESs,
'1.3.6.1.2.1.10.39.2.2.1.1.2': SONET_MIB.sonetFarEndPathCurrentSESs,
'1.3.6.1.2.1.10.39.2.2.1.1.3': SONET_MIB.sonetFarEndPathCurrentCVs,
'1.3.6.1.2.1.10.39.2.2.1.1.4': SONET_MIB.sonetFarEndPathCurrentUASs,
'1.3.6.1.2.1.10.39.2.2.2.1.1': SONET_MIB.sonetFarEndPathIntervalNumber,
'1.3.6.1.2.1.10.39.2.2.2.1.2': SONET_MIB.sonetFarEndPathIntervalESs,
'1.3.6.1.2.1.10.39.2.2.2.1.3': SONET_MIB.sonetFarEndPathIntervalSESs,
'1.3.6.1.2.1.10.39.2.2.2.1.4': SONET_MIB.sonetFarEndPathIntervalCVs,
'1.3.6.1.2.1.10.39.2.2.2.1.5': SONET_MIB.sonetFarEndPathIntervalUASs,
'1.3.6.1.2.1.10.39.2.2.2.1.6': SONET_MIB.sonetFarEndPathIntervalValidData,
'1.3.6.1.2.1.10.39.3.1.1.1.1': SONET_MIB.sonetVTCurrentWidth,
'1.3.6.1.2.1.10.39.3.1.1.1.2': SONET_MIB.sonetVTCurrentStatus,
'1.3.6.1.2.1.10.39.3.1.1.1.3': SONET_MIB.sonetVTCurrentESs,
'1.3.6.1.2.1.10.39.3.1.1.1.4': SONET_MIB.sonetVTCurrentSESs,
'1.3.6.1.2.1.10.39.3.1.1.1.5': SONET_MIB.sonetVTCurrentCVs,
'1.3.6.1.2.1.10.39.3.1.1.1.6': SONET_MIB.sonetVTCurrentUASs,
'1.3.6.1.2.1.10.39.3.1.2.1.1': SONET_MIB.sonetVTIntervalNumber,
'1.3.6.1.2.1.10.39.3.1.2.1.2': SONET_MIB.sonetVTIntervalESs,
'1.3.6.1.2.1.10.39.3.1.2.1.3': SONET_MIB.sonetVTIntervalSESs,
'1.3.6.1.2.1.10.39.3.1.2.1.4': SONET_MIB.sonetVTIntervalCVs,
'1.3.6.1.2.1.10.39.3.1.2.1.5': SONET_MIB.sonetVTIntervalUASs,
'1.3.6.1.2.1.10.39.3.1.2.1.6': SONET_MIB.sonetVTIntervalValidData,
'1.3.6.1.2.1.10.39.3.2.1.1.1': SONET_MIB.sonetFarEndVTCurrentESs,
'1.3.6.1.2.1.10.39.3.2.1.1.2': SONET_MIB.sonetFarEndVTCurrentSESs,
'1.3.6.1.2.1.10.39.3.2.1.1.3': SONET_MIB.sonetFarEndVTCurrentCVs,
'1.3.6.1.2.1.10.39.3.2.1.1.4': SONET_MIB.sonetFarEndVTCurrentUASs,
'1.3.6.1.2.1.10.39.3.2.2.1.1': SONET_MIB.sonetFarEndVTIntervalNumber,
'1.3.6.1.2.1.10.39.3.2.2.1.2': SONET_MIB.sonetFarEndVTIntervalESs,
'1.3.6.1.2.1.10.39.3.2.2.1.3': SONET_MIB.sonetFarEndVTIntervalSESs,
'1.3.6.1.2.1.10.39.3.2.2.1.4': SONET_MIB.sonetFarEndVTIntervalCVs,
'1.3.6.1.2.1.10.39.3.2.2.1.5': SONET_MIB.sonetFarEndVTIntervalUASs,
'1.3.6.1.2.1.10.39.3.2.2.1.6': SONET_MIB.sonetFarEndVTIntervalValidData,
'1.3.6.1.2.1.10.39.4.1.1': SONET_MIB.sonetMediumStuff,
'1.3.6.1.2.1.10.39.4.1.2': SONET_MIB.sonetSectionStuff,
'1.3.6.1.2.1.10.39.4.1.3': SONET_MIB.sonetLineStuff,
'1.3.6.1.2.1.10.39.4.1.4': SONET_MIB.sonetFarEndLineStuff,
'1.3.6.1.2.1.10.39.4.1.5': SONET_MIB.sonetPathStuff,
'1.3.6.1.2.1.10.39.4.1.6': SONET_MIB.sonetFarEndPathStuff,
'1.3.6.1.2.1.10.39.4.1.7': SONET_MIB.sonetVTStuff,
'1.3.6.1.2.1.10.39.4.1.8': SONET_MIB.sonetFarEndVTStuff,
'1.3.6.1.2.1.10.39.4.1.9': SONET_MIB.sonetMediumStuff2,
'1.3.6.1.2.1.10.39.4.1.10': SONET_MIB.sonetSectionStuff2,
'1.3.6.1.2.1.10.39.4.1.11': SONET_MIB.sonetLineStuff2,
'1.3.6.1.2.1.10.39.4.1.12': SONET_MIB.sonetPathStuff2,
'1.3.6.1.2.1.10.39.4.1.13': SONET_MIB.sonetVTStuff2,
'1.3.6.1.2.1.10.39.4.1.14': SONET_MIB.sonetFarEndLineStuff2,
'1.3.6.1.2.1.10.39.4.1.15': SONET_MIB.sonetFarEndPathStuff2,
'1.3.6.1.2.1.10.39.4.1.16': SONET_MIB.sonetFarEndVTStuff2,
}
