################################################################
# Licensed to the VoerEir AB under one                         #
# or more contributor license agreements.  See the NOTICE file #
# distributed with this work for additional information        #
# regarding copyright ownership.  The ASF licenses this file   #
# to you under the Apache License, Version 2.0 (the            #
# "License"); you may not use this file except in compliance   #
# with the License.  You may obtain a copy of the License at   #
#                                                              #
#  http://www.apache.org/licenses/LICENSE-2.0                  #
#                                                              #
# Unless required by applicable law or agreed to in writing,   #
# software distributed under the License is distributed on an  #
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY       #
# KIND, either express or implied.  See the License for the    #
# specific language governing permissions and limitations      #
# under the License.                                           #
################################################################

from __future__ import print_function
import argparse
import json
import os
import sys
import enum

import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape


class ExportFormat(enum.Enum):
    PDF = "pdf"
    HTML = "html"


class SpecExporter:
    def __init__(self, spec_json, template_path=None, export_file_name=None):

        if not template_path:
            self.template_path = './templates'

        if not export_file_name:
            self.export_file_name = "specification"

        self.env = Environment(
            loader=PackageLoader(__name__, './templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        self.spec = self._load_spec(spec_json)
        self._load_template()

    def _load_spec(self, spec_json):
        return json.loads(spec_json)

    def _load_template(self):
        self.template = self.env.get_template('main.html')

    def render(self):
        info = self.spec['info']
        paths = self.spec['paths']
        securityDefinitions = self.spec['securityDefinitions']
        return self.template.render(
            info=info,
            securityDefinitions=securityDefinitions,
            paths=paths
        )

    def export_to_pdf(self, path):
        path = os.path.join(path, self.export_file_name + '.' + ExportFormat.PDF.value)
        pdfkit.from_string(self.render(), path)

    def export_to_html(self, path):
        path = os.path.join(path, self.export_file_name + '.' + ExportFormat.HTML.value)
        with open(path, 'w') as file:
            file.write(self.render())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--spec', help='Swagger Spec json file path', required=True)
    parser.add_argument('-o', '--output', help='output path', required=True)
    parser.add_argument('-e', '--export-type', help='Export format html or pdf',
                        default=ExportFormat.PDF.value,
                        required=False)

    args = parser.parse_args()

    if not os.path.exists(args.spec) or os.path.exists(args.output):
        error = '{0} File Not Found'.format(args.spec)
        print(error, file=sys.stderr)

    with open(args.spec, 'r') as file:
        spec_json = file.read()
        spec = SpecExporter(spec_json=spec_json)
        if args.export_type == ExportFormat.PDF.value:
            spec.export_to_pdf(args.output)
        elif args.export_type == ExportFormat.HTML.value:
            spec.export_to_html(args.output)
        else:
            raise ValueError("Invalid export type")


if __name__ == '__main__':
    sys.exit(main())
