# python
# This file is generated by a program (mib2py). 

import RSVP_MIB

OIDMAP = {
'1.3.6.1.2.1.51': RSVP_MIB.rsvp,
'1.3.6.1.2.1.51.1': RSVP_MIB.rsvpObjects,
'1.3.6.1.2.1.51.2': RSVP_MIB.rsvpGenObjects,
'1.3.6.1.2.1.51.3': RSVP_MIB.rsvpNotificationsPrefix,
'1.3.6.1.2.1.51.3.0': RSVP_MIB.rsvpNotifications,
'1.3.6.1.2.1.51.4': RSVP_MIB.rsvpConformance,
'1.3.6.1.2.1.51.4.1': RSVP_MIB.rsvpGroups,
'1.3.6.1.2.1.51.4.2': RSVP_MIB.rsvpCompliances,
'1.3.6.1.2.1.51.2.1': RSVP_MIB.rsvpBadPackets,
'1.3.6.1.2.1.51.2.2': RSVP_MIB.rsvpSenderNewIndex,
'1.3.6.1.2.1.51.2.3': RSVP_MIB.rsvpResvNewIndex,
'1.3.6.1.2.1.51.2.4': RSVP_MIB.rsvpResvFwdNewIndex,
'1.3.6.1.2.1.51.1.1.1.1': RSVP_MIB.rsvpSessionNumber,
'1.3.6.1.2.1.51.1.1.1.2': RSVP_MIB.rsvpSessionType,
'1.3.6.1.2.1.51.1.1.1.3': RSVP_MIB.rsvpSessionDestAddr,
'1.3.6.1.2.1.51.1.1.1.4': RSVP_MIB.rsvpSessionDestAddrLength,
'1.3.6.1.2.1.51.1.1.1.5': RSVP_MIB.rsvpSessionProtocol,
'1.3.6.1.2.1.51.1.1.1.6': RSVP_MIB.rsvpSessionPort,
'1.3.6.1.2.1.51.1.1.1.7': RSVP_MIB.rsvpSessionSenders,
'1.3.6.1.2.1.51.1.1.1.8': RSVP_MIB.rsvpSessionReceivers,
'1.3.6.1.2.1.51.1.1.1.9': RSVP_MIB.rsvpSessionRequests,
'1.3.6.1.2.1.51.1.2.1.1': RSVP_MIB.rsvpSenderNumber,
'1.3.6.1.2.1.51.1.2.1.2': RSVP_MIB.rsvpSenderType,
'1.3.6.1.2.1.51.1.2.1.3': RSVP_MIB.rsvpSenderDestAddr,
'1.3.6.1.2.1.51.1.2.1.4': RSVP_MIB.rsvpSenderAddr,
'1.3.6.1.2.1.51.1.2.1.5': RSVP_MIB.rsvpSenderDestAddrLength,
'1.3.6.1.2.1.51.1.2.1.6': RSVP_MIB.rsvpSenderAddrLength,
'1.3.6.1.2.1.51.1.2.1.7': RSVP_MIB.rsvpSenderProtocol,
'1.3.6.1.2.1.51.1.2.1.8': RSVP_MIB.rsvpSenderDestPort,
'1.3.6.1.2.1.51.1.2.1.9': RSVP_MIB.rsvpSenderPort,
'1.3.6.1.2.1.51.1.2.1.10': RSVP_MIB.rsvpSenderFlowId,
'1.3.6.1.2.1.51.1.2.1.11': RSVP_MIB.rsvpSenderHopAddr,
'1.3.6.1.2.1.51.1.2.1.12': RSVP_MIB.rsvpSenderHopLih,
'1.3.6.1.2.1.51.1.2.1.13': RSVP_MIB.rsvpSenderInterface,
'1.3.6.1.2.1.51.1.2.1.14': RSVP_MIB.rsvpSenderTSpecRate,
'1.3.6.1.2.1.51.1.2.1.15': RSVP_MIB.rsvpSenderTSpecPeakRate,
'1.3.6.1.2.1.51.1.2.1.16': RSVP_MIB.rsvpSenderTSpecBurst,
'1.3.6.1.2.1.51.1.2.1.17': RSVP_MIB.rsvpSenderTSpecMinTU,
'1.3.6.1.2.1.51.1.2.1.18': RSVP_MIB.rsvpSenderTSpecMaxTU,
'1.3.6.1.2.1.51.1.2.1.19': RSVP_MIB.rsvpSenderInterval,
'1.3.6.1.2.1.51.1.2.1.20': RSVP_MIB.rsvpSenderRSVPHop,
'1.3.6.1.2.1.51.1.2.1.21': RSVP_MIB.rsvpSenderLastChange,
'1.3.6.1.2.1.51.1.2.1.22': RSVP_MIB.rsvpSenderPolicy,
'1.3.6.1.2.1.51.1.2.1.23': RSVP_MIB.rsvpSenderAdspecBreak,
'1.3.6.1.2.1.51.1.2.1.24': RSVP_MIB.rsvpSenderAdspecHopCount,
'1.3.6.1.2.1.51.1.2.1.25': RSVP_MIB.rsvpSenderAdspecPathBw,
'1.3.6.1.2.1.51.1.2.1.26': RSVP_MIB.rsvpSenderAdspecMinLatency,
'1.3.6.1.2.1.51.1.2.1.27': RSVP_MIB.rsvpSenderAdspecMtu,
'1.3.6.1.2.1.51.1.2.1.28': RSVP_MIB.rsvpSenderAdspecGuaranteedSvc,
'1.3.6.1.2.1.51.1.2.1.29': RSVP_MIB.rsvpSenderAdspecGuaranteedBreak,
'1.3.6.1.2.1.51.1.2.1.30': RSVP_MIB.rsvpSenderAdspecGuaranteedCtot,
'1.3.6.1.2.1.51.1.2.1.31': RSVP_MIB.rsvpSenderAdspecGuaranteedDtot,
'1.3.6.1.2.1.51.1.2.1.32': RSVP_MIB.rsvpSenderAdspecGuaranteedCsum,
'1.3.6.1.2.1.51.1.2.1.33': RSVP_MIB.rsvpSenderAdspecGuaranteedDsum,
'1.3.6.1.2.1.51.1.2.1.34': RSVP_MIB.rsvpSenderAdspecGuaranteedHopCount,
'1.3.6.1.2.1.51.1.2.1.35': RSVP_MIB.rsvpSenderAdspecGuaranteedPathBw,
'1.3.6.1.2.1.51.1.2.1.36': RSVP_MIB.rsvpSenderAdspecGuaranteedMinLatency,
'1.3.6.1.2.1.51.1.2.1.37': RSVP_MIB.rsvpSenderAdspecGuaranteedMtu,
'1.3.6.1.2.1.51.1.2.1.38': RSVP_MIB.rsvpSenderAdspecCtrlLoadSvc,
'1.3.6.1.2.1.51.1.2.1.39': RSVP_MIB.rsvpSenderAdspecCtrlLoadBreak,
'1.3.6.1.2.1.51.1.2.1.40': RSVP_MIB.rsvpSenderAdspecCtrlLoadHopCount,
'1.3.6.1.2.1.51.1.2.1.41': RSVP_MIB.rsvpSenderAdspecCtrlLoadPathBw,
'1.3.6.1.2.1.51.1.2.1.42': RSVP_MIB.rsvpSenderAdspecCtrlLoadMinLatency,
'1.3.6.1.2.1.51.1.2.1.43': RSVP_MIB.rsvpSenderAdspecCtrlLoadMtu,
'1.3.6.1.2.1.51.1.2.1.44': RSVP_MIB.rsvpSenderStatus,
'1.3.6.1.2.1.51.1.2.1.45': RSVP_MIB.rsvpSenderTTL,
'1.3.6.1.2.1.51.1.3.1.1': RSVP_MIB.rsvpSenderOutInterfaceStatus,
'1.3.6.1.2.1.51.1.4.1.1': RSVP_MIB.rsvpResvNumber,
'1.3.6.1.2.1.51.1.4.1.2': RSVP_MIB.rsvpResvType,
'1.3.6.1.2.1.51.1.4.1.3': RSVP_MIB.rsvpResvDestAddr,
'1.3.6.1.2.1.51.1.4.1.4': RSVP_MIB.rsvpResvSenderAddr,
'1.3.6.1.2.1.51.1.4.1.5': RSVP_MIB.rsvpResvDestAddrLength,
'1.3.6.1.2.1.51.1.4.1.6': RSVP_MIB.rsvpResvSenderAddrLength,
'1.3.6.1.2.1.51.1.4.1.7': RSVP_MIB.rsvpResvProtocol,
'1.3.6.1.2.1.51.1.4.1.8': RSVP_MIB.rsvpResvDestPort,
'1.3.6.1.2.1.51.1.4.1.9': RSVP_MIB.rsvpResvPort,
'1.3.6.1.2.1.51.1.4.1.10': RSVP_MIB.rsvpResvHopAddr,
'1.3.6.1.2.1.51.1.4.1.11': RSVP_MIB.rsvpResvHopLih,
'1.3.6.1.2.1.51.1.4.1.12': RSVP_MIB.rsvpResvInterface,
'1.3.6.1.2.1.51.1.4.1.13': RSVP_MIB.rsvpResvService,
'1.3.6.1.2.1.51.1.4.1.14': RSVP_MIB.rsvpResvTSpecRate,
'1.3.6.1.2.1.51.1.4.1.15': RSVP_MIB.rsvpResvTSpecPeakRate,
'1.3.6.1.2.1.51.1.4.1.16': RSVP_MIB.rsvpResvTSpecBurst,
'1.3.6.1.2.1.51.1.4.1.17': RSVP_MIB.rsvpResvTSpecMinTU,
'1.3.6.1.2.1.51.1.4.1.18': RSVP_MIB.rsvpResvTSpecMaxTU,
'1.3.6.1.2.1.51.1.4.1.19': RSVP_MIB.rsvpResvRSpecRate,
'1.3.6.1.2.1.51.1.4.1.20': RSVP_MIB.rsvpResvRSpecSlack,
'1.3.6.1.2.1.51.1.4.1.21': RSVP_MIB.rsvpResvInterval,
'1.3.6.1.2.1.51.1.4.1.22': RSVP_MIB.rsvpResvScope,
'1.3.6.1.2.1.51.1.4.1.23': RSVP_MIB.rsvpResvShared,
'1.3.6.1.2.1.51.1.4.1.24': RSVP_MIB.rsvpResvExplicit,
'1.3.6.1.2.1.51.1.4.1.25': RSVP_MIB.rsvpResvRSVPHop,
'1.3.6.1.2.1.51.1.4.1.26': RSVP_MIB.rsvpResvLastChange,
'1.3.6.1.2.1.51.1.4.1.27': RSVP_MIB.rsvpResvPolicy,
'1.3.6.1.2.1.51.1.4.1.28': RSVP_MIB.rsvpResvStatus,
'1.3.6.1.2.1.51.1.4.1.29': RSVP_MIB.rsvpResvTTL,
'1.3.6.1.2.1.51.1.4.1.30': RSVP_MIB.rsvpResvFlowId,
'1.3.6.1.2.1.51.1.5.1.1': RSVP_MIB.rsvpResvFwdNumber,
'1.3.6.1.2.1.51.1.5.1.2': RSVP_MIB.rsvpResvFwdType,
'1.3.6.1.2.1.51.1.5.1.3': RSVP_MIB.rsvpResvFwdDestAddr,
'1.3.6.1.2.1.51.1.5.1.4': RSVP_MIB.rsvpResvFwdSenderAddr,
'1.3.6.1.2.1.51.1.5.1.5': RSVP_MIB.rsvpResvFwdDestAddrLength,
'1.3.6.1.2.1.51.1.5.1.6': RSVP_MIB.rsvpResvFwdSenderAddrLength,
'1.3.6.1.2.1.51.1.5.1.7': RSVP_MIB.rsvpResvFwdProtocol,
'1.3.6.1.2.1.51.1.5.1.8': RSVP_MIB.rsvpResvFwdDestPort,
'1.3.6.1.2.1.51.1.5.1.9': RSVP_MIB.rsvpResvFwdPort,
'1.3.6.1.2.1.51.1.5.1.10': RSVP_MIB.rsvpResvFwdHopAddr,
'1.3.6.1.2.1.51.1.5.1.11': RSVP_MIB.rsvpResvFwdHopLih,
'1.3.6.1.2.1.51.1.5.1.12': RSVP_MIB.rsvpResvFwdInterface,
'1.3.6.1.2.1.51.1.5.1.13': RSVP_MIB.rsvpResvFwdService,
'1.3.6.1.2.1.51.1.5.1.14': RSVP_MIB.rsvpResvFwdTSpecRate,
'1.3.6.1.2.1.51.1.5.1.15': RSVP_MIB.rsvpResvFwdTSpecPeakRate,
'1.3.6.1.2.1.51.1.5.1.16': RSVP_MIB.rsvpResvFwdTSpecBurst,
'1.3.6.1.2.1.51.1.5.1.17': RSVP_MIB.rsvpResvFwdTSpecMinTU,
'1.3.6.1.2.1.51.1.5.1.18': RSVP_MIB.rsvpResvFwdTSpecMaxTU,
'1.3.6.1.2.1.51.1.5.1.19': RSVP_MIB.rsvpResvFwdRSpecRate,
'1.3.6.1.2.1.51.1.5.1.20': RSVP_MIB.rsvpResvFwdRSpecSlack,
'1.3.6.1.2.1.51.1.5.1.21': RSVP_MIB.rsvpResvFwdInterval,
'1.3.6.1.2.1.51.1.5.1.22': RSVP_MIB.rsvpResvFwdScope,
'1.3.6.1.2.1.51.1.5.1.23': RSVP_MIB.rsvpResvFwdShared,
'1.3.6.1.2.1.51.1.5.1.24': RSVP_MIB.rsvpResvFwdExplicit,
'1.3.6.1.2.1.51.1.5.1.25': RSVP_MIB.rsvpResvFwdRSVPHop,
'1.3.6.1.2.1.51.1.5.1.26': RSVP_MIB.rsvpResvFwdLastChange,
'1.3.6.1.2.1.51.1.5.1.27': RSVP_MIB.rsvpResvFwdPolicy,
'1.3.6.1.2.1.51.1.5.1.28': RSVP_MIB.rsvpResvFwdStatus,
'1.3.6.1.2.1.51.1.5.1.29': RSVP_MIB.rsvpResvFwdTTL,
'1.3.6.1.2.1.51.1.5.1.30': RSVP_MIB.rsvpResvFwdFlowId,
'1.3.6.1.2.1.51.1.6.1.1': RSVP_MIB.rsvpIfUdpNbrs,
'1.3.6.1.2.1.51.1.6.1.2': RSVP_MIB.rsvpIfIpNbrs,
'1.3.6.1.2.1.51.1.6.1.3': RSVP_MIB.rsvpIfNbrs,
'1.3.6.1.2.1.51.1.6.1.4': RSVP_MIB.rsvpIfRefreshBlockadeMultiple,
'1.3.6.1.2.1.51.1.6.1.5': RSVP_MIB.rsvpIfRefreshMultiple,
'1.3.6.1.2.1.51.1.6.1.6': RSVP_MIB.rsvpIfTTL,
'1.3.6.1.2.1.51.1.6.1.7': RSVP_MIB.rsvpIfRefreshInterval,
'1.3.6.1.2.1.51.1.6.1.8': RSVP_MIB.rsvpIfRouteDelay,
'1.3.6.1.2.1.51.1.6.1.9': RSVP_MIB.rsvpIfEnabled,
'1.3.6.1.2.1.51.1.6.1.10': RSVP_MIB.rsvpIfUdpRequired,
'1.3.6.1.2.1.51.1.6.1.11': RSVP_MIB.rsvpIfStatus,
'1.3.6.1.2.1.51.1.7.1.1': RSVP_MIB.rsvpNbrAddress,
'1.3.6.1.2.1.51.1.7.1.2': RSVP_MIB.rsvpNbrProtocol,
'1.3.6.1.2.1.51.1.7.1.3': RSVP_MIB.rsvpNbrStatus,
'1.3.6.1.2.1.51.3.0.1': RSVP_MIB.newFlow,
'1.3.6.1.2.1.51.3.0.2': RSVP_MIB.lostFlow,
'1.3.6.1.2.1.51.4.1.1': RSVP_MIB.rsvpSessionGroup,
'1.3.6.1.2.1.51.4.1.2': RSVP_MIB.rsvpSenderGroup,
'1.3.6.1.2.1.51.4.1.3': RSVP_MIB.rsvpResvGroup,
'1.3.6.1.2.1.51.4.1.4': RSVP_MIB.rsvpResvFwdGroup,
'1.3.6.1.2.1.51.4.1.6': RSVP_MIB.rsvpIfGroup,
'1.3.6.1.2.1.51.4.1.7': RSVP_MIB.rsvpNbrGroup,
'1.3.6.1.2.1.51.4.1.8': RSVP_MIB.rsvpNotificationGroup,
}
