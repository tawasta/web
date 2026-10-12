/** @odoo-module **/

import {FileInput} from "@web/core/file_input/file_input";
import {Many2ManyBinaryField} from "@web/views/fields/many2many_binary/many2many_binary_field";
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
    supportedOptions: Many2ManyBinaryField.supportedOptions,
    supportedTypes: Many2ManyBinaryField.supportedTypes,
    isEmpty: Many2ManyBinaryField.isEmpty,
    relatedFields: [
        {name: "name", type: "char"},
        {name: "mimetype", type: "char"},
    ],
    extractProps: ({attrs, options}) => ({
        acceptedFileExtensions: options.accepted_file_extensions,
        className: attrs.class,
        numberOfFiles: options.number_of_files,
    }),
};

registry.category("fields").add("many2many_binary_url", many2ManyBinaryUrlField);
