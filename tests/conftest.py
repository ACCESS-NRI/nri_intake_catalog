# Copyright 2023 ACCESS-NRI and contributors. See the top-level COPYRIGHT file for details.
# SPDX-License-Identifier: Apache-2.0

import os
import warnings
from pathlib import Path

from pytest import fixture

here = os.path.abspath(os.path.dirname(__file__))


def _get_xfail():
    """
    Get the XFAILS environment variable. We're going to to use a default of 1
    """
    xfails_default = 1

    try:
        return int(os.environ["XFAILS"])
    except KeyError:
        warnings.warn(
            "XFAILS enabled by default as coordinate discovery disabled by default. ",
            "This will be deprecated when coordinate discovery is enabled by default",
            PendingDeprecationWarning,
        )
        return xfails_default


_add_xfail = _get_xfail()


@fixture(scope="session")
def test_data():
    return Path(os.path.join(here, "data"))


def pytest_collection_modifyitems(config, items):
    """
    This function is called by pytest to modify the items collected during test
    collection. I'm going to use it here to mark the xfail tests in
    test_builders::test_parse_access_ncfile when we check the file contents &
    """
    for item in items:
        if (
            item.name
            in (
                "test_parse_access_ncfile[AccessOm2Builder-access-om2/output000/ocean/ocean_grid.nc-expected0-True]",
            )
            and _add_xfail
        ):
            item.add_marker("xfail")
