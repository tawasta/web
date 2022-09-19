odoo.define('systray_buttons_parameter.systray', function (require) {
"use strict";
var SystrayMenu = require('web.SystrayMenu');
var Widget = require('web.Widget');
var Rpc = require('web.rpc');
var Core = require('web.core');
var session = require('web.session');

Rpc.query({
    model: "ir.config_parameter",
    method: 'search_read',
    context: {},
    domain: [['key', 'ilike', 'systray.']],
})
.then(function (result) {
   for (var r in  result) {
        var button = Widget.extend({
            url:result[r].value,
            title:result[r].key.split('.')[2],
            img:result[r].key.split('.')[1],
            template:'systray.button',
            events: {
                    "click": "on_click",
                },
            on_click: function (event) {
                    window.open(this.url, '_blank');
                },
       });
       SystrayMenu.Items.push(button);
  }
});
});
