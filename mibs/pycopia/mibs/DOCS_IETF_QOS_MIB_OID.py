# python
# This file is generated by a program (mib2py). 

import DOCS_IETF_QOS_MIB

OIDMAP = {
'1.3.6.1.2.1.127': DOCS_IETF_QOS_MIB.docsIetfQosMIB,
'1.3.6.1.2.1.127.0': DOCS_IETF_QOS_MIB.docsIetfQosNotifications,
'1.3.6.1.2.1.127.1': DOCS_IETF_QOS_MIB.docsIetfQosMIBObjects,
'1.3.6.1.2.1.127.2': DOCS_IETF_QOS_MIB.docsIetfQosConformance,
'1.3.6.1.2.1.127.2.1': DOCS_IETF_QOS_MIB.docsIetfQosGroups,
'1.3.6.1.2.1.127.2.2': DOCS_IETF_QOS_MIB.docsIetfQosCompliances,
'1.3.6.1.2.1.127.1.1.1.1': DOCS_IETF_QOS_MIB.docsIetfQosPktClassId,
'1.3.6.1.2.1.127.1.1.1.2': DOCS_IETF_QOS_MIB.docsIetfQosPktClassDirection,
'1.3.6.1.2.1.127.1.1.1.3': DOCS_IETF_QOS_MIB.docsIetfQosPktClassPriority,
'1.3.6.1.2.1.127.1.1.1.4': DOCS_IETF_QOS_MIB.docsIetfQosPktClassIpTosLow,
'1.3.6.1.2.1.127.1.1.1.5': DOCS_IETF_QOS_MIB.docsIetfQosPktClassIpTosHigh,
'1.3.6.1.2.1.127.1.1.1.6': DOCS_IETF_QOS_MIB.docsIetfQosPktClassIpTosMask,
'1.3.6.1.2.1.127.1.1.1.7': DOCS_IETF_QOS_MIB.docsIetfQosPktClassIpProtocol,
'1.3.6.1.2.1.127.1.1.1.8': DOCS_IETF_QOS_MIB.docsIetfQosPktClassInetAddressType,
'1.3.6.1.2.1.127.1.1.1.9': DOCS_IETF_QOS_MIB.docsIetfQosPktClassInetSourceAddr,
'1.3.6.1.2.1.127.1.1.1.10': DOCS_IETF_QOS_MIB.docsIetfQosPktClassInetSourceMask,
'1.3.6.1.2.1.127.1.1.1.11': DOCS_IETF_QOS_MIB.docsIetfQosPktClassInetDestAddr,
'1.3.6.1.2.1.127.1.1.1.12': DOCS_IETF_QOS_MIB.docsIetfQosPktClassInetDestMask,
'1.3.6.1.2.1.127.1.1.1.13': DOCS_IETF_QOS_MIB.docsIetfQosPktClassSourcePortStart,
'1.3.6.1.2.1.127.1.1.1.14': DOCS_IETF_QOS_MIB.docsIetfQosPktClassSourcePortEnd,
'1.3.6.1.2.1.127.1.1.1.15': DOCS_IETF_QOS_MIB.docsIetfQosPktClassDestPortStart,
'1.3.6.1.2.1.127.1.1.1.16': DOCS_IETF_QOS_MIB.docsIetfQosPktClassDestPortEnd,
'1.3.6.1.2.1.127.1.1.1.17': DOCS_IETF_QOS_MIB.docsIetfQosPktClassDestMacAddr,
'1.3.6.1.2.1.127.1.1.1.18': DOCS_IETF_QOS_MIB.docsIetfQosPktClassDestMacMask,
'1.3.6.1.2.1.127.1.1.1.19': DOCS_IETF_QOS_MIB.docsIetfQosPktClassSourceMacAddr,
'1.3.6.1.2.1.127.1.1.1.20': DOCS_IETF_QOS_MIB.docsIetfQosPktClassEnetProtocolType,
'1.3.6.1.2.1.127.1.1.1.21': DOCS_IETF_QOS_MIB.docsIetfQosPktClassEnetProtocol,
'1.3.6.1.2.1.127.1.1.1.22': DOCS_IETF_QOS_MIB.docsIetfQosPktClassUserPriLow,
'1.3.6.1.2.1.127.1.1.1.23': DOCS_IETF_QOS_MIB.docsIetfQosPktClassUserPriHigh,
'1.3.6.1.2.1.127.1.1.1.24': DOCS_IETF_QOS_MIB.docsIetfQosPktClassVlanId,
'1.3.6.1.2.1.127.1.1.1.25': DOCS_IETF_QOS_MIB.docsIetfQosPktClassStateActive,
'1.3.6.1.2.1.127.1.1.1.26': DOCS_IETF_QOS_MIB.docsIetfQosPktClassPkts,
'1.3.6.1.2.1.127.1.1.1.27': DOCS_IETF_QOS_MIB.docsIetfQosPktClassBitMap,
'1.3.6.1.2.1.127.1.2.1.1': DOCS_IETF_QOS_MIB.docsIetfQosParamSetServiceClassName,
'1.3.6.1.2.1.127.1.2.1.2': DOCS_IETF_QOS_MIB.docsIetfQosParamSetPriority,
'1.3.6.1.2.1.127.1.2.1.3': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMaxTrafficRate,
'1.3.6.1.2.1.127.1.2.1.4': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMaxTrafficBurst,
'1.3.6.1.2.1.127.1.2.1.5': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMinReservedRate,
'1.3.6.1.2.1.127.1.2.1.6': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMinReservedPkt,
'1.3.6.1.2.1.127.1.2.1.7': DOCS_IETF_QOS_MIB.docsIetfQosParamSetActiveTimeout,
'1.3.6.1.2.1.127.1.2.1.8': DOCS_IETF_QOS_MIB.docsIetfQosParamSetAdmittedTimeout,
'1.3.6.1.2.1.127.1.2.1.9': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMaxConcatBurst,
'1.3.6.1.2.1.127.1.2.1.10': DOCS_IETF_QOS_MIB.docsIetfQosParamSetSchedulingType,
'1.3.6.1.2.1.127.1.2.1.11': DOCS_IETF_QOS_MIB.docsIetfQosParamSetNomPollInterval,
'1.3.6.1.2.1.127.1.2.1.12': DOCS_IETF_QOS_MIB.docsIetfQosParamSetTolPollJitter,
'1.3.6.1.2.1.127.1.2.1.13': DOCS_IETF_QOS_MIB.docsIetfQosParamSetUnsolicitGrantSize,
'1.3.6.1.2.1.127.1.2.1.14': DOCS_IETF_QOS_MIB.docsIetfQosParamSetNomGrantInterval,
'1.3.6.1.2.1.127.1.2.1.15': DOCS_IETF_QOS_MIB.docsIetfQosParamSetTolGrantJitter,
'1.3.6.1.2.1.127.1.2.1.16': DOCS_IETF_QOS_MIB.docsIetfQosParamSetGrantsPerInterval,
'1.3.6.1.2.1.127.1.2.1.17': DOCS_IETF_QOS_MIB.docsIetfQosParamSetTosAndMask,
'1.3.6.1.2.1.127.1.2.1.18': DOCS_IETF_QOS_MIB.docsIetfQosParamSetTosOrMask,
'1.3.6.1.2.1.127.1.2.1.19': DOCS_IETF_QOS_MIB.docsIetfQosParamSetMaxLatency,
'1.3.6.1.2.1.127.1.2.1.20': DOCS_IETF_QOS_MIB.docsIetfQosParamSetType,
'1.3.6.1.2.1.127.1.2.1.21': DOCS_IETF_QOS_MIB.docsIetfQosParamSetRequestPolicyOct,
'1.3.6.1.2.1.127.1.2.1.22': DOCS_IETF_QOS_MIB.docsIetfQosParamSetBitMap,
'1.3.6.1.2.1.127.1.3.1.1': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowId,
'1.3.6.1.2.1.127.1.3.1.2': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowSID,
'1.3.6.1.2.1.127.1.3.1.3': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowDirection,
'1.3.6.1.2.1.127.1.3.1.4': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowPrimary,
'1.3.6.1.2.1.127.1.4.1.1': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowPkts,
'1.3.6.1.2.1.127.1.4.1.2': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowOctets,
'1.3.6.1.2.1.127.1.4.1.3': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowTimeCreated,
'1.3.6.1.2.1.127.1.4.1.4': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowTimeActive,
'1.3.6.1.2.1.127.1.4.1.5': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowPHSUnknowns,
'1.3.6.1.2.1.127.1.4.1.6': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowPolicedDropPkts,
'1.3.6.1.2.1.127.1.4.1.7': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowPolicedDelayPkts,
'1.3.6.1.2.1.127.1.5.1.1': DOCS_IETF_QOS_MIB.docsIetfQosSID,
'1.3.6.1.2.1.127.1.5.1.2': DOCS_IETF_QOS_MIB.docsIetfQosUpstreamFragments,
'1.3.6.1.2.1.127.1.5.1.3': DOCS_IETF_QOS_MIB.docsIetfQosUpstreamFragDiscards,
'1.3.6.1.2.1.127.1.5.1.4': DOCS_IETF_QOS_MIB.docsIetfQosUpstreamConcatBursts,
'1.3.6.1.2.1.127.1.6.1.1': DOCS_IETF_QOS_MIB.docsIetfQosIfDirection,
'1.3.6.1.2.1.127.1.6.1.2': DOCS_IETF_QOS_MIB.docsIetfQosDSAReqs,
'1.3.6.1.2.1.127.1.6.1.3': DOCS_IETF_QOS_MIB.docsIetfQosDSARsps,
'1.3.6.1.2.1.127.1.6.1.4': DOCS_IETF_QOS_MIB.docsIetfQosDSAAcks,
'1.3.6.1.2.1.127.1.6.1.5': DOCS_IETF_QOS_MIB.docsIetfQosDSCReqs,
'1.3.6.1.2.1.127.1.6.1.6': DOCS_IETF_QOS_MIB.docsIetfQosDSCRsps,
'1.3.6.1.2.1.127.1.6.1.7': DOCS_IETF_QOS_MIB.docsIetfQosDSCAcks,
'1.3.6.1.2.1.127.1.6.1.8': DOCS_IETF_QOS_MIB.docsIetfQosDSDReqs,
'1.3.6.1.2.1.127.1.6.1.9': DOCS_IETF_QOS_MIB.docsIetfQosDSDRsps,
'1.3.6.1.2.1.127.1.6.1.10': DOCS_IETF_QOS_MIB.docsIetfQosDynamicAdds,
'1.3.6.1.2.1.127.1.6.1.11': DOCS_IETF_QOS_MIB.docsIetfQosDynamicAddFails,
'1.3.6.1.2.1.127.1.6.1.12': DOCS_IETF_QOS_MIB.docsIetfQosDynamicChanges,
'1.3.6.1.2.1.127.1.6.1.13': DOCS_IETF_QOS_MIB.docsIetfQosDynamicChangeFails,
'1.3.6.1.2.1.127.1.6.1.14': DOCS_IETF_QOS_MIB.docsIetfQosDynamicDeletes,
'1.3.6.1.2.1.127.1.6.1.15': DOCS_IETF_QOS_MIB.docsIetfQosDynamicDeleteFails,
'1.3.6.1.2.1.127.1.6.1.16': DOCS_IETF_QOS_MIB.docsIetfQosDCCReqs,
'1.3.6.1.2.1.127.1.6.1.17': DOCS_IETF_QOS_MIB.docsIetfQosDCCRsps,
'1.3.6.1.2.1.127.1.6.1.18': DOCS_IETF_QOS_MIB.docsIetfQosDCCAcks,
'1.3.6.1.2.1.127.1.6.1.19': DOCS_IETF_QOS_MIB.docsIetfQosDCCs,
'1.3.6.1.2.1.127.1.6.1.20': DOCS_IETF_QOS_MIB.docsIetfQosDCCFails,
'1.3.6.1.2.1.127.1.7.1.1': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogIndex,
'1.3.6.1.2.1.127.1.7.1.2': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogIfIndex,
'1.3.6.1.2.1.127.1.7.1.3': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogSFID,
'1.3.6.1.2.1.127.1.7.1.4': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogCmMac,
'1.3.6.1.2.1.127.1.7.1.5': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogPkts,
'1.3.6.1.2.1.127.1.7.1.6': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogOctets,
'1.3.6.1.2.1.127.1.7.1.7': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogTimeDeleted,
'1.3.6.1.2.1.127.1.7.1.8': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogTimeCreated,
'1.3.6.1.2.1.127.1.7.1.9': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogTimeActive,
'1.3.6.1.2.1.127.1.7.1.10': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogDirection,
'1.3.6.1.2.1.127.1.7.1.11': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogPrimary,
'1.3.6.1.2.1.127.1.7.1.12': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogServiceClassName,
'1.3.6.1.2.1.127.1.7.1.13': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogPolicedDropPkts,
'1.3.6.1.2.1.127.1.7.1.14': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogPolicedDelayPkts,
'1.3.6.1.2.1.127.1.7.1.15': DOCS_IETF_QOS_MIB.docsIetfQosServiceFlowLogControl,
'1.3.6.1.2.1.127.1.8.1.1': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassName,
'1.3.6.1.2.1.127.1.8.1.2': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassStatus,
'1.3.6.1.2.1.127.1.8.1.3': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPriority,
'1.3.6.1.2.1.127.1.8.1.4': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMaxTrafficRate,
'1.3.6.1.2.1.127.1.8.1.5': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMaxTrafficBurst,
'1.3.6.1.2.1.127.1.8.1.6': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMinReservedRate,
'1.3.6.1.2.1.127.1.8.1.7': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMinReservedPkt,
'1.3.6.1.2.1.127.1.8.1.8': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMaxConcatBurst,
'1.3.6.1.2.1.127.1.8.1.9': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassNomPollInterval,
'1.3.6.1.2.1.127.1.8.1.10': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassTolPollJitter,
'1.3.6.1.2.1.127.1.8.1.11': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassUnsolicitGrantSize,
'1.3.6.1.2.1.127.1.8.1.12': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassNomGrantInterval,
'1.3.6.1.2.1.127.1.8.1.13': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassTolGrantJitter,
'1.3.6.1.2.1.127.1.8.1.14': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassGrantsPerInterval,
'1.3.6.1.2.1.127.1.8.1.15': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassMaxLatency,
'1.3.6.1.2.1.127.1.8.1.16': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassActiveTimeout,
'1.3.6.1.2.1.127.1.8.1.17': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassAdmittedTimeout,
'1.3.6.1.2.1.127.1.8.1.18': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassSchedulingType,
'1.3.6.1.2.1.127.1.8.1.19': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassRequestPolicy,
'1.3.6.1.2.1.127.1.8.1.20': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassTosAndMask,
'1.3.6.1.2.1.127.1.8.1.21': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassTosOrMask,
'1.3.6.1.2.1.127.1.8.1.22': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassDirection,
'1.3.6.1.2.1.127.1.8.1.23': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassStorageType,
'1.3.6.1.2.1.127.1.8.1.24': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassDSCPOverwrite,
'1.3.6.1.2.1.127.1.9.1.1': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPolicyIndex,
'1.3.6.1.2.1.127.1.9.1.2': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPolicyName,
'1.3.6.1.2.1.127.1.9.1.3': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPolicyRulePriority,
'1.3.6.1.2.1.127.1.9.1.4': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPolicyStatus,
'1.3.6.1.2.1.127.1.9.1.5': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassPolicyStorageType,
'1.3.6.1.2.1.127.1.10.1.1': DOCS_IETF_QOS_MIB.docsIetfQosPHSField,
'1.3.6.1.2.1.127.1.10.1.2': DOCS_IETF_QOS_MIB.docsIetfQosPHSMask,
'1.3.6.1.2.1.127.1.10.1.3': DOCS_IETF_QOS_MIB.docsIetfQosPHSSize,
'1.3.6.1.2.1.127.1.10.1.4': DOCS_IETF_QOS_MIB.docsIetfQosPHSVerify,
'1.3.6.1.2.1.127.1.10.1.5': DOCS_IETF_QOS_MIB.docsIetfQosPHSIndex,
'1.3.6.1.2.1.127.1.11.1.1': DOCS_IETF_QOS_MIB.docsIetfQosCmtsCmMac,
'1.3.6.1.2.1.127.1.11.1.2': DOCS_IETF_QOS_MIB.docsIetfQosCmtsServiceFlowId,
'1.3.6.1.2.1.127.1.11.1.3': DOCS_IETF_QOS_MIB.docsIetfQosCmtsIfIndex,
'1.3.6.1.2.1.127.2.1.1': DOCS_IETF_QOS_MIB.docsIetfQosBaseGroup,
'1.3.6.1.2.1.127.2.1.2': DOCS_IETF_QOS_MIB.docsIetfQosParamSetGroup,
'1.3.6.1.2.1.127.2.1.3': DOCS_IETF_QOS_MIB.docsIetfQosCmtsGroup,
'1.3.6.1.2.1.127.2.1.4': DOCS_IETF_QOS_MIB.docsIetfQosSrvClassPolicyGroup,
'1.3.6.1.2.1.127.2.1.5': DOCS_IETF_QOS_MIB.docsIetfQosServiceClassGroup,
}
