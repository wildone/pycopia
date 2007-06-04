#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

#  DTD for LOGML 1.0.0 


#  logml.dtd 


#  Date 06-25-2001 


#  Authors: John Punin and Gerard Uffelman


#  Computer Science Department 


#  Rensselaer Polytechnic Institute 


# ENTITY REFERENCES


# ================================================================


#  Standard XML Namespace attribute 


# Boolean Type


# Positive Number Type


# Name Token Type


# Identifier Type


# String Type


# Date Type


# URI Type


#  Global Attributes 


#  Global Required Attributes 


#  Standard XML Attributes 


#  XGMML Attributes 


#  General Access Log Attributes 


#  General Hit Log Attributes 


#  General Count Log Attributes 


#  Counter of Elements Attribute 


# ROOT ELEMENT


# ================================================================


class Logml(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xmlns', 1, 14, u'http://www.cs.rpi.edu/LOGML'), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:space', pycopia.XML.POM.Enumeration(['default', 'preserve']), 12, None), 
         pycopia.XML.POM.XMLAttribute('start_date', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('end_date', 1, 11, None), 
         ])
	_name = u'logml'


# WEBSITE INFORMATION


# ================================================================


class Graph(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('directed', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'graph'


class Node(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('weight', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('hits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('ehits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('indp', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'node'


class Edge(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('weight', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('source', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('target', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('hits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('indp', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'edge'


class Att(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('value', 1, 12, None), 
         ])
	_name = u'att'


# HOST INFORMATION


# ================================================================


class Hosts(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'hosts'


class Host(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('ip', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('is_internal', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'host'


# DOMAIN INFORMATION


# ================================================================


class Domains(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'domains'


class Domain(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'domain'


# DIRECTORY INFORMATION


# ================================================================


class Directories(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'directories'


class Directory(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('total_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'directory'


# USER AGENT INFORMATION


# ================================================================


class Useragents(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'userAgents'


class Useragent(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('is_spider', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'userAgent'


# REFERER INFORMATION


# ================================================================


class Referers(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'referers'


class Referer(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('target', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('is_internal', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'referer'


class Hostreferers(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'hostReferers'


class Hostreferer(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('is_search_engine', pycopia.XML.POM.Enumeration(['0', '1']), 12, None), 
         ])
	_name = u'hostReferer'


# KEYWORD INFORMATION


# ================================================================


class Keywords(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('search_engine_name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('search_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'keywords'


class Keyword(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('total_count', 7, 12, None), 
         ])
	_name = u'keyword'


# GENERAL STATISTICS INFORMATION


# ================================================================


class Summary(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('requests', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('sessions', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('nhtml_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('inline_objects', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('hyperlink_html', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('hyperlink_nhtml', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_entry_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('nhtml_entry_pages', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_sites', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_host_referers', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_se_referers', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_external_url_referers', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_internal_url_referers', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_user_agents', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('requests_hour', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('requests_day', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('kbytes_day', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('kbytes_hour', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('searches', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('unique_keywords', 7, 12, None), 
         ])
	_name = u'summary'


class Httpcode(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('code', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('total_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'httpCode'


class Httpmethod(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('total_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'httpMethod'


class Httpversion(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('total_count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'httpVersion'


class Datestat(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'dateStat'


class Monthstat(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('month', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('hits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'monthStat'


class Daystat(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('day', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('hits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'dayStat'


class Hourstat(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('hour', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('hits', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('bytes', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('html_pages', 7, 12, None), 
         ])
	_name = u'hourStat'


# USER SESSION INFORMATION


# ================================================================


class Usersessions(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('max_edges', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('min_edges', 7, 12, None), 
         ])
	_name = u'userSessions'


class Usersession(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('name', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('label', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('ureferer', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('entry_page', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('start_time', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('access_count', 7, 12, None), 
         ])
	_name = u'userSession'


class Path(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('count', 7, 12, None), 
         ])
	_name = u'path'


class Uedge(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(None)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('source', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('target', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('utime', 1, 12, None), 
         ])
	_name = u'uedge'


# ================================================================


# END LOGML DTD


GENERAL_ENTITIES = {}
