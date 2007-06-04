# python
# This file is generated by a program (mib2py). 

import HDSL2_SHDSL_LINE_MIB

OIDMAP = {
'1.3.6.1.2.1.10.48': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMIB,
'1.3.6.1.2.1.10.48.0': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslNotifications,
'1.3.6.1.2.1.10.48.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMibObjects,
'1.3.6.1.2.1.10.48.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslConformance,
'1.3.6.1.2.1.10.48.3.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslGroups,
'1.3.6.1.2.1.10.48.3.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslCompliances,
'1.3.6.1.2.1.10.48.1.1.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfNumRepeaters,
'1.3.6.1.2.1.10.48.1.1.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfProfile,
'1.3.6.1.2.1.10.48.1.1.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfAlarmProfile,
'1.3.6.1.2.1.10.48.1.2.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusNumAvailRepeaters,
'1.3.6.1.2.1.10.48.1.2.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusMaxAttainableLineRate,
'1.3.6.1.2.1.10.48.1.2.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusActualLineRate,
'1.3.6.1.2.1.10.48.1.2.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusTransmissionModeCurrent,
'1.3.6.1.2.1.10.48.1.2.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusMaxAttainablePayloadRate,
'1.3.6.1.2.1.10.48.1.2.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslStatusActualPayloadRate,
'1.3.6.1.2.1.10.48.1.3.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvIndex,
'1.3.6.1.2.1.10.48.1.3.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorID,
'1.3.6.1.2.1.10.48.1.3.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorModelNumber,
'1.3.6.1.2.1.10.48.1.3.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorSerialNumber,
'1.3.6.1.2.1.10.48.1.3.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorEOCSoftwareVersion,
'1.3.6.1.2.1.10.48.1.3.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvStandardVersion,
'1.3.6.1.2.1.10.48.1.3.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorListNumber,
'1.3.6.1.2.1.10.48.1.3.1.8': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorIssueNumber,
'1.3.6.1.2.1.10.48.1.3.1.9': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorSoftwareVersion,
'1.3.6.1.2.1.10.48.1.3.1.10': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvEquipmentCode,
'1.3.6.1.2.1.10.48.1.3.1.11': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvVendorOther,
'1.3.6.1.2.1.10.48.1.3.1.12': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInvTransmissionModeCapability,
'1.3.6.1.2.1.10.48.1.4.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointSide,
'1.3.6.1.2.1.10.48.1.4.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointWirePair,
'1.3.6.1.2.1.10.48.1.4.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointAlarmConfProfile,
'1.3.6.1.2.1.10.48.1.5.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrAtn,
'1.3.6.1.2.1.10.48.1.5.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrSnrMgn,
'1.3.6.1.2.1.10.48.1.5.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrStatus,
'1.3.6.1.2.1.10.48.1.5.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointES,
'1.3.6.1.2.1.10.48.1.5.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointSES,
'1.3.6.1.2.1.10.48.1.5.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCRCanomalies,
'1.3.6.1.2.1.10.48.1.5.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointLOSWS,
'1.3.6.1.2.1.10.48.1.5.1.8': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointUAS,
'1.3.6.1.2.1.10.48.1.5.1.9': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinTimeElapsed,
'1.3.6.1.2.1.10.48.1.5.1.10': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinES,
'1.3.6.1.2.1.10.48.1.5.1.11': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinSES,
'1.3.6.1.2.1.10.48.1.5.1.12': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinCRCanomalies,
'1.3.6.1.2.1.10.48.1.5.1.13': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinLOSWS,
'1.3.6.1.2.1.10.48.1.5.1.14': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr15MinUAS,
'1.3.6.1.2.1.10.48.1.5.1.15': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DayTimeElapsed,
'1.3.6.1.2.1.10.48.1.5.1.16': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DayES,
'1.3.6.1.2.1.10.48.1.5.1.17': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DaySES,
'1.3.6.1.2.1.10.48.1.5.1.18': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DayCRCanomalies,
'1.3.6.1.2.1.10.48.1.5.1.19': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DayLOSWS,
'1.3.6.1.2.1.10.48.1.5.1.20': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurr1DayUAS,
'1.3.6.1.2.1.10.48.1.5.1.21': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrTipRingReversal,
'1.3.6.1.2.1.10.48.1.5.1.22': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrActivationState,
'1.3.6.1.2.1.10.48.1.6.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalNumber,
'1.3.6.1.2.1.10.48.1.6.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalES,
'1.3.6.1.2.1.10.48.1.6.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalSES,
'1.3.6.1.2.1.10.48.1.6.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalCRCanomalies,
'1.3.6.1.2.1.10.48.1.6.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalLOSWS,
'1.3.6.1.2.1.10.48.1.6.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalUAS,
'1.3.6.1.2.1.10.48.1.7.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalNumber,
'1.3.6.1.2.1.10.48.1.7.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalMoniSecs,
'1.3.6.1.2.1.10.48.1.7.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalES,
'1.3.6.1.2.1.10.48.1.7.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalSES,
'1.3.6.1.2.1.10.48.1.7.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalCRCanomalies,
'1.3.6.1.2.1.10.48.1.7.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalLOSWS,
'1.3.6.1.2.1.10.48.1.7.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalUAS,
'1.3.6.1.2.1.10.48.1.8.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintLoopbackConfig,
'1.3.6.1.2.1.10.48.1.8.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintTipRingReversal,
'1.3.6.1.2.1.10.48.1.8.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintPowerBackOff,
'1.3.6.1.2.1.10.48.1.8.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintSoftRestart,
'1.3.6.1.2.1.10.48.1.9.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintLoopbackTimeout,
'1.3.6.1.2.1.10.48.1.9.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintUnitPowerSource,
'1.3.6.1.2.1.10.48.1.10.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfProfileName,
'1.3.6.1.2.1.10.48.1.10.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfWireInterface,
'1.3.6.1.2.1.10.48.1.10.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfMinLineRate,
'1.3.6.1.2.1.10.48.1.10.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfMaxLineRate,
'1.3.6.1.2.1.10.48.1.10.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfPSD,
'1.3.6.1.2.1.10.48.1.10.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfTransmissionMode,
'1.3.6.1.2.1.10.48.1.10.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfRemoteEnabled,
'1.3.6.1.2.1.10.48.1.10.1.8': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfPowerFeeding,
'1.3.6.1.2.1.10.48.1.10.1.9': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfCurrCondTargetMarginDown,
'1.3.6.1.2.1.10.48.1.10.1.10': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfWorstCaseTargetMarginDown,
'1.3.6.1.2.1.10.48.1.10.1.11': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfCurrCondTargetMarginUp,
'1.3.6.1.2.1.10.48.1.10.1.12': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfWorstCaseTargetMarginUp,
'1.3.6.1.2.1.10.48.1.10.1.13': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfUsedTargetMargins,
'1.3.6.1.2.1.10.48.1.10.1.14': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfReferenceClock,
'1.3.6.1.2.1.10.48.1.10.1.15': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfLineProbeEnable,
'1.3.6.1.2.1.10.48.1.10.1.16': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfProfileRowStatus,
'1.3.6.1.2.1.10.48.1.11.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointAlarmConfProfileName,
'1.3.6.1.2.1.10.48.1.11.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshLoopAttenuation,
'1.3.6.1.2.1.10.48.1.11.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshSNRMargin,
'1.3.6.1.2.1.10.48.1.11.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshES,
'1.3.6.1.2.1.10.48.1.11.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshSES,
'1.3.6.1.2.1.10.48.1.11.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshCRCanomalies,
'1.3.6.1.2.1.10.48.1.11.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshLOSWS,
'1.3.6.1.2.1.10.48.1.11.1.8': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointThreshUAS,
'1.3.6.1.2.1.10.48.1.11.1.9': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointAlarmConfProfileRowStatus,
'1.3.6.1.2.1.10.48.0.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslLoopAttenCrossing,
'1.3.6.1.2.1.10.48.0.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSNRMarginCrossing,
'1.3.6.1.2.1.10.48.0.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPerfESThresh,
'1.3.6.1.2.1.10.48.0.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPerfSESThresh,
'1.3.6.1.2.1.10.48.0.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPerfCRCanomaliesThresh,
'1.3.6.1.2.1.10.48.0.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPerfLOSWSThresh,
'1.3.6.1.2.1.10.48.0.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPerfUASThresh,
'1.3.6.1.2.1.10.48.0.8': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanInvalidNumRepeaters,
'1.3.6.1.2.1.10.48.0.9': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslLoopbackFailure,
'1.3.6.1.2.1.10.48.0.10': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslpowerBackoff,
'1.3.6.1.2.1.10.48.0.11': HDSL2_SHDSL_LINE_MIB.hdsl2ShdsldeviceFault,
'1.3.6.1.2.1.10.48.0.12': HDSL2_SHDSL_LINE_MIB.hdsl2ShdsldcContinuityFault,
'1.3.6.1.2.1.10.48.0.13': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslconfigInitFailure,
'1.3.6.1.2.1.10.48.0.14': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslprotocolInitFailure,
'1.3.6.1.2.1.10.48.0.15': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslnoNeighborPresent,
'1.3.6.1.2.1.10.48.0.16': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslLocalPowerLoss,
'1.3.6.1.2.1.10.48.3.1.1': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfGroup,
'1.3.6.1.2.1.10.48.3.1.2': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanStatusGroup,
'1.3.6.1.2.1.10.48.3.1.3': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInventoryShdslGroup,
'1.3.6.1.2.1.10.48.3.1.4': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanShdslStatusGroup,
'1.3.6.1.2.1.10.48.3.1.5': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslInventoryGroup,
'1.3.6.1.2.1.10.48.3.1.6': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointConfGroup,
'1.3.6.1.2.1.10.48.3.1.7': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointCurrGroup,
'1.3.6.1.2.1.10.48.3.1.8': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl15MinIntervalGroup,
'1.3.6.1.2.1.10.48.3.1.9': HDSL2_SHDSL_LINE_MIB.hdsl2Shdsl1DayIntervalGroup,
'1.3.6.1.2.1.10.48.3.1.10': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslMaintenanceGroup,
'1.3.6.1.2.1.10.48.3.1.11': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslEndpointAlarmConfGroup,
'1.3.6.1.2.1.10.48.3.1.12': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslNotificationGroup,
'1.3.6.1.2.1.10.48.3.1.13': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslSpanConfProfileGroup,
'1.3.6.1.2.1.10.48.3.1.14': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslWirePairGroup,
'1.3.6.1.2.1.10.48.3.1.15': HDSL2_SHDSL_LINE_MIB.hdsl2ShdslPayloadRateGroup,
}
