select avg(duration) as avg_duration, avg(revenue) as avg_revenue
from {{ ref("raw_chat_events") }}
where ping_event is not null
