{% if 'user_name' in view_data %}
You are logged in as {{view_data['user_name']}}
{% else %}
No user logged in
{% endif %}