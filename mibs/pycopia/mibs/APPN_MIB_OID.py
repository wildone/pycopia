# python
# This file is generated by a program (mib2py). 

import APPN_MIB

OIDMAP = {
'1.3.6.1.2.1.34.4': APPN_MIB.appnMIB,
'1.3.6.1.2.1.34.4.1': APPN_MIB.appnObjects,
'1.3.6.1.2.1.34.4.1.1': APPN_MIB.appnNode,
'1.3.6.1.2.1.34.4.1.1.1': APPN_MIB.appnGeneralInfoAndCaps,
'1.3.6.1.2.1.34.4.1.1.2': APPN_MIB.appnNnUniqueInfoAndCaps,
'1.3.6.1.2.1.34.4.1.1.3': APPN_MIB.appnEnUniqueCaps,
'1.3.6.1.2.1.34.4.1.1.4': APPN_MIB.appnPortInformation,
'1.3.6.1.2.1.34.4.1.1.5': APPN_MIB.appnLinkStationInformation,
'1.3.6.1.2.1.34.4.1.1.6': APPN_MIB.appnVrnInfo,
'1.3.6.1.2.1.34.4.1.2': APPN_MIB.appnNn,
'1.3.6.1.2.1.34.4.1.2.1': APPN_MIB.appnNnTopo,
'1.3.6.1.2.1.34.4.1.2.2': APPN_MIB.appnNnTopology,
'1.3.6.1.2.1.34.4.1.3': APPN_MIB.appnLocalTopology,
'1.3.6.1.2.1.34.4.1.4': APPN_MIB.appnDir,
'1.3.6.1.2.1.34.4.1.4.1': APPN_MIB.appnDirPerf,
'1.3.6.1.2.1.34.4.1.5': APPN_MIB.appnCos,
'1.3.6.1.2.1.34.4.1.6': APPN_MIB.appnSessIntermediate,
'1.3.6.1.2.1.34.4.1.6.1': APPN_MIB.appnIsInGlobal,
'1.3.6.1.2.1.34.4.2': APPN_MIB.appnTraps,
'1.3.6.1.2.1.34.4.3': APPN_MIB.appnConformance,
'1.3.6.1.2.1.34.4.3.1': APPN_MIB.appnCompliances,
'1.3.6.1.2.1.34.4.3.2': APPN_MIB.appnGroups,
'1.3.6.1.2.1.34.4.1.1.1.1': APPN_MIB.appnNodeCpName,
'1.3.6.1.2.1.34.4.1.1.1.2': APPN_MIB.appnNodeMibVersion,
'1.3.6.1.2.1.34.4.1.1.1.3': APPN_MIB.appnNodeId,
'1.3.6.1.2.1.34.4.1.1.1.4': APPN_MIB.appnNodeType,
'1.3.6.1.2.1.34.4.1.1.1.5': APPN_MIB.appnNodeUpTime,
'1.3.6.1.2.1.34.4.1.1.1.6': APPN_MIB.appnNodeParallelTg,
'1.3.6.1.2.1.34.4.1.1.1.7': APPN_MIB.appnNodeAdaptiveBindPacing,
'1.3.6.1.2.1.34.4.1.1.1.8': APPN_MIB.appnNodeHprSupport,
'1.3.6.1.2.1.34.4.1.1.1.9': APPN_MIB.appnNodeMaxSessPerRtpConn,
'1.3.6.1.2.1.34.4.1.1.1.10': APPN_MIB.appnNodeHprIntRteSetups,
'1.3.6.1.2.1.34.4.1.1.1.11': APPN_MIB.appnNodeHprIntRteRejects,
'1.3.6.1.2.1.34.4.1.1.1.12': APPN_MIB.appnNodeHprOrgRteSetups,
'1.3.6.1.2.1.34.4.1.1.1.13': APPN_MIB.appnNodeHprOrgRteRejects,
'1.3.6.1.2.1.34.4.1.1.1.14': APPN_MIB.appnNodeHprEndRteSetups,
'1.3.6.1.2.1.34.4.1.1.1.15': APPN_MIB.appnNodeHprEndRteRejects,
'1.3.6.1.2.1.34.4.1.1.1.16': APPN_MIB.appnNodeCounterDisconTime,
'1.3.6.1.2.1.34.4.1.1.1.17': APPN_MIB.appnNodeLsCounterType,
'1.3.6.1.2.1.34.4.1.1.1.18': APPN_MIB.appnNodeBrNn,
'1.3.6.1.2.1.34.4.1.1.2.1': APPN_MIB.appnNodeNnCentralDirectory,
'1.3.6.1.2.1.34.4.1.1.2.2': APPN_MIB.appnNodeNnTreeCache,
'1.3.6.1.2.1.34.4.1.1.2.3': APPN_MIB.appnNodeNnRouteAddResist,
'1.3.6.1.2.1.34.4.1.1.2.4': APPN_MIB.appnNodeNnIsr,
'1.3.6.1.2.1.34.4.1.1.2.5': APPN_MIB.appnNodeNnFrsn,
'1.3.6.1.2.1.34.4.1.1.2.6': APPN_MIB.appnNodeNnPeriBorderSup,
'1.3.6.1.2.1.34.4.1.1.2.7': APPN_MIB.appnNodeNnInterchangeSup,
'1.3.6.1.2.1.34.4.1.1.2.8': APPN_MIB.appnNodeNnExteBorderSup,
'1.3.6.1.2.1.34.4.1.1.2.9': APPN_MIB.appnNodeNnSafeStoreFreq,
'1.3.6.1.2.1.34.4.1.1.2.10': APPN_MIB.appnNodeNnRsn,
'1.3.6.1.2.1.34.4.1.1.2.11': APPN_MIB.appnNodeNnCongested,
'1.3.6.1.2.1.34.4.1.1.2.12': APPN_MIB.appnNodeNnIsrDepleted,
'1.3.6.1.2.1.34.4.1.1.2.13': APPN_MIB.appnNodeNnQuiescing,
'1.3.6.1.2.1.34.4.1.1.2.14': APPN_MIB.appnNodeNnGateway,
'1.3.6.1.2.1.34.4.1.1.3.1': APPN_MIB.appnNodeEnModeCosMap,
'1.3.6.1.2.1.34.4.1.1.3.2': APPN_MIB.appnNodeEnNnServer,
'1.3.6.1.2.1.34.4.1.1.3.3': APPN_MIB.appnNodeEnLuSearch,
'1.3.6.1.2.1.34.4.1.2.1.1': APPN_MIB.appnNnTopoMaxNodes,
'1.3.6.1.2.1.34.4.1.2.1.2': APPN_MIB.appnNnTopoCurNumNodes,
'1.3.6.1.2.1.34.4.1.2.1.3': APPN_MIB.appnNnTopoNodePurges,
'1.3.6.1.2.1.34.4.1.2.1.4': APPN_MIB.appnNnTopoTgPurges,
'1.3.6.1.2.1.34.4.1.2.1.5': APPN_MIB.appnNnTopoTotalTduWars,
'1.3.6.1.2.1.34.4.1.4.1.1': APPN_MIB.appnDirMaxCaches,
'1.3.6.1.2.1.34.4.1.4.1.2': APPN_MIB.appnDirCurCaches,
'1.3.6.1.2.1.34.4.1.4.1.3': APPN_MIB.appnDirCurHomeEntries,
'1.3.6.1.2.1.34.4.1.4.1.4': APPN_MIB.appnDirRegEntries,
'1.3.6.1.2.1.34.4.1.4.1.5': APPN_MIB.appnDirInLocates,
'1.3.6.1.2.1.34.4.1.4.1.6': APPN_MIB.appnDirInBcastLocates,
'1.3.6.1.2.1.34.4.1.4.1.7': APPN_MIB.appnDirOutLocates,
'1.3.6.1.2.1.34.4.1.4.1.8': APPN_MIB.appnDirOutBcastLocates,
'1.3.6.1.2.1.34.4.1.4.1.9': APPN_MIB.appnDirNotFoundLocates,
'1.3.6.1.2.1.34.4.1.4.1.10': APPN_MIB.appnDirNotFoundBcastLocates,
'1.3.6.1.2.1.34.4.1.4.1.11': APPN_MIB.appnDirLocateOutstands,
'1.3.6.1.2.1.34.4.1.6.1.1': APPN_MIB.appnIsInGlobeCtrAdminStatus,
'1.3.6.1.2.1.34.4.1.6.1.2': APPN_MIB.appnIsInGlobeCtrOperStatus,
'1.3.6.1.2.1.34.4.1.6.1.3': APPN_MIB.appnIsInGlobeCtrStatusTime,
'1.3.6.1.2.1.34.4.1.6.1.4': APPN_MIB.appnIsInGlobeRscv,
'1.3.6.1.2.1.34.4.1.6.1.5': APPN_MIB.appnIsInGlobeRscvTime,
'1.3.6.1.2.1.34.4.1.6.1.6': APPN_MIB.appnIsInGlobeActSess,
'1.3.6.1.2.1.34.4.1.6.1.7': APPN_MIB.appnIsInGlobeHprBfActSess,
'1.3.6.1.2.1.34.4.2.2': APPN_MIB.alertIdNumber,
'1.3.6.1.2.1.34.4.2.3': APPN_MIB.affectedObject,
'1.3.6.1.2.1.34.4.1.1.4.1.1.1': APPN_MIB.appnPortName,
'1.3.6.1.2.1.34.4.1.1.4.1.1.2': APPN_MIB.appnPortCommand,
'1.3.6.1.2.1.34.4.1.1.4.1.1.3': APPN_MIB.appnPortOperState,
'1.3.6.1.2.1.34.4.1.1.4.1.1.4': APPN_MIB.appnPortDlcType,
'1.3.6.1.2.1.34.4.1.1.4.1.1.5': APPN_MIB.appnPortPortType,
'1.3.6.1.2.1.34.4.1.1.4.1.1.6': APPN_MIB.appnPortSIMRIM,
'1.3.6.1.2.1.34.4.1.1.4.1.1.7': APPN_MIB.appnPortLsRole,
'1.3.6.1.2.1.34.4.1.1.4.1.1.8': APPN_MIB.appnPortNegotLs,
'1.3.6.1.2.1.34.4.1.1.4.1.1.9': APPN_MIB.appnPortDynamicLinkSupport,
'1.3.6.1.2.1.34.4.1.1.4.1.1.10': APPN_MIB.appnPortMaxRcvBtuSize,
'1.3.6.1.2.1.34.4.1.1.4.1.1.11': APPN_MIB.appnPortMaxIframeWindow,
'1.3.6.1.2.1.34.4.1.1.4.1.1.12': APPN_MIB.appnPortDefLsGoodXids,
'1.3.6.1.2.1.34.4.1.1.4.1.1.13': APPN_MIB.appnPortDefLsBadXids,
'1.3.6.1.2.1.34.4.1.1.4.1.1.14': APPN_MIB.appnPortDynLsGoodXids,
'1.3.6.1.2.1.34.4.1.1.4.1.1.15': APPN_MIB.appnPortDynLsBadXids,
'1.3.6.1.2.1.34.4.1.1.4.1.1.16': APPN_MIB.appnPortSpecific,
'1.3.6.1.2.1.34.4.1.1.4.1.1.17': APPN_MIB.appnPortDlcLocalAddr,
'1.3.6.1.2.1.34.4.1.1.4.1.1.18': APPN_MIB.appnPortCounterDisconTime,
'1.3.6.1.2.1.34.4.1.1.5.1.1.1': APPN_MIB.appnLsName,
'1.3.6.1.2.1.34.4.1.1.5.1.1.2': APPN_MIB.appnLsCommand,
'1.3.6.1.2.1.34.4.1.1.5.1.1.3': APPN_MIB.appnLsOperState,
'1.3.6.1.2.1.34.4.1.1.5.1.1.4': APPN_MIB.appnLsPortName,
'1.3.6.1.2.1.34.4.1.1.5.1.1.5': APPN_MIB.appnLsDlcType,
'1.3.6.1.2.1.34.4.1.1.5.1.1.6': APPN_MIB.appnLsDynamic,
'1.3.6.1.2.1.34.4.1.1.5.1.1.7': APPN_MIB.appnLsAdjCpName,
'1.3.6.1.2.1.34.4.1.1.5.1.1.8': APPN_MIB.appnLsAdjNodeType,
'1.3.6.1.2.1.34.4.1.1.5.1.1.9': APPN_MIB.appnLsTgNum,
'1.3.6.1.2.1.34.4.1.1.5.1.1.10': APPN_MIB.appnLsLimResource,
'1.3.6.1.2.1.34.4.1.1.5.1.1.11': APPN_MIB.appnLsActOnDemand,
'1.3.6.1.2.1.34.4.1.1.5.1.1.12': APPN_MIB.appnLsMigration,
'1.3.6.1.2.1.34.4.1.1.5.1.1.13': APPN_MIB.appnLsPartnerNodeId,
'1.3.6.1.2.1.34.4.1.1.5.1.1.14': APPN_MIB.appnLsCpCpSessionSupport,
'1.3.6.1.2.1.34.4.1.1.5.1.1.15': APPN_MIB.appnLsMaxSendBtuSize,
'1.3.6.1.2.1.34.4.1.1.5.1.1.16': APPN_MIB.appnLsInXidBytes,
'1.3.6.1.2.1.34.4.1.1.5.1.1.17': APPN_MIB.appnLsInMsgBytes,
'1.3.6.1.2.1.34.4.1.1.5.1.1.18': APPN_MIB.appnLsInXidFrames,
'1.3.6.1.2.1.34.4.1.1.5.1.1.19': APPN_MIB.appnLsInMsgFrames,
'1.3.6.1.2.1.34.4.1.1.5.1.1.20': APPN_MIB.appnLsOutXidBytes,
'1.3.6.1.2.1.34.4.1.1.5.1.1.21': APPN_MIB.appnLsOutMsgBytes,
'1.3.6.1.2.1.34.4.1.1.5.1.1.22': APPN_MIB.appnLsOutXidFrames,
'1.3.6.1.2.1.34.4.1.1.5.1.1.23': APPN_MIB.appnLsOutMsgFrames,
'1.3.6.1.2.1.34.4.1.1.5.1.1.24': APPN_MIB.appnLsEchoRsps,
'1.3.6.1.2.1.34.4.1.1.5.1.1.25': APPN_MIB.appnLsCurrentDelay,
'1.3.6.1.2.1.34.4.1.1.5.1.1.26': APPN_MIB.appnLsMaxDelay,
'1.3.6.1.2.1.34.4.1.1.5.1.1.27': APPN_MIB.appnLsMinDelay,
'1.3.6.1.2.1.34.4.1.1.5.1.1.28': APPN_MIB.appnLsMaxDelayTime,
'1.3.6.1.2.1.34.4.1.1.5.1.1.29': APPN_MIB.appnLsGoodXids,
'1.3.6.1.2.1.34.4.1.1.5.1.1.30': APPN_MIB.appnLsBadXids,
'1.3.6.1.2.1.34.4.1.1.5.1.1.31': APPN_MIB.appnLsSpecific,
'1.3.6.1.2.1.34.4.1.1.5.1.1.32': APPN_MIB.appnLsActiveTime,
'1.3.6.1.2.1.34.4.1.1.5.1.1.33': APPN_MIB.appnLsCurrentStateTime,
'1.3.6.1.2.1.34.4.1.1.5.1.1.34': APPN_MIB.appnLsHprSup,
'1.3.6.1.2.1.34.4.1.1.5.1.1.35': APPN_MIB.appnLsErrRecoSup,
'1.3.6.1.2.1.34.4.1.1.5.1.1.36': APPN_MIB.appnLsForAnrLabel,
'1.3.6.1.2.1.34.4.1.1.5.1.1.37': APPN_MIB.appnLsRevAnrLabel,
'1.3.6.1.2.1.34.4.1.1.5.1.1.38': APPN_MIB.appnLsCpCpNceId,
'1.3.6.1.2.1.34.4.1.1.5.1.1.39': APPN_MIB.appnLsRouteNceId,
'1.3.6.1.2.1.34.4.1.1.5.1.1.40': APPN_MIB.appnLsBfNceId,
'1.3.6.1.2.1.34.4.1.1.5.1.1.41': APPN_MIB.appnLsLocalAddr,
'1.3.6.1.2.1.34.4.1.1.5.1.1.42': APPN_MIB.appnLsRemoteAddr,
'1.3.6.1.2.1.34.4.1.1.5.1.1.43': APPN_MIB.appnLsRemoteLsName,
'1.3.6.1.2.1.34.4.1.1.5.1.1.44': APPN_MIB.appnLsCounterDisconTime,
'1.3.6.1.2.1.34.4.1.1.5.1.1.45': APPN_MIB.appnLsMltgMember,
'1.3.6.1.2.1.34.4.1.1.5.2.1.1': APPN_MIB.appnLsStatusIndex,
'1.3.6.1.2.1.34.4.1.1.5.2.1.2': APPN_MIB.appnLsStatusTime,
'1.3.6.1.2.1.34.4.1.1.5.2.1.3': APPN_MIB.appnLsStatusLsName,
'1.3.6.1.2.1.34.4.1.1.5.2.1.4': APPN_MIB.appnLsStatusCpName,
'1.3.6.1.2.1.34.4.1.1.5.2.1.5': APPN_MIB.appnLsStatusPartnerId,
'1.3.6.1.2.1.34.4.1.1.5.2.1.6': APPN_MIB.appnLsStatusTgNum,
'1.3.6.1.2.1.34.4.1.1.5.2.1.7': APPN_MIB.appnLsStatusGeneralSense,
'1.3.6.1.2.1.34.4.1.1.5.2.1.8': APPN_MIB.appnLsStatusRetry,
'1.3.6.1.2.1.34.4.1.1.5.2.1.9': APPN_MIB.appnLsStatusEndSense,
'1.3.6.1.2.1.34.4.1.1.5.2.1.10': APPN_MIB.appnLsStatusXidLocalSense,
'1.3.6.1.2.1.34.4.1.1.5.2.1.11': APPN_MIB.appnLsStatusXidRemoteSense,
'1.3.6.1.2.1.34.4.1.1.5.2.1.12': APPN_MIB.appnLsStatusXidByteInError,
'1.3.6.1.2.1.34.4.1.1.5.2.1.13': APPN_MIB.appnLsStatusXidBitInError,
'1.3.6.1.2.1.34.4.1.1.5.2.1.14': APPN_MIB.appnLsStatusDlcType,
'1.3.6.1.2.1.34.4.1.1.5.2.1.15': APPN_MIB.appnLsStatusLocalAddr,
'1.3.6.1.2.1.34.4.1.1.5.2.1.16': APPN_MIB.appnLsStatusRemoteAddr,
'1.3.6.1.2.1.34.4.1.1.6.1.1.1': APPN_MIB.appnVrnName,
'1.3.6.1.2.1.34.4.1.1.6.1.1.2': APPN_MIB.appnVrnTgNum,
'1.3.6.1.2.1.34.4.1.1.6.1.1.3': APPN_MIB.appnVrnPortName,
'1.3.6.1.2.1.34.4.1.2.2.3.1.1': APPN_MIB.appnNnNodeFRFrsn,
'1.3.6.1.2.1.34.4.1.2.2.3.1.2': APPN_MIB.appnNnNodeFRName,
'1.3.6.1.2.1.34.4.1.2.2.3.1.3': APPN_MIB.appnNnNodeFREntryTimeLeft,
'1.3.6.1.2.1.34.4.1.2.2.3.1.4': APPN_MIB.appnNnNodeFRType,
'1.3.6.1.2.1.34.4.1.2.2.3.1.5': APPN_MIB.appnNnNodeFRRsn,
'1.3.6.1.2.1.34.4.1.2.2.3.1.6': APPN_MIB.appnNnNodeFRRouteAddResist,
'1.3.6.1.2.1.34.4.1.2.2.3.1.7': APPN_MIB.appnNnNodeFRCongested,
'1.3.6.1.2.1.34.4.1.2.2.3.1.8': APPN_MIB.appnNnNodeFRIsrDepleted,
'1.3.6.1.2.1.34.4.1.2.2.3.1.9': APPN_MIB.appnNnNodeFRQuiescing,
'1.3.6.1.2.1.34.4.1.2.2.3.1.10': APPN_MIB.appnNnNodeFRGateway,
'1.3.6.1.2.1.34.4.1.2.2.3.1.11': APPN_MIB.appnNnNodeFRCentralDirectory,
'1.3.6.1.2.1.34.4.1.2.2.3.1.12': APPN_MIB.appnNnNodeFRIsr,
'1.3.6.1.2.1.34.4.1.2.2.3.1.13': APPN_MIB.appnNnNodeFRGarbageCollect,
'1.3.6.1.2.1.34.4.1.2.2.3.1.14': APPN_MIB.appnNnNodeFRHprSupport,
'1.3.6.1.2.1.34.4.1.2.2.3.1.15': APPN_MIB.appnNnNodeFRPeriBorderSup,
'1.3.6.1.2.1.34.4.1.2.2.3.1.16': APPN_MIB.appnNnNodeFRInterchangeSup,
'1.3.6.1.2.1.34.4.1.2.2.3.1.17': APPN_MIB.appnNnNodeFRExteBorderSup,
'1.3.6.1.2.1.34.4.1.2.2.3.1.18': APPN_MIB.appnNnNodeFRBranchAwareness,
'1.3.6.1.2.1.34.4.1.2.2.4.1.1': APPN_MIB.appnNnTgFRFrsn,
'1.3.6.1.2.1.34.4.1.2.2.4.1.2': APPN_MIB.appnNnTgFROwner,
'1.3.6.1.2.1.34.4.1.2.2.4.1.3': APPN_MIB.appnNnTgFRDest,
'1.3.6.1.2.1.34.4.1.2.2.4.1.4': APPN_MIB.appnNnTgFRNum,
'1.3.6.1.2.1.34.4.1.2.2.4.1.5': APPN_MIB.appnNnTgFREntryTimeLeft,
'1.3.6.1.2.1.34.4.1.2.2.4.1.6': APPN_MIB.appnNnTgFRDestVirtual,
'1.3.6.1.2.1.34.4.1.2.2.4.1.7': APPN_MIB.appnNnTgFRDlcData,
'1.3.6.1.2.1.34.4.1.2.2.4.1.8': APPN_MIB.appnNnTgFRRsn,
'1.3.6.1.2.1.34.4.1.2.2.4.1.9': APPN_MIB.appnNnTgFROperational,
'1.3.6.1.2.1.34.4.1.2.2.4.1.10': APPN_MIB.appnNnTgFRQuiescing,
'1.3.6.1.2.1.34.4.1.2.2.4.1.11': APPN_MIB.appnNnTgFRCpCpSession,
'1.3.6.1.2.1.34.4.1.2.2.4.1.12': APPN_MIB.appnNnTgFREffCap,
'1.3.6.1.2.1.34.4.1.2.2.4.1.13': APPN_MIB.appnNnTgFRConnCost,
'1.3.6.1.2.1.34.4.1.2.2.4.1.14': APPN_MIB.appnNnTgFRByteCost,
'1.3.6.1.2.1.34.4.1.2.2.4.1.15': APPN_MIB.appnNnTgFRSecurity,
'1.3.6.1.2.1.34.4.1.2.2.4.1.16': APPN_MIB.appnNnTgFRDelay,
'1.3.6.1.2.1.34.4.1.2.2.4.1.17': APPN_MIB.appnNnTgFRUsr1,
'1.3.6.1.2.1.34.4.1.2.2.4.1.18': APPN_MIB.appnNnTgFRUsr2,
'1.3.6.1.2.1.34.4.1.2.2.4.1.19': APPN_MIB.appnNnTgFRUsr3,
'1.3.6.1.2.1.34.4.1.2.2.4.1.20': APPN_MIB.appnNnTgFRGarbageCollect,
'1.3.6.1.2.1.34.4.1.2.2.4.1.21': APPN_MIB.appnNnTgFRSubareaNum,
'1.3.6.1.2.1.34.4.1.2.2.4.1.22': APPN_MIB.appnNnTgFRHprSup,
'1.3.6.1.2.1.34.4.1.2.2.4.1.23': APPN_MIB.appnNnTgFRDestHprTrans,
'1.3.6.1.2.1.34.4.1.2.2.4.1.24': APPN_MIB.appnNnTgFRTypeIndicator,
'1.3.6.1.2.1.34.4.1.2.2.4.1.25': APPN_MIB.appnNnTgFRIntersubnet,
'1.3.6.1.2.1.34.4.1.2.2.4.1.26': APPN_MIB.appnNnTgFRMltgLinkType,
'1.3.6.1.2.1.34.4.1.2.2.4.1.27': APPN_MIB.appnNnTgFRBranchTg,
'1.3.6.1.2.1.34.4.1.3.1.1.1': APPN_MIB.appnLocalTgDest,
'1.3.6.1.2.1.34.4.1.3.1.1.2': APPN_MIB.appnLocalTgNum,
'1.3.6.1.2.1.34.4.1.3.1.1.3': APPN_MIB.appnLocalTgDestVirtual,
'1.3.6.1.2.1.34.4.1.3.1.1.4': APPN_MIB.appnLocalTgDlcData,
'1.3.6.1.2.1.34.4.1.3.1.1.5': APPN_MIB.appnLocalTgPortName,
'1.3.6.1.2.1.34.4.1.3.1.1.6': APPN_MIB.appnLocalTgQuiescing,
'1.3.6.1.2.1.34.4.1.3.1.1.7': APPN_MIB.appnLocalTgOperational,
'1.3.6.1.2.1.34.4.1.3.1.1.8': APPN_MIB.appnLocalTgCpCpSession,
'1.3.6.1.2.1.34.4.1.3.1.1.9': APPN_MIB.appnLocalTgEffCap,
'1.3.6.1.2.1.34.4.1.3.1.1.10': APPN_MIB.appnLocalTgConnCost,
'1.3.6.1.2.1.34.4.1.3.1.1.11': APPN_MIB.appnLocalTgByteCost,
'1.3.6.1.2.1.34.4.1.3.1.1.12': APPN_MIB.appnLocalTgSecurity,
'1.3.6.1.2.1.34.4.1.3.1.1.13': APPN_MIB.appnLocalTgDelay,
'1.3.6.1.2.1.34.4.1.3.1.1.14': APPN_MIB.appnLocalTgUsr1,
'1.3.6.1.2.1.34.4.1.3.1.1.15': APPN_MIB.appnLocalTgUsr2,
'1.3.6.1.2.1.34.4.1.3.1.1.16': APPN_MIB.appnLocalTgUsr3,
'1.3.6.1.2.1.34.4.1.3.1.1.17': APPN_MIB.appnLocalTgHprSup,
'1.3.6.1.2.1.34.4.1.3.1.1.18': APPN_MIB.appnLocalTgIntersubnet,
'1.3.6.1.2.1.34.4.1.3.1.1.19': APPN_MIB.appnLocalTgMltgLinkType,
'1.3.6.1.2.1.34.4.1.3.1.1.20': APPN_MIB.appnLocalTgBranchLinkType,
'1.3.6.1.2.1.34.4.1.3.2.1.1': APPN_MIB.appnLocalEnTgOrigin,
'1.3.6.1.2.1.34.4.1.3.2.1.2': APPN_MIB.appnLocalEnTgDest,
'1.3.6.1.2.1.34.4.1.3.2.1.3': APPN_MIB.appnLocalEnTgNum,
'1.3.6.1.2.1.34.4.1.3.2.1.4': APPN_MIB.appnLocalEnTgEntryTimeLeft,
'1.3.6.1.2.1.34.4.1.3.2.1.5': APPN_MIB.appnLocalEnTgDestVirtual,
'1.3.6.1.2.1.34.4.1.3.2.1.6': APPN_MIB.appnLocalEnTgDlcData,
'1.3.6.1.2.1.34.4.1.3.2.1.7': APPN_MIB.appnLocalEnTgOperational,
'1.3.6.1.2.1.34.4.1.3.2.1.8': APPN_MIB.appnLocalEnTgCpCpSession,
'1.3.6.1.2.1.34.4.1.3.2.1.9': APPN_MIB.appnLocalEnTgEffCap,
'1.3.6.1.2.1.34.4.1.3.2.1.10': APPN_MIB.appnLocalEnTgConnCost,
'1.3.6.1.2.1.34.4.1.3.2.1.11': APPN_MIB.appnLocalEnTgByteCost,
'1.3.6.1.2.1.34.4.1.3.2.1.12': APPN_MIB.appnLocalEnTgSecurity,
'1.3.6.1.2.1.34.4.1.3.2.1.13': APPN_MIB.appnLocalEnTgDelay,
'1.3.6.1.2.1.34.4.1.3.2.1.14': APPN_MIB.appnLocalEnTgUsr1,
'1.3.6.1.2.1.34.4.1.3.2.1.15': APPN_MIB.appnLocalEnTgUsr2,
'1.3.6.1.2.1.34.4.1.3.2.1.16': APPN_MIB.appnLocalEnTgUsr3,
'1.3.6.1.2.1.34.4.1.3.2.1.17': APPN_MIB.appnLocalEnTgMltgLinkType,
'1.3.6.1.2.1.34.4.1.4.2.1.1': APPN_MIB.appnDirLuName,
'1.3.6.1.2.1.34.4.1.4.2.1.2': APPN_MIB.appnDirNnServerName,
'1.3.6.1.2.1.34.4.1.4.2.1.3': APPN_MIB.appnDirLuOwnerName,
'1.3.6.1.2.1.34.4.1.4.2.1.4': APPN_MIB.appnDirLuLocation,
'1.3.6.1.2.1.34.4.1.4.2.1.5': APPN_MIB.appnDirType,
'1.3.6.1.2.1.34.4.1.4.2.1.6': APPN_MIB.appnDirApparentLuOwnerName,
'1.3.6.1.2.1.34.4.1.5.1.1.1': APPN_MIB.appnCosModeName,
'1.3.6.1.2.1.34.4.1.5.1.1.2': APPN_MIB.appnCosModeCosName,
'1.3.6.1.2.1.34.4.1.5.2.1.1': APPN_MIB.appnCosName,
'1.3.6.1.2.1.34.4.1.5.2.1.2': APPN_MIB.appnCosTransPriority,
'1.3.6.1.2.1.34.4.1.5.3.1.1': APPN_MIB.appnCosNodeRowName,
'1.3.6.1.2.1.34.4.1.5.3.1.2': APPN_MIB.appnCosNodeRowIndex,
'1.3.6.1.2.1.34.4.1.5.3.1.3': APPN_MIB.appnCosNodeRowWgt,
'1.3.6.1.2.1.34.4.1.5.3.1.4': APPN_MIB.appnCosNodeRowResistMin,
'1.3.6.1.2.1.34.4.1.5.3.1.5': APPN_MIB.appnCosNodeRowResistMax,
'1.3.6.1.2.1.34.4.1.5.3.1.6': APPN_MIB.appnCosNodeRowMinCongestAllow,
'1.3.6.1.2.1.34.4.1.5.3.1.7': APPN_MIB.appnCosNodeRowMaxCongestAllow,
'1.3.6.1.2.1.34.4.1.5.4.1.1': APPN_MIB.appnCosTgRowName,
'1.3.6.1.2.1.34.4.1.5.4.1.2': APPN_MIB.appnCosTgRowIndex,
'1.3.6.1.2.1.34.4.1.5.4.1.3': APPN_MIB.appnCosTgRowWgt,
'1.3.6.1.2.1.34.4.1.5.4.1.4': APPN_MIB.appnCosTgRowEffCapMin,
'1.3.6.1.2.1.34.4.1.5.4.1.5': APPN_MIB.appnCosTgRowEffCapMax,
'1.3.6.1.2.1.34.4.1.5.4.1.6': APPN_MIB.appnCosTgRowConnCostMin,
'1.3.6.1.2.1.34.4.1.5.4.1.7': APPN_MIB.appnCosTgRowConnCostMax,
'1.3.6.1.2.1.34.4.1.5.4.1.8': APPN_MIB.appnCosTgRowByteCostMin,
'1.3.6.1.2.1.34.4.1.5.4.1.9': APPN_MIB.appnCosTgRowByteCostMax,
'1.3.6.1.2.1.34.4.1.5.4.1.10': APPN_MIB.appnCosTgRowSecurityMin,
'1.3.6.1.2.1.34.4.1.5.4.1.11': APPN_MIB.appnCosTgRowSecurityMax,
'1.3.6.1.2.1.34.4.1.5.4.1.12': APPN_MIB.appnCosTgRowDelayMin,
'1.3.6.1.2.1.34.4.1.5.4.1.13': APPN_MIB.appnCosTgRowDelayMax,
'1.3.6.1.2.1.34.4.1.5.4.1.14': APPN_MIB.appnCosTgRowUsr1Min,
'1.3.6.1.2.1.34.4.1.5.4.1.15': APPN_MIB.appnCosTgRowUsr1Max,
'1.3.6.1.2.1.34.4.1.5.4.1.16': APPN_MIB.appnCosTgRowUsr2Min,
'1.3.6.1.2.1.34.4.1.5.4.1.17': APPN_MIB.appnCosTgRowUsr2Max,
'1.3.6.1.2.1.34.4.1.5.4.1.18': APPN_MIB.appnCosTgRowUsr3Min,
'1.3.6.1.2.1.34.4.1.5.4.1.19': APPN_MIB.appnCosTgRowUsr3Max,
'1.3.6.1.2.1.34.4.1.6.2.1.1': APPN_MIB.appnIsInFqCpName,
'1.3.6.1.2.1.34.4.1.6.2.1.2': APPN_MIB.appnIsInPcid,
'1.3.6.1.2.1.34.4.1.6.2.1.3': APPN_MIB.appnIsInSessState,
'1.3.6.1.2.1.34.4.1.6.2.1.4': APPN_MIB.appnIsInPriLuName,
'1.3.6.1.2.1.34.4.1.6.2.1.5': APPN_MIB.appnIsInSecLuName,
'1.3.6.1.2.1.34.4.1.6.2.1.6': APPN_MIB.appnIsInModeName,
'1.3.6.1.2.1.34.4.1.6.2.1.7': APPN_MIB.appnIsInCosName,
'1.3.6.1.2.1.34.4.1.6.2.1.8': APPN_MIB.appnIsInTransPriority,
'1.3.6.1.2.1.34.4.1.6.2.1.9': APPN_MIB.appnIsInSessType,
'1.3.6.1.2.1.34.4.1.6.2.1.10': APPN_MIB.appnIsInSessUpTime,
'1.3.6.1.2.1.34.4.1.6.2.1.11': APPN_MIB.appnIsInCtrUpTime,
'1.3.6.1.2.1.34.4.1.6.2.1.12': APPN_MIB.appnIsInP2SFmdPius,
'1.3.6.1.2.1.34.4.1.6.2.1.13': APPN_MIB.appnIsInS2PFmdPius,
'1.3.6.1.2.1.34.4.1.6.2.1.14': APPN_MIB.appnIsInP2SNonFmdPius,
'1.3.6.1.2.1.34.4.1.6.2.1.15': APPN_MIB.appnIsInS2PNonFmdPius,
'1.3.6.1.2.1.34.4.1.6.2.1.16': APPN_MIB.appnIsInP2SFmdBytes,
'1.3.6.1.2.1.34.4.1.6.2.1.17': APPN_MIB.appnIsInS2PFmdBytes,
'1.3.6.1.2.1.34.4.1.6.2.1.18': APPN_MIB.appnIsInP2SNonFmdBytes,
'1.3.6.1.2.1.34.4.1.6.2.1.19': APPN_MIB.appnIsInS2PNonFmdBytes,
'1.3.6.1.2.1.34.4.1.6.2.1.20': APPN_MIB.appnIsInPsAdjCpName,
'1.3.6.1.2.1.34.4.1.6.2.1.21': APPN_MIB.appnIsInPsAdjTgNum,
'1.3.6.1.2.1.34.4.1.6.2.1.22': APPN_MIB.appnIsInPsSendMaxBtuSize,
'1.3.6.1.2.1.34.4.1.6.2.1.23': APPN_MIB.appnIsInPsSendPacingType,
'1.3.6.1.2.1.34.4.1.6.2.1.24': APPN_MIB.appnIsInPsSendRpc,
'1.3.6.1.2.1.34.4.1.6.2.1.25': APPN_MIB.appnIsInPsSendNxWndwSize,
'1.3.6.1.2.1.34.4.1.6.2.1.26': APPN_MIB.appnIsInPsRecvPacingType,
'1.3.6.1.2.1.34.4.1.6.2.1.27': APPN_MIB.appnIsInPsRecvRpc,
'1.3.6.1.2.1.34.4.1.6.2.1.28': APPN_MIB.appnIsInPsRecvNxWndwSize,
'1.3.6.1.2.1.34.4.1.6.2.1.29': APPN_MIB.appnIsInSsAdjCpName,
'1.3.6.1.2.1.34.4.1.6.2.1.30': APPN_MIB.appnIsInSsAdjTgNum,
'1.3.6.1.2.1.34.4.1.6.2.1.31': APPN_MIB.appnIsInSsSendMaxBtuSize,
'1.3.6.1.2.1.34.4.1.6.2.1.32': APPN_MIB.appnIsInSsSendPacingType,
'1.3.6.1.2.1.34.4.1.6.2.1.33': APPN_MIB.appnIsInSsSendRpc,
'1.3.6.1.2.1.34.4.1.6.2.1.34': APPN_MIB.appnIsInSsSendNxWndwSize,
'1.3.6.1.2.1.34.4.1.6.2.1.35': APPN_MIB.appnIsInSsRecvPacingType,
'1.3.6.1.2.1.34.4.1.6.2.1.36': APPN_MIB.appnIsInSsRecvRpc,
'1.3.6.1.2.1.34.4.1.6.2.1.37': APPN_MIB.appnIsInSsRecvNxWndwSize,
'1.3.6.1.2.1.34.4.1.6.2.1.38': APPN_MIB.appnIsInRouteInfo,
'1.3.6.1.2.1.34.4.1.6.2.1.39': APPN_MIB.appnIsInRtpNceId,
'1.3.6.1.2.1.34.4.1.6.2.1.40': APPN_MIB.appnIsInRtpTcid,
'1.3.6.1.2.1.34.4.1.6.3.1.1': APPN_MIB.appnIsRtpNceId,
'1.3.6.1.2.1.34.4.1.6.3.1.2': APPN_MIB.appnIsRtpTcid,
'1.3.6.1.2.1.34.4.1.6.3.1.3': APPN_MIB.appnIsRtpSessions,
'1.3.6.1.2.1.34.4.2.1': APPN_MIB.alertTrap,
'1.3.6.1.2.1.34.4.3.2.1': APPN_MIB.appnGeneralConfGroup,
'1.3.6.1.2.1.34.4.3.2.2': APPN_MIB.appnPortConfGroup,
'1.3.6.1.2.1.34.4.3.2.3': APPN_MIB.appnLinkConfGroup,
'1.3.6.1.2.1.34.4.3.2.4': APPN_MIB.appnLocalTgConfGroup,
'1.3.6.1.2.1.34.4.3.2.5': APPN_MIB.appnDirTableConfGroup,
'1.3.6.1.2.1.34.4.3.2.6': APPN_MIB.appnNnUniqueConfGroup,
'1.3.6.1.2.1.34.4.3.2.7': APPN_MIB.appnEnUniqueConfGroup,
'1.3.6.1.2.1.34.4.3.2.8': APPN_MIB.appnVrnConfGroup,
'1.3.6.1.2.1.34.4.3.2.9': APPN_MIB.appnNnTopoConfGroup,
'1.3.6.1.2.1.34.4.3.2.10': APPN_MIB.appnLocalEnTopoConfGroup,
'1.3.6.1.2.1.34.4.3.2.11': APPN_MIB.appnLocalDirPerfConfGroup,
'1.3.6.1.2.1.34.4.3.2.12': APPN_MIB.appnCosConfGroup,
'1.3.6.1.2.1.34.4.3.2.13': APPN_MIB.appnIntSessConfGroup,
'1.3.6.1.2.1.34.4.3.2.14': APPN_MIB.appnHprBaseConfGroup,
'1.3.6.1.2.1.34.4.3.2.15': APPN_MIB.appnHprRtpConfGroup,
'1.3.6.1.2.1.34.4.3.2.16': APPN_MIB.appnHprCtrlFlowsRtpConfGroup,
'1.3.6.1.2.1.34.4.3.2.17': APPN_MIB.appnHprBfConfGroup,
'1.3.6.1.2.1.34.4.3.2.18': APPN_MIB.appnTrapConfGroup,
'1.3.6.1.2.1.34.4.3.2.19': APPN_MIB.appnTrapNotifGroup,
'1.3.6.1.2.1.34.4.3.2.20': APPN_MIB.appnBrNnConfGroup,
'1.3.6.1.2.1.34.4.3.2.26': APPN_MIB.appnGeneralConfGroup2,
'1.3.6.1.2.1.34.4.3.2.27': APPN_MIB.appnLinkConfGroup2,
'1.3.6.1.2.1.34.4.3.2.28': APPN_MIB.appnLocalTgConfGroup2,
'1.3.6.1.2.1.34.4.3.2.29': APPN_MIB.appnDirTableConfGroup2,
'1.3.6.1.2.1.34.4.3.2.30': APPN_MIB.appnNnTopoConfGroup2,
'1.3.6.1.2.1.34.4.3.2.31': APPN_MIB.appnLocalEnTopoConfGroup2,
}
