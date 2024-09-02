select
    ape.astrolog_id,
    ape.astrolog_name,
    strftime('%Y-%m-%d', ape.timestamp) as ping_day,
    count(ape.astrolog_id) as pings_count,
    count(distinct cep.id) as successful_sessions
from {{ ref("int_astrolog_ping_event_extended") }} ape
left join
    {{ ref("raw_chat_events") }} cep
    on ape.id = cep.ping_event
    and cep.astrolog = ape.astrolog_id
group by ape.astrolog_id, ape.astrolog_name, ping_day
