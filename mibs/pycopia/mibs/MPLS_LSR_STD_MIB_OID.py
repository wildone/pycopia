# python
# This file is generated by a program (mib2py). 

import MPLS_LSR_STD_MIB

OIDMAP = {
'1.3.6.1.2.1.10.166.2': MPLS_LSR_STD_MIB.mplsLsrStdMIB,
'1.3.6.1.2.1.10.166.2.0': MPLS_LSR_STD_MIB.mplsLsrNotifications,
'1.3.6.1.2.1.10.166.2.1': MPLS_LSR_STD_MIB.mplsLsrObjects,
'1.3.6.1.2.1.10.166.2.2': MPLS_LSR_STD_MIB.mplsLsrConformance,
'1.3.6.1.2.1.10.166.2.2.1': MPLS_LSR_STD_MIB.mplsLsrGroups,
'1.3.6.1.2.1.10.166.2.2.2': MPLS_LSR_STD_MIB.mplsLsrCompliances,
'1.3.6.1.2.1.10.166.2.1.3': MPLS_LSR_STD_MIB.mplsInSegmentIndexNext,
'1.3.6.1.2.1.10.166.2.1.6': MPLS_LSR_STD_MIB.mplsOutSegmentIndexNext,
'1.3.6.1.2.1.10.166.2.1.9': MPLS_LSR_STD_MIB.mplsXCIndexNext,
'1.3.6.1.2.1.10.166.2.1.11': MPLS_LSR_STD_MIB.mplsMaxLabelStackDepth,
'1.3.6.1.2.1.10.166.2.1.12': MPLS_LSR_STD_MIB.mplsLabelStackIndexNext,
'1.3.6.1.2.1.10.166.2.1.15': MPLS_LSR_STD_MIB.mplsXCNotificationsEnable,
'1.3.6.1.2.1.10.166.2.1.1.1.1': MPLS_LSR_STD_MIB.mplsInterfaceIndex,
'1.3.6.1.2.1.10.166.2.1.1.1.2': MPLS_LSR_STD_MIB.mplsInterfaceLabelMinIn,
'1.3.6.1.2.1.10.166.2.1.1.1.3': MPLS_LSR_STD_MIB.mplsInterfaceLabelMaxIn,
'1.3.6.1.2.1.10.166.2.1.1.1.4': MPLS_LSR_STD_MIB.mplsInterfaceLabelMinOut,
'1.3.6.1.2.1.10.166.2.1.1.1.5': MPLS_LSR_STD_MIB.mplsInterfaceLabelMaxOut,
'1.3.6.1.2.1.10.166.2.1.1.1.6': MPLS_LSR_STD_MIB.mplsInterfaceTotalBandwidth,
'1.3.6.1.2.1.10.166.2.1.1.1.7': MPLS_LSR_STD_MIB.mplsInterfaceAvailableBandwidth,
'1.3.6.1.2.1.10.166.2.1.1.1.8': MPLS_LSR_STD_MIB.mplsInterfaceLabelParticipationType,
'1.3.6.1.2.1.10.166.2.1.2.1.1': MPLS_LSR_STD_MIB.mplsInterfacePerfInLabelsInUse,
'1.3.6.1.2.1.10.166.2.1.2.1.2': MPLS_LSR_STD_MIB.mplsInterfacePerfInLabelLookupFailures,
'1.3.6.1.2.1.10.166.2.1.2.1.3': MPLS_LSR_STD_MIB.mplsInterfacePerfOutLabelsInUse,
'1.3.6.1.2.1.10.166.2.1.2.1.4': MPLS_LSR_STD_MIB.mplsInterfacePerfOutFragmentedPkts,
'1.3.6.1.2.1.10.166.2.1.4.1.1': MPLS_LSR_STD_MIB.mplsInSegmentIndex,
'1.3.6.1.2.1.10.166.2.1.4.1.2': MPLS_LSR_STD_MIB.mplsInSegmentInterface,
'1.3.6.1.2.1.10.166.2.1.4.1.3': MPLS_LSR_STD_MIB.mplsInSegmentLabel,
'1.3.6.1.2.1.10.166.2.1.4.1.4': MPLS_LSR_STD_MIB.mplsInSegmentLabelPtr,
'1.3.6.1.2.1.10.166.2.1.4.1.5': MPLS_LSR_STD_MIB.mplsInSegmentNPop,
'1.3.6.1.2.1.10.166.2.1.4.1.6': MPLS_LSR_STD_MIB.mplsInSegmentAddrFamily,
'1.3.6.1.2.1.10.166.2.1.4.1.7': MPLS_LSR_STD_MIB.mplsInSegmentXCIndex,
'1.3.6.1.2.1.10.166.2.1.4.1.8': MPLS_LSR_STD_MIB.mplsInSegmentOwner,
'1.3.6.1.2.1.10.166.2.1.4.1.9': MPLS_LSR_STD_MIB.mplsInSegmentTrafficParamPtr,
'1.3.6.1.2.1.10.166.2.1.4.1.10': MPLS_LSR_STD_MIB.mplsInSegmentRowStatus,
'1.3.6.1.2.1.10.166.2.1.4.1.11': MPLS_LSR_STD_MIB.mplsInSegmentStorageType,
'1.3.6.1.2.1.10.166.2.1.5.1.1': MPLS_LSR_STD_MIB.mplsInSegmentPerfOctets,
'1.3.6.1.2.1.10.166.2.1.5.1.2': MPLS_LSR_STD_MIB.mplsInSegmentPerfPackets,
'1.3.6.1.2.1.10.166.2.1.5.1.3': MPLS_LSR_STD_MIB.mplsInSegmentPerfErrors,
'1.3.6.1.2.1.10.166.2.1.5.1.4': MPLS_LSR_STD_MIB.mplsInSegmentPerfDiscards,
'1.3.6.1.2.1.10.166.2.1.5.1.5': MPLS_LSR_STD_MIB.mplsInSegmentPerfHCOctets,
'1.3.6.1.2.1.10.166.2.1.5.1.6': MPLS_LSR_STD_MIB.mplsInSegmentPerfDiscontinuityTime,
'1.3.6.1.2.1.10.166.2.1.7.1.1': MPLS_LSR_STD_MIB.mplsOutSegmentIndex,
'1.3.6.1.2.1.10.166.2.1.7.1.2': MPLS_LSR_STD_MIB.mplsOutSegmentInterface,
'1.3.6.1.2.1.10.166.2.1.7.1.3': MPLS_LSR_STD_MIB.mplsOutSegmentPushTopLabel,
'1.3.6.1.2.1.10.166.2.1.7.1.4': MPLS_LSR_STD_MIB.mplsOutSegmentTopLabel,
'1.3.6.1.2.1.10.166.2.1.7.1.5': MPLS_LSR_STD_MIB.mplsOutSegmentTopLabelPtr,
'1.3.6.1.2.1.10.166.2.1.7.1.6': MPLS_LSR_STD_MIB.mplsOutSegmentNextHopAddrType,
'1.3.6.1.2.1.10.166.2.1.7.1.7': MPLS_LSR_STD_MIB.mplsOutSegmentNextHopAddr,
'1.3.6.1.2.1.10.166.2.1.7.1.8': MPLS_LSR_STD_MIB.mplsOutSegmentXCIndex,
'1.3.6.1.2.1.10.166.2.1.7.1.9': MPLS_LSR_STD_MIB.mplsOutSegmentOwner,
'1.3.6.1.2.1.10.166.2.1.7.1.10': MPLS_LSR_STD_MIB.mplsOutSegmentTrafficParamPtr,
'1.3.6.1.2.1.10.166.2.1.7.1.11': MPLS_LSR_STD_MIB.mplsOutSegmentRowStatus,
'1.3.6.1.2.1.10.166.2.1.7.1.12': MPLS_LSR_STD_MIB.mplsOutSegmentStorageType,
'1.3.6.1.2.1.10.166.2.1.8.1.1': MPLS_LSR_STD_MIB.mplsOutSegmentPerfOctets,
'1.3.6.1.2.1.10.166.2.1.8.1.2': MPLS_LSR_STD_MIB.mplsOutSegmentPerfPackets,
'1.3.6.1.2.1.10.166.2.1.8.1.3': MPLS_LSR_STD_MIB.mplsOutSegmentPerfErrors,
'1.3.6.1.2.1.10.166.2.1.8.1.4': MPLS_LSR_STD_MIB.mplsOutSegmentPerfDiscards,
'1.3.6.1.2.1.10.166.2.1.8.1.5': MPLS_LSR_STD_MIB.mplsOutSegmentPerfHCOctets,
'1.3.6.1.2.1.10.166.2.1.8.1.6': MPLS_LSR_STD_MIB.mplsOutSegmentPerfDiscontinuityTime,
'1.3.6.1.2.1.10.166.2.1.10.1.1': MPLS_LSR_STD_MIB.mplsXCIndex,
'1.3.6.1.2.1.10.166.2.1.10.1.2': MPLS_LSR_STD_MIB.mplsXCInSegmentIndex,
'1.3.6.1.2.1.10.166.2.1.10.1.3': MPLS_LSR_STD_MIB.mplsXCOutSegmentIndex,
'1.3.6.1.2.1.10.166.2.1.10.1.4': MPLS_LSR_STD_MIB.mplsXCLspId,
'1.3.6.1.2.1.10.166.2.1.10.1.5': MPLS_LSR_STD_MIB.mplsXCLabelStackIndex,
'1.3.6.1.2.1.10.166.2.1.10.1.6': MPLS_LSR_STD_MIB.mplsXCOwner,
'1.3.6.1.2.1.10.166.2.1.10.1.7': MPLS_LSR_STD_MIB.mplsXCRowStatus,
'1.3.6.1.2.1.10.166.2.1.10.1.8': MPLS_LSR_STD_MIB.mplsXCStorageType,
'1.3.6.1.2.1.10.166.2.1.10.1.9': MPLS_LSR_STD_MIB.mplsXCAdminStatus,
'1.3.6.1.2.1.10.166.2.1.10.1.10': MPLS_LSR_STD_MIB.mplsXCOperStatus,
'1.3.6.1.2.1.10.166.2.1.13.1.1': MPLS_LSR_STD_MIB.mplsLabelStackIndex,
'1.3.6.1.2.1.10.166.2.1.13.1.2': MPLS_LSR_STD_MIB.mplsLabelStackLabelIndex,
'1.3.6.1.2.1.10.166.2.1.13.1.3': MPLS_LSR_STD_MIB.mplsLabelStackLabel,
'1.3.6.1.2.1.10.166.2.1.13.1.4': MPLS_LSR_STD_MIB.mplsLabelStackLabelPtr,
'1.3.6.1.2.1.10.166.2.1.13.1.5': MPLS_LSR_STD_MIB.mplsLabelStackRowStatus,
'1.3.6.1.2.1.10.166.2.1.13.1.6': MPLS_LSR_STD_MIB.mplsLabelStackStorageType,
'1.3.6.1.2.1.10.166.2.1.14.1.1': MPLS_LSR_STD_MIB.mplsInSegmentMapInterface,
'1.3.6.1.2.1.10.166.2.1.14.1.2': MPLS_LSR_STD_MIB.mplsInSegmentMapLabel,
'1.3.6.1.2.1.10.166.2.1.14.1.3': MPLS_LSR_STD_MIB.mplsInSegmentMapLabelPtrIndex,
'1.3.6.1.2.1.10.166.2.1.14.1.4': MPLS_LSR_STD_MIB.mplsInSegmentMapIndex,
'1.3.6.1.2.1.10.166.2.0.1': MPLS_LSR_STD_MIB.mplsXCUp,
'1.3.6.1.2.1.10.166.2.0.2': MPLS_LSR_STD_MIB.mplsXCDown,
'1.3.6.1.2.1.10.166.2.2.1.1': MPLS_LSR_STD_MIB.mplsInterfaceGroup,
'1.3.6.1.2.1.10.166.2.2.1.2': MPLS_LSR_STD_MIB.mplsInSegmentGroup,
'1.3.6.1.2.1.10.166.2.2.1.3': MPLS_LSR_STD_MIB.mplsOutSegmentGroup,
'1.3.6.1.2.1.10.166.2.2.1.4': MPLS_LSR_STD_MIB.mplsXCGroup,
'1.3.6.1.2.1.10.166.2.2.1.5': MPLS_LSR_STD_MIB.mplsPerfGroup,
'1.3.6.1.2.1.10.166.2.2.1.6': MPLS_LSR_STD_MIB.mplsHCInSegmentPerfGroup,
'1.3.6.1.2.1.10.166.2.2.1.7': MPLS_LSR_STD_MIB.mplsHCOutSegmentPerfGroup,
'1.3.6.1.2.1.10.166.2.2.1.8': MPLS_LSR_STD_MIB.mplsLabelStackGroup,
'1.3.6.1.2.1.10.166.2.2.1.9': MPLS_LSR_STD_MIB.mplsLsrNotificationGroup,
}
