import {
  Many2ManyBinaryField,
  many2ManyBinaryField,
} from "@web/views/fields/many2many_binary/many2many_binary_field";
import {registry} from "@web/core/registry";

export class Many2ManyBinaryUrlField extends Many2ManyBinaryField {
  static template = "web_widget_many2many_binary_url.Many2ManyBinaryUrlField";

  getUrl(id) {
    // Without "?download=true" the browser opens the file instead of saving it
    return "/web/content/" + id;
  }
}

export const many2ManyBinaryUrlField = {
  ...many2ManyBinaryField,
  component: Many2ManyBinaryUrlField,
};

registry.category("fields").add("many2many_binary_url", many2ManyBinaryUrlField);
