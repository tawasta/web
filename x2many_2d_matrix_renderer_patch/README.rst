.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
x2many_2d_matrix_renderer_patch
===============================

This module overrides and extends the default 2D matrix renderer for x2many fields,
specifically enhancing the handling of float values by displaying and accepting time
input in `HH:mm` format. This improves clarity and usability when working with
timesheet-like data.

Key Features
============

- Replaces default float display with `HH:mm` format (e.g. 1.5 → 01:30)
- Allows user input in `HH:mm` format directly in matrix cells
- Ensures internal float value consistency for Odoo records
- Maintains full aggregation support (row, column, total) with time formatting
- Backward-compatible with original matrix structure

Configuration
=============

No additional configuration required. Just install and it replaces the default renderer.


Usage
=====

1. Install this module from the Odoo Apps menu
2. Use any view leveraging `web_widget_x2many_2d_matrix`
3. The matrix values will appear in `HH:mm` format
4. You can directly edit cells using `HH:mm` input

Known issues / Roadmap
======================

Credits
=======

Contributors
------------

* Valtteri Lattu <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by Futural Oy
