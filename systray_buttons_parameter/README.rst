.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================
Systray Button Parameter
========================

Overview
--------
This module allows adding custom buttons to Odoo's systray section.
New buttons are dynamically imported from system parameters where the key value contains the word 'systray'.

Example Configuration:
----------------------
- **Key:** ``systray.fa-shop.Shop``
- **Value:** ``/shop``

Configuration
=============
No specific configuration is required. Define system parameters to include buttons in the systray.

Usage
=====
1. Go to **Settings** -> **Technical** -> **System Parameters**.
2. Add a new entry:
   - **Key:** ``systray.fa-home.Home``
   - **Value:** ``/web/home``
3. The new button appears in the systray menu automatically.

Known Issues / Roadmap
======================
- Improve styling for better UI integration.
- Add more customization options for button behavior.

Credits
=======

Contributors
------------
* **Valtteri Lattu** <valtteri.lattu@futural.fi>

Maintainer
----------

.. image:: https://futural.fi/templates/tawastrap/images/logo.png
   :alt: Futural Oy
   :target: https://futural.fi/

This module is maintained by **Futural Oy**
