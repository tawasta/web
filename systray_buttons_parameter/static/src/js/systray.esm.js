import {Component, useState} from "@odoo/owl";
import {Dropdown} from "@web/core/dropdown/dropdown";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";

export class SystrayButtons extends Component {
  static template = "systray_buttons";
  static components = {Dropdown};

  setup() {
    this.orm = useService("orm");
    this.action = useService("action");
    this.ui = useState(useService("ui"));
    this.state = useState({systrayButtons: []});

    this.fetchSystrayButtons();
  }

  async fetchSystrayButtons() {
    try {
      const records = await this.orm.call("ir.config_parameter", "search_read", [
        [["key", "ilike", "systray."]],
        ["key", "value"],
      ]);

      if (records.length > 0) {
        this.state.systrayButtons = records.map((item) => ({
          title: item.key.split(".")[2] || "Unknown",
          img: item.key.split(".")[1] || "question-circle",
          url: item.value || "#",
        }));
      } else {
        console.warn("No systray buttons found!");
      }
    } catch (error) {
      console.error("Error fetching systray buttons:", error);
    }
  }

  openUrl(url) {
    window.open(url, "_blank");
  }
}

registry
  .category("systray")
  .add(
    "systray_buttons_parameter.systray_buttons",
    {Component: SystrayButtons},
    {sequence: 10}
  );
