# This file is part of ts_config_latiss.
#
# Developed for the LSST Telescope and Site Systems.
# This product includes software developed by the LSST Project
# (https://www.lsst.org).
# See the COPYRIGHT file at the top-level directory of this distribution
# for details of code ownership.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import pathlib
import unittest

from lsst.ts import salobj


class ConfigTestCase(salobj.BaseConfigTestCase, unittest.TestCase):
    def setUp(self):
        self.config_package_root = pathlib.Path(__file__).parents[1]

    def test_ATSpectrograph(self):
        self.check_standard_config_files(sal_name="ATSpectrograph",
                                         module_name="lsst.ts.atspectrograph",
                                         config_package_root=self.config_package_root)

    def test_NumberProperValuesInArrays(self):
        import yaml
        # Run setUp to get self.config_package_root
        self.setUp()

        module_name="lsst.ts.atspectrograph"
        sal_name="ATSpectrograph"

        num_dots = len(module_name.split("."))
        csc_package_root = self.get_module_dir(module_name).parents[num_dots]

        schema_subpath=None
        schema = self.get_schema(
            csc_package_root=csc_package_root,
            sal_name=sal_name,
            schema_subpath=schema_subpath,
        )

        config_dir = self.get_config_dir(self.config_package_root, sal_name, schema)

        config_dir = pathlib.Path(config_dir)

        config_files = config_dir.glob("*.yaml")

        for config_file in config_files:
            if config_file.name == "_labels.yaml":
                continue

            with open(config_file, "r") as f:
                config_yaml = f.read()
                config_dict = yaml.safe_load(config_yaml)
                print(config_dict)
                print(config_dict['filters']['name'])

                # Verify each field has 4 entries
                self.assertEqual(len(config_dict['filters']['name']), 4)
                self.assertEqual(len(config_dict['filters']['central_wavelength']), 4)
                self.assertEqual(len(config_dict['filters']['focus_offset']), 4)

                self.assertEqual(len(config_dict['gratings']['name']), 4)
                self.assertEqual(len(config_dict['gratings']['focus_offset']), 4)


