# ----------------------------------------------------------------------
# Numenta Platform for Intelligent Computing (NuPIC)
# Copyright (C) 2015, Numenta, Inc.  Unless you have purchased from
# Numenta, Inc. a separate commercial license for this software code, the
# following terms and conditions apply:
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with this program.  If not, see http://www.gnu.org/licenses.
#
# http://numenta.org/licenses/
# ----------------------------------------------------------------------

"""A simple script to test nupic and static files imports when the 
script is frozen"""

print "==> Testing imports from nupic ..."
from nupic.algorithms.anomaly_likelihood import AnomalyLikelihood
print "    SUCCESS: %s" % AnomalyLikelihood

print "==> Testing imports from nupic.bidings ..."
from nupic.bindings.math import Random
print "    SUCCESS: %s" % Random

print "==> Testing static files imports ..."
import pyproj.datadir
print "    SUCCESS: %s" % pyproj.datadir
with open("stats_schema.json", "rb") as f:
    print "    SUCCESS: %s" %f



