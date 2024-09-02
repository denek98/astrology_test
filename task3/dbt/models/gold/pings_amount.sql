select strftime('%Y-%m-%d', timestamp) as ping_day, count(id) as ping_amount
from {{ ref("raw_astrolog_ping_events") }}
group by ping_day
