# python
# This file is generated by a program (mib2py). 

import PKTC_IETF_MTA_MIB

OIDMAP = {
'1.3.6.1.2.1.140': PKTC_IETF_MTA_MIB.pktcIetfMtaMib,
'1.3.6.1.2.1.140.0': PKTC_IETF_MTA_MIB.pktcMtaNotification,
'1.3.6.1.2.1.140.1': PKTC_IETF_MTA_MIB.pktcMtaMibObjects,
'1.3.6.1.2.1.140.1.1': PKTC_IETF_MTA_MIB.pktcMtaDevBase,
'1.3.6.1.2.1.140.1.2': PKTC_IETF_MTA_MIB.pktcMtaDevServer,
'1.3.6.1.2.1.140.1.3': PKTC_IETF_MTA_MIB.pktcMtaDevSecurity,
'1.3.6.1.2.1.140.1.4': PKTC_IETF_MTA_MIB.pktcMtaDevErrors,
'1.3.6.1.2.1.140.1.4.1': PKTC_IETF_MTA_MIB.pktcMtaDevErrorsTooManyErrors,
'1.3.6.1.2.1.140.2': PKTC_IETF_MTA_MIB.pktcMtaConformance,
'1.3.6.1.2.1.140.2.1': PKTC_IETF_MTA_MIB.pktcMtaCompliances,
'1.3.6.1.2.1.140.2.2': PKTC_IETF_MTA_MIB.pktcMtaGroups,
'1.3.6.1.2.1.140.1.1.1': PKTC_IETF_MTA_MIB.pktcMtaDevResetNow,
'1.3.6.1.2.1.140.1.1.2': PKTC_IETF_MTA_MIB.pktcMtaDevSerialNumber,
'1.3.6.1.2.1.140.1.1.3': PKTC_IETF_MTA_MIB.pktcMtaDevSwCurrentVers,
'1.3.6.1.2.1.140.1.1.4': PKTC_IETF_MTA_MIB.pktcMtaDevFQDN,
'1.3.6.1.2.1.140.1.1.5': PKTC_IETF_MTA_MIB.pktcMtaDevEndPntCount,
'1.3.6.1.2.1.140.1.1.6': PKTC_IETF_MTA_MIB.pktcMtaDevEnabled,
'1.3.6.1.2.1.140.1.1.7': PKTC_IETF_MTA_MIB.pktcMtaDevTypeIdentifier,
'1.3.6.1.2.1.140.1.1.8': PKTC_IETF_MTA_MIB.pktcMtaDevProvisioningState,
'1.3.6.1.2.1.140.1.1.9': PKTC_IETF_MTA_MIB.pktcMtaDevHttpAccess,
'1.3.6.1.2.1.140.1.1.10': PKTC_IETF_MTA_MIB.pktcMtaDevProvisioningTimer,
'1.3.6.1.2.1.140.1.1.11': PKTC_IETF_MTA_MIB.pktcMtaDevProvisioningCounter,
'1.3.6.1.2.1.140.1.2.1': PKTC_IETF_MTA_MIB.pktcMtaDevDhcpServerAddressType,
'1.3.6.1.2.1.140.1.2.2': PKTC_IETF_MTA_MIB.pktcMtaDevServerDhcp1,
'1.3.6.1.2.1.140.1.2.3': PKTC_IETF_MTA_MIB.pktcMtaDevServerDhcp2,
'1.3.6.1.2.1.140.1.2.4': PKTC_IETF_MTA_MIB.pktcMtaDevDnsServerAddressType,
'1.3.6.1.2.1.140.1.2.5': PKTC_IETF_MTA_MIB.pktcMtaDevServerDns1,
'1.3.6.1.2.1.140.1.2.6': PKTC_IETF_MTA_MIB.pktcMtaDevServerDns2,
'1.3.6.1.2.1.140.1.2.7': PKTC_IETF_MTA_MIB.pktcMtaDevTimeServerAddressType,
'1.3.6.1.2.1.140.1.2.8': PKTC_IETF_MTA_MIB.pktcMtaDevTimeServer,
'1.3.6.1.2.1.140.1.2.9': PKTC_IETF_MTA_MIB.pktcMtaDevConfigFile,
'1.3.6.1.2.1.140.1.2.10': PKTC_IETF_MTA_MIB.pktcMtaDevSnmpEntity,
'1.3.6.1.2.1.140.1.2.11': PKTC_IETF_MTA_MIB.pktcMtaDevProvConfigHash,
'1.3.6.1.2.1.140.1.2.12': PKTC_IETF_MTA_MIB.pktcMtaDevProvConfigKey,
'1.3.6.1.2.1.140.1.2.13': PKTC_IETF_MTA_MIB.pktcMtaDevProvConfigEncryptAlg,
'1.3.6.1.2.1.140.1.2.14': PKTC_IETF_MTA_MIB.pktcMtaDevProvSolicitedKeyTimeout,
'1.3.6.1.2.1.140.1.2.15': PKTC_IETF_MTA_MIB.pktcMtaDevProvUnsolicitedKeyMaxTimeout,
'1.3.6.1.2.1.140.1.2.16': PKTC_IETF_MTA_MIB.pktcMtaDevProvUnsolicitedKeyNomTimeout,
'1.3.6.1.2.1.140.1.2.17': PKTC_IETF_MTA_MIB.pktcMtaDevProvUnsolicitedKeyMaxRetries,
'1.3.6.1.2.1.140.1.2.18': PKTC_IETF_MTA_MIB.pktcMtaDevProvKerbRealmName,
'1.3.6.1.2.1.140.1.2.19': PKTC_IETF_MTA_MIB.pktcMtaDevProvState,
'1.3.6.1.2.1.140.1.3.1': PKTC_IETF_MTA_MIB.pktcMtaDevManufacturerCertificate,
'1.3.6.1.2.1.140.1.3.2': PKTC_IETF_MTA_MIB.pktcMtaDevCertificate,
'1.3.6.1.2.1.140.1.3.3': PKTC_IETF_MTA_MIB.pktcMtaDevCorrelationId,
'1.3.6.1.2.1.140.1.3.4': PKTC_IETF_MTA_MIB.pktcMtaDevTelephonyRootCertificate,
'1.3.6.1.2.1.140.1.3.5': PKTC_IETF_MTA_MIB.pktcMtaDevRealmAvailSlot,
'1.3.6.1.2.1.140.1.3.7': PKTC_IETF_MTA_MIB.pktcMtaDevCmsAvailSlot,
'1.3.6.1.2.1.140.1.3.9': PKTC_IETF_MTA_MIB.pktcMtaDevResetKrbTickets,
'1.3.6.1.2.1.140.1.1.12.1.1': PKTC_IETF_MTA_MIB.pktcMtaDevErrorOidIndex,
'1.3.6.1.2.1.140.1.1.12.1.2': PKTC_IETF_MTA_MIB.pktcMtaDevErrorOid,
'1.3.6.1.2.1.140.1.1.12.1.3': PKTC_IETF_MTA_MIB.pktcMtaDevErrorValue,
'1.3.6.1.2.1.140.1.1.12.1.4': PKTC_IETF_MTA_MIB.pktcMtaDevErrorReason,
'1.3.6.1.2.1.140.1.3.6.1.1': PKTC_IETF_MTA_MIB.pktcMtaDevRealmIndex,
'1.3.6.1.2.1.140.1.3.6.1.2': PKTC_IETF_MTA_MIB.pktcMtaDevRealmName,
'1.3.6.1.2.1.140.1.3.6.1.3': PKTC_IETF_MTA_MIB.pktcMtaDevRealmPkinitGracePeriod,
'1.3.6.1.2.1.140.1.3.6.1.4': PKTC_IETF_MTA_MIB.pktcMtaDevRealmTgsGracePeriod,
'1.3.6.1.2.1.140.1.3.6.1.5': PKTC_IETF_MTA_MIB.pktcMtaDevRealmOrgName,
'1.3.6.1.2.1.140.1.3.6.1.6': PKTC_IETF_MTA_MIB.pktcMtaDevRealmUnsolicitedKeyMaxTimeout,
'1.3.6.1.2.1.140.1.3.6.1.7': PKTC_IETF_MTA_MIB.pktcMtaDevRealmUnsolicitedKeyNomTimeout,
'1.3.6.1.2.1.140.1.3.6.1.8': PKTC_IETF_MTA_MIB.pktcMtaDevRealmUnsolicitedKeyMaxRetries,
'1.3.6.1.2.1.140.1.3.6.1.9': PKTC_IETF_MTA_MIB.pktcMtaDevRealmStatus,
'1.3.6.1.2.1.140.1.3.8.1.1': PKTC_IETF_MTA_MIB.pktcMtaDevCmsIndex,
'1.3.6.1.2.1.140.1.3.8.1.2': PKTC_IETF_MTA_MIB.pktcMtaDevCmsFqdn,
'1.3.6.1.2.1.140.1.3.8.1.3': PKTC_IETF_MTA_MIB.pktcMtaDevCmsKerbRealmName,
'1.3.6.1.2.1.140.1.3.8.1.4': PKTC_IETF_MTA_MIB.pktcMtaDevCmsMaxClockSkew,
'1.3.6.1.2.1.140.1.3.8.1.5': PKTC_IETF_MTA_MIB.pktcMtaDevCmsSolicitedKeyTimeout,
'1.3.6.1.2.1.140.1.3.8.1.6': PKTC_IETF_MTA_MIB.pktcMtaDevCmsUnsolicitedKeyMaxTimeout,
'1.3.6.1.2.1.140.1.3.8.1.7': PKTC_IETF_MTA_MIB.pktcMtaDevCmsUnsolicitedKeyNomTimeout,
'1.3.6.1.2.1.140.1.3.8.1.8': PKTC_IETF_MTA_MIB.pktcMtaDevCmsUnsolicitedKeyMaxRetries,
'1.3.6.1.2.1.140.1.3.8.1.9': PKTC_IETF_MTA_MIB.pktcMtaDevCmsIpsecCtrl,
'1.3.6.1.2.1.140.1.3.8.1.10': PKTC_IETF_MTA_MIB.pktcMtaDevCmsStatus,
'1.3.6.1.2.1.140.0.1': PKTC_IETF_MTA_MIB.pktcMtaDevProvisioningEnrollment,
'1.3.6.1.2.1.140.0.2': PKTC_IETF_MTA_MIB.pktcMtaDevProvisioningStatus,
'1.3.6.1.2.1.140.2.2.1': PKTC_IETF_MTA_MIB.pktcMtaGroup,
'1.3.6.1.2.1.140.2.2.2': PKTC_IETF_MTA_MIB.pktcMtaNotificationGroup,
}
