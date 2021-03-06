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

from setuptools import setup, find_packages
import os

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='swag_export',
    version='0.0.1',
    packages=find_packages(),
    url='http://voereir.com',
    author='VoerEir AB',
    author_email='info@voereir.com',
    description='Swag Exporter for exporting swagger spec json as html to pdf',
    install_requires=required,
    include_package_data=True,
    entry_points={
        'console_scripts' : [
             'VoerEir_Engines = swag.main:main'
         ]
    }
)
