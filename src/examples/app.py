#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Zendesk API
# Copyright (c) 2008-2025 Hive Solutions Lda.
#
# This file is part of Hive Zendesk API.
#
# Hive Zendesk API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Zendesk API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Zendesk API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base


class ZendeskApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(self, name="zendesk", *args, **kwargs)

    @appier.route("/", "GET")
    def index(self):
        return self.tickets()

    @appier.route("/tickets", "GET")
    def tickets(self):
        api = self.get_api()
        tickets = api.list_tickets()
        return tickets

    @appier.route("/ticket_fields", "GET")
    def ticket_fields(self):
        api = self.get_api()
        ticket_fields = api.list_ticket_fields()
        return ticket_fields

    def get_api(self):
        api = base.get_api()
        return api


if __name__ == "__main__":
    app = ZendeskApp()
    app.serve()
else:
    __path__ = []
