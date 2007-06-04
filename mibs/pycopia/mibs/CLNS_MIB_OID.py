# python
# This file is generated by a program (mib2py). 

import CLNS_MIB

OIDMAP = {
'1.3.6.1.3.1': CLNS_MIB.clns,
'1.3.6.1.3.1.1': CLNS_MIB.clnp,
'1.3.6.1.3.1.2': CLNS_MIB.error,
'1.3.6.1.3.1.3': CLNS_MIB.echo,
'1.3.6.1.3.1.4': CLNS_MIB.es_is,
'1.3.6.1.3.1.1.1': CLNS_MIB.clnpForwarding,
'1.3.6.1.3.1.1.2': CLNS_MIB.clnpDefaultLifeTime,
'1.3.6.1.3.1.1.3': CLNS_MIB.clnpInReceives,
'1.3.6.1.3.1.1.4': CLNS_MIB.clnpInHdrErrors,
'1.3.6.1.3.1.1.5': CLNS_MIB.clnpInAddrErrors,
'1.3.6.1.3.1.1.6': CLNS_MIB.clnpForwPDUs,
'1.3.6.1.3.1.1.7': CLNS_MIB.clnpInUnknownNLPs,
'1.3.6.1.3.1.1.8': CLNS_MIB.clnpInUnknownULPs,
'1.3.6.1.3.1.1.9': CLNS_MIB.clnpInDiscards,
'1.3.6.1.3.1.1.10': CLNS_MIB.clnpInDelivers,
'1.3.6.1.3.1.1.11': CLNS_MIB.clnpOutRequests,
'1.3.6.1.3.1.1.12': CLNS_MIB.clnpOutDiscards,
'1.3.6.1.3.1.1.13': CLNS_MIB.clnpOutNoRoutes,
'1.3.6.1.3.1.1.14': CLNS_MIB.clnpReasmTimeout,
'1.3.6.1.3.1.1.15': CLNS_MIB.clnpReasmReqds,
'1.3.6.1.3.1.1.16': CLNS_MIB.clnpReasmOKs,
'1.3.6.1.3.1.1.17': CLNS_MIB.clnpReasmFails,
'1.3.6.1.3.1.1.18': CLNS_MIB.clnpSegOKs,
'1.3.6.1.3.1.1.19': CLNS_MIB.clnpSegFails,
'1.3.6.1.3.1.1.20': CLNS_MIB.clnpSegCreates,
'1.3.6.1.3.1.1.25': CLNS_MIB.clnpInOpts,
'1.3.6.1.3.1.1.26': CLNS_MIB.clnpOutOpts,
'1.3.6.1.3.1.1.27': CLNS_MIB.clnpRoutingDiscards,
'1.3.6.1.3.1.2.1': CLNS_MIB.clnpInErrors,
'1.3.6.1.3.1.2.2': CLNS_MIB.clnpOutErrors,
'1.3.6.1.3.1.2.3': CLNS_MIB.clnpInErrUnspecs,
'1.3.6.1.3.1.2.4': CLNS_MIB.clnpInErrProcs,
'1.3.6.1.3.1.2.5': CLNS_MIB.clnpInErrCksums,
'1.3.6.1.3.1.2.6': CLNS_MIB.clnpInErrCongests,
'1.3.6.1.3.1.2.7': CLNS_MIB.clnpInErrHdrs,
'1.3.6.1.3.1.2.8': CLNS_MIB.clnpInErrSegs,
'1.3.6.1.3.1.2.9': CLNS_MIB.clnpInErrIncomps,
'1.3.6.1.3.1.2.10': CLNS_MIB.clnpInErrDups,
'1.3.6.1.3.1.2.11': CLNS_MIB.clnpInErrUnreachDsts,
'1.3.6.1.3.1.2.12': CLNS_MIB.clnpInErrUnknownDsts,
'1.3.6.1.3.1.2.13': CLNS_MIB.clnpInErrSRUnspecs,
'1.3.6.1.3.1.2.14': CLNS_MIB.clnpInErrSRSyntaxes,
'1.3.6.1.3.1.2.15': CLNS_MIB.clnpInErrSRUnkAddrs,
'1.3.6.1.3.1.2.16': CLNS_MIB.clnpInErrSRBadPaths,
'1.3.6.1.3.1.2.17': CLNS_MIB.clnpInErrHops,
'1.3.6.1.3.1.2.18': CLNS_MIB.clnpInErrHopReassms,
'1.3.6.1.3.1.2.19': CLNS_MIB.clnpInErrUnsOptions,
'1.3.6.1.3.1.2.20': CLNS_MIB.clnpInErrUnsVersions,
'1.3.6.1.3.1.2.21': CLNS_MIB.clnpInErrUnsSecurities,
'1.3.6.1.3.1.2.22': CLNS_MIB.clnpInErrUnsSRs,
'1.3.6.1.3.1.2.23': CLNS_MIB.clnpInErrUnsRRs,
'1.3.6.1.3.1.2.24': CLNS_MIB.clnpInErrInterferences,
'1.3.6.1.3.1.2.25': CLNS_MIB.clnpOutErrUnspecs,
'1.3.6.1.3.1.2.26': CLNS_MIB.clnpOutErrProcs,
'1.3.6.1.3.1.2.27': CLNS_MIB.clnpOutErrCksums,
'1.3.6.1.3.1.2.28': CLNS_MIB.clnpOutErrCongests,
'1.3.6.1.3.1.2.29': CLNS_MIB.clnpOutErrHdrs,
'1.3.6.1.3.1.2.30': CLNS_MIB.clnpOutErrSegs,
'1.3.6.1.3.1.2.31': CLNS_MIB.clnpOutErrIncomps,
'1.3.6.1.3.1.2.32': CLNS_MIB.clnpOutErrDups,
'1.3.6.1.3.1.2.33': CLNS_MIB.clnpOutErrUnreachDsts,
'1.3.6.1.3.1.2.34': CLNS_MIB.clnpOutErrUnknownDsts,
'1.3.6.1.3.1.2.35': CLNS_MIB.clnpOutErrSRUnspecs,
'1.3.6.1.3.1.2.36': CLNS_MIB.clnpOutErrSRSyntaxes,
'1.3.6.1.3.1.2.37': CLNS_MIB.clnpOutErrSRUnkAddrs,
'1.3.6.1.3.1.2.38': CLNS_MIB.clnpOutErrSRBadPaths,
'1.3.6.1.3.1.2.39': CLNS_MIB.clnpOutErrHops,
'1.3.6.1.3.1.2.40': CLNS_MIB.clnpOutErrHopReassms,
'1.3.6.1.3.1.2.41': CLNS_MIB.clnpOutErrUnsOptions,
'1.3.6.1.3.1.2.42': CLNS_MIB.clnpOutErrUnsVersions,
'1.3.6.1.3.1.2.43': CLNS_MIB.clnpOutErrUnsSecurities,
'1.3.6.1.3.1.2.44': CLNS_MIB.clnpOutErrUnsSRs,
'1.3.6.1.3.1.2.45': CLNS_MIB.clnpOutErrUnsRRs,
'1.3.6.1.3.1.2.46': CLNS_MIB.clnpOutErrInterferences,
'1.3.6.1.3.1.4.1': CLNS_MIB.esisESHins,
'1.3.6.1.3.1.4.2': CLNS_MIB.esisESHouts,
'1.3.6.1.3.1.4.3': CLNS_MIB.esisISHins,
'1.3.6.1.3.1.4.4': CLNS_MIB.esisISHouts,
'1.3.6.1.3.1.4.5': CLNS_MIB.esisRDUins,
'1.3.6.1.3.1.4.6': CLNS_MIB.esisRDUouts,
'1.3.6.1.3.1.1.21.1.1': CLNS_MIB.clnpAdEntAddr,
'1.3.6.1.3.1.1.21.1.2': CLNS_MIB.clnpAdEntIfIndex,
'1.3.6.1.3.1.1.21.1.3': CLNS_MIB.clnpAdEntReasmMaxSize,
'1.3.6.1.3.1.1.22.1.1': CLNS_MIB.clnpRouteDest,
'1.3.6.1.3.1.1.22.1.2': CLNS_MIB.clnpRouteIfIndex,
'1.3.6.1.3.1.1.22.1.3': CLNS_MIB.clnpRouteMetric1,
'1.3.6.1.3.1.1.22.1.4': CLNS_MIB.clnpRouteMetric2,
'1.3.6.1.3.1.1.22.1.5': CLNS_MIB.clnpRouteMetric3,
'1.3.6.1.3.1.1.22.1.6': CLNS_MIB.clnpRouteMetric4,
'1.3.6.1.3.1.1.22.1.7': CLNS_MIB.clnpRouteNextHop,
'1.3.6.1.3.1.1.22.1.8': CLNS_MIB.clnpRouteType,
'1.3.6.1.3.1.1.22.1.9': CLNS_MIB.clnpRouteProto,
'1.3.6.1.3.1.1.22.1.10': CLNS_MIB.clnpRouteAge,
'1.3.6.1.3.1.1.22.1.11': CLNS_MIB.clnpRouteMetric5,
'1.3.6.1.3.1.1.22.1.12': CLNS_MIB.clnpRouteInfo,
'1.3.6.1.3.1.1.23.1.1': CLNS_MIB.clnpNetToMediaIfIndex,
'1.3.6.1.3.1.1.23.1.2': CLNS_MIB.clnpNetToMediaPhysAddress,
'1.3.6.1.3.1.1.23.1.3': CLNS_MIB.clnpNetToMediaNetAddress,
'1.3.6.1.3.1.1.23.1.4': CLNS_MIB.clnpNetToMediaType,
'1.3.6.1.3.1.1.23.1.5': CLNS_MIB.clnpNetToMediaAge,
'1.3.6.1.3.1.1.23.1.6': CLNS_MIB.clnpNetToMediaHoldTime,
'1.3.6.1.3.1.1.24.1.1': CLNS_MIB.clnpMediaToNetIfIndex,
'1.3.6.1.3.1.1.24.1.2': CLNS_MIB.clnpMediaToNetAddress,
'1.3.6.1.3.1.1.24.1.3': CLNS_MIB.clnpMediaToNetPhysAddress,
'1.3.6.1.3.1.1.24.1.4': CLNS_MIB.clnpMediaToNetType,
'1.3.6.1.3.1.1.24.1.5': CLNS_MIB.clnpMediaToNetAge,
'1.3.6.1.3.1.1.24.1.6': CLNS_MIB.clnpMediaToNetHoldTime,
}
