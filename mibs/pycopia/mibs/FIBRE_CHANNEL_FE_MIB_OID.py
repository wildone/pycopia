# python
# This file is generated by a program (mib2py). 

import FIBRE_CHANNEL_FE_MIB

OIDMAP = {
'1.3.6.1.2.1.75': FIBRE_CHANNEL_FE_MIB.fcFeMIB,
'1.3.6.1.2.1.75.1': FIBRE_CHANNEL_FE_MIB.fcFeMIBObjects,
'1.3.6.1.2.1.75.1.1': FIBRE_CHANNEL_FE_MIB.fcFeConfig,
'1.3.6.1.2.1.75.1.2': FIBRE_CHANNEL_FE_MIB.fcFeStatus,
'1.3.6.1.2.1.75.1.3': FIBRE_CHANNEL_FE_MIB.fcFeError,
'1.3.6.1.2.1.75.1.4': FIBRE_CHANNEL_FE_MIB.fcFeAccounting,
'1.3.6.1.2.1.75.1.5': FIBRE_CHANNEL_FE_MIB.fcFeCapabilities,
'1.3.6.1.2.1.75.2': FIBRE_CHANNEL_FE_MIB.fcFeMIBConformance,
'1.3.6.1.2.1.75.2.1': FIBRE_CHANNEL_FE_MIB.fcFeMIBCompliances,
'1.3.6.1.2.1.75.2.2': FIBRE_CHANNEL_FE_MIB.fcFeMIBGroups,
'1.3.6.1.2.1.75.1.1.1': FIBRE_CHANNEL_FE_MIB.fcFeFabricName,
'1.3.6.1.2.1.75.1.1.2': FIBRE_CHANNEL_FE_MIB.fcFeElementName,
'1.3.6.1.2.1.75.1.1.3': FIBRE_CHANNEL_FE_MIB.fcFeModuleCapacity,
'1.3.6.1.2.1.75.1.1.4.1.1': FIBRE_CHANNEL_FE_MIB.fcFeModuleIndex,
'1.3.6.1.2.1.75.1.1.4.1.2': FIBRE_CHANNEL_FE_MIB.fcFeModuleDescr,
'1.3.6.1.2.1.75.1.1.4.1.3': FIBRE_CHANNEL_FE_MIB.fcFeModuleObjectID,
'1.3.6.1.2.1.75.1.1.4.1.4': FIBRE_CHANNEL_FE_MIB.fcFeModuleOperStatus,
'1.3.6.1.2.1.75.1.1.4.1.5': FIBRE_CHANNEL_FE_MIB.fcFeModuleLastChange,
'1.3.6.1.2.1.75.1.1.4.1.6': FIBRE_CHANNEL_FE_MIB.fcFeModuleFxPortCapacity,
'1.3.6.1.2.1.75.1.1.4.1.7': FIBRE_CHANNEL_FE_MIB.fcFeModuleName,
'1.3.6.1.2.1.75.1.1.5.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortIndex,
'1.3.6.1.2.1.75.1.1.5.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortName,
'1.3.6.1.2.1.75.1.1.5.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortFcphVersionHigh,
'1.3.6.1.2.1.75.1.1.5.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortFcphVersionLow,
'1.3.6.1.2.1.75.1.1.5.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortBbCredit,
'1.3.6.1.2.1.75.1.1.5.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortRxBufSize,
'1.3.6.1.2.1.75.1.1.5.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortRatov,
'1.3.6.1.2.1.75.1.1.5.1.8': FIBRE_CHANNEL_FE_MIB.fcFxPortEdtov,
'1.3.6.1.2.1.75.1.1.5.1.9': FIBRE_CHANNEL_FE_MIB.fcFxPortCosSupported,
'1.3.6.1.2.1.75.1.1.5.1.10': FIBRE_CHANNEL_FE_MIB.fcFxPortIntermixSupported,
'1.3.6.1.2.1.75.1.1.5.1.11': FIBRE_CHANNEL_FE_MIB.fcFxPortStackedConnMode,
'1.3.6.1.2.1.75.1.1.5.1.12': FIBRE_CHANNEL_FE_MIB.fcFxPortClass2SeqDeliv,
'1.3.6.1.2.1.75.1.1.5.1.13': FIBRE_CHANNEL_FE_MIB.fcFxPortClass3SeqDeliv,
'1.3.6.1.2.1.75.1.1.5.1.14': FIBRE_CHANNEL_FE_MIB.fcFxPortHoldTime,
'1.3.6.1.2.1.75.1.2.1.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortID,
'1.3.6.1.2.1.75.1.2.1.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortBbCreditAvailable,
'1.3.6.1.2.1.75.1.2.1.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortOperMode,
'1.3.6.1.2.1.75.1.2.1.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortAdminMode,
'1.3.6.1.2.1.75.1.2.2.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortPhysAdminStatus,
'1.3.6.1.2.1.75.1.2.2.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortPhysOperStatus,
'1.3.6.1.2.1.75.1.2.2.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortPhysLastChange,
'1.3.6.1.2.1.75.1.2.2.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortPhysRttov,
'1.3.6.1.2.1.75.1.2.3.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortNxLoginIndex,
'1.3.6.1.2.1.75.1.2.3.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortFcphVersionAgreed,
'1.3.6.1.2.1.75.1.2.3.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortNxPortBbCredit,
'1.3.6.1.2.1.75.1.2.3.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortNxPortRxDataFieldSize,
'1.3.6.1.2.1.75.1.2.3.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortCosSuppAgreed,
'1.3.6.1.2.1.75.1.2.3.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortIntermixSuppAgreed,
'1.3.6.1.2.1.75.1.2.3.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortStackedConnModeAgreed,
'1.3.6.1.2.1.75.1.2.3.1.8': FIBRE_CHANNEL_FE_MIB.fcFxPortClass2SeqDelivAgreed,
'1.3.6.1.2.1.75.1.2.3.1.9': FIBRE_CHANNEL_FE_MIB.fcFxPortClass3SeqDelivAgreed,
'1.3.6.1.2.1.75.1.2.3.1.10': FIBRE_CHANNEL_FE_MIB.fcFxPortNxPortName,
'1.3.6.1.2.1.75.1.2.3.1.11': FIBRE_CHANNEL_FE_MIB.fcFxPortConnectedNxPort,
'1.3.6.1.2.1.75.1.2.3.1.12': FIBRE_CHANNEL_FE_MIB.fcFxPortBbCreditModel,
'1.3.6.1.2.1.75.1.3.1.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortLinkFailures,
'1.3.6.1.2.1.75.1.3.1.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortSyncLosses,
'1.3.6.1.2.1.75.1.3.1.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortSigLosses,
'1.3.6.1.2.1.75.1.3.1.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortPrimSeqProtoErrors,
'1.3.6.1.2.1.75.1.3.1.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortInvalidTxWords,
'1.3.6.1.2.1.75.1.3.1.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortInvalidCrcs,
'1.3.6.1.2.1.75.1.3.1.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortDelimiterErrors,
'1.3.6.1.2.1.75.1.3.1.1.8': FIBRE_CHANNEL_FE_MIB.fcFxPortAddressIdErrors,
'1.3.6.1.2.1.75.1.3.1.1.9': FIBRE_CHANNEL_FE_MIB.fcFxPortLinkResetIns,
'1.3.6.1.2.1.75.1.3.1.1.10': FIBRE_CHANNEL_FE_MIB.fcFxPortLinkResetOuts,
'1.3.6.1.2.1.75.1.3.1.1.11': FIBRE_CHANNEL_FE_MIB.fcFxPortOlsIns,
'1.3.6.1.2.1.75.1.3.1.1.12': FIBRE_CHANNEL_FE_MIB.fcFxPortOlsOuts,
'1.3.6.1.2.1.75.1.4.1.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortC1InFrames,
'1.3.6.1.2.1.75.1.4.1.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortC1OutFrames,
'1.3.6.1.2.1.75.1.4.1.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortC1InOctets,
'1.3.6.1.2.1.75.1.4.1.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortC1OutOctets,
'1.3.6.1.2.1.75.1.4.1.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortC1Discards,
'1.3.6.1.2.1.75.1.4.1.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortC1FbsyFrames,
'1.3.6.1.2.1.75.1.4.1.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortC1FrjtFrames,
'1.3.6.1.2.1.75.1.4.1.1.8': FIBRE_CHANNEL_FE_MIB.fcFxPortC1InConnections,
'1.3.6.1.2.1.75.1.4.1.1.9': FIBRE_CHANNEL_FE_MIB.fcFxPortC1OutConnections,
'1.3.6.1.2.1.75.1.4.1.1.10': FIBRE_CHANNEL_FE_MIB.fcFxPortC1ConnTime,
'1.3.6.1.2.1.75.1.4.2.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortC2InFrames,
'1.3.6.1.2.1.75.1.4.2.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortC2OutFrames,
'1.3.6.1.2.1.75.1.4.2.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortC2InOctets,
'1.3.6.1.2.1.75.1.4.2.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortC2OutOctets,
'1.3.6.1.2.1.75.1.4.2.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortC2Discards,
'1.3.6.1.2.1.75.1.4.2.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortC2FbsyFrames,
'1.3.6.1.2.1.75.1.4.2.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortC2FrjtFrames,
'1.3.6.1.2.1.75.1.4.3.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortC3InFrames,
'1.3.6.1.2.1.75.1.4.3.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortC3OutFrames,
'1.3.6.1.2.1.75.1.4.3.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortC3InOctets,
'1.3.6.1.2.1.75.1.4.3.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortC3OutOctets,
'1.3.6.1.2.1.75.1.4.3.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortC3Discards,
'1.3.6.1.2.1.75.1.5.1.1.1': FIBRE_CHANNEL_FE_MIB.fcFxPortCapFcphVersionHigh,
'1.3.6.1.2.1.75.1.5.1.1.2': FIBRE_CHANNEL_FE_MIB.fcFxPortCapFcphVersionLow,
'1.3.6.1.2.1.75.1.5.1.1.3': FIBRE_CHANNEL_FE_MIB.fcFxPortCapBbCreditMax,
'1.3.6.1.2.1.75.1.5.1.1.4': FIBRE_CHANNEL_FE_MIB.fcFxPortCapBbCreditMin,
'1.3.6.1.2.1.75.1.5.1.1.5': FIBRE_CHANNEL_FE_MIB.fcFxPortCapRxDataFieldSizeMax,
'1.3.6.1.2.1.75.1.5.1.1.6': FIBRE_CHANNEL_FE_MIB.fcFxPortCapRxDataFieldSizeMin,
'1.3.6.1.2.1.75.1.5.1.1.7': FIBRE_CHANNEL_FE_MIB.fcFxPortCapCos,
'1.3.6.1.2.1.75.1.5.1.1.8': FIBRE_CHANNEL_FE_MIB.fcFxPortCapIntermix,
'1.3.6.1.2.1.75.1.5.1.1.9': FIBRE_CHANNEL_FE_MIB.fcFxPortCapStackedConnMode,
'1.3.6.1.2.1.75.1.5.1.1.10': FIBRE_CHANNEL_FE_MIB.fcFxPortCapClass2SeqDeliv,
'1.3.6.1.2.1.75.1.5.1.1.11': FIBRE_CHANNEL_FE_MIB.fcFxPortCapClass3SeqDeliv,
'1.3.6.1.2.1.75.1.5.1.1.12': FIBRE_CHANNEL_FE_MIB.fcFxPortCapHoldTimeMax,
'1.3.6.1.2.1.75.1.5.1.1.13': FIBRE_CHANNEL_FE_MIB.fcFxPortCapHoldTimeMin,
'1.3.6.1.2.1.75.2.2.1': FIBRE_CHANNEL_FE_MIB.fcFeConfigGroup,
'1.3.6.1.2.1.75.2.2.2': FIBRE_CHANNEL_FE_MIB.fcFeStatusGroup,
'1.3.6.1.2.1.75.2.2.3': FIBRE_CHANNEL_FE_MIB.fcFeErrorGroup,
'1.3.6.1.2.1.75.2.2.4': FIBRE_CHANNEL_FE_MIB.fcFeClass1AccountingGroup,
'1.3.6.1.2.1.75.2.2.5': FIBRE_CHANNEL_FE_MIB.fcFeClass2AccountingGroup,
'1.3.6.1.2.1.75.2.2.6': FIBRE_CHANNEL_FE_MIB.fcFeClass3AccountingGroup,
'1.3.6.1.2.1.75.2.2.7': FIBRE_CHANNEL_FE_MIB.fcFeCapabilitiesGroup,
}
