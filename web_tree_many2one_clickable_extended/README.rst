.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================================
Extension for clickable many2one fields for tree views
======================================================

Extension for clickable many2one fields for tree views

Installation
============

Install the module form Settings->Local Modules

Configuration
=============
If you want to have all many2one fields clickable by default, you have to define in Configuration > Technical > Parameters > System parameters, a new parameter with name web_tree_many2one_clickable_extended.default and with value true.

Usage
=====
You can get to partner-spesific projects from partner form by pressing projects-button.
Projects have new menuitems for My procects/My tasks/Project Templates.
Kanban views have been modified.

For the widget option, you need to add widget="many2one_clickable" attribute in the XML field definition in the tree view.

For example:

<field name="partner_id" widget="many2one_clickable" />

will open the linked partner in a form view.

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>


Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
