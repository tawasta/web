//-*- coding: utf-8 -*-
//############################################################################
//
//   OpenERP, Open Source Management Solution
//   This module copyright
//     (C) 2013 Therp BV (<http://therp.nl>).
//     (c) 2015 Serv. Tecnol. Avanzados (http://www.serviciosbaeza.com)
//              Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
//
//   This program is free software: you can redistribute it and/or modify
//   it under the terms of the GNU Affero General Public License as
//   published by the Free Software Foundation, either version 3 of the
//   License, or (at your option) any later version.
//
//   This program is distributed in the hope that it will be useful,
//   but WITHOUT ANY WARRANTY; without even the implied warranty of
//   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//   GNU Affero General Public License for more details.
//
//   You should have received a copy of the GNU Affero General Public License
//   along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
//############################################################################

openerp.web_tree_many2one_clickable_extended = function(instance, local)
{
    instance.web.list.Column.include({
        /*
        Load config parameter at init and store it in an accessible variable.
        */
        init: function(id, tag, attrs) {
            this._super(id, tag, attrs);

            if (this.name == 'name') {
                this.use_name_clickable = true;
            }

            if (this.widget == 'many2one_clickable') {
                this.use_many2one_clickable = true;
            } else if (this.type == 'many2one') {
                this.get_options();
            }
        },

        get_options: function() {
            if (_.isUndefined(this.ir_option_clickable_loaded)) {
                var self = this; // Needed for binding the instance
                this.ir_option_clickable_loaded = $.Deferred();
                this.use_many2one_clickable = false;
                (new instance.web.Model("ir.config_parameter"))
                    .query(["value"])
                    .filter([['key', '=', 'web_tree_many2one_clickable_extended.default']])
                    .first()
                    .then(function(param) {
                        if (param) {
                            self.use_many2one_clickable = (param.value.toLowerCase() == 'true');
                        }
                        self.ir_option_clickable_loaded.resolve();
                    });
                return this.ir_option_clickable_loaded;
            }
            return $.when();
        },

        _format: function (row_data, options)
        {
            if (this.use_many2one_clickable) {

                var url = window.location.href;
                var begining = url.split("#");

                begining[0] += "#id=";
                begining[0] += row_data[this.id].value[0];
                begining[0] += "&view_type=form&model=";
                begining[0] += this.relation;

                return _.str.sprintf('<a class="oe_form_uri" data-many2one-clickable-model="%s" href="%s" data-many2one-clickable-id="%s">%s</a>',
                    this.relation,
                    begining[0],
                    row_data[this.id].value[0],
                    _.escape(row_data[this.id].value[1] || options.value_if_empty));
            }
            else if (this.use_name_clickable) {

                var url = window.location.href;
                var beginning = url.split("#");
                var url_attrs = beginning[1].split("&");

                beginning[0] += "#id=";
                beginning[0] += options.id;
                beginning[0] += "&view_type=form&model=";
                beginning[0] += options.model;
                // TODO: this isn't very reliable reference
                beginning[0] += "&";
                beginning[0] += url_attrs[4];

                return _.str.sprintf('<a class="oe_form_uri" href="%s">%s</a>',
                    beginning[0],
                    row_data[this.id].value);
            }
            else {
                return this._super(row_data, options);
            }
        },

    });

    /* many2one_clickable widget */

    instance.web.list.columns.add(
            'field.many2one_clickable',
            'instance.web_tree_many2one_clickable_extended.Many2OneClickable');

    instance.web_tree_many2one_clickable_extended.Many2OneClickable = openerp.web.list.Column.extend({
    });

    /* click action */

    instance.web.ListView.List.include({
        render: function()
        {
            var result = this._super(this, arguments),
                self = this;
            this.$current.delegate('a[data-many2one-clickable-model]',
                'click', function()
                {
                    self.view.do_action({
                        type: 'ir.actions.act_window',
                        res_model: jQuery(this).data('many2one-clickable-model'),
                        res_id: jQuery(this).data('many2one-clickable-id'),
                        views: [[false, 'form']],
                    });
                });
            return result;
        },
    });
}
