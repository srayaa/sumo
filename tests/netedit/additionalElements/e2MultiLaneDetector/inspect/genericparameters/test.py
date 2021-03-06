#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    test.py
# @author  Pablo Alvarez Lopez
# @date    2016-11-25
# @version $Id$

# import common functions for netedit tests
import os
import sys

testRoot = os.path.join(os.environ.get('SUMO_HOME', '.'), 'tests')
neteditTestRoot = os.path.join(
    os.environ.get('TEXTTEST_HOME', testRoot), 'netedit')
sys.path.append(neteditTestRoot)
import neteditTestFunctions as netedit  # noqa

# Open netedit
neteditProcess, referencePosition = netedit.setupAndStart(neteditTestRoot, ['--gui-testing-debug-gl'])

# recompute
netedit.rebuildNetwork()

# go to additional mode
netedit.additionalMode()

# select E2
netedit.changeAdditional("e2MultilaneDetector")

# create E2 with default parameters
netedit.leftClick(referencePosition, 190, 240)
netedit.leftClick(referencePosition, 440, 240)
netedit.typeEnter()

# go to additional mode
netedit.inspectMode()

#inspect E2
netedit.leftClick(referencePosition, 320, 240)

# Change generic parameters with a dummy value
netedit.modifyAttribute(13, "dummyGenericParameters")

# Change generic parameters with a invalid format
netedit.modifyAttribute(13, "key1|key2|key3")

# Change generic parameters with a valid value
netedit.modifyAttribute(13, "key1=value1|key2=value2|key3=value3")

# Change generic parameters with a valid value (empty values)
netedit.modifyAttribute(13, "key1=|key2=|key3=")

# Change generic parameters with a valid value (all empty)
netedit.modifyAttribute(13, "")

# Change generic parameters with an invalid value (duplicated)
netedit.modifyAttribute(13, "key1duplicated=value1|key1duplicated=value2|key3=value3")

# Change generic parameters with a valid value
netedit.modifyAttribute(13, "key1=valueDuplicated|key2=valueDuplicated|key3=valueDuplicated")

# Change generic parameters with an invalid value (invalid key characters)
netedit.modifyAttribute(13, "keyInvalid.;%>%$$=value1|key2=value2|key3=value3")

# Change generic parameters with a invalid value (invalid value characters)
netedit.modifyAttribute(13, "key1=valueInvalid%;%$<>$$%|key2=value2|key3=value3")

# Change generic parameters with a valid value
netedit.modifyAttribute(13, "keyFinal1=value1|keyFinal2=value2|keyFinal3=value3")

# Check undo redo
netedit.undo(referencePosition, 8)
netedit.redo(referencePosition, 8)

# save additionals
netedit.saveAdditionals()

# save network
netedit.saveNetwork()

# quit netedit
netedit.quit(neteditProcess)
