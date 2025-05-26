/** @odoo-module **/

import {Component, onWillUpdateProps} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {Domain} from "@web/core/domain";
import {evaluateExpr} from "@web/core/py_js/py";
const fieldRegistry = registry.category("fields");

export class X2Many2DMatrixRenderer extends Component {
    setup() {
        this.ValueFieldComponent = this._getValueFieldComponent();
        this.columns = this._getColumns();
        this.rows = this._getRows();
        this.matrix = this._getMatrix();
        this.ValueFieldType = this._getValueFieldType();

        onWillUpdateProps((newProps) => {
            this.columns = this._getColumns(newProps.list.records);
            this.rows = this._getRows(newProps.list.records);
            this.matrix = this._getMatrix(newProps.list.records);
        });
    }

    _formatFloatToHHMM(floatValue) {
        const totalMinutes = Math.round(floatValue * 60);
        const hours = Math.floor(totalMinutes / 60);
        const minutes = totalMinutes % 60;
        return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}`;
    }

    _getColumns(records = this.list.records) {
        const columns = [];
        records.forEach((record) => {
            const column = {
                value: record.data[this.matrixFields.x],
                text: record.data[this.matrixFields.x],
            };
            if (record.fields[this.matrixFields.x].type === "many2one") {
                column.text = column.value[1];
                column.value = column.value[0];
            }
            if (columns.findIndex((c) => c.value === column.value) !== -1) return;
            columns.push(column);
        });
        return columns;
    }

    _getRows(records = this.list.records) {
        const rows = [];
        records.forEach((record) => {
            const row = {
                value: record.data[this.matrixFields.y],
                text: record.data[this.matrixFields.y],
            };
            if (record.fields[this.matrixFields.y].type === "many2one") {
                row.text = row.value[1];
                row.value = row.value[0];
            }
            if (rows.findIndex((r) => r.value === row.value) !== -1) return;
            rows.push(row);
        });
        return rows;
    }

    _getPointOfRecord(record) {
        let xValue = record.data[this.matrixFields.x];
        if (record.fields[this.matrixFields.x].type === "many2one") {
            xValue = xValue[0];
        }
        let yValue = record.data[this.matrixFields.y];
        if (record.fields[this.matrixFields.y].type === "many2one") {
            yValue = yValue[0];
        }
        const x = this.columns.findIndex((c) => c.value === xValue);
        const y = this.rows.findIndex((r) => r.value === yValue);
        return {x, y};
    }

    _getMatrix(records = this.list.records) {
        const matrix = this.rows.map(() =>
            new Array(this.columns.length).fill(null).map(() => {
                return {
                    value: 0,
                    displayValue: '00:00',
                    records: []
                };
            })
        );
        records.forEach((record) => {
            const rawValue = record.data[this.matrixFields.value];
            const { x, y } = this._getPointOfRecord(record);
            matrix[y][x].value += rawValue;
            matrix[y][x].displayValue = this._formatFloatToHHMM(matrix[y][x].value);
            matrix[y][x].records.push(record);
        });
        return matrix;
    }

    get list() {
        return this.props.list;
    }

    get matrixFields() {
        return this.props.matrixFields;
    }

    _getValueFieldComponent() {
        const field = this.list.fields[this.matrixFields.value];
        if (!field.widget) {
            return fieldRegistry.get(field.type).component;
        }
        return fieldRegistry.get(field.widget).component;
    }

    _getValueFieldType() {
        const field = this.list.fields[this.matrixFields.value];
        return field.type;
    }

    _aggregateRow(row) {
        const y = this.rows.findIndex((r) => r.value === row);
        const total = this.matrix[y].map((r) => r.value).reduce((aggr, x) => aggr + x);
        if (this.ValueFieldType === "integer") {
            return total;
        }
        return this._formatFloatToHHMM(total);
    }

    _aggregateColumn(column) {
        const x = this.columns.findIndex((c) => c.value === column);
        const total = this.matrix
            .map((r) => r[x])
            .map((r) => r.value)
            .reduce((aggr, y) => aggr + y);
        if (this.ValueFieldType === "integer") {
            return total;
        }
        return this._formatFloatToHHMM(total);
    }

    _aggregateAll() {
        const total = this.matrix
            .map((r) => r.map((x) => x.value).reduce((aggr, x) => aggr + x))
            .reduce((aggr, y) => aggr + y);
        if (this.ValueFieldType === "integer") {
            return total;
        }
        return this._formatFloatToHHMM(total);
    }

    _canAggregate() {
        return ["integer", "float", "monetary"].includes(this.list.fields[this.matrixFields.value].type);
    }

    getValueFieldProps(column, row) {
        const x = this.columns.findIndex((c) => c.value === column);
        const y = this.rows.findIndex((r) => r.value === row);
        let record = null;
        let value = null;
        if (this.matrix[y] && this.matrix[y][x] && (record = this.matrix[y][x].records[0])) {
            record = this.matrix[y][x].records[0];
            value = this.matrix[y][x].value;
        }
        value = record ? record.data[this.matrixFields.value] : value;
        this.matrix[y][x].value = value;
        const result = {
            readonly: this.props.readonly,
            record: record,
            name: this.matrixFields.value,
            canCreate: this.props.canCreate,
            canOpen: this.props.canOpen,
            canWrite: this.props.canWrite,
            canQuickCreate: this.props.canQuickCreate,
            canCreateEdit: this.props.canCreateEdit,
        };
        const domain = record.fields[this.matrixFields.value].domain;
        if (domain) {
            result.domain = new Domain(evaluateExpr(domain, record.evalContext)).toList();
        }
        if (value === null) {
            result.readonly = true;
        }
        return result;
    }

    // Uusi metodi: päivitetään float-arvo HH:mm -syötteen perusteella
    updateFromDisplayValue(hhmmString, columnVal, rowVal) {
        const x = this.columns.findIndex((c) => c.value === columnVal);
        const y = this.rows.findIndex((r) => r.value === rowVal);
        const cell = this.matrix[y][x];

        const match = hhmmString.match(/^(\d{1,2}):([0-5]\d)$/);
        if (!match) return;

        const hours = parseInt(match[1], 10);
        const minutes = parseInt(match[2], 10);
        const newFloat = hours + minutes / 60;

        cell.value = newFloat;
        cell.displayValue = this._formatFloatToHHMM(newFloat);

        // Päivitä oikea record oikein:
        if (cell.records.length > 0) {
            const record = cell.records[0];
            record.update({ [this.matrixFields.value]: newFloat });
        }

        // Triggeröi re-renderöinti
        this.render();
    }

}

X2Many2DMatrixRenderer.template = "web_widget_x2many_2d_matrix.X2Many2DMatrixRenderer";
X2Many2DMatrixRenderer.props = {
    list: { type: Object, optional: true },
    matrixFields: { type: Object, optional: true },
    readonly: { type: Boolean, optional: true },
    domain: { type: [Array, Function], optional: true },
    showRowTotals: { type: Boolean, optional: true },
    showColumnTotals: { type: Boolean, optional: true },
    canOpen: { type: Boolean, optional: true },
    canCreate: { type: Boolean, optional: true },
    canWrite: { type: Boolean, optional: true },
    canQuickCreate: { type: Boolean, optional: true },
    canCreateEdit: { type: Boolean, optional: true },
};
