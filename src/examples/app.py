#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Zendesk API
# Copyright (c) 2008-2015 Hive Solutions Lda.
#
# This file is part of Hive Zendesk API.
#
# Hive Zendesk API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Zendesk API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Zendesk API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import appier

import base

class ZendeskApp(appier.WebApp):

    def __init__(self):
        appier.WebApp.__init__(self, name = "live")

    @appier.route("/", "GET")
    def index(self):
        return self.tickets()

    @appier.route("/tickets", "GET")
    def tickets(self):
        api = self.get_api()
        tickets = api.list_tickets()
        return tickets

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = ZendeskApp()
    app.serve()
