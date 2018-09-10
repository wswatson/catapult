# Copyright 2018 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Quest and Execution for running a performance test in Swarming."""

import copy

from dashboard.pinpoint.models.quest import run_test

_DEFAULT_EXTRA_ARGS = [
    '--isolated-script-test-output', '${ISOLATED_OUTDIR}/output.json',
    '--isolated-script-test-chartjson-output',
    '${ISOLATED_OUTDIR}/chartjson-output.json',
]

class RunPerformanceTest(run_test.RunTest):

  @classmethod
  def _ExtraTestArgs(cls, arguments):
    extra_test_args = copy.copy(_DEFAULT_EXTRA_ARGS)
    extra_test_args += super(RunPerformanceTest, cls)._ExtraTestArgs(arguments)
    return extra_test_args
