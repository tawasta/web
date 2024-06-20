/** @odoo-module  */

import {HtmlField} from "@web_editor/js/backend/html_field";
import {patch} from "@web/core/utils/patch";

patch(HtmlField.prototype, {
    /**
     * @override
     */
    async startWysiwyg(wysiwyg) {
        this.wysiwyg = wysiwyg;
        await this.wysiwyg.startEdition();
        wysiwyg.$editable[0].classList.add("odoo-editor-qweb");

        const $codeviewButtonToolbar = $(`
            <div id="codeview-btn-group" class="btn-group">
                <button class="o_codeview_btn btn btn-primary">
                    <i class="fa fa-code"></i>
                </button>
            </div>
        `);
        this.wysiwyg.toolbarEl.append($codeviewButtonToolbar[0]);
        $codeviewButtonToolbar.click(this.toggleCodeView.bind(this));

        this.wysiwyg.odooEditor.addEventListener("historyStep", () =>
            this.props.record.model.bus.trigger("FIELD_IS_DIRTY", this._isDirty())
        );

        this.isRendered = true;
    },
});

export default HtmlField;
