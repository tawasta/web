odoo.define("web_action_menus_hide_for_group.ActionMenus", function (require) {
    "use strict";

    const {patch} = require("web.utils");
    const ActionMenus = require("web.ActionMenus");
    var session = require("web.session");

    patch(ActionMenus, "web_action_menus", {
        /**
         * Check if user is in group for which menus are hidden
         * @returns boolean indicating check result
         */
        async _hideActionMenus() {
            const res = await session.user_has_group(
                "web_action_menus_hide_for_group.group_hide_action_menus"
            );

            return res;
        },

        /**
         * Override core with a group check
         */
        async willStart() {
            if (await this._hideActionMenus()) {
                this.actionItems = [];
                this.printItems = [];
            } else {
                // If not in group, proceed as in core
                this.actionItems = await this._setActionItems(this.props);
                this.printItems = await this._setPrintItems(this.props);
            }
        },

        /**
         * Override core with a group check
         *
         * @param {*} nextProps
         */
        async willUpdateProps(nextProps) {
            if (await this._hideActionMenus()) {
                this.actionItems = [];
                this.printItems = [];
            } else {
                // If not in group, proceed as in core
                this.actionItems = await this._setActionItems(nextProps);
                this.printItems = await this._setPrintItems(nextProps);
            }
        },
    });
});
