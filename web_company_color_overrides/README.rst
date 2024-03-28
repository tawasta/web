.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================================
Web Company Color: Style overrides 
==================================

* When using OCA's web_company_color module and setting the link colors, 
  that affects also the link colors in certain places where they become 
  hard to read against a dark background
* This module overrides links inside the following places back to being colored white:

  * many2many widget: badges
  * top search bar's filter list: hovered active filter

* If you're not using web_company_color, there is no need to install this module

Configuration
=============
* None needed

Usage
=====
\-

Known issues / Roadmap
======================
\-

Credits
=======

Contributors
------------

* Timo Talvitie <timo.talvitie@tawasta.fi>

Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
