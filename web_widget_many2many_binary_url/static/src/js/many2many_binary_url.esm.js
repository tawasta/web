/** @odoo-module **/

import {
    Many2ManyBinaryField,
    many2ManyBinaryField,
} from "@web/views/fields/many2many_binary/many2many_binary_field";
import {FileInput} from "@web/core/file_input/file_input";
import {registry} from "@web/core/registry";

export class Many2ManyBinaryUrlField extends Many2ManyBinaryField {
    static template = "web_widget_many2many_binary_url.Many2ManyBinaryUrlField";
    static components = {
        FileInput,
    };
    static props = {
        ...super.props,
    };

    setup() {
        super.setup();
    }

    getUrl(id) {
        return "/web/content/" + id;
    }
}

export const many2ManyBinaryUrlField = {
    component: Many2ManyBinaryUrlField,
    supportedOptions: many2ManyBinaryField.supportedOptions,
    supportedTypes: many2ManyBinaryField.supportedTypes,
    isEmpty: many2ManyBinaryField.isEmpty,
    relatedFields: many2ManyBinaryField.relatedFields,
    extractProps: many2ManyBinaryField.extractProps,
};

registry.category("fields").add("many2many_binary_url", many2ManyBinaryUrlField);
