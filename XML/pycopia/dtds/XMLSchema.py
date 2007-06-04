#!/usr/bin/python

# This file generated by a program. do not edit.


import pycopia.XML.POM

#  DTD for XML Schemas: Part 1: Structures
#      Public Identifier: "-//W3C//DTD XMLSCHEMA 200102//EN"
#      Official Location: http://www.w3.org/2001/XMLSchema.dtd 


#  $Id$ 


#  Note this DTD is NOT normative, or even definitive. 


# d


#  prose copy in the structures REC is the definitive version 


# d


#  (which shouldn't differ from this one except for this 


# d


#  comment and entity expansions, but just in case) 


# d


#  With the exception of cases with multiple namespace
#      prefixes for the XML Schema namespace, any XML document which is
#      not valid per this DTD given redefinitions in its internal subset of the
#      'p' and 's' parameter entities below appropriate to its namespace
#      declaration of the XML Schema namespace is almost certainly not
#      a valid schema. 


#  The simpleType element and its constituent parts
#      are defined in XML Schema: Part 2: Datatypes 


#  can be overriden in the internal subset of a
#                          schema document to establish a different
#                          namespace prefix 


#  if %p is defined (e.g. as foo:) then you must
#                          also define %s as the suffix for the appropriate
#                          namespace declaration (e.g. :foo) 


#  Define all the element names, with optional prefix 


#  annotation elements 


#  Customisation entities for the ATTLIST of each element type.
#      Define one of these if your schema takes advantage of the
#      anyAttribute='##other' in the schema for schemas 


#  #all or space-separated list drawn from derivationChoice 


#  #all or space-separated list drawn from
#                       derivationChoice + 'substitution' 


#  This is used in part2 


# 
#         DTD for XML Schemas: Part 2: Datatypes
#         $Id$
#         Note this DTD is NOT normative, or even definitive. - - the
#         prose copy in the datatypes REC is the definitive version
#         (which shouldn't differ from this one except for this comment
#         and entity expansions, but just in case)
#   


# 
#         This DTD cannot be used on its own, it is intended
#         only for incorporation in XMLSchema.dtd, q.v.
#   


#  Define all the element names, with optional prefix 


# 
#         Customisation entities for the ATTLIST of each element
#         type. Define one of these if your schema takes advantage
#         of the anyAttribute='##other' in the schema for schemas
#   


#  Define some entities for informative use as attribute
#         types 


# 
#         #all or space-separated list drawn from derivationChoice
#   


# 
#         Note that the use of 'facet' below is less restrictive
#         than is really intended:  There should in fact be no
#         more than one of each of minInclusive, minExclusive,
#         maxInclusive, maxExclusive, totalDigits, fractionDigits,
#         length, maxLength, minLength within datatype,
#         and the min- and max- variants of Inclusive and Exclusive
#         are mutually exclusive. On the other hand,  pattern and
#         enumeration may repeat.
#   


class Xs_simpletype(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('final', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:simpleType'


#  name is required at top level 


class Xs_restriction(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('base', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:restriction'


# 
#         base and simpleType child are mutually exclusive,
#         one is required.
# 
#         restriction is shared between simpleType and
#         simpleContent and complexContent (in XMLSchema.xsd).
#         restriction1 is for the latter cases, when this
#         is restricting a complex type, as is attrDecls.
#   


class Xs_list(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('itemType', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:list'


# 
#         itemType and simpleType child are mutually exclusive,
#         one is required
#   


class Xs_union(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('memberTypes', 8, 12, None), 
         ])
	_name = u'xs:union'


# 
#         At least one item in memberTypes or one simpleType
#         child is required
#   


class Xs_maxexclusive(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:maxExclusive'


class Xs_minexclusive(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:minExclusive'


class Xs_maxinclusive(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:maxInclusive'


class Xs_mininclusive(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:minInclusive'


class Xs_totaldigits(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:totalDigits'


class Xs_fractiondigits(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:fractionDigits'


class Xs_length(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:length'


class Xs_minlength(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:minLength'


class Xs_maxlength(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:maxLength'


#  This one can be repeated 


class Xs_enumeration(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:enumeration'


class Xs_whitespace(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         ])
	_name = u'xs:whiteSpace'


#  This one can be repeated 


class Xs_pattern(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('value', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:pattern'


#  the duplication below is to produce an unambiguous content model
#      which allows annotation everywhere 


class Xs_schema(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('targetNamespace', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('version', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('xmlns:xs', 1, 14, u'http://www.w3.org/2001/XMLSchema'), 
         pycopia.XML.POM.XMLAttribute('xmlns', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('finalDefault', 1, 13, u''), 
         pycopia.XML.POM.XMLAttribute('blockDefault', 1, 13, u''), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('elementFormDefault', pycopia.XML.POM.Enumeration(['qualified', 'unqualified']), 13, u'unqualified'), 
         pycopia.XML.POM.XMLAttribute('attributeFormDefault', pycopia.XML.POM.Enumeration(['qualified', 'unqualified']), 13, u'unqualified'), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 1, 12, None), 
         ])
	_name = u'xs:schema'


#  Note the xmlns declaration is NOT in the Schema for Schemas,
#      because at the Infoset level where schemas operate,
#      xmlns(:prefix) is NOT an attribute! 


#  The declaration of xmlns is a convenience for schema authors 


#  The id attribute here and below is for use in external references
#      from non-schemas using simple fragment identifiers.
#      It is NOT used for schema-to-schema reference, internal or
#      external. 


#  a type is a named content type specification which allows attribute
#      declarations


#  


class Xs_complextype(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('abstract', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         pycopia.XML.POM.XMLAttribute('final', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('block', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('mixed', pycopia.XML.POM.Enumeration(['true', 'false']), 13, u'false'), 
         ])
	_name = u'xs:complexType'


#  particleAndAttrs is shorthand for a root type 


#  mixed is disallowed if simpleContent, overriden if complexContent
#      has one too. 


#  If anyAttribute appears in one or more referenced attributeGroups
#      and/or explicitly, the intersection of the permissions is used 


class Xs_complexcontent(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('mixed', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:complexContent'


#  restriction should use the branch defined above, not the simple
#      one from part2; extension should use the full model  


class Xs_simplecontent(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:simpleContent'


#  restriction should use the simple branch from part2, not the 
#      one defined above; extension should have no particle  


class Xs_extension(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('base', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:extension'


#  an element is declared by either:
#  a name and a type (either nested or referenced via the type attribute)
#  or a ref to an existing element declaration 


class Xs_element(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('ref', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('type', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('minOccurs', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('nillable', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         pycopia.XML.POM.XMLAttribute('substitutionGroup', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('abstract', pycopia.XML.POM.Enumeration(['true', 'false']), 12, None), 
         pycopia.XML.POM.XMLAttribute('final', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('block', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('default', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('form', pycopia.XML.POM.Enumeration(['qualified', 'unqualified']), 12, None), 
         ])
	_name = u'xs:element'


#  simpleType or complexType only if no type|ref attribute 


#  ref not allowed at top level 


#  type and ref are mutually exclusive.
#      name and ref are mutually exclusive, one is required 


#  In the absence of type AND ref, type defaults to type of
#      substitutionGroup, if any, else the ur-type, i.e. unconstrained 


#  default and fixed are mutually exclusive 


class Xs_group(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('ref', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('minOccurs', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:group'


class Xs_all(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('minOccurs', pycopia.XML.POM.Enumeration(['1']), 12, None), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', pycopia.XML.POM.Enumeration(['1']), 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:all'


class Xs_choice(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('minOccurs', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:choice'


class Xs_sequence(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('minOccurs', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:sequence'


#  an anonymous grouping in a model, or
#      a top-level named group definition, or a reference to same 


#  Note that if order is 'all', group is not allowed inside.
#      If order is 'all' THIS group must be alone (or referenced alone) at
#      the top level of a content model 


#  If order is 'all', minOccurs==maxOccurs==1 on element/any inside 


#  Should allow minOccurs=0 inside order='all' . . . 


class Xs_any(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('namespace', 1, 13, u'##any'), 
         pycopia.XML.POM.XMLAttribute('processContents', pycopia.XML.POM.Enumeration(['skip', 'lax', 'strict']), 13, u'strict'), 
         pycopia.XML.POM.XMLAttribute('minOccurs', 7, 13, u'1'), 
         pycopia.XML.POM.XMLAttribute('maxOccurs', 1, 13, u'1'), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:any'


#  namespace is interpreted as follows:
#                   ##any      - - any non-conflicting WFXML at all
# 
#                   ##other    - - any non-conflicting WFXML from namespace other
#                                   than targetNamespace
# 
#                   ##local    - - any unqualified non-conflicting WFXML/attribute
#                   one or     - - any non-conflicting WFXML from
#                   more URI        the listed namespaces
#                   references
# 
#                   ##targetNamespace ##local may appear in the above list,
#                     with the obvious meaning 


class Xs_anyattribute(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('namespace', 1, 13, u'##any'), 
         pycopia.XML.POM.XMLAttribute('processContents', pycopia.XML.POM.Enumeration(['skip', 'lax', 'strict']), 13, u'strict'), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:anyAttribute'


#  namespace is interpreted as for 'any' above 


#  simpleType only if no type|ref attribute 


#  ref not allowed at top level, name iff at top level 


class Xs_attribute(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('ref', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('type', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('use', pycopia.XML.POM.Enumeration(['prohibited', 'optional', 'required']), 12, None), 
         pycopia.XML.POM.XMLAttribute('default', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('fixed', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('form', pycopia.XML.POM.Enumeration(['qualified', 'unqualified']), 12, None), 
         ])
	_name = u'xs:attribute'


#  type and ref are mutually exclusive.
#      name and ref are mutually exclusive, one is required 


#  default for use is optional when nested, none otherwise 


#  default and fixed are mutually exclusive 


#  type attr and simpleType content are mutually exclusive 


#  an attributeGroup is a named collection of attribute decls, or a
#      reference thereto 


class Xs_attributegroup(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('ref', 7, 12, None), 
         ])
	_name = u'xs:attributeGroup'


#  ref iff no content, no name.  ref iff not top level 


#  better reference mechanisms 


class Xs_unique(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:unique'


class Xs_key(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:key'


class Xs_keyref(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('refer', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:keyref'


class Xs_selector(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xpath', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:selector'


class Xs_field(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('xpath', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:field'


#  Schema combination mechanisms 


class Xs_include(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('schemaLocation', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:include'


class Xs_import(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('namespace', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('schemaLocation', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:import'


class Xs_redefine(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('schemaLocation', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:redefine'


class Xs_notation(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('name', 7, 11, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('public', 1, 11, None), 
         pycopia.XML.POM.XMLAttribute('system', 1, 12, None), 
         ])
	_name = u'xs:notation'


#  Annotation is either application information or documentation 


#  By having these here they are available for datatypes as well
#      as all the structures elements 


class Xs_annotation(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel((True,))
	_name = u'xs:annotation'


#  User must define annotation elements in internal subset for this
#      to work 


class Xs_appinfo(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(True)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('source', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         ])
	_name = u'xs:appinfo'


#  too restrictive 


class Xs_documentation(pycopia.XML.POM.ElementNode):
	CONTENTMODEL = pycopia.XML.POM.ContentModel(True)
	ATTLIST = pycopia.XML.POM.AttributeList([
         pycopia.XML.POM.XMLAttribute('source', 1, 12, None), 
         pycopia.XML.POM.XMLAttribute('id', 2, 12, None), 
         pycopia.XML.POM.XMLAttribute('xml:lang', 1, 12, None), 
         ])
	_name = u'xs:documentation'


#  too restrictive 


Xmlschemastructures = pycopia.XML.POM.Notation(u'XMLSchemaStructures', u'structures', u'http://www.w3.org/2001/XMLSchema.xsd')

Xml = pycopia.XML.POM.Notation(u'XML', u'REC-xml-1998-0210', u'http://www.w3.org/TR/1998/REC-xml-19980210')

GENERAL_ENTITIES = {}
