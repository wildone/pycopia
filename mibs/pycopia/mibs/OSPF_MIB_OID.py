# python
# This file is generated by a program (mib2py). 

import OSPF_MIB

OIDMAP = {
'1.3.6.1.2.1.14': OSPF_MIB.ospf,
'1.3.6.1.2.1.14.1': OSPF_MIB.ospfGeneralGroup,
'1.3.6.1.2.1.14.13': OSPF_MIB.ospfRouteGroup,
'1.3.6.1.2.1.14.13.1': OSPF_MIB.ospfIntraArea,
'1.3.6.1.2.1.14.13.2': OSPF_MIB.ospfInterArea,
'1.3.6.1.2.1.14.13.3': OSPF_MIB.ospfExternalType1,
'1.3.6.1.2.1.14.13.4': OSPF_MIB.ospfExternalType2,
'1.3.6.1.2.1.14.15': OSPF_MIB.ospfConformance,
'1.3.6.1.2.1.14.15.1': OSPF_MIB.ospfGroups,
'1.3.6.1.2.1.14.15.2': OSPF_MIB.ospfCompliances,
'1.3.6.1.2.1.14.1.1': OSPF_MIB.ospfRouterId,
'1.3.6.1.2.1.14.1.2': OSPF_MIB.ospfAdminStat,
'1.3.6.1.2.1.14.1.3': OSPF_MIB.ospfVersionNumber,
'1.3.6.1.2.1.14.1.4': OSPF_MIB.ospfAreaBdrRtrStatus,
'1.3.6.1.2.1.14.1.5': OSPF_MIB.ospfASBdrRtrStatus,
'1.3.6.1.2.1.14.1.6': OSPF_MIB.ospfExternLsaCount,
'1.3.6.1.2.1.14.1.7': OSPF_MIB.ospfExternLsaCksumSum,
'1.3.6.1.2.1.14.1.8': OSPF_MIB.ospfTOSSupport,
'1.3.6.1.2.1.14.1.9': OSPF_MIB.ospfOriginateNewLsas,
'1.3.6.1.2.1.14.1.10': OSPF_MIB.ospfRxNewLsas,
'1.3.6.1.2.1.14.1.11': OSPF_MIB.ospfExtLsdbLimit,
'1.3.6.1.2.1.14.1.12': OSPF_MIB.ospfMulticastExtensions,
'1.3.6.1.2.1.14.1.13': OSPF_MIB.ospfExitOverflowInterval,
'1.3.6.1.2.1.14.1.14': OSPF_MIB.ospfDemandExtensions,
'1.3.6.1.2.1.14.1.15': OSPF_MIB.ospfRFC1583Compatibility,
'1.3.6.1.2.1.14.1.16': OSPF_MIB.ospfOpaqueLsaSupport,
'1.3.6.1.2.1.14.1.17': OSPF_MIB.ospfReferenceBandwidth,
'1.3.6.1.2.1.14.1.18': OSPF_MIB.ospfRestartSupport,
'1.3.6.1.2.1.14.1.19': OSPF_MIB.ospfRestartInterval,
'1.3.6.1.2.1.14.1.20': OSPF_MIB.ospfRestartStrictLsaChecking,
'1.3.6.1.2.1.14.1.21': OSPF_MIB.ospfRestartStatus,
'1.3.6.1.2.1.14.1.22': OSPF_MIB.ospfRestartAge,
'1.3.6.1.2.1.14.1.23': OSPF_MIB.ospfRestartExitReason,
'1.3.6.1.2.1.14.1.24': OSPF_MIB.ospfAsLsaCount,
'1.3.6.1.2.1.14.1.25': OSPF_MIB.ospfAsLsaCksumSum,
'1.3.6.1.2.1.14.1.26': OSPF_MIB.ospfStubRouterSupport,
'1.3.6.1.2.1.14.1.27': OSPF_MIB.ospfStubRouterAdvertisement,
'1.3.6.1.2.1.14.1.28': OSPF_MIB.ospfDiscontinuityTime,
'1.3.6.1.2.1.14.2.1.1': OSPF_MIB.ospfAreaId,
'1.3.6.1.2.1.14.2.1.2': OSPF_MIB.ospfAuthType,
'1.3.6.1.2.1.14.2.1.3': OSPF_MIB.ospfImportAsExtern,
'1.3.6.1.2.1.14.2.1.4': OSPF_MIB.ospfSpfRuns,
'1.3.6.1.2.1.14.2.1.5': OSPF_MIB.ospfAreaBdrRtrCount,
'1.3.6.1.2.1.14.2.1.6': OSPF_MIB.ospfAsBdrRtrCount,
'1.3.6.1.2.1.14.2.1.7': OSPF_MIB.ospfAreaLsaCount,
'1.3.6.1.2.1.14.2.1.8': OSPF_MIB.ospfAreaLsaCksumSum,
'1.3.6.1.2.1.14.2.1.9': OSPF_MIB.ospfAreaSummary,
'1.3.6.1.2.1.14.2.1.10': OSPF_MIB.ospfAreaStatus,
'1.3.6.1.2.1.14.2.1.11': OSPF_MIB.ospfAreaNssaTranslatorRole,
'1.3.6.1.2.1.14.2.1.12': OSPF_MIB.ospfAreaNssaTranslatorState,
'1.3.6.1.2.1.14.2.1.13': OSPF_MIB.ospfAreaNssaTranslatorStabilityInterval,
'1.3.6.1.2.1.14.2.1.14': OSPF_MIB.ospfAreaNssaTranslatorEvents,
'1.3.6.1.2.1.14.3.1.1': OSPF_MIB.ospfStubAreaId,
'1.3.6.1.2.1.14.3.1.2': OSPF_MIB.ospfStubTOS,
'1.3.6.1.2.1.14.3.1.3': OSPF_MIB.ospfStubMetric,
'1.3.6.1.2.1.14.3.1.4': OSPF_MIB.ospfStubStatus,
'1.3.6.1.2.1.14.3.1.5': OSPF_MIB.ospfStubMetricType,
'1.3.6.1.2.1.14.4.1.1': OSPF_MIB.ospfLsdbAreaId,
'1.3.6.1.2.1.14.4.1.2': OSPF_MIB.ospfLsdbType,
'1.3.6.1.2.1.14.4.1.3': OSPF_MIB.ospfLsdbLsid,
'1.3.6.1.2.1.14.4.1.4': OSPF_MIB.ospfLsdbRouterId,
'1.3.6.1.2.1.14.4.1.5': OSPF_MIB.ospfLsdbSequence,
'1.3.6.1.2.1.14.4.1.6': OSPF_MIB.ospfLsdbAge,
'1.3.6.1.2.1.14.4.1.7': OSPF_MIB.ospfLsdbChecksum,
'1.3.6.1.2.1.14.4.1.8': OSPF_MIB.ospfLsdbAdvertisement,
'1.3.6.1.2.1.14.5.1.1': OSPF_MIB.ospfAreaRangeAreaId,
'1.3.6.1.2.1.14.5.1.2': OSPF_MIB.ospfAreaRangeNet,
'1.3.6.1.2.1.14.5.1.3': OSPF_MIB.ospfAreaRangeMask,
'1.3.6.1.2.1.14.5.1.4': OSPF_MIB.ospfAreaRangeStatus,
'1.3.6.1.2.1.14.5.1.5': OSPF_MIB.ospfAreaRangeEffect,
'1.3.6.1.2.1.14.6.1.1': OSPF_MIB.ospfHostIpAddress,
'1.3.6.1.2.1.14.6.1.2': OSPF_MIB.ospfHostTOS,
'1.3.6.1.2.1.14.6.1.3': OSPF_MIB.ospfHostMetric,
'1.3.6.1.2.1.14.6.1.4': OSPF_MIB.ospfHostStatus,
'1.3.6.1.2.1.14.6.1.5': OSPF_MIB.ospfHostAreaID,
'1.3.6.1.2.1.14.6.1.6': OSPF_MIB.ospfHostCfgAreaID,
'1.3.6.1.2.1.14.7.1.1': OSPF_MIB.ospfIfIpAddress,
'1.3.6.1.2.1.14.7.1.2': OSPF_MIB.ospfAddressLessIf,
'1.3.6.1.2.1.14.7.1.3': OSPF_MIB.ospfIfAreaId,
'1.3.6.1.2.1.14.7.1.4': OSPF_MIB.ospfIfType,
'1.3.6.1.2.1.14.7.1.5': OSPF_MIB.ospfIfAdminStat,
'1.3.6.1.2.1.14.7.1.6': OSPF_MIB.ospfIfRtrPriority,
'1.3.6.1.2.1.14.7.1.7': OSPF_MIB.ospfIfTransitDelay,
'1.3.6.1.2.1.14.7.1.8': OSPF_MIB.ospfIfRetransInterval,
'1.3.6.1.2.1.14.7.1.9': OSPF_MIB.ospfIfHelloInterval,
'1.3.6.1.2.1.14.7.1.10': OSPF_MIB.ospfIfRtrDeadInterval,
'1.3.6.1.2.1.14.7.1.11': OSPF_MIB.ospfIfPollInterval,
'1.3.6.1.2.1.14.7.1.12': OSPF_MIB.ospfIfState,
'1.3.6.1.2.1.14.7.1.13': OSPF_MIB.ospfIfDesignatedRouter,
'1.3.6.1.2.1.14.7.1.14': OSPF_MIB.ospfIfBackupDesignatedRouter,
'1.3.6.1.2.1.14.7.1.15': OSPF_MIB.ospfIfEvents,
'1.3.6.1.2.1.14.7.1.16': OSPF_MIB.ospfIfAuthKey,
'1.3.6.1.2.1.14.7.1.17': OSPF_MIB.ospfIfStatus,
'1.3.6.1.2.1.14.7.1.18': OSPF_MIB.ospfIfMulticastForwarding,
'1.3.6.1.2.1.14.7.1.19': OSPF_MIB.ospfIfDemand,
'1.3.6.1.2.1.14.7.1.20': OSPF_MIB.ospfIfAuthType,
'1.3.6.1.2.1.14.7.1.21': OSPF_MIB.ospfIfLsaCount,
'1.3.6.1.2.1.14.7.1.22': OSPF_MIB.ospfIfLsaCksumSum,
'1.3.6.1.2.1.14.7.1.23': OSPF_MIB.ospfIfDesignatedRouterId,
'1.3.6.1.2.1.14.7.1.24': OSPF_MIB.ospfIfBackupDesignatedRouterId,
'1.3.6.1.2.1.14.8.1.1': OSPF_MIB.ospfIfMetricIpAddress,
'1.3.6.1.2.1.14.8.1.2': OSPF_MIB.ospfIfMetricAddressLessIf,
'1.3.6.1.2.1.14.8.1.3': OSPF_MIB.ospfIfMetricTOS,
'1.3.6.1.2.1.14.8.1.4': OSPF_MIB.ospfIfMetricValue,
'1.3.6.1.2.1.14.8.1.5': OSPF_MIB.ospfIfMetricStatus,
'1.3.6.1.2.1.14.9.1.1': OSPF_MIB.ospfVirtIfAreaId,
'1.3.6.1.2.1.14.9.1.2': OSPF_MIB.ospfVirtIfNeighbor,
'1.3.6.1.2.1.14.9.1.3': OSPF_MIB.ospfVirtIfTransitDelay,
'1.3.6.1.2.1.14.9.1.4': OSPF_MIB.ospfVirtIfRetransInterval,
'1.3.6.1.2.1.14.9.1.5': OSPF_MIB.ospfVirtIfHelloInterval,
'1.3.6.1.2.1.14.9.1.6': OSPF_MIB.ospfVirtIfRtrDeadInterval,
'1.3.6.1.2.1.14.9.1.7': OSPF_MIB.ospfVirtIfState,
'1.3.6.1.2.1.14.9.1.8': OSPF_MIB.ospfVirtIfEvents,
'1.3.6.1.2.1.14.9.1.9': OSPF_MIB.ospfVirtIfAuthKey,
'1.3.6.1.2.1.14.9.1.10': OSPF_MIB.ospfVirtIfStatus,
'1.3.6.1.2.1.14.9.1.11': OSPF_MIB.ospfVirtIfAuthType,
'1.3.6.1.2.1.14.9.1.12': OSPF_MIB.ospfVirtIfLsaCount,
'1.3.6.1.2.1.14.9.1.13': OSPF_MIB.ospfVirtIfLsaCksumSum,
'1.3.6.1.2.1.14.10.1.1': OSPF_MIB.ospfNbrIpAddr,
'1.3.6.1.2.1.14.10.1.2': OSPF_MIB.ospfNbrAddressLessIndex,
'1.3.6.1.2.1.14.10.1.3': OSPF_MIB.ospfNbrRtrId,
'1.3.6.1.2.1.14.10.1.4': OSPF_MIB.ospfNbrOptions,
'1.3.6.1.2.1.14.10.1.5': OSPF_MIB.ospfNbrPriority,
'1.3.6.1.2.1.14.10.1.6': OSPF_MIB.ospfNbrState,
'1.3.6.1.2.1.14.10.1.7': OSPF_MIB.ospfNbrEvents,
'1.3.6.1.2.1.14.10.1.8': OSPF_MIB.ospfNbrLsRetransQLen,
'1.3.6.1.2.1.14.10.1.9': OSPF_MIB.ospfNbmaNbrStatus,
'1.3.6.1.2.1.14.10.1.10': OSPF_MIB.ospfNbmaNbrPermanence,
'1.3.6.1.2.1.14.10.1.11': OSPF_MIB.ospfNbrHelloSuppressed,
'1.3.6.1.2.1.14.10.1.12': OSPF_MIB.ospfNbrRestartHelperStatus,
'1.3.6.1.2.1.14.10.1.13': OSPF_MIB.ospfNbrRestartHelperAge,
'1.3.6.1.2.1.14.10.1.14': OSPF_MIB.ospfNbrRestartHelperExitReason,
'1.3.6.1.2.1.14.11.1.1': OSPF_MIB.ospfVirtNbrArea,
'1.3.6.1.2.1.14.11.1.2': OSPF_MIB.ospfVirtNbrRtrId,
'1.3.6.1.2.1.14.11.1.3': OSPF_MIB.ospfVirtNbrIpAddr,
'1.3.6.1.2.1.14.11.1.4': OSPF_MIB.ospfVirtNbrOptions,
'1.3.6.1.2.1.14.11.1.5': OSPF_MIB.ospfVirtNbrState,
'1.3.6.1.2.1.14.11.1.6': OSPF_MIB.ospfVirtNbrEvents,
'1.3.6.1.2.1.14.11.1.7': OSPF_MIB.ospfVirtNbrLsRetransQLen,
'1.3.6.1.2.1.14.11.1.8': OSPF_MIB.ospfVirtNbrHelloSuppressed,
'1.3.6.1.2.1.14.11.1.9': OSPF_MIB.ospfVirtNbrRestartHelperStatus,
'1.3.6.1.2.1.14.11.1.10': OSPF_MIB.ospfVirtNbrRestartHelperAge,
'1.3.6.1.2.1.14.11.1.11': OSPF_MIB.ospfVirtNbrRestartHelperExitReason,
'1.3.6.1.2.1.14.12.1.1': OSPF_MIB.ospfExtLsdbType,
'1.3.6.1.2.1.14.12.1.2': OSPF_MIB.ospfExtLsdbLsid,
'1.3.6.1.2.1.14.12.1.3': OSPF_MIB.ospfExtLsdbRouterId,
'1.3.6.1.2.1.14.12.1.4': OSPF_MIB.ospfExtLsdbSequence,
'1.3.6.1.2.1.14.12.1.5': OSPF_MIB.ospfExtLsdbAge,
'1.3.6.1.2.1.14.12.1.6': OSPF_MIB.ospfExtLsdbChecksum,
'1.3.6.1.2.1.14.12.1.7': OSPF_MIB.ospfExtLsdbAdvertisement,
'1.3.6.1.2.1.14.14.1.1': OSPF_MIB.ospfAreaAggregateAreaID,
'1.3.6.1.2.1.14.14.1.2': OSPF_MIB.ospfAreaAggregateLsdbType,
'1.3.6.1.2.1.14.14.1.3': OSPF_MIB.ospfAreaAggregateNet,
'1.3.6.1.2.1.14.14.1.4': OSPF_MIB.ospfAreaAggregateMask,
'1.3.6.1.2.1.14.14.1.5': OSPF_MIB.ospfAreaAggregateStatus,
'1.3.6.1.2.1.14.14.1.6': OSPF_MIB.ospfAreaAggregateEffect,
'1.3.6.1.2.1.14.14.1.7': OSPF_MIB.ospfAreaAggregateExtRouteTag,
'1.3.6.1.2.1.14.17.1.1': OSPF_MIB.ospfLocalLsdbIpAddress,
'1.3.6.1.2.1.14.17.1.2': OSPF_MIB.ospfLocalLsdbAddressLessIf,
'1.3.6.1.2.1.14.17.1.3': OSPF_MIB.ospfLocalLsdbType,
'1.3.6.1.2.1.14.17.1.4': OSPF_MIB.ospfLocalLsdbLsid,
'1.3.6.1.2.1.14.17.1.5': OSPF_MIB.ospfLocalLsdbRouterId,
'1.3.6.1.2.1.14.17.1.6': OSPF_MIB.ospfLocalLsdbSequence,
'1.3.6.1.2.1.14.17.1.7': OSPF_MIB.ospfLocalLsdbAge,
'1.3.6.1.2.1.14.17.1.8': OSPF_MIB.ospfLocalLsdbChecksum,
'1.3.6.1.2.1.14.17.1.9': OSPF_MIB.ospfLocalLsdbAdvertisement,
'1.3.6.1.2.1.14.18.1.1': OSPF_MIB.ospfVirtLocalLsdbTransitArea,
'1.3.6.1.2.1.14.18.1.2': OSPF_MIB.ospfVirtLocalLsdbNeighbor,
'1.3.6.1.2.1.14.18.1.3': OSPF_MIB.ospfVirtLocalLsdbType,
'1.3.6.1.2.1.14.18.1.4': OSPF_MIB.ospfVirtLocalLsdbLsid,
'1.3.6.1.2.1.14.18.1.5': OSPF_MIB.ospfVirtLocalLsdbRouterId,
'1.3.6.1.2.1.14.18.1.6': OSPF_MIB.ospfVirtLocalLsdbSequence,
'1.3.6.1.2.1.14.18.1.7': OSPF_MIB.ospfVirtLocalLsdbAge,
'1.3.6.1.2.1.14.18.1.8': OSPF_MIB.ospfVirtLocalLsdbChecksum,
'1.3.6.1.2.1.14.18.1.9': OSPF_MIB.ospfVirtLocalLsdbAdvertisement,
'1.3.6.1.2.1.14.19.1.1': OSPF_MIB.ospfAsLsdbType,
'1.3.6.1.2.1.14.19.1.2': OSPF_MIB.ospfAsLsdbLsid,
'1.3.6.1.2.1.14.19.1.3': OSPF_MIB.ospfAsLsdbRouterId,
'1.3.6.1.2.1.14.19.1.4': OSPF_MIB.ospfAsLsdbSequence,
'1.3.6.1.2.1.14.19.1.5': OSPF_MIB.ospfAsLsdbAge,
'1.3.6.1.2.1.14.19.1.6': OSPF_MIB.ospfAsLsdbChecksum,
'1.3.6.1.2.1.14.19.1.7': OSPF_MIB.ospfAsLsdbAdvertisement,
'1.3.6.1.2.1.14.20.1.1': OSPF_MIB.ospfAreaLsaCountAreaId,
'1.3.6.1.2.1.14.20.1.2': OSPF_MIB.ospfAreaLsaCountLsaType,
'1.3.6.1.2.1.14.20.1.3': OSPF_MIB.ospfAreaLsaCountNumber,
'1.3.6.1.2.1.14.15.1.1': OSPF_MIB.ospfBasicGroup,
'1.3.6.1.2.1.14.15.1.2': OSPF_MIB.ospfAreaGroup,
'1.3.6.1.2.1.14.15.1.3': OSPF_MIB.ospfStubAreaGroup,
'1.3.6.1.2.1.14.15.1.4': OSPF_MIB.ospfLsdbGroup,
'1.3.6.1.2.1.14.15.1.6': OSPF_MIB.ospfHostGroup,
'1.3.6.1.2.1.14.15.1.7': OSPF_MIB.ospfIfGroup,
'1.3.6.1.2.1.14.15.1.8': OSPF_MIB.ospfIfMetricGroup,
'1.3.6.1.2.1.14.15.1.9': OSPF_MIB.ospfVirtIfGroup,
'1.3.6.1.2.1.14.15.1.10': OSPF_MIB.ospfNbrGroup,
'1.3.6.1.2.1.14.15.1.11': OSPF_MIB.ospfVirtNbrGroup,
'1.3.6.1.2.1.14.15.1.12': OSPF_MIB.ospfExtLsdbGroup,
'1.3.6.1.2.1.14.15.1.13': OSPF_MIB.ospfAreaAggregateGroup,
'1.3.6.1.2.1.14.15.1.14': OSPF_MIB.ospfLocalLsdbGroup,
'1.3.6.1.2.1.14.15.1.15': OSPF_MIB.ospfVirtLocalLsdbGroup,
'1.3.6.1.2.1.14.15.1.16': OSPF_MIB.ospfAsLsdbGroup,
'1.3.6.1.2.1.14.15.1.17': OSPF_MIB.ospfBasicGroup2,
'1.3.6.1.2.1.14.15.1.18': OSPF_MIB.ospfAreaGroup2,
'1.3.6.1.2.1.14.15.1.19': OSPF_MIB.ospfIfGroup2,
'1.3.6.1.2.1.14.15.1.20': OSPF_MIB.ospfVirtIfGroup2,
'1.3.6.1.2.1.14.15.1.21': OSPF_MIB.ospfNbrGroup2,
'1.3.6.1.2.1.14.15.1.22': OSPF_MIB.ospfVirtNbrGroup2,
'1.3.6.1.2.1.14.15.1.23': OSPF_MIB.ospfAreaAggregateGroup2,
'1.3.6.1.2.1.14.15.1.24': OSPF_MIB.ospfAreaLsaCountGroup,
'1.3.6.1.2.1.14.15.1.25': OSPF_MIB.ospfHostGroup2,
}
