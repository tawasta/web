odoo.define('web_tree_many2one_clickable_specific.many2one_clickable_specific', function (require) {
    'use strict';

    // Copy-pasted code from web_tree_many2one_clickable module and changed
    // it to work only on many2one_is_clickable widget
    var ListRenderer = require('web.ListRenderer');
    var ListFieldMany2One = require('web.relational_fields').ListFieldMany2One;
    var rpc = require('web.rpc');

    ListRenderer.include({
       _renderBodyCell: function (record, node, colIndex, options) {
           if (node.attrs.widget == 'many2one_is_clickable' && node.attrs.name &&
               this.state.fields[node.attrs.name] &&
               this.state.fields[node.attrs.name].type === 'many2one') {
               node.attrs.widget = 'many2one';
           }
           return this._super(record, node, colIndex, options);
       },
    });

    ListFieldMany2One.include({
        _renderReadonly: function () {
            this._super.apply(this, arguments);
            var self = this;

            if (!this.noOpen && this.value) {
                this.$el.removeClass("o_form_uri");
                this.$el = $("<span/>", {
                    html: this.$el.html(),
                    class: this.$el.attr("class") + " o_field_text" + "many2one_clickable",
                    name: this.$el.attr("name"),
                    style: "color: #7C7BAD;",
                }).on('click', function (ev) {
                    ev.preventDefault();
                    ev.stopPropagation();

                    rpc.query({
                        model: self.field.relation,
                        method: 'get_formview_action',
                        args: [[self.value.res_id]],
                    }).then(function (action) {
                        return self.do_action(action);
                    });
                });
            }
        },

        getFocusableElement: function () {
            if (this.mode === 'readonly') {
                return $('');
            }
            return this._super.apply(this, arguments);
        },
    });
});
