# python
# This file is generated by a program (mib2py). 

import ADSL_LINE_MIB

OIDMAP = {
'1.3.6.1.2.1.10.94': ADSL_LINE_MIB.adslMIB,
'1.3.6.1.2.1.10.94.1': ADSL_LINE_MIB.adslLineMib,
'1.3.6.1.2.1.10.94.1.1': ADSL_LINE_MIB.adslMibObjects,
'1.3.6.1.2.1.10.94.1.1.16': ADSL_LINE_MIB.adslLCSMib,
'1.3.6.1.2.1.10.94.1.2': ADSL_LINE_MIB.adslTraps,
'1.3.6.1.2.1.10.94.1.2.1': ADSL_LINE_MIB.adslAtucTraps,
'1.3.6.1.2.1.10.94.1.2.2': ADSL_LINE_MIB.adslAturTraps,
'1.3.6.1.2.1.10.94.1.3': ADSL_LINE_MIB.adslConformance,
'1.3.6.1.2.1.10.94.1.3.1': ADSL_LINE_MIB.adslGroups,
'1.3.6.1.2.1.10.94.1.3.2': ADSL_LINE_MIB.adslCompliances,
'1.3.6.1.2.1.10.94.1.1.1.1.1': ADSL_LINE_MIB.adslLineCoding,
'1.3.6.1.2.1.10.94.1.1.1.1.2': ADSL_LINE_MIB.adslLineType,
'1.3.6.1.2.1.10.94.1.1.1.1.3': ADSL_LINE_MIB.adslLineSpecific,
'1.3.6.1.2.1.10.94.1.1.1.1.4': ADSL_LINE_MIB.adslLineConfProfile,
'1.3.6.1.2.1.10.94.1.1.1.1.5': ADSL_LINE_MIB.adslLineAlarmConfProfile,
'1.3.6.1.2.1.10.94.1.1.2.1.1': ADSL_LINE_MIB.adslAtucInvSerialNumber,
'1.3.6.1.2.1.10.94.1.1.2.1.2': ADSL_LINE_MIB.adslAtucInvVendorID,
'1.3.6.1.2.1.10.94.1.1.2.1.3': ADSL_LINE_MIB.adslAtucInvVersionNumber,
'1.3.6.1.2.1.10.94.1.1.2.1.4': ADSL_LINE_MIB.adslAtucCurrSnrMgn,
'1.3.6.1.2.1.10.94.1.1.2.1.5': ADSL_LINE_MIB.adslAtucCurrAtn,
'1.3.6.1.2.1.10.94.1.1.2.1.6': ADSL_LINE_MIB.adslAtucCurrStatus,
'1.3.6.1.2.1.10.94.1.1.2.1.7': ADSL_LINE_MIB.adslAtucCurrOutputPwr,
'1.3.6.1.2.1.10.94.1.1.2.1.8': ADSL_LINE_MIB.adslAtucCurrAttainableRate,
'1.3.6.1.2.1.10.94.1.1.3.1.1': ADSL_LINE_MIB.adslAturInvSerialNumber,
'1.3.6.1.2.1.10.94.1.1.3.1.2': ADSL_LINE_MIB.adslAturInvVendorID,
'1.3.6.1.2.1.10.94.1.1.3.1.3': ADSL_LINE_MIB.adslAturInvVersionNumber,
'1.3.6.1.2.1.10.94.1.1.3.1.4': ADSL_LINE_MIB.adslAturCurrSnrMgn,
'1.3.6.1.2.1.10.94.1.1.3.1.5': ADSL_LINE_MIB.adslAturCurrAtn,
'1.3.6.1.2.1.10.94.1.1.3.1.6': ADSL_LINE_MIB.adslAturCurrStatus,
'1.3.6.1.2.1.10.94.1.1.3.1.7': ADSL_LINE_MIB.adslAturCurrOutputPwr,
'1.3.6.1.2.1.10.94.1.1.3.1.8': ADSL_LINE_MIB.adslAturCurrAttainableRate,
'1.3.6.1.2.1.10.94.1.1.4.1.1': ADSL_LINE_MIB.adslAtucChanInterleaveDelay,
'1.3.6.1.2.1.10.94.1.1.4.1.2': ADSL_LINE_MIB.adslAtucChanCurrTxRate,
'1.3.6.1.2.1.10.94.1.1.4.1.3': ADSL_LINE_MIB.adslAtucChanPrevTxRate,
'1.3.6.1.2.1.10.94.1.1.4.1.4': ADSL_LINE_MIB.adslAtucChanCrcBlockLength,
'1.3.6.1.2.1.10.94.1.1.5.1.1': ADSL_LINE_MIB.adslAturChanInterleaveDelay,
'1.3.6.1.2.1.10.94.1.1.5.1.2': ADSL_LINE_MIB.adslAturChanCurrTxRate,
'1.3.6.1.2.1.10.94.1.1.5.1.3': ADSL_LINE_MIB.adslAturChanPrevTxRate,
'1.3.6.1.2.1.10.94.1.1.5.1.4': ADSL_LINE_MIB.adslAturChanCrcBlockLength,
'1.3.6.1.2.1.10.94.1.1.6.1.1': ADSL_LINE_MIB.adslAtucPerfLofs,
'1.3.6.1.2.1.10.94.1.1.6.1.2': ADSL_LINE_MIB.adslAtucPerfLoss,
'1.3.6.1.2.1.10.94.1.1.6.1.3': ADSL_LINE_MIB.adslAtucPerfLols,
'1.3.6.1.2.1.10.94.1.1.6.1.4': ADSL_LINE_MIB.adslAtucPerfLprs,
'1.3.6.1.2.1.10.94.1.1.6.1.5': ADSL_LINE_MIB.adslAtucPerfESs,
'1.3.6.1.2.1.10.94.1.1.6.1.6': ADSL_LINE_MIB.adslAtucPerfInits,
'1.3.6.1.2.1.10.94.1.1.6.1.7': ADSL_LINE_MIB.adslAtucPerfValidIntervals,
'1.3.6.1.2.1.10.94.1.1.6.1.8': ADSL_LINE_MIB.adslAtucPerfInvalidIntervals,
'1.3.6.1.2.1.10.94.1.1.6.1.9': ADSL_LINE_MIB.adslAtucPerfCurr15MinTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.6.1.10': ADSL_LINE_MIB.adslAtucPerfCurr15MinLofs,
'1.3.6.1.2.1.10.94.1.1.6.1.11': ADSL_LINE_MIB.adslAtucPerfCurr15MinLoss,
'1.3.6.1.2.1.10.94.1.1.6.1.12': ADSL_LINE_MIB.adslAtucPerfCurr15MinLols,
'1.3.6.1.2.1.10.94.1.1.6.1.13': ADSL_LINE_MIB.adslAtucPerfCurr15MinLprs,
'1.3.6.1.2.1.10.94.1.1.6.1.14': ADSL_LINE_MIB.adslAtucPerfCurr15MinESs,
'1.3.6.1.2.1.10.94.1.1.6.1.15': ADSL_LINE_MIB.adslAtucPerfCurr15MinInits,
'1.3.6.1.2.1.10.94.1.1.6.1.16': ADSL_LINE_MIB.adslAtucPerfCurr1DayTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.6.1.17': ADSL_LINE_MIB.adslAtucPerfCurr1DayLofs,
'1.3.6.1.2.1.10.94.1.1.6.1.18': ADSL_LINE_MIB.adslAtucPerfCurr1DayLoss,
'1.3.6.1.2.1.10.94.1.1.6.1.19': ADSL_LINE_MIB.adslAtucPerfCurr1DayLols,
'1.3.6.1.2.1.10.94.1.1.6.1.20': ADSL_LINE_MIB.adslAtucPerfCurr1DayLprs,
'1.3.6.1.2.1.10.94.1.1.6.1.21': ADSL_LINE_MIB.adslAtucPerfCurr1DayESs,
'1.3.6.1.2.1.10.94.1.1.6.1.22': ADSL_LINE_MIB.adslAtucPerfCurr1DayInits,
'1.3.6.1.2.1.10.94.1.1.6.1.23': ADSL_LINE_MIB.adslAtucPerfPrev1DayMoniSecs,
'1.3.6.1.2.1.10.94.1.1.6.1.24': ADSL_LINE_MIB.adslAtucPerfPrev1DayLofs,
'1.3.6.1.2.1.10.94.1.1.6.1.25': ADSL_LINE_MIB.adslAtucPerfPrev1DayLoss,
'1.3.6.1.2.1.10.94.1.1.6.1.26': ADSL_LINE_MIB.adslAtucPerfPrev1DayLols,
'1.3.6.1.2.1.10.94.1.1.6.1.27': ADSL_LINE_MIB.adslAtucPerfPrev1DayLprs,
'1.3.6.1.2.1.10.94.1.1.6.1.28': ADSL_LINE_MIB.adslAtucPerfPrev1DayESs,
'1.3.6.1.2.1.10.94.1.1.6.1.29': ADSL_LINE_MIB.adslAtucPerfPrev1DayInits,
'1.3.6.1.2.1.10.94.1.1.7.1.1': ADSL_LINE_MIB.adslAturPerfLofs,
'1.3.6.1.2.1.10.94.1.1.7.1.2': ADSL_LINE_MIB.adslAturPerfLoss,
'1.3.6.1.2.1.10.94.1.1.7.1.3': ADSL_LINE_MIB.adslAturPerfLprs,
'1.3.6.1.2.1.10.94.1.1.7.1.4': ADSL_LINE_MIB.adslAturPerfESs,
'1.3.6.1.2.1.10.94.1.1.7.1.5': ADSL_LINE_MIB.adslAturPerfValidIntervals,
'1.3.6.1.2.1.10.94.1.1.7.1.6': ADSL_LINE_MIB.adslAturPerfInvalidIntervals,
'1.3.6.1.2.1.10.94.1.1.7.1.7': ADSL_LINE_MIB.adslAturPerfCurr15MinTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.7.1.8': ADSL_LINE_MIB.adslAturPerfCurr15MinLofs,
'1.3.6.1.2.1.10.94.1.1.7.1.9': ADSL_LINE_MIB.adslAturPerfCurr15MinLoss,
'1.3.6.1.2.1.10.94.1.1.7.1.10': ADSL_LINE_MIB.adslAturPerfCurr15MinLprs,
'1.3.6.1.2.1.10.94.1.1.7.1.11': ADSL_LINE_MIB.adslAturPerfCurr15MinESs,
'1.3.6.1.2.1.10.94.1.1.7.1.12': ADSL_LINE_MIB.adslAturPerfCurr1DayTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.7.1.13': ADSL_LINE_MIB.adslAturPerfCurr1DayLofs,
'1.3.6.1.2.1.10.94.1.1.7.1.14': ADSL_LINE_MIB.adslAturPerfCurr1DayLoss,
'1.3.6.1.2.1.10.94.1.1.7.1.15': ADSL_LINE_MIB.adslAturPerfCurr1DayLprs,
'1.3.6.1.2.1.10.94.1.1.7.1.16': ADSL_LINE_MIB.adslAturPerfCurr1DayESs,
'1.3.6.1.2.1.10.94.1.1.7.1.17': ADSL_LINE_MIB.adslAturPerfPrev1DayMoniSecs,
'1.3.6.1.2.1.10.94.1.1.7.1.18': ADSL_LINE_MIB.adslAturPerfPrev1DayLofs,
'1.3.6.1.2.1.10.94.1.1.7.1.19': ADSL_LINE_MIB.adslAturPerfPrev1DayLoss,
'1.3.6.1.2.1.10.94.1.1.7.1.20': ADSL_LINE_MIB.adslAturPerfPrev1DayLprs,
'1.3.6.1.2.1.10.94.1.1.7.1.21': ADSL_LINE_MIB.adslAturPerfPrev1DayESs,
'1.3.6.1.2.1.10.94.1.1.8.1.1': ADSL_LINE_MIB.adslAtucIntervalNumber,
'1.3.6.1.2.1.10.94.1.1.8.1.2': ADSL_LINE_MIB.adslAtucIntervalLofs,
'1.3.6.1.2.1.10.94.1.1.8.1.3': ADSL_LINE_MIB.adslAtucIntervalLoss,
'1.3.6.1.2.1.10.94.1.1.8.1.4': ADSL_LINE_MIB.adslAtucIntervalLols,
'1.3.6.1.2.1.10.94.1.1.8.1.5': ADSL_LINE_MIB.adslAtucIntervalLprs,
'1.3.6.1.2.1.10.94.1.1.8.1.6': ADSL_LINE_MIB.adslAtucIntervalESs,
'1.3.6.1.2.1.10.94.1.1.8.1.7': ADSL_LINE_MIB.adslAtucIntervalInits,
'1.3.6.1.2.1.10.94.1.1.8.1.8': ADSL_LINE_MIB.adslAtucIntervalValidData,
'1.3.6.1.2.1.10.94.1.1.9.1.1': ADSL_LINE_MIB.adslAturIntervalNumber,
'1.3.6.1.2.1.10.94.1.1.9.1.2': ADSL_LINE_MIB.adslAturIntervalLofs,
'1.3.6.1.2.1.10.94.1.1.9.1.3': ADSL_LINE_MIB.adslAturIntervalLoss,
'1.3.6.1.2.1.10.94.1.1.9.1.4': ADSL_LINE_MIB.adslAturIntervalLprs,
'1.3.6.1.2.1.10.94.1.1.9.1.5': ADSL_LINE_MIB.adslAturIntervalESs,
'1.3.6.1.2.1.10.94.1.1.9.1.6': ADSL_LINE_MIB.adslAturIntervalValidData,
'1.3.6.1.2.1.10.94.1.1.10.1.1': ADSL_LINE_MIB.adslAtucChanReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.2': ADSL_LINE_MIB.adslAtucChanTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.3': ADSL_LINE_MIB.adslAtucChanCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.4': ADSL_LINE_MIB.adslAtucChanUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.5': ADSL_LINE_MIB.adslAtucChanPerfValidIntervals,
'1.3.6.1.2.1.10.94.1.1.10.1.6': ADSL_LINE_MIB.adslAtucChanPerfInvalidIntervals,
'1.3.6.1.2.1.10.94.1.1.10.1.7': ADSL_LINE_MIB.adslAtucChanPerfCurr15MinTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.10.1.8': ADSL_LINE_MIB.adslAtucChanPerfCurr15MinReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.9': ADSL_LINE_MIB.adslAtucChanPerfCurr15MinTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.10': ADSL_LINE_MIB.adslAtucChanPerfCurr15MinCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.11': ADSL_LINE_MIB.adslAtucChanPerfCurr15MinUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.12': ADSL_LINE_MIB.adslAtucChanPerfCurr1DayTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.10.1.13': ADSL_LINE_MIB.adslAtucChanPerfCurr1DayReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.14': ADSL_LINE_MIB.adslAtucChanPerfCurr1DayTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.15': ADSL_LINE_MIB.adslAtucChanPerfCurr1DayCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.16': ADSL_LINE_MIB.adslAtucChanPerfCurr1DayUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.17': ADSL_LINE_MIB.adslAtucChanPerfPrev1DayMoniSecs,
'1.3.6.1.2.1.10.94.1.1.10.1.18': ADSL_LINE_MIB.adslAtucChanPerfPrev1DayReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.19': ADSL_LINE_MIB.adslAtucChanPerfPrev1DayTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.20': ADSL_LINE_MIB.adslAtucChanPerfPrev1DayCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.10.1.21': ADSL_LINE_MIB.adslAtucChanPerfPrev1DayUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.1': ADSL_LINE_MIB.adslAturChanReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.2': ADSL_LINE_MIB.adslAturChanTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.3': ADSL_LINE_MIB.adslAturChanCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.4': ADSL_LINE_MIB.adslAturChanUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.5': ADSL_LINE_MIB.adslAturChanPerfValidIntervals,
'1.3.6.1.2.1.10.94.1.1.11.1.6': ADSL_LINE_MIB.adslAturChanPerfInvalidIntervals,
'1.3.6.1.2.1.10.94.1.1.11.1.7': ADSL_LINE_MIB.adslAturChanPerfCurr15MinTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.11.1.8': ADSL_LINE_MIB.adslAturChanPerfCurr15MinReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.9': ADSL_LINE_MIB.adslAturChanPerfCurr15MinTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.10': ADSL_LINE_MIB.adslAturChanPerfCurr15MinCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.11': ADSL_LINE_MIB.adslAturChanPerfCurr15MinUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.12': ADSL_LINE_MIB.adslAturChanPerfCurr1DayTimeElapsed,
'1.3.6.1.2.1.10.94.1.1.11.1.13': ADSL_LINE_MIB.adslAturChanPerfCurr1DayReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.14': ADSL_LINE_MIB.adslAturChanPerfCurr1DayTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.15': ADSL_LINE_MIB.adslAturChanPerfCurr1DayCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.16': ADSL_LINE_MIB.adslAturChanPerfCurr1DayUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.17': ADSL_LINE_MIB.adslAturChanPerfPrev1DayMoniSecs,
'1.3.6.1.2.1.10.94.1.1.11.1.18': ADSL_LINE_MIB.adslAturChanPerfPrev1DayReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.19': ADSL_LINE_MIB.adslAturChanPerfPrev1DayTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.20': ADSL_LINE_MIB.adslAturChanPerfPrev1DayCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.11.1.21': ADSL_LINE_MIB.adslAturChanPerfPrev1DayUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.12.1.1': ADSL_LINE_MIB.adslAtucChanIntervalNumber,
'1.3.6.1.2.1.10.94.1.1.12.1.2': ADSL_LINE_MIB.adslAtucChanIntervalReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.12.1.3': ADSL_LINE_MIB.adslAtucChanIntervalTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.12.1.4': ADSL_LINE_MIB.adslAtucChanIntervalCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.12.1.5': ADSL_LINE_MIB.adslAtucChanIntervalUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.12.1.6': ADSL_LINE_MIB.adslAtucChanIntervalValidData,
'1.3.6.1.2.1.10.94.1.1.13.1.1': ADSL_LINE_MIB.adslAturChanIntervalNumber,
'1.3.6.1.2.1.10.94.1.1.13.1.2': ADSL_LINE_MIB.adslAturChanIntervalReceivedBlks,
'1.3.6.1.2.1.10.94.1.1.13.1.3': ADSL_LINE_MIB.adslAturChanIntervalTransmittedBlks,
'1.3.6.1.2.1.10.94.1.1.13.1.4': ADSL_LINE_MIB.adslAturChanIntervalCorrectedBlks,
'1.3.6.1.2.1.10.94.1.1.13.1.5': ADSL_LINE_MIB.adslAturChanIntervalUncorrectBlks,
'1.3.6.1.2.1.10.94.1.1.13.1.6': ADSL_LINE_MIB.adslAturChanIntervalValidData,
'1.3.6.1.2.1.10.94.1.1.14.1.1': ADSL_LINE_MIB.adslLineConfProfileName,
'1.3.6.1.2.1.10.94.1.1.14.1.2': ADSL_LINE_MIB.adslAtucConfRateMode,
'1.3.6.1.2.1.10.94.1.1.14.1.3': ADSL_LINE_MIB.adslAtucConfRateChanRatio,
'1.3.6.1.2.1.10.94.1.1.14.1.4': ADSL_LINE_MIB.adslAtucConfTargetSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.5': ADSL_LINE_MIB.adslAtucConfMaxSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.6': ADSL_LINE_MIB.adslAtucConfMinSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.7': ADSL_LINE_MIB.adslAtucConfDownshiftSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.8': ADSL_LINE_MIB.adslAtucConfUpshiftSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.9': ADSL_LINE_MIB.adslAtucConfMinUpshiftTime,
'1.3.6.1.2.1.10.94.1.1.14.1.10': ADSL_LINE_MIB.adslAtucConfMinDownshiftTime,
'1.3.6.1.2.1.10.94.1.1.14.1.11': ADSL_LINE_MIB.adslAtucChanConfFastMinTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.12': ADSL_LINE_MIB.adslAtucChanConfInterleaveMinTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.13': ADSL_LINE_MIB.adslAtucChanConfFastMaxTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.14': ADSL_LINE_MIB.adslAtucChanConfInterleaveMaxTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.15': ADSL_LINE_MIB.adslAtucChanConfMaxInterleaveDelay,
'1.3.6.1.2.1.10.94.1.1.14.1.16': ADSL_LINE_MIB.adslAturConfRateMode,
'1.3.6.1.2.1.10.94.1.1.14.1.17': ADSL_LINE_MIB.adslAturConfRateChanRatio,
'1.3.6.1.2.1.10.94.1.1.14.1.18': ADSL_LINE_MIB.adslAturConfTargetSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.19': ADSL_LINE_MIB.adslAturConfMaxSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.20': ADSL_LINE_MIB.adslAturConfMinSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.21': ADSL_LINE_MIB.adslAturConfDownshiftSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.22': ADSL_LINE_MIB.adslAturConfUpshiftSnrMgn,
'1.3.6.1.2.1.10.94.1.1.14.1.23': ADSL_LINE_MIB.adslAturConfMinUpshiftTime,
'1.3.6.1.2.1.10.94.1.1.14.1.24': ADSL_LINE_MIB.adslAturConfMinDownshiftTime,
'1.3.6.1.2.1.10.94.1.1.14.1.25': ADSL_LINE_MIB.adslAturChanConfFastMinTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.26': ADSL_LINE_MIB.adslAturChanConfInterleaveMinTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.27': ADSL_LINE_MIB.adslAturChanConfFastMaxTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.28': ADSL_LINE_MIB.adslAturChanConfInterleaveMaxTxRate,
'1.3.6.1.2.1.10.94.1.1.14.1.29': ADSL_LINE_MIB.adslAturChanConfMaxInterleaveDelay,
'1.3.6.1.2.1.10.94.1.1.14.1.30': ADSL_LINE_MIB.adslLineConfProfileRowStatus,
'1.3.6.1.2.1.10.94.1.1.15.1.1': ADSL_LINE_MIB.adslLineAlarmConfProfileName,
'1.3.6.1.2.1.10.94.1.1.15.1.2': ADSL_LINE_MIB.adslAtucThresh15MinLofs,
'1.3.6.1.2.1.10.94.1.1.15.1.3': ADSL_LINE_MIB.adslAtucThresh15MinLoss,
'1.3.6.1.2.1.10.94.1.1.15.1.4': ADSL_LINE_MIB.adslAtucThresh15MinLols,
'1.3.6.1.2.1.10.94.1.1.15.1.5': ADSL_LINE_MIB.adslAtucThresh15MinLprs,
'1.3.6.1.2.1.10.94.1.1.15.1.6': ADSL_LINE_MIB.adslAtucThresh15MinESs,
'1.3.6.1.2.1.10.94.1.1.15.1.7': ADSL_LINE_MIB.adslAtucThreshFastRateUp,
'1.3.6.1.2.1.10.94.1.1.15.1.8': ADSL_LINE_MIB.adslAtucThreshInterleaveRateUp,
'1.3.6.1.2.1.10.94.1.1.15.1.9': ADSL_LINE_MIB.adslAtucThreshFastRateDown,
'1.3.6.1.2.1.10.94.1.1.15.1.10': ADSL_LINE_MIB.adslAtucThreshInterleaveRateDown,
'1.3.6.1.2.1.10.94.1.1.15.1.11': ADSL_LINE_MIB.adslAtucInitFailureTrapEnable,
'1.3.6.1.2.1.10.94.1.1.15.1.12': ADSL_LINE_MIB.adslAturThresh15MinLofs,
'1.3.6.1.2.1.10.94.1.1.15.1.13': ADSL_LINE_MIB.adslAturThresh15MinLoss,
'1.3.6.1.2.1.10.94.1.1.15.1.14': ADSL_LINE_MIB.adslAturThresh15MinLprs,
'1.3.6.1.2.1.10.94.1.1.15.1.15': ADSL_LINE_MIB.adslAturThresh15MinESs,
'1.3.6.1.2.1.10.94.1.1.15.1.16': ADSL_LINE_MIB.adslAturThreshFastRateUp,
'1.3.6.1.2.1.10.94.1.1.15.1.17': ADSL_LINE_MIB.adslAturThreshInterleaveRateUp,
'1.3.6.1.2.1.10.94.1.1.15.1.18': ADSL_LINE_MIB.adslAturThreshFastRateDown,
'1.3.6.1.2.1.10.94.1.1.15.1.19': ADSL_LINE_MIB.adslAturThreshInterleaveRateDown,
'1.3.6.1.2.1.10.94.1.1.15.1.20': ADSL_LINE_MIB.adslLineAlarmConfProfileRowStatus,
'1.3.6.1.2.1.10.94.1.2.1.0.1': ADSL_LINE_MIB.adslAtucPerfLofsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.2': ADSL_LINE_MIB.adslAtucPerfLossThreshTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.3': ADSL_LINE_MIB.adslAtucPerfLprsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.4': ADSL_LINE_MIB.adslAtucPerfESsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.5': ADSL_LINE_MIB.adslAtucRateChangeTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.6': ADSL_LINE_MIB.adslAtucPerfLolsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.1.0.7': ADSL_LINE_MIB.adslAtucInitFailureTrap,
'1.3.6.1.2.1.10.94.1.2.2.0.1': ADSL_LINE_MIB.adslAturPerfLofsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.2.0.2': ADSL_LINE_MIB.adslAturPerfLossThreshTrap,
'1.3.6.1.2.1.10.94.1.2.2.0.3': ADSL_LINE_MIB.adslAturPerfLprsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.2.0.4': ADSL_LINE_MIB.adslAturPerfESsThreshTrap,
'1.3.6.1.2.1.10.94.1.2.2.0.5': ADSL_LINE_MIB.adslAturRateChangeTrap,
'1.3.6.1.2.1.10.94.1.3.1.1': ADSL_LINE_MIB.adslLineGroup,
'1.3.6.1.2.1.10.94.1.3.1.2': ADSL_LINE_MIB.adslPhysicalGroup,
'1.3.6.1.2.1.10.94.1.3.1.3': ADSL_LINE_MIB.adslChannelGroup,
'1.3.6.1.2.1.10.94.1.3.1.4': ADSL_LINE_MIB.adslAtucPhysPerfRawCounterGroup,
'1.3.6.1.2.1.10.94.1.3.1.5': ADSL_LINE_MIB.adslAtucPhysPerfIntervalGroup,
'1.3.6.1.2.1.10.94.1.3.1.6': ADSL_LINE_MIB.adslAturPhysPerfRawCounterGroup,
'1.3.6.1.2.1.10.94.1.3.1.7': ADSL_LINE_MIB.adslAturPhysPerfIntervalGroup,
'1.3.6.1.2.1.10.94.1.3.1.8': ADSL_LINE_MIB.adslAtucChanPerformanceGroup,
'1.3.6.1.2.1.10.94.1.3.1.9': ADSL_LINE_MIB.adslAturChanPerformanceGroup,
'1.3.6.1.2.1.10.94.1.3.1.10': ADSL_LINE_MIB.adslLineConfProfileGroup,
'1.3.6.1.2.1.10.94.1.3.1.11': ADSL_LINE_MIB.adslLineAlarmConfProfileGroup,
'1.3.6.1.2.1.10.94.1.3.1.12': ADSL_LINE_MIB.adslLineConfProfileControlGroup,
'1.3.6.1.2.1.10.94.1.3.1.13': ADSL_LINE_MIB.adslNotificationsGroup,
'1.3.6.1.2.1.10.94.1.3.1.14': ADSL_LINE_MIB.adslAturLineGroup,
'1.3.6.1.2.1.10.94.1.3.1.15': ADSL_LINE_MIB.adslAturPhysicalGroup,
'1.3.6.1.2.1.10.94.1.3.1.16': ADSL_LINE_MIB.adslAturChannelGroup,
'1.3.6.1.2.1.10.94.1.3.1.17': ADSL_LINE_MIB.adslAturAtucPhysPerfRawCounterGroup,
'1.3.6.1.2.1.10.94.1.3.1.18': ADSL_LINE_MIB.adslAturAtucPhysPerfIntervalGroup,
'1.3.6.1.2.1.10.94.1.3.1.19': ADSL_LINE_MIB.adslAturAturPhysPerfRawCounterGroup,
'1.3.6.1.2.1.10.94.1.3.1.20': ADSL_LINE_MIB.adslAturAturPhysPerfIntervalGroup,
'1.3.6.1.2.1.10.94.1.3.1.21': ADSL_LINE_MIB.adslAturAtucChanPerformanceGroup,
'1.3.6.1.2.1.10.94.1.3.1.22': ADSL_LINE_MIB.adslAturAturChanPerformanceGroup,
'1.3.6.1.2.1.10.94.1.3.1.23': ADSL_LINE_MIB.adslAturLineAlarmConfProfileGroup,
'1.3.6.1.2.1.10.94.1.3.1.24': ADSL_LINE_MIB.adslAturLineConfProfileControlGroup,
'1.3.6.1.2.1.10.94.1.3.1.25': ADSL_LINE_MIB.adslAturNotificationsGroup,
}
