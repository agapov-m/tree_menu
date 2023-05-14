# tree_menu
The tree menu is created using django-mptt. 

The menu is displayed on the web page using django inclusion tags. 

It is stored in the database and edited in the standard Django admin site. 

There can be multiple menus, each corresponding to a separate model.

Rendering each menu requires exactly 1 database query.

To draw a menu on any desired page is used the command: 
{% draw_menu 'menu_name' %}, where 'menu_name' is the name of the model.

Clicking on the menu leads to the URL specified in it.