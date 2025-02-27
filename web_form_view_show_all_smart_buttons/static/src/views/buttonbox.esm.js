/** @odoo-module  */

import {ButtonBox} from "@web/views/form/button_box/button_box";
import {patch} from "@web/core/utils/patch";

patch(ButtonBox.prototype, {
    setup() {
        super.setup(...arguments);
        this.getMaxButtons = () => 100;
    },
});
