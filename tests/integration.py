# jacoco-badge-generator: Github action for generating a jacoco coverage
# percentage badge.
# 
# Copyright (c) 2020-2021 Vincent A Cicirello
# https://www.cicirello.org/
#
# MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import unittest
import json
import JacocoBadgeGenerator as jbg

class IntegrationTest(unittest.TestCase) :

    def testIntegrationInstructionsBadge(self) :
        with open("tests/100.svg","r") as expected :
            with open("tests/badges/jacoco.svg","r") as generated :
                self.assertEqual(expected.read(), generated.read())

    def testIntegrationBranchesBadge(self) :
        with open("tests/90b.svg","r") as expected :
            with open("tests/badges/branches.svg","r") as generated :
                self.assertEqual(expected.read(), generated.read())

    def testIntegrationMultiJacocoReportsCase(self) :
        with open("tests/78.svg","r") as expected :
            with open("tests/badges/coverageMulti.svg","r") as generated :
                self.assertEqual(expected.read(), generated.read())
        with open("tests/87b.svg","r") as expected :
            with open("tests/badges/branchesMulti.svg","r") as generated :
                self.assertEqual(expected.read(), generated.read())

    def testIntegrationSummaryReport(self) :
        with open("tests/summary/coverage-summary.json", "r") as f :
            d = json.load(f)
            self.assertAlmostEqual(72.72727272727272, d["coverage"])
            self.assertAlmostEqual(77.77777777777777, d["branches"])

    def testIntegrationInstructionsJSON(self) :
        with open("tests/endpoints/jacoco.json", "r") as f :
            d = json.load(f)
            self.assertEqual(1, d["schemaVersion"])
            self.assertEqual("coverage", d["label"])
            self.assertEqual("100%", d["message"])
            self.assertEqual(jbg.defaultColors[0], d["color"])

    def testIntegrationBranchesJSON(self) :
        with open("tests/endpoints/branches.json", "r") as f :
            d = json.load(f)
            self.assertEqual(1, d["schemaVersion"])
            self.assertEqual("branches", d["label"])
            self.assertEqual("90%", d["message"])
            self.assertEqual(jbg.defaultColors[1], d["color"])
    
