odoo.define("web_form_view_show_all_smart_buttons.form_renderer", function (require) {
    "use strict";

    var FormRenderer = require("web.FormRenderer");

    FormRenderer.include({
        /**
         * @override
         */
        _renderButtonBoxNbButtons: function () {
            return 100;
        },
    });
});
