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

import json
import os
from setuptools import setup
from setuptools import find_packages

current_path = os.path.abspath(os.path.dirname(__file__))

with open('requirements.txt') as f:
    required = f.read().splitlines()

version_file = os.path.join(current_path, 'swag_exporter', 'setup_info.json')
with open(version_file) as f:
    pkg_info = json.loads(f.read())

setup(
    name=pkg_info["name"],
    version=pkg_info["version"],
    license=pkg_info['license'],
    packages=find_packages(exclude=pkg_info['exclude_folders']),
    url=pkg_info["url"],
    author=pkg_info["author"],
    author_email=pkg_info["author_email"],
    description=pkg_info["description"],
    long_description=pkg_info['long_description'],
    install_requires=required,
    include_package_data=True,
    classifiers=pkg_info['classifiers'],
    platforms=pkg_info['platforms'],
    python_requires=pkg_info['python_requires'],
    package_data=pkg_info['package_data'],
    entry_points=pkg_info['entry_points'],
)
