"""
toolboks-cli - Command line interface for toolboks library

Copyright (C) 2022 Mikael Tranbom

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse

import toolboks as tb


def toolboks_config():
    """Command line interface for toolboks.conf.read_config"""
    parser = argparse.ArgumentParser(description='Configuration file reader')
    parser.add_argument(
        'filename',
        type=str,
        help='Configuration file path'
    )

    parser.add_argument(
        'section',
        type=str,
        nargs='?',
        help='Section to read in configuration file'
    )

    parser.add_argument(
        'key',
        type=str,
        nargs='?',
        help='Key to read from section in configuration file'
    )

    section = None
    value = None

    args = parser.parse_args()
    conf = tb.read_config(args.filename)

    try:
        section = getattr(conf, args.section)
        value = getattr(section, args.key)

        print(value)
    except TypeError:
        pass
    except AttributeError:
        pass


def main():
    """Main function"""
